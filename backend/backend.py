from flask import Flask, request, jsonify, render_template


import requests
import json
import os
# import predictionguard as pg


# url = "https://us-west-2.aws.data.mongodb-api.com/app/data-zfksj/endpoint/data/v1/action/findOne"
# mongoUri = "mongodb+srv://ashutoshpatil610:mBUQ728xrpss5T8G@bhojan.hiqnkos.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# mongo_client = MongoClient(mongoUri)
# db = mongo_client['cluster']  # Use your database name
# collection = db['db-tweets']  # Use your collection name

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return "Hello World"

@app.route('/postTweet', methods=['POST'])
def postTweet():
    data = request.get_json()
    print(data)
    if data['tweet']:
        if 'FlightTracker'.lower() in data['tweet'].lower():
            ec2IP = "<ec2-instance-public-ip>"
            topic_name = "<kafka-topic>"
            url = 'http://' + ec2IP + ':8082/topics/' + topic_name

            data = {"records":[
                    {"value":request.get_json()}
                    ]}
            # print(data)
            headers = {'Content-type': 'application/vnd.kafka.json.v2+json'}
            response = requests.post(url, json=data, headers=headers)
            return response.json()
            # print(response.json())
    return "response.json()",404

@app.route('/reply', methods = ['POST'])
def replyTweet():
    """ Reply to Tweets """
    print(request.form)
    data = request.form
    return reply.reply_toTweet(data['tweetId'], data['complain'], data['complain_type'], data['user'])
        
    
if __name__ == '__main__':
    app.run("0.0.0.0")
