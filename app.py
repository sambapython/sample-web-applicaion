from flask import Flask, render_template,request
import logging
from db_structure import get_conn, close_conn
logging.basicConfig(filename="log.txt",
					format="%(asctime)s->%(levelname)s->%(message)s")

app = Flask(__name__)
logging.info("App instace created")

@app.route("/")
def home():
	logging.info("calling / url")
	return render_template("home.html")

@app.route("/signup/")
def signup():
	msg=""
	logging.info("calling /signup/ url")
	if request.method=="POST":
		data  = request.form
		logging.debug("form data: %s"%data)
		con,cur = get_conn()
		cur.execute("insert into users values()")


	return render_template("signup.html",msg=msg)


if __name__ == "__main__":
	app.run(debug=True)