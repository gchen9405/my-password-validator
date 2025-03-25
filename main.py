import flask


# TODO: change this to your academic email
AUTHOR = "gordonc1@sas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # check if password length is valid 
    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "Password is too short"}), 400
    # check if at least 1 uppercase letter 
    if not any(x.isupper() for x in pw):
        return flask.jsonify({"valid": False, "reason": "Password does not contain an uppercase letter"}), 400
    # check if at least 1 digit 
    if not any(x.isdigit() for x in pw):
        return flask.jsonify({"valid": False, "reason": "Password does not contain a digit"}), 400
    # check if at least 1 special character
    if not any(not x.isalnum() for x in pw):
        return flask.jsonify({"valid": False, "reason": "Password does not contain a special character"}), 400
    else:
        return flask.jsonify({"valid": True, "reason": "is valid"})
