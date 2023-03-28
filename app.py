from flask import Flask, render_template
import boto3

app = Flask(__name__)

@app.route("/")
def index():
    instance_id = get_instance_id()
    return render_template("index.html", instance_id=instance_id)

@app.route("/health")
def health_check():
    return "OK", 200

def get_instance_id():
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances()
    instance_id = response["Reservations"][0]["Instances"][0]["InstanceId"]
    return instance_id

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=80)