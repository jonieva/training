from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps


class GitFailedStatus(Resource):
    def get(self):
        return {
          "state": "failure",
          "target_url": "https://kk.com:5000/git_response",
          "description": "Manual response"
        }

if __name__ == '__main__':
    app = Flask(__name__)
    app.config["SERVER_NAME"] = "kk.com:5000"
    api = Api(app)
    api.add_resource(GitFailedStatus, '/git')
    app.run(host='0.0.0.0')
