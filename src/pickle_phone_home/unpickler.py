"""
An unpickling webserver for medicinal purposes.

Base on sample code from
https://davidhamann.de/2020/04/05/exploiting-python-pickle/

NOTE:
Currently not working.

Testing the code with e.g
curl -d "pickled=gASVbgAAAAAAAACMBX..." http://127.0.0.1:5000/unpickle
results in the error message: 
_pickle.UnpicklingError: pickle data was truncated
"""

import pickle
import base64
from flask import Flask, request


app = Flask(__name__)


@app.route("/unpickle", methods=["POST"])
def unpickle():
    form_data = request.form["pickled"]
    print(form_data)
    decoded_data = base64.urlsafe_b64decode(form_data)
    print(decoded_data)
    deserialized = pickle.loads(decoded_data)
    
    # you got hacked!

    return "", 204

if __name__ == "__main__":
    app.run()