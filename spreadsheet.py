import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from text_utils import *

class GoogleWorkspaceForMe():
    def __init__(self, verbose=False):
        # set verbosity level
        self.verbose = verbose

        # Path to the service account key file
        self.KEY_FILE_PATH = "botGoogleWorkspaceForMe.json" 

        # Scopes required by the API
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']
        
        # Make credentials
        self._makeCredentials()

        # Email of service account
        self.serviceEmail = "googleworkspaceforme@phrasal-aegis-400216.iam.gserviceaccount.com"


    def _makeCredentials(self):
        # Authenticate and create the service
        self.credentials = service_account.Credentials.from_service_account_file(
            self.KEY_FILE_PATH,
            scopes=self.SCOPES
        )


    def makeSpreadsheetService(self):
        self.spreadsheetService = build('sheets', 'v4', credentials=self.credentials)


    def makeNewSpreadsheet(self, title="My new spreadsheet"):
        service = self.spreadsheetService

        # Spreadsheet details
        spreadsheet_body = {
            'properties': {'title': title}
        }

        # Create a new spreadsheet
        spreadsheet = service.spreadsheets().create(body=spreadsheet_body).execute()
        sheet_id = spreadsheet.get('spreadsheetId') 
        if self.verbose:
            print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
            url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit"
            print("Spreadsheet URL:", url)
        return sheet_id    


    def makeDriveService(self):
        self.driveService = build('drive', 'v3', credentials=self.credentials)


    def shareSpreadsheet(self, sheet_id, user_email):
        drive_service = self.driveService

        # Define the permission to be granted
        permission = {
                'type': 'user',  # Sharing with a user
                'role': 'writer',  # Providing write access; can be 'reader', 'writer', or 'owner'
                'emailAddress': user_email  # Email address of the user the sheet is being shared with
        }

        # Share the sheet with your user account
        drive_service.permissions().create(
                fileId=sheet_id,
                body=permission,
                fields='id'  # We are only interested in the id field of the response
        ).execute()
        if self.verbose:
            print(f'Spreadsheet id {sheet_id} shared with {user_email}')


    def listSpreadsheets(self):
        drive_service = self.driveService

        results = drive_service.files().list(
            q="mimeType='application/vnd.google-apps.spreadsheet'",  # Query for Google Sheets
            fields="nextPageToken, files(id, name)"  # Fields to be included in the response
        ).execute()

        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(f'{item["name"]} ({item["id"]})')
        return items        


    def deleteSpreadsheets(self, items, onlyTrash=True):
        drive_service = self.driveService

        # Replace with the IDs of the spreadsheets you want to delete
        spreadsheet_ids_to_delete = [item["id"] for item in items]

        if onlyTrash:
            for sheet_id in spreadsheet_ids_to_delete:
                drive_service.files().update(fileId=sheet_id, body={'trashed': True}).execute()
                print(f'Moved spreadsheet with ID: {sheet_id} to trash')
        else:        
            for sheet_id in spreadsheet_ids_to_delete:
                drive_service.files().delete(fileId=sheet_id).execute()
                print(f'Deleted spreadsheet with ID: {sheet_id}')


    def updateSpreadsheetBatch(self, sheet_id, requests): 
        service = self.spreadsheetService

        # Make the batchUpdate request
        service.spreadsheets().batchUpdate(spreadsheetId=sheet_id, body={'requests': requests}).execute()
        if self.verbose:
            print(f"Succesfull update of spreadsheet id {sheet_id}")


    def _create_rows(self, df):
        rows = [
            {'values': [ {'userEnteredValue' : {'stringValue': col } } for col in df.columns.to_list()]}
        ]

        for index, row in df.iterrows():
            values = []
            for col in df.columns:
                value = {}
                if pd.api.types.is_numeric_dtype(df[col]):
                    value['userEnteredValue'] = {'numberValue': row[col]}
                elif pd.api.types.is_bool_dtype(df[col]):
                    value['userEnteredValue'] = {'boolValue': row[col]}
                else:  # For strings and other types
                    value['userEnteredValue'] = {'stringValue': str(row[col])}
                values.append(value)
            rows.append({'values': values})
        return rows


    def dataframetoSpreadsheet(self, sheet_id, df, updateNow=False):
        # Preapare the list of rows to insert, including header row
        rows = [df.columns.tolist()] + df.values.tolist()

        # Create the batchUpdate request body
        requests = [{
            'appendCells': {
                'sheetId': 0, # Assuming you are working with the first (and only) sheet in the spreadsheet
                'rows': self._create_rows(df),
                'fields': 'userEnteredValue.stringValue',
                }
        }]

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests


    def protectSpreadsheetColumns(self, sheet_id, start_col_index, end_col_index, updateNow=False):
        # Preapare the request body
        requests = [
            {
                'addProtectedRange': {
                    'protectedRange': {
                        'range': {
                            'sheetId': 0,  # Typically 0 for the first (and often only) sheet
                            'startRowIndex': start_col_index,
                            'endRowIndex': end_col_index,
                        },
                        'editors': {
                            'users': [self.serviceEmail]
                        },
                        'description': 'unprotect some columns',
                        'warningOnly': False
                    }
                }
            }
            for range_to_protect in ranges_to_protect
        ]

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests

    def protectSpreadsheetRows(self, sheet_id, start_row_index, end_row_index, updateNow=False):
        # Set the range of rows to protect. For example, to protect rows 1-2.
        requests = [{
            'addProtectedRange': {
                'protectedRange': {
                    'range': {
                        'sheetId': 0,  # Typically 0 for the first (and often only) sheet
                        'startRowIndex': start_row_index,
                        'endRowIndex': end_row_index,
                    },
                    'description': 'Cells only editable by service account',
                    'warningOnly': False,  # Set to True if you want users to be able to edit anyway
                    'editors': {
                        'users': [self.serviceEmail]
                    }
                }
            }
        }]

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests


    def protectSpreadsheetRowsandColumns(self, sheet_id, existing_row_counts, existing_column_counts, updateNow=False):
        unprotected_ranges = [
            {
                'sheetId': 0,
                'startRowIndex': rows[0],
                'endRowIndex': rows[1],
                'startColumnIndex': cols[0],
                'endColumnIndex': cols[1]
            }
            for rows, cols in zip(existing_row_counts, existing_column_counts)
        ]
        # Prepare the request body
        requests = [
            {
                'addProtectedRange': {
                    'protectedRange': {
                        'range': {
                            'sheetId': 0,
                        },
                        'unprotectedRanges': unprotected_ranges,
                        'editors': {
                            'users': [self.serviceEmail],
                        },
                        'description': 'Only the service account can add more rows or columns.',
                        'warningOnly': False
                    }
                }
            }
        ]    

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests


    def unprotectSpreadsheetRowsandColumns(self, sheet_id, protectedRangeId, existing_row_counts, existing_column_counts, updateNow=False):
        unprotected_ranges = [
            {
                'sheetId': 0,
                'startRowIndex': rows[0],
                'endRowIndex': rows[1],
                'startColumnIndex': cols[0],
                'endColumnIndex': cols[1]
            }
            for rows, cols in zip(existing_row_counts, existing_column_counts)
        ]
        # Prepare the request body
        requests = [
            {
                'updateProtectedRange': {
                    'protectedRange': {
                        'protectedRangeId': protectedRangeId,
                        'unprotectedRanges': unprotected_ranges,
                    },
                    'fields': 'unprotectedRanges'
                }
            }
        ]    

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests


    def getProtectedRangesId(self, sheet_id):
        service = self.spreadsheetService
        # Fetch the spreadsheet details
        response = service.spreadsheets().get(spreadsheetId=sheet_id, fields='sheets.protectedRanges').execute()

        # Extract the protectedRanges from the response
        sheets = response.get('sheets', [])
        for sheet in sheets:
            sheet_title = sheet.get('properties', {}).get('title', 'Unnamed Sheet')
            protected_ranges = sheet.get('protectedRanges', [])
            if not protected_ranges:
                print(f"No protected ranges in sheet: {sheet_title}")
                continue
            print(f"Protected ranges in sheet: {sheet_title}")
            for protected_range in protected_ranges:
                range_id = protected_range.get('protectedRangeId')
                description = protected_range.get('description', 'No Description')
                warning_only = protected_range.get('warningOnly', False)
                unprotectedRanges = protected_range.get('unprotectedRanges', [])
                print(f"  ID: {range_id}, Description: {description}, Warning Only: {warning_only}")
                print(f"  unprotectedRanges:\n {unprotectedRanges}")

        return range_id


    def prependRowsinSpreadsheet(self, sheet_id, values, updateNow=False):
        # Create requests for batchUpdate
        requests = [
            {
                'insertRange': {
                    'range': {
                        'sheetId': 0,
                        'startRowIndex': 0,
                        'endRowIndex': len(values)  # One row is being inserted at the start.
                    },
                    'shiftDimension': 'ROWS'  # Shift existing rows down
                }
            },
            {
                'updateCells': {
                    'rows': [{'values': [{'userEnteredValue': {'stringValue': value}} for value in row]} for row in values],
                    'fields': 'userEnteredValue.stringValue',
                    'range': {
                        'sheetId': 0,
                        'startRowIndex': 0,  # The new row starts here.
                        'endRowIndex': len(values),
                        'startColumnIndex': 0,  # Assuming data starts at the first column.
                        'endColumnIndex': len(values[0])  # The number of columns in your data.
                    }
                }
            }
        ]

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests


    def addSelectorinCellSpreadsheet(self, sheet_id, values, positions, inputMessage, updateNow=False):
        if len(values)<3:
            showCustomUi = True
        else:
            showCustomUi = False
        # Prepare the request body
        requests = [
            {
                'setDataValidation': {
                    'range': {
                        'sheetId': 0,
                        'startRowIndex': position[0],  # 0-based index, for cell A1
                        'endRowIndex': position[0]+1,  # Exclusive
                        'startColumnIndex': position[1],  # 0-based index, for cell A1
                        'endColumnIndex': position[1]+1  # Exclusive
                    },
                    'rule': {
                        'condition': {
                            'type': 'ONE_OF_LIST',
                            'values': [
                                {'userEnteredValue': value} for value in values
                            ]
                        },
                        'inputMessage': inputMessage,
                        'strict': True,  # Strict means invalid values are rejected
                        'showCustomUi': showCustomUi  # Will show a dropdown to the user
                    }
                }
            }
            for position in positions
        ]

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests


    def limitRowsColumnsinSpreadsheet(self, sheet_id, row_limit, column_limit, updateNow=False):
        # Prepare the request body
        requests = [
            {
                'updateSheetProperties': {
                    'properties': {
                        'sheetId': 0,
                        'gridProperties': {
                            'rowCount': row_limit,
                            'columnCount': column_limit
                        }
                    },
                    'fields': 'gridProperties(rowCount,columnCount)'
                }
            }
        ]

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests


    def conditionalColorMinMaxSpreadsheet(self, sheet_id, rows, cols, minmax, updateNow=False):
        format_range = {
            'sheetId': 0,
            'startRowIndex': rows[0],  # 0-based index, adjust as needed
            'endRowIndex': rows[1],  # Adjust as needed
            'startColumnIndex': cols[0],  # 0-based index, adjust as needed
            'endColumnIndex': cols[1],  # Adjust as needed
        }

        # Prepare the request body
        requests = [
            {
                'addConditionalFormatRule': {
                    'rule': {
                        'ranges': [format_range],
                        'gradientRule': {
                            'minpoint': {
                                'color': {'red': 1, 'green': 1, 'blue': 0},  # Yellow
                                'type': 'NUMBER',
                                'value': str(minmax[0])
                            },
                            'midpoint': {
                                'color': {'red': 0, 'green': 1, 'blue': 0}, # Green
                                'type': 'NUMBER',
                                'value': str((minmax[1]-minmax[0])/2)
                            }, 
                            'maxpoint': {
                                'color': {'red': 0, 'green': 0, 'blue': 1},  # Blue 
                                'type': 'NUMBER',
                                'value': str(minmax[1])
                            },
                        }
                    },
                    'index': 1  # Gradient rule should be applied first.
                }
            },
            {
                'addConditionalFormatRule': {
                    'rule': {
                        'ranges': [format_range],
                        'booleanRule': {
                            'condition': {
                                'type': 'NUMBER_NOT_BETWEEN',
                                'values': [
                                    {'userEnteredValue': str(minmax[0])},  # min value
                                    {'userEnteredValue': str(minmax[1])}  # max value
                                ],
                            },
                            'format': {
                                'backgroundColor': {'red': 1, 'green': 0, 'blue': 0},  # Red 
                            }
                        }
                    },
                    'index': 0  # This rule should be applied second.
                }
            }
        ]

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests


    def conditionalColorBoolSpreadsheet(self, sheet_id, rows, cols, num, updateNow=False):
        format_range = {
            'sheetId': 0,
            'startRowIndex': rows[0],  # 0-based index, adjust as needed
            'endRowIndex': rows[1],  # Adjust as needed
            'startColumnIndex': cols[0],  # 0-based index, adjust as needed
            'endColumnIndex': cols[1],  # Adjust as needed
        }
        # Prepare the request body
        requests = [
            {
                'addConditionalFormatRule': {
                    'rule': {
                        'ranges': [format_range],
                        'booleanRule': {
                            'condition': {
                                'type': 'NUMBER_EQ',
                                'values': [{'userEnteredValue': str(num)}]  # Color if value is greater than 10
                            },
                            'format': {
                                'backgroundColor': {'red': 0, 'green': 1, 'blue': 0}  # green
                            }
                        }
                    },
                    'index': 0  # 0-based index, defining the order of execution of the rule
                }
            },
            {
                'addConditionalFormatRule': {
                    'rule': {
                        'ranges': [format_range],
                        'booleanRule': {
                            'condition': {
                                'type': 'NUMBER_NOT_EQ',
                                'values': [{'userEnteredValue': str(num)}]  # Color if value is greater than 10
                            },
                            'format': {
                                'backgroundColor': {'red': 1, 'green': 0, 'blue': 0}  # red
                            }
                        }
                    },
                    'index': 1  # 0-based index, defining the order of execution of the rule
                }
            }
        ]
        
        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests


    def controlIfProductinRange(self, sheet_id, rang_str, rang_num, position, updateNow=False):
        # Prepare the request body
        rang = f"{rang_str[0]}:{rang_str[1]}"
        formula =  f'=IF(\
                        AND(\
                            MIN(ARRAYFORMULA({rang})) >= {rang_num[0]},\
                            MAX(ARRAYFORMULA({rang})) <= {rang_num[1]},\
                            COUNTIF(ARRAYFORMULA(ISNUMBER({rang})), FALSE) <= 0),\
                        1,\
                        0)'
        formula = AuxCleanWhitespace(formula)
        requests = [
            {
                'updateCells': {
                    'range': {
                        'sheetId': 0, 
                        'startRowIndex': position[0], 
                        'startColumnIndex': position[1], 
                        'endRowIndex': position[0]+1, 
                        'endColumnIndex': position[1]+1
                    },
                    'rows': [
                        {'values': [{'userEnteredValue': 
                                     {'formulaValue': formula}
                                   }]}
                    ],
                    'fields': 'userEnteredValue.formulaValue'
                }
            }
        ]

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests

    def controlIfProductinRange_2(self, sheet_id, rang_str, rang_num, position, poscontrol_str, updateNow=False):
        # Prepare the request body
        rang = f"{rang_str[0]}:{rang_str[1]}"
        #formula =  f'=IF(\
        #                    {poscontrol_str}<={rang_num[0]},\
        #                    1,\
        #                    IF(\
        #                        AND(\
        #                            MIN(ARRAYFORMULA({rang})) >= {rang_num[0]},\
        #                            MAX(ARRAYFORMULA({rang})) <= {rang_num[1]},\
        #                            MAX(ARRAYFORMULA({rang})) >= {poscontrol_str},\
        #                            COUNTIF(ARRAYFORMULA(ISNUMBER({rang})), FALSE) <= 0),\
        #                        1,\
        #                        0) )'
        formula =  f'=IF(\
                        AND(\
                            MIN(ARRAYFORMULA({rang})) >= {rang_num[0]},\
                            MAX(ARRAYFORMULA({rang})) <= {rang_num[1]},\
                            MAX(ARRAYFORMULA({rang})) = {poscontrol_str},\
                            COUNTIF(ARRAYFORMULA(ISNUMBER({rang})), FALSE) <= 0),\
                        1,\
                        0)'
        formula = AuxCleanWhitespace(formula)
        requests = [
            {
                'updateCells': {
                    'range': {
                        'sheetId': 0, 
                        'startRowIndex': position[0], 
                        'startColumnIndex': position[1], 
                        'endRowIndex': position[0]+1, 
                        'endColumnIndex': position[1]+1
                    },
                    'rows': [
                        {'values': [{'userEnteredValue': 
                                     {'formulaValue': formula}
                                   }]}
                    ],
                    'fields': 'userEnteredValue.formulaValue'
                }
            }
        ]

        if updateNow:
            self.updateSpreadsheetBatch(sheet_id, requests)
            return []
        else:
            return requests

    def _to_cell_notation(self, row_idx, col_idx):
        col_str = ''
        while col_idx >= 0:
            quotient, remainder = divmod(col_idx, 26)
            col_str = chr(65 + remainder) + col_str  # 65 is ASCII value for 'A'
            col_idx = quotient - 1
        row_str = str(row_idx + 1)  # converting 0-based index to 1-based row number
        return col_str + row_str


    def readSpreadsheet(self, sheet_id, RANGE_NAME):
        service = self.spreadsheetService

        # Read the sheet
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id, range=RANGE_NAME).execute()
        values = result.get('values', [])

        if self.verbose:
            if not values:
                print('No data found.')
            else:
                print(f"first row is {values[0]}")
        return values


