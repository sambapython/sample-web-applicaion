import yaml
import psycopg2
import logging
from constants import SUCCESS_INSERT, SUCCESS_UPDATE, ERROR_INSERT
f=open("config.yaml")
con_data = yaml.load(f)['database']

class db:
	def __init__(self):
		self.host = con_data['host']
		self.user = con_data['user']
		self.password = con_data['password']
		self.port = con_data['port']
		self.con, self.cur = get_con()

    def create(self, data):
    	try:
	    	columns = data.keys()
	    	values = data.values()
	    	q = "insert into %s %s values(%s)"%(data.table_name, columns, values)
	    	self.cur.execute(q)
	    	return True, SUCCESS_INSERT

	    except Exceptioon as err:
	    	logging.exception("%s"%err)
	    	return False, ERROR_INSERT

	def close(self):
		self.con.close()
		self.cur.close()

	def commit(self):
		self.con.commit()

if __name__ == "__main__":
	db1=db()
	db1.cur.execute("create table student(id int primary key, name varchar(250) not null, \
		password varchar(10), registered_date TIMESTAMP, login_date TIMESTAMP null, phone varchar(10) unique not null)")
	db1.commit()
	db1.close()
