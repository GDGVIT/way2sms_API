import tornado.ioloop
import tornado.web
from msg import msg

class MainHandler(tornado.web.RequestHandler):

    def post(self):

        username=self.get_argument("uname")
        password=self.get_argument("pswd")
        message=self.get_argument("msg")
        mobileNo=self.get_argument("mob")

        self.write(dict(Status = msg(username, password, message, mobileNo)))

#main fuction to start the API
if __name__ == "__main__":
	application = tornado.web.Application([ (r"/", MainHandler)], debug = True)
	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()