def auxMakeDF():
    # create the dataframe
    data = {
            'Name': ['John', 'Paul', 'George', 'Ringo'],
            'Instrument': ['Guitar', 'Bass', 'Guitar', 'Drums'],
            # 'Vocals': ['Lead', 'Lead', 'Backup', 'Backup']
            }
    df = pd.DataFrame(data)
    questions = ["delete_comment", "answer_comment"]
    reasons_to_delete = ["delete_hate", "delete_sexual", "delete_other"]
    reasons_to_answer = ["answer_good", "answer_help", "answer_other"]
    prefix = "_is_complete"
    reasons = {"delete_comment":reasons_to_delete, "answer_comment":reasons_to_answer}
    for question in questions:
        df[question] = -1
        for reason_i in reasons[question]:
           df[reason_i] = -1
        df[question+"_is_complete"] = -1
    return df, reasons, prefix


def auxListandDeleteSpreadsheets():
    # create the googleworkspace helper
    gw = GoogleWorkspaceForMe(verbose=True)

    # initialize the services
    gw.makeDriveService()
    gw.makeSpreadsheetService()

    # get the spreadsheet items
    items = gw.listSpreadsheets()

    # delete the items  NOTE this is permanent erease!!
    if items:
        gw.deleteSpreadsheets(items, onlyTrash=False)


