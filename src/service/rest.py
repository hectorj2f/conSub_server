import httplib

from common.log import logger

from service.api import messages, topics
#from tornado import gen
from tornado.web import RequestHandler


class TopicHandler(RequestHandler):
    # POST HTTP method should redirect to this function with arguments /<topic>/<username>
    def post(self, topic, username):
        logger.info('Subscribe username {0} to topic {1} ...'.format(username, topic))

        try:
            topics.subscribe(username, topic)

            self.write("User subscribed!")
            self.set_status(httplib.CREATED)
        except Exception as error:
            logger.error(error)
            self.set_status(httplib.BAD_REQUEST)


    # DELETE HTTP method should redirect to this function with arguments /<topic>/<username>
    def delete(self, topic, username):
        logger.info('Unsubscribing {0} from topic {1}'.format(topic, username))

        try:
            topics.unsubscribe(username, topic)

            self.write("Unsubscribed from topic!")
            self.set_status(httplib.OK)
        except Exception as error:
            logger.error(error)
            self.set_status(httplib.BAD_REQUEST)

    # GET HTTP method /<topic>/<username>
    def get(self, topic, username=None):
        logger.info('Getting next message for {0} from topic {1}...'.format(username, topic))

        message, error_code = messages.get_latest_message(username, topic)
        if message is None:
            self.write("We couldn't get any message for you")
            self.set_status(error_code)
        else:
            self.write("Getting message {0}".format(message))
            self.set_status(httplib.OK)


class MessageHandler(RequestHandler):
    # GET HTTP method /<topic>/<username>
    def get(self, topic, username=None):
        logger.info('Getting next message for {0} from topic {1}...'.format(username, topic))

        message, error_code = messages.get_latest_message(username, topic)
        if message is None:
            self.write("We couldn't get any message for you")
            self.set_status(error_code)
        else:
            self.write("Getting message {0}".format(message))
            self.set_status(httplib.OK)

    # POST HTTP method should publish a message in the topic /<topic>
    def post(self, topic):
        logger.info('Publish message {0} ...'.format(topic))

        messages.add_message(topic, self.request.body)
        self.set_status(httplib.OK)

        self.write("Message published {0}!".format(self.request.body))
