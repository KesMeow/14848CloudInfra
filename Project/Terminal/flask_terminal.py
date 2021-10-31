from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():

    msg = "\t****************************************************" + \
    "\t***  Welcome to the Big Data Processing Toolbox  ***" + \
    "\t****************************************************"
    return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0')