def auxReadSheet(sheet_id, RANGE_NAME):
    # create the googleworkspace helper
    gw = GoogleWorkspaceForMe(verbose=True)

    # initialize the services
    gw.makeDriveService()
    gw.makeSpreadsheetService()

    # get the values stored in the spreadsheet
    values = gw.readSpreadsheet(sheet_id, RANGE_NAME)

    # check if spreadsheet is finished
    if values[0][0] == '0':
        print("Not Finished yet")
        return None

    # make the dataframe
    df = pd.DataFrame(values[2:], columns=values[1])
    return df


def auxCreateExampleSpreadsheet(df, reasons, prefix, user_email):
    # create the googleworkspace helper
    gw = GoogleWorkspaceForMe(verbose=True)

    # initialize the services
    gw.makeDriveService()
    gw.makeSpreadsheetService()

    # create a new spreadsheet
    sheet_id = gw.makeNewSpreadsheet()

    # share the spreadsheet with an user
    # user_email = "gabriel.diaz.iturry@gmail.com"
    gw.shareSpreadsheet(sheet_id, user_email)

    # create te dataframe
    #df = auxMakeDF()

    # prepare the requests
    requests = []

    # fill the spreadsheet with the df data
    requests.append(gw.dataframetoSpreadsheet(sheet_id, df, updateNow=False))


    # prepend rows
    values = [["", "is the sheet ready?"]]
    requests.append(gw.prependRowsinSpreadsheet(sheet_id, values, updateNow=False))
     
    # addtional variables
    row_limit = len(df)+2
    column_limit = len(df.columns)
    minmax = [0, 10]

    # add selectors to indicate how is an option
    options = reasons.keys()
    values = [str(i) for i in range(-1, 11)]
    existing_row_counts = []
    existing_column_counts = []
    for option in options:
        # questions
        # add a selector for some cells
        col_index = df.columns.get_loc(option)
        positions = [[i+2, col_index] for i in range(len(df))] 
        inputMessage = f'how {option} is it?'
        requests.append(gw.addSelectorinCellSpreadsheet(sheet_id, values, positions, inputMessage, updateNow=False))
        # add control if the product is in given range
        rang_str = []
        rang_str.append(gw._to_cell_notation(2, col_index))
        rang_str.append(gw._to_cell_notation(row_limit-1, col_index))
        position = [0, col_index]
        requests.append(gw.controlIfProductinRange(sheet_id, rang_str, minmax, position, updateNow=False))
        # Color cell
        num = 1
        rows = [0, 1]
        cols = [col_index, col_index+1]
        requests.append(gw.conditionalColorBoolSpreadsheet(sheet_id, rows, cols, num, updateNow=False))
        # color cells with condition
        rows = [2, row_limit]
        cols = [col_index, col_index+len(reasons[option])+1]
        requests.append(gw.conditionalColorMinMaxSpreadsheet(sheet_id, rows, cols, minmax, updateNow=False))
        existing_row_counts.append(rows)
        existing_column_counts.append(cols)
        # reasons
        for reason_i in reasons[option]:
            # add a selector for some cells
            col_index = df.columns.get_loc(reason_i)
            positions = [[i+2, col_index] for i in range(len(df))] 
            inputMessage = f'how {reason_i} is it?'
            requests.append(gw.addSelectorinCellSpreadsheet(sheet_id, values, positions, inputMessage, updateNow=False))
            # add control if the product is in given range
            rang_str = []
            rang_str.append(gw._to_cell_notation(2, col_index))
            rang_str.append(gw._to_cell_notation(row_limit-1, col_index))
            position = [0, col_index]
            requests.append(gw.controlIfProductinRange(sheet_id, rang_str, minmax, position, updateNow=False))
            # Color cell
            num = 1
            rows = [0, 1]
            cols = [col_index, col_index+1]
            requests.append(gw.conditionalColorBoolSpreadsheet(sheet_id, rows, cols, num, updateNow=False))

        # prefix
        col_index = df.columns.get_loc(option+prefix)
        for row_index in range(2, row_limit):
            # add control if the product is in given range
            rang_str = []
            rang_str.append(gw._to_cell_notation(row_index, col_index-len(reasons[option])))
            rang_str.append(gw._to_cell_notation(row_index, col_index-1))
            position = [row_index, col_index]
            poscontrol_str = gw._to_cell_notation(row_index, col_index-len(reasons[option])-1)
            requests.append(gw.controlIfProductinRange_2(sheet_id, rang_str, minmax, position, poscontrol_str, updateNow=False))
        # add control if the product is in given range
        rang_str = []
        rang_str.append(gw._to_cell_notation(2, col_index))
        rang_str.append(gw._to_cell_notation(row_limit-1, col_index))
        position = [0, col_index]
        requests.append(gw.controlIfProductinRange(sheet_id, rang_str, [1,1], position, updateNow=False))    
        # Color cell
        num = 1
        rows = [0, 1]
        cols = [col_index, col_index+1]
        requests.append(gw.conditionalColorBoolSpreadsheet(sheet_id, rows, cols, num, updateNow=False))
        num = 1
        rows = [2, row_limit]
        cols = [col_index, col_index+1]
        requests.append(gw.conditionalColorBoolSpreadsheet(sheet_id, rows, cols, num, updateNow=False))


    


    # add limits to column and rows
    # requests.append(gw.limitRowsColumnsinSpreadsheet(sheet_id, row_limit, column_limit, updateNow=False))

    # color cells with condition
    # rows = [2, row_limit]
    # cols = [2, column_limit]
    # requests.append(gw.conditionalColorMinMaxSpreadsheet(sheet_id, rows, cols, minmax, updateNow=False))

    # add control if the product is in given range
    rang_str = []
    rang_str.append(gw._to_cell_notation(0, column_limit-len(options)))
    rang_str.append(gw._to_cell_notation(0, column_limit-1))
    position = [0, 0]
    requests.append(gw.controlIfProductinRange(sheet_id, rang_str, [1,1], position, updateNow=False))
    # Color cell
    num = 1
    rows = [0, 1]
    cols = [0, 1]
    requests.append(gw.conditionalColorBoolSpreadsheet(sheet_id, rows, cols, num, updateNow=False))

    # protect the spreadsheet
    #existing_row_counts=[[2,row_limit]]
    #existing_column_counts=[[column_limit-len(options), column_limit]]
    requests.append(gw.protectSpreadsheetRowsandColumns(sheet_id, existing_row_counts, existing_column_counts, updateNow=False))

    # make the update
    gw.updateSpreadsheetBatch(sheet_id, requests)

    # preapre the output
    s = gw._to_cell_notation(row_limit-1, column_limit-1)
    return sheet_id, "Sheet1!A1:"+s

# df, reasons, prefix = auxMakeDF()
# auxCreateExampleSpreadsheet(df, reasons, prefix, "gabriel.diaz.iturry@gmail.com")

def modifySpreadsheet(sheet_id="1qJlNTPTG52NW5ijHt0u8xATJGO2dMo7zjK5ZOAshkCI"):
    # create the googleworkspace helper
    gw = GoogleWorkspaceForMe(verbose=True)

    # initialize the services
    gw.makeDriveService()
    gw.makeSpreadsheetService()

    # additional variables
    row_limit = 6
    column_limit = 5
    options = ["good", "bad"]

    # create the requests
    requests = []
    

    # make the update
    gw.updateSpreadsheetBatch(sheet_id, requests)
