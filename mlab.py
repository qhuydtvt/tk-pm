
import mongoengine


#mongodb://<dbuser>:<dbpassword>@ds035643.mlab.com:35643/tk-pm

host = "ds035643.mlab.com"
port = 35643
db_name = "tk-pm"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())