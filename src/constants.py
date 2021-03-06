class Constants:

    #HTTP constants
    OK = 200
    RESOURCE_CREATED = 201
    ACCEPTED = 202
    INTERNAL_SERVER_ERROR = 500
    AUTH_ERROR = 403

    #Sign Up constants
    ERROR_INVALID_INPUT = 'Invalid input.'
    ERROR_INVALID_EMAIL = 'Email cannot be empty'
    ERROR_INVALID_FIRST_NAME = 'First name cannot be empty'
    ERROR_SIGNUP = 'Error occured during sign up. Please try later'
    RESPONSE_SIGNUP = '{ "links" : [{"url":"/users/login/","method": "POST"}]}'

    # Login constants
    ERROR_DB = 'DB Exception. Cannot retrieve user document'
    ERROR_LOGIN = 'Invalid user name or password'
    RESPONSE_LOGIN = '{"links": [{"url": "/users/{userId}/boards", "method" : "GET"},' \
                 '{"url": "/users/{userId}/boards", "method" : "POST"}]}'
    ERROR_SESSION = 'Invalid user session. Please login via "/users/login/" url'

    #User constants
    EMAIL = 'email'
    FIRST_NAME = 'firstName'
    DOCUMENT_ID = '_id'
    USER_ID = '{userId}'
    PASSWORD = 'password'
    EMAIL_REGEX = '\.|@'
    NORMALIZE_CHAR = '-'
    COOKIE_KEY = 'pinterest-user'

    #DB Constants
    WRITE_URL = "http://192.168.0.87:5984/pinterest"
    READ_URL = "http://192.168.0.87:5984/pinterest"
    CACHE_SIZE = 100

    #Board constants
    create_board_error = 'Error occurred while creating the board. Please try later'
    create_board_response = '{links:[{"url":"/users/{UserId}/boards/{boardName}","method":"GET"},' \
                            '{"url":"/users/{UserId}/boards/{boardName}","method":"PUT"},' \
                            '{"url":"/users/{UserId}/boards/{boardName},"method":"DELETE"},' \
                            '{"url":"/users/{UserId}/boards/{boardName}/pins","method":"POST"}]}'

    get_board_response = '{"board":{"boardName":"boardNameValue","boardDesc":"boardDescValue",' \
                         '"category":"categoryValue","isPrivate":"isPrivateValue"},' \
                         '"links":[{"url":"/users/{UserId}/boards/{boardName}","method":"PUT"},' \
                         '{"url":"/users/{UserId}/boards/{boardName}","method":"DELETE"},' \
                         '{"url":"/users/{UserId}/boards/{boardName}/pins","method":"POST"}]}'

    delete_board_response = '{"url":"/users/{UserId}/boards","method":"POST"}'

    get_boards_error = 'Error occurred while getting the list of boards'
    get_board_error = 'Error while fetching the board details'
    update_board_error = 'Error while updating the board'
    delete_board_error = 'Error while deleting the board'
    boards_empty_error = 'No boards created. Create new.'

    #pin constants
    create_pin_response ='{links:[{"url":"users/{UserId}/boards/{boardName}/pins/{pinId}","method":"GET"},' \
                        '{"url":"users/{UserId}/boards/{boardName}/pins/{pinId}","method":"PUT"},' \
                        '{"url":"users/{UserId}/boards/{boardName}/pins/{pinId},"method":"DELETE"}]}'
    
    add_comment_response ='{links:[{"url":"users/{UserId}/boards/{boardName}/pins/{pinId}/comments","method":"POST"},' \
                        '{"url":"users/{UserId}/boards/{boardName}/pins/{pinId}/comments/{addedby}/{comment},"method":"DELETE"}]}'
    add_comment_error = 'Error while adding comment'
    update_comment_error = 'Error while updating the comment'
    delete_comment_error = 'Error while deleting the comment' 

    USERID = '{UserId}'
    BOARD_NAME = '{boardName}'
    PIN_NAME = '{pinName}'
    ADDED_BY = '{addedBy}'
    HYPHEN = '-'
    WHITESPACE = ' '
    BOARDS = 'boards'
    BOARD_NAME_VALUE = 'boardNameValue'
    BOARD_DESC_VALUE = 'boardDescValue'
    CATEGORY_VALUE = 'categoryValue'
    IS_PRIVATE_VALUE = 'isPrivateValue'
    BOARDNAME = 'boardName'
    BOARD_DESC = 'boardDesc'
    CATEGORY = 'category'
    ISPRIVATE = 'isPrivate'
    PINS = 'pins'