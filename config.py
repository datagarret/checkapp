
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    if os.environ.get('GAE_INSTANCE'):
        pass
    else:
        load_dotenv(os.path.join(basedir, '.env'))

    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PROJECT_ID = os.environ['PROJECT_ID']
    CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']

    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_NAME = os.environ['DB_NAME']
    CLOUDSQL_CONNECTION_NAME = os.environ['CLOUDSQL_CONNECTION_NAME']

    REDCAP_URL = os.environ['REDCAP_URL']
    HARMONY_TOKEN = os.environ['HARMONY_TOKEN']

    # Alternatively, you could use a local MySQL instance for testing.
    LOCAL_SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'check.db')

    # When running on App Engine a unix socket is used to connect to the cloudsql
    # instance.
    LIVE_SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@localhost/{database}'
        '?unix_socket=/cloudsql/{connection_name}').format(
            user=DB_USER, password=DB_PASSWORD,
            database=DB_NAME, connection_name=CLOUDSQL_CONNECTION_NAME)

    if os.environ.get('GAE_INSTANCE'):
        SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
    else:
        SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI
