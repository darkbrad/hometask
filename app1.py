import json

from flask import Flask,render_template


app = Flask(__name__)
with open("data.json") as file:
    schedule=json.load(file)
print(schedule)
@app.route("/")
def hello():
    return render_template("main.html",schedule=schedule)

if __name__=='__main__':
    app.run(debug=True)