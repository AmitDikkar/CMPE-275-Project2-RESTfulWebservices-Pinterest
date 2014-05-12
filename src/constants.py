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
    WRITE_URL = "http://127.0.0.1:5984/pinterest"
    READ_URL = "http://127.0.0.1:5984/pinterest"
    CACHE_SIZE = 100