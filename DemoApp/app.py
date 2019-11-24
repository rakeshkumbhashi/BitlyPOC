from flask import Blueprint
from flask_restful import Api
from resources.URLGenerator import URLGen
from resources.URLRedirect import URLRedirect

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(URLGen, '/URLGen')
api.add_resource(URLRedirect, '/URLRedirect')
