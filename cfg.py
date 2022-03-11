class ProductionConfig:
    # Edit from here:
    DEBUF = False
    HOST = {YOUR IP ADDRESS}
    PORT = 17300
    SECRET_KEY = "Ane;ri-qlklqe/dw?ckjnwl_lw"

    # SQL
    SQLALCHEMY_DATABASE_URI= "mysql://{ACCOUNT}:{PASSWORD}@127.0.0.1/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYSQL_DATABASE_CHARSET = 'utf8mb4'
    AUTHY_API_KEY = "r1jjy98p51MSFQT681w99LDW3XCjezt6"

class DevelopmentConfig:
    # Don't modify here!
    DEBUG = True
    # Flask
    HOST = {YOUR IP ADDRESS}
    PORT = 17400
    SECRET_KEY = "Sln;uh-pl;lOP/dw?ckjnwl_qq"
    
    # SQL
    SQLALCHEMY_DATABASE_URI= "mysql://{ACCOUNT}:{PASSWORD}@127.0.0.1/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYSQL_DATABASE_CHARSET = 'utf8mb4'

    AUTHY_API_KEY = "r1jjy98p51MSFQT681w99LDW3XCjezt6"
    

