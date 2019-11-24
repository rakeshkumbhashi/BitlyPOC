from flask_restful import Resource
from flask import jsonify, request, redirect
from Models.Model import URLRep
import sys
import hashlib
import datetime

class URLRedirect(Resource):
    def get(self):
        shorturlUser = request.args.get('shorturl')
        desired_documents = URLRep.objects(shorturl=shorturlUser)
        responseURLDoc = desired_documents[0]

        longurl = responseURLDoc["longurl"]
        return redirect(longurl, code=302)
