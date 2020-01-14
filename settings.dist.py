ENV = 'development'

# flask mail settings
MAIL_DEFAULT_SENDER = 'sender@localhost'

# project settings
PROJECT_PASSWORD_HASH_METHOD = 'pbkdf2:sha1'
PROJECT_SITE_NAME = u'Flask email service'
PROJECT_SITE_URL = u'http://127.0.0.1:5000'
PROJECT_SIGNUP_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds
PROJECT_RECOVER_PASSWORD_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds

DEFAULT_SENDER = 'test@local.lan'

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = 'no-reply@localhost'
MAIL_PASSWORD = '$3cREt'
MAIL_USE_TLS = False
MAIL_DEBUG = False

MAIL_SEND_DELAY = 300  # time in ms between query fetch. Default 300ms
