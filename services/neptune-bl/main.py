import json
import os

import tornado.web
import tornado.ioloop


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
        for slot in slots:
            values = slots[slot]["values"]
            for value in values:
                value["resolved"] = 1
                value["value"] = value["tokens"].capitalize()
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

