import json
import os

import tornado.web
import tornado.ioloop

"""
    'tune': 'tune',
    'tunes': 'tune',
    'songs': 'tune',
    'tracks': 'tune',
    'music': 'tune',
    'albums': 'album'
"""

action_type_mappings = []
subject_type_mappings = {
    'genre': ['house', 'jazz', 'rock'],
    'artist': ['artist', 'composer', 'albums'],
    'album': ['albums', 'albums'],
    'track': ['song', 'tune', 'tunes', 'songs']
}
subject_relationship_mappings = []
subject_mappings = []

slot_name_map = {
    "_SUBJECT_TYPE_": subject_type_mappings,
    "_SUBJECT_RELATIONSHIP_": subject_relationship_mappings,
    "_SUBJECT_": subject_mappings,
}

def generate_response(slots):
    """Parse slot value"""
    slots["_SUGGESTIONS_"] = {}
    for slot_name in slots:
        if slot_name not in slot_name_map:
            print("SLOT NAME NOT IN MAP")
    if not "_SUBJECT_TYPE_" in slots:
        print("NO SUBJECT TYPE")
        if "_SUBJECT_" in slots:
            print("SUBJECT BUT NO SUBJECT TYPE")
            print("SHOULD RECOMMEND TRACKS FROM THAT SUBJECT")
    elif not "_SUBJECT_" in slots:
        print("NO SUBJECT")
        if "_SUBJECT_TYPE_" in slots:
            print("SUBJECT TYPE BUT NO SUBJECT")
    else:
        print("SUBJECT AND SUBJECT_TYPE")
        subject_type = slots["_SUBJECT_TYPE_"]
        subject = slots["_SUBJECT_"]
        if subject_type["values"][0]["track"] != "NULL":
            print("FIND TRACK FOR SUBJECT")
            slots["_SUGGESTIONS_"]["type"] = "track"
            slots["_SUGGESTIONS_"]["resolved"] = 1
            slots["_SUGGESTIONS_"]["values"] = [
                {
                    "value": "The Motto by Drake", 
                    "resolved": 1,
                },
                {
                    "value": "Sound and Vision by David Bowie",
                    "resolved": 1,
                }
            ]
        elif subject_type["values"][0]["album"] != "NULL":
            print("FIND ALBUM FOR SUBJECT")
            slots["_SUGGESTIONS_"]["type"] = "album"
            slots["_SUGGESTIONS_"]["resolved"] = 1
            slots["_SUGGESTIONS_"]["values"] = [
                {
                    "value": "Take Care by Drake", 
                    "resolved": 1,
                },
                {
                    "value": "Low by David Bowie",
                    "resolved": 1,
                }
            ]
    # Account for slot mapping hit
    pass

class RequestHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')

    def get(self):
        self.write("GET")

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        print('data before')
        print(data)
        slots = data['slots']
        for slot_name in slots:
            values = slots[slot_name]["values"]
            for value in values:
                value["resolved"] = 1
                value["value"] = value["tokens"]
        generate_response(slots)
        print('data after')
        print(data)
        self.write(data)

def make_app():
    return tornado.web.Application([
        (r"/", RequestHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    port = int(os.environ.get("PORT", 5000))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

