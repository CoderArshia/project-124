from flask import Flask, request,jsonify
import jinja2
app = Flask(__name__)
@app.route("/")


def hello():
    return "Arshia"

tasks = [
    {
        "id":1,
        "name":"arshia",
        "contact":1234567,
        "done":False
    },

        {
        "id":2,
        "name":"syeda",
        "contact":"9254922",
        "done":False
    },
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify ({
            "status":"error",
            "message":"please provide the data"
        },400)

    task = {
        "id":tasks[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact"),
        "done":False
            
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfuly"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
        


if __name__=="__main__":
    app.run()

