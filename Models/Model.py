from mongoengine import *
from DemoApp import db
from datetime import datetime

class URLRep(db.Document):
    shorturl = StringField(max_length=20, null=False,required=True)
    creation_date = DateTimeField(default=datetime.utcnow, null=False)
    longurl = StringField(max_length=200, null=False)
    expirationTime = IntField(default=0)
    userId = LongField(default=100000)

    meta = {'collection': 'URLGen',
            'indexes': [
                'shorturl',
                'longurl'
                ]
            }

    def __init__(self, shorturl, longurl,*args, **kwargs):
        super(db.Document, self).__init__(*args, **kwargs)
        self.shorturl = shorturl
        self.longurl = longurl
