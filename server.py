import os
import socket
from flask import Flask, jsonify
from flask_gssapi import GSSAPI

# TODO Change to your path
os.environ["KRB5_KTNAME"] = "/home/senyaaa/Work/kerberos/kerberos-auth/flask.keytab"

app = Flask(__name__)

app.config['GSSAPI_HOSTNAME'] = 'localhost'
# Initialize Flask-GSSAPI
gssapi = GSSAPI(app)

@app.route('/protected')
@gssapi.require_auth()
def protected(username):
    return jsonify(message=f"You are authenticated as {username}")

@app.route('/')
def index():
    return jsonify(message="public page")



if __name__ == '__main__':
    fqdn = socket.getfqdn()
    print("Fully Qualified Domain Name (FQDN):", fqdn)
    app.run(host='127.0.0.1', port=5000, debug=True)
