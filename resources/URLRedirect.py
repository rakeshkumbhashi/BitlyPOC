from flask_restful import Resource
from flask import jsonify, request, redirect
from Models.Model import URLRep
from flask_api import status


class URLRedirect(Resource):
    def get(self):
        shorturlUser = request.args.get('shorturl')
        if shorturlUser is None:
            return "ShortURL input parameter missing", status.HTTP_400_BAD_REQUEST

        desired_documents = URLRep.objects(shorturl=shorturlUser)

        if desired_documents.count() == 0:
            return "No long URL found for input shorturl", status.HTTP_404_NOT_FOUND

        responseURLDoc = desired_documents[0]

        longurl = responseURLDoc["longurl"]
        return redirect(longurl, code=302)
