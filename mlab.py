
import mongoengine


#mongodb://<dbuser>:<dbpassword>@ds145168.mlab.com:45168/a-note

host = "ds145168.mlab.com"
port = 45168
db_name = "a-note"
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