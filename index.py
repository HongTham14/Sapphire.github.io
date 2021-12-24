from datetime import datetime
#from os import name
from flask import Flask, app, render_template

app = Flask(__name__)


@app.route('/xinchao/<tenPy>')
def xinchao():

    return render_template('index.html')




if __name__ == "main":
    app.run(port=5050)
