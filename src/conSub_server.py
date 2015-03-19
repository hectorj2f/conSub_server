
from common.config import settings
from service.rest import TopicHandler, MessageHandler

from tornado.ioloop import IOLoop
from tornado.web import Application, url


def start_server():
   port = settings['tornado']['port']
   application = Application([
        url(r"/(.+)/(.+)", TopicHandler),
        url(r"/(.+)", MessageHandler),
        ], debug=True)

   application.listen(port)
   IOLoop.current().start()

if __name__ == "__main__":
   start_server()
