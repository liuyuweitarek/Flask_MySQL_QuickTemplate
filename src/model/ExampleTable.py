import uuid
from app import sqldb as db
from datetime import datetime
from sqlalchemy import text

class Example_Table(db.Model):
    __tablename__ = 'example_table'
    __table_args__ =  {'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_unicode_ci'}
    pid = db.Column(db.String(36), default=lambda: str(uuid.uuid4()), primary_key=True)
    example_string = db.Column(db.String(40), nullable=False)
    example_timestamp = db.Column(db.DateTime, nullable=False)
    example_int = db.Column(db.Integer, nullable=False)
    
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now,default=datetime.now)


    def __init__(self,example_string, example_timestamp, example_int):
        self.example_string = example_string
        self.example_timestamp = example_timestamp
        self.example_int = example_int
