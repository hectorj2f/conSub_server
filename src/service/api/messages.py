import datetime
import httplib

from common.log import logger
from common.database import query
from service.api import topics


def add_message(topic, message):
    logger.info('Add message {0} to topic {1} ...'.format(message, topic))
    statement = "SELECT username FROM subscriptors WHERE topic = ?"
    data = (topic, )

    users = query.find(statement, data)

    for user in users:
        statement = "INSERT INTO messages VALUES (?, ?, ?, ?)"
        time = datetime.datetime.now()
        data = (topic, user[0], message, time)

        query.add(statement, data)

def get_latest_message(username, topic):
    logger.info('Get latest message for username {0} to topic {1} ...'.format(username, topic))

    if topics.get_subscriber(username, topic) is None:
        return None, httplib.NOT_FOUND

    statement = "SELECT message FROM messages WHERE username = ? AND topic = ? ORDER BY created"
    data = (username, topic)

    messages = query.find(statement, data)

    for msg in messages:
        print msg[0]
        return (msg[0], None)

    return (None, httplib.NO_CONTENT)
