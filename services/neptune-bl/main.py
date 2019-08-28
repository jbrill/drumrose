import tornado.ioloop
import tornado.web

import os


class RequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(self.request.body)
        self.write("Hello, world?")

    def post(self):
        self.write(self.request.body)

def make_app():
    return tornado.web.Application([
        (r"/", RequestHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    port = int(os.environ.get("PORT", 5000))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

