from common.log import logger
from common.database import query


def subscribe(username, topic):
    logger.info('Subscribe username {0} to topic {1} ...'.format(username, topic))
    statement = "INSERT INTO subscriptors VALUES (?, ?)"
    data = (topic, username)

    query.add(statement, data)

def unsubscribe(username, topic):
    logger.info('Unsubscribe username {0} to topic {1} ...'.format(username, topic))
    statement = "DELETE FROM subscriptors WHERE username = ? and topic = ?"
    data = (username, topic)

    query.delete(statement, data)

def get_subscriptor(username, topic):
    logger.info('Get subscriptor username {0} to topic {1} ...'.format(username, topic))
    statement = "SELECT username FROM subscriptors WHERE username = ? AND topic = ?"
    data = (username, topic)

    result = query.find(statement, data)

    if len(result) > 0:
        return result[0][0]

    return None
