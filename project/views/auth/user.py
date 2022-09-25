from flask_restx import Resource, Namespace

user_ns = Namespace("user")
@user_ns.route("/get_token")
class UserView(Resource):
    def get("")