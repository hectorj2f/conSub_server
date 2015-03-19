import httplib

from common.log import logger

from service.api import message, topic
#from tornado import gen
from tornado.web import RequestHandler


class TopicHandler(RequestHandler):
    # POST HTTP method should redirect to this function with arguments /<topic>/<username>
    def post(self, topic, username):
        logger.info('Subscribe username {0} to topic {1} ...'.format(username, topic))

        try:
            topic.subscribe(username, topic)

            self.write("User subscribed")
            self.set_status(httplib.CREATED)
        except:
            self.set_status(httplib.BAD_REQUEST)


    # DELETE HTTP method should redirect to this function with arguments /<topic>/<username>
    def delete(self, topic, username):
        logger.info('Unsubscribing {0} from topic {1}'.format(topic, username))

        try:
            topic.unsubscribe(username, topic)

            self.write("Unsubscribed from topic")
            self.set_status(httplib.OK)
        except:
            self.set_status(httplib.BAD_REQUEST)


class MessageHandler(RequestHandler):
    # GET HTTP method /<topic>/<username>
    def get(self, topic, username):
        logger.info('Getting next message for {0} from topic {1}...'.format(username, topic))

        message = message.get_latest_message(username, topic)
        if message is None:
            self.set_status(httplib.NOT_FOUND)
        if message is None:
            self.set_status(NO_CONTENT)

        self.write("Message Get")
        self.set_status(httplib.OK)

    # POST HTTP method should publish a message in the topic /<topic>
    def post(self, topic):
        logger.info('Publish message {0} ...'.format(topic))

        self.write("Updated article {0}".format(self.request.body))

        message.add_message(topic, self.request.body)
        self.set_status(httplib.OK)