from flask_restful import Resource
from flask import jsonify, request
from flask_api import status
from Models.Model import URLRep
import sys
import hashlib
import datetime

class URLGen(Resource):
    def get(self):
        shorturlUser = request.args.get('shorturl')
        if shorturlUser is None:
            return "ShortURL input parameter missing", status.HTTP_400_BAD_REQUEST

        desired_documents = URLRep.objects(shorturl=shorturlUser)
        if desired_documents.count() ==0:
            return "No long URL found for input shorturl", status.HTTP_404_NOT_FOUND
        responseURLDoc = desired_documents[0]

        return jsonify(
            {
                "shorturl": responseURLDoc['shorturl'],
                "longurl": responseURLDoc["longurl"],
                "creation_date": responseURLDoc["creation_date"],
                "userId":responseURLDoc["userId"]
            }
        )

    def get_md5_bytes_as_base62(self,urlstring):
        digestStr = hashlib.md5(urlstring.encode('utf-8')).hexdigest()

        #Above is 32 char (2 char per byte so 128 bit hash)

        #Lets take only first 10 digits for shortness
        digestStr = digestStr[:10]

        md5int = int(digestStr, 16)

        #Add current micro seconds to bring uniqueness
        md5int += datetime.datetime.now().microsecond
        return self.base62_encode_i(md5int)

    def base62_encode_i(self,dec):
        s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ret = ''
        while dec > 0:
            ret = s[dec % 62] + ret
            dec = int(dec/62)
        return ret


    def post(self):
        print(str(request.data), sys.stderr)

        json_data = request.get_json(force=True)
        longurl = json_data["longurl"]
        shorturl = "http://" + self.get_md5_bytes_as_base62(longurl)


        try:
            #data= paste_schema.loads(request.data)
            urlrep = URLRep(shorturl, json_data["longurl"])
            urlrep.save()
        except Exception as e:
            return str(e), 422

        return jsonify({ "shorturl" : shorturl, "longurl": json_data['longurl'] })

