from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/")
def index():
    instance_id = get_instance_id()
    return render_template("index.html", instance_id=instance_id)

@app.route("/health")
def health_check():
    return "OK", 200

def get_instance_id():
    r = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
    instance_id = r.text
    return instance_id

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)