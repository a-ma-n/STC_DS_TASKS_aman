from flask import Flask
app = Flask(__name__)# instance of flask class ,name of appplications module if we use a single module like here


@app.route('/')
#decorator tells flask url user has to browse thorgh in order for fn underneath to be called
def running():
    return 'aman  was here !'
#returns flask is running when the user enters
