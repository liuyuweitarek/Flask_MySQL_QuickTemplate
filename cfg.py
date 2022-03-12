class ProductionConfig:
    # Edit from here:
    DEBUG = False
    HOST = {YOUR IP ADDRESS}
    PORT = {PORT which is available on your machine}
    SECRET_KEY = "Ane;ri-qlklqe/dw?ckjnwl_lw"

    # SQL
    SQLALCHEMY_DATABASE_URI= "mysql://{ACCOUNT}:{PASSWORD}@127.0.0.1/{DATABASE_NAME}_prod"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYSQL_DATABASE_CHARSET = 'utf8mb4'
    AUTHY_API_KEY = "r1jjy98p51MSFQT681w99LDW3XCjezt6"

class DevelopmentConfig:
    # Don't modify here!
    DEBUG = True
    # Flask
    HOST = {YOUR IP ADDRESS}
    PORT = {PORT which is available on your machine}
    SECRET_KEY = "Sln;uh-pl;lOP/dw?ckjnwl_qq"
    
    # SQL
    SQLALCHEMY_DATABASE_URI= "mysql://{ACCOUNT}:{PASSWORD}@127.0.0.1/{DATABASE_NAME}_dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYSQL_DATABASE_CHARSET = 'utf8mb4'

    AUTHY_API_KEY = "r1jjy98p51MSFQT681w99LDW3XCjezt6"
    

