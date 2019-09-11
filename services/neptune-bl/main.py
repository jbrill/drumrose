"""
Neptune's Business Logic Communciator
"""
import json
import os

import tornado.web
import tornado.ioloop


slot_name_map = [
    "_SUBJECT_TYPE_",
    "_SUBJECT_RELATIONSHIP_",
    "_SUBJECT_"
]

subject_types = ["track", "genre", "artist", "album"]
subject_relationships = ["from", "like", "similar to"]

def generate_suggestions(slots):
    """
    Generates a list of suggestions for specified slots
    """
    slots["_SUGGESTIONS_"] = {}
    for slot_name in slots:
        if slot_name not in slot_name_map:
            print("{} not recognized.".format(slot_name))
            return
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


class RequestHandler(tornado.web.RequestHandler):
    """
    Tornado Request Handler
    """
    def set_default_headers(self):
        """
        Override Default Headers For Responses
        """
        self.set_header("Content-Type", 'application/json')

    def get(self):
        """
        GET '/'
        - Placeholder
        """
        self.write("GET")

    def post(self):
        """
        POST '/'
        """
        data = tornado.escape.json_decode(self.request.body)
        print('data before')
        print(data)
        slots = data['slots']
        for slot_name in slots:
            values = slots[slot_name]["values"]
            for value in values:
                value["resolved"] = 1
                value["value"] = value["tokens"]
        generate_suggestions(slots)
        print('data after')
        print(data)
        self.write(data)

def make_app():
    """
    Tornado App Entrypoint
    """
    return tornado.web.Application([
        (r"/", RequestHandler),
    ])

if __name__ == "__main__":
    """
    Main Entrypoint
    """
    app = make_app()
    port = int(os.environ.get("PORT", 5000))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

