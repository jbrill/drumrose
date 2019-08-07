import tornado.ioloop
import tornado.web

class RequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(self.request.body)
        self.write("Hello, world?")

    def post(self):
        postData = self.get_argument('data', 'No data')
        self.write(self.request.body)

def make_app():
    return tornado.web.Application([
        (r"/", RequestHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

