def get_db_uri(dbinfo):
    username = dbinfo.get('user') or "root"
    password = dbinfo.get('pwd') or "123456"
    host = dbinfo.get('host') or "localhost"
    port = dbinfo.get('port') or "3306"
    database = dbinfo.get('dbname') or "pythonixf"
    driver = dbinfo.get('driver') or "pymysql"
    dialect = dbinfo.get('dialect') or "mysql"

    return "{}+{}://{}:{}@{}:{}/{}".format(dialect,driver,username,password,host,port,database)



class Config():
    DEBUG = False
    TESTING = False
    SECRET_KEY = '110'
    SESSION_TYPE = 'redis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False



class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        "user": "root",
        "pwd": "123456",
        "host": "127.0.0.1",
        "port": "3306",
        "dialect": "mysql",
        "driver": "pymysql",
        "dbname": "pythonixf",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        "user": "root",
        "pwd": "123456",
        "host": "127.0.0.1",
        "port": "3306",
        "dialect": "mysql",
        "driver": "pymysql",
        "dbname": "pythonixf",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ShowConfig(Config):
    DEBUG = True

    DATABASE = {
        "user": "root",
        "pwd": "123456",
        "host": "127.0.0.1",
        "port": "3306",
        "dialect": "mysql",
        "driver": "pymysql",
        "dbname": "pythonixf",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DEBUG = True

    DATABASE = {
        "user": "root",
        "pwd": "123456",
        "host": "127.0.0.1",
        "port": "3306",
        "dialect": "mysql",
        "driver": "pymysql",
        "dbname": "pythonixf",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


config = {
    "developConfig" : DevelopConfig,
    "testingConfig" : TestingConfig,
    "showConfig" : ShowConfig,
    "productConfig" : ProductConfig,
    "default" : DevelopConfig,
}