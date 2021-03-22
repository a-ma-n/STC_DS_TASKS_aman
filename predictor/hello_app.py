from flask import request
from flask import jsonify
from flask import Flask

app=Flask(__name__)

@app.route('/hello',methods=['POST'])
#post request to actually send the data to
#the server as well as recieve from the hello endpoint

def hello():
    message = request.get_json(force=True)
    #force accept even if unsure of daatatype

    #message takes in the value entered by the user
    # and then stores it and converts it to json format

    name=message['name']#key called name

    response={
        #variable defined called response
        'greeting' : 'Hello,' + name + '!'
    }
    return jsonify(response)
#we can place static files like html in static