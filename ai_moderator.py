"""
    This code is for calling an AI moderator that says if a comment is acceptable or not
"""

import openai
import tiktoken
import json
import random
import time
# from openai.embeddings_utils import (
#     get_embedding)

from utils import *

openai.api_key = '{openai_key}'

def AuxOpenAIRetryWithExponentialBackoff(
    func,
    initial_delay: float = 1,
    exponential_base: float = 2,
    jitter: bool = True,
    max_retries: int = 10,
    # errors: tuple = (openai.error.RateLimitError,),
    errors: tuple = (openai),
):
    """
    A decorator for Retry a function with exponential backoff
    use like:
    @AuxOpenAIRetryWithExponentialBackoff
    def func(**kwargs):
        do something
        return something

    then call
    func(**kwargs)    
    """

    def wrapper(*args, **kwargs):
        # Initialize variables
        num_retries = 0
        delay = initial_delay

        # Loop until a successful response or max_retries is hit or an exception is raised
        while True:
            try:
                return func(*args, **kwargs)

            # Retry on specified errors
            except errors as e:
                # Increment retries
                num_retries += 1

                # Check if max retries has been reached
                if num_retries > max_retries:
                    raise Exception(
                        f"Maximum number of retries ({max_retries}) exceeded."
                    )

                # Increment the delay
                delay *= exponential_base * (1 + jitter * random.random())

                # Sleep for the delay
                time.sleep(delay)

            # Raise exceptions for any errors not specified
            except Exception as e:
                raise e

    return wrapper

def AuxGetOpenAINumTokensFromSingleText(customer_text, **kwargs):
    """
    Returns the number of tokens used by a single text, first transforms into a gpt conversation
    """
    messages = AuxMakeMessagesFromSingleText(customer_text)
    return AuxGetOpenAINumTokensFromMessages(messages, **kwargs)


def AuxGetOpenAINumTokensFromMessages(messages, model="gpt-3.5-turbo-0613", verbose=False):
    """
    Returns the number of tokens used by a list of messages
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        if verbose:
            print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model:
        if verbose:
            print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return AuxGetOpenAINumTokensFromMessages(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        if verbose:
            print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return AuxGetOpenAINumTokensFromMessages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""GetOpenAINumTokensFromMessages() is not implemented for model {model}. 
            See https://github.com/openai/openai-python/blob/main/chatml.md 
            for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens

def AuxMakeMessagesFromSingleText(customer_text):
    """
    Return a message to be used by chat gpt in ChatCompletions
    """
    messages = [{"role": "user", "content": customer_text}]
    return messages


@AuxOpenAIRetryWithExponentialBackoff
def OpenAICommentDescription(customer_text, model="gpt-3.5-turbo-0613"):
    """
    Make a ChatCompletion git chatgpt, we get some info about a customer text
    """
    messages = AuxMakeMessagesFromSingleText(customer_text)
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        functions = [
            {
                "name": "get_customer_response",
                "description": """
                give me response more relevant to it
                
                """,
                "parameters": {
                    "type": "object",
                    "properties": {
                        'information': {
                            'type':'string',
                            'description':'if customer asks for information return yes',
                            'enum':['yes','no']
                        },
                        'spam':{
                            'type':'string',
                            'description':'if customer is writting a spam message return yes',
                            'enum':['yes','no']
                        },
                        'hate':{
                            'type':'string',
                            'description':'if customer is writting a hate message return yes',
                            'enum':['yes','no']
                        }
                    },
                    "required": ['information','spam','hate'],
                },
            }
        ],
        function_call = {'name':'get_customer_response'}
    )
    
    message = response["choices"][0]["message"]
    message1 = message['function_call']['arguments']
    answer = json.loads(message1)
    return answer, message

def GetOpenAICommentDescription(comments, model="gpt-3.5-turbo-0613", allowedAuthors=[]):
    descriptions = []
    for comment in comments:
        if comment.comment_author_id in allowedAuthors:
            continue

        response = openai.Moderation.create(input=comment.comment_text)
        flagged = response["results"][0]["flagged"]

        if not flagged:
            answer, _ = OpenAICommentDescription(comment.comment_text, model)
        else:
            answer = None    

        comment.comment_flagged = flagged
        comment.comment_description = answer

        descriptions.append(comment)
    
    return descriptions


@AuxOpenAIRetryWithExponentialBackoff
def OpenAIEmbedding(customer_text, model="text-embedding-ada-002"):
    """
    Get the emmbedding vector from a text using embedding functionality of OpenAi
    can pass batches of len tokens <8191
    """
    return get_embedding(customer_text, model)
