import re


def CleanText(input_string, **kwargs):
    """
    cleans a string
    """
    out_string = input_string

    # Remove unecesary whitespaces
    if not kwargs.get("notCleanWhitespace"):
        out_string = AuxCleanWhitespace(out_string)
    
    # Remove urls
    if not kwargs.get("notSubstituteURL"):
        out_string = AuxSubstituteURL(out_string)

    return out_string


def AuxCleanWhitespace(input_string):
    """
    Substituting continuous whitespace characters with a single space
    """
    return re.sub(r'\s+', ' ', input_string)

def AuxSubstituteURL(input_string, url_token = "<URL>"):
    """
    Substitutes urls with a given token
    """
    url_pattern = re.compile(
    r'http[s]?:\S+'
    r'|'  # OR
    r'ftp://\S+'
    r'|'  # OR
    r'www\.\S+'
    )
    
    return re.sub(url_pattern, url_token, input_string)
