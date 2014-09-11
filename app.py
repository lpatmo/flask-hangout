# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!!!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	value = value + 89
	return "correct %s" % value 

@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	value = value + 5
	return "correct %g" % value

@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "linda":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found", 404

# start the development server using the run() method
if __name__ == "__main__":
	app.run()