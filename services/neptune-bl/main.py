import json
import os

import tornado.web
import tornado.ioloop


slot_name_map = {
    'tune': 'tune',
    'tunes': 'tune',
    'songs': 'tune',
    'tracks': 'tune',
    'music': 'tune',
    'albums': 'album'
}

def parse_value(slot_name, slot_value):
    """Parse slot value"""
    print("PARSING {} for {}".format(slot_value, slot_name))
    if slot_name not in slot_name_map:
        print("SLOT NAME NOT IN MAP")

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
                parse_value(slot_name, value["value"])
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

