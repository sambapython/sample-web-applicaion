from db_structure import db
from datetime import datetime
import logging
class student(db):
    def __init__(self, **kwargs):
        self.table_name = "student"
        self.id=kwargs.get("id")
        self.name=kwargs.get("name")
        self.phone = kwargs.get("phone")
        self.registered_date = kwargs.get("registered_date") or datetime.now()
        self.login_date = kwargs.get("login_date")
        self.logoff_date = kwargs.get("logoff_date")
        
    def create(self):
        status, msg = db.create(self, self.__dict__)
        logging.debug("student insertion: status: %s, msg: %s"%(status, msg))
        if status:
            self.browse(phone=self.phone)
        else:
            return status, msg
        
    def update(self):
        pass
    def browse(self):
        pass
s1=student()
print s1.__dict__

