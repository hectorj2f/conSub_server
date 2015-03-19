
from common.database import query


def subscribe(username, topic):
    statement = "INSERT INTO subscriptors VALUES ('%s','%s')"
    data = (topic, username)

    query.add(statement, data)

def unsubscribe(username, topic):
    statement = "DELETE subscriptors WHERE username = %s and topic = %s"
    data = (username, topic)

    query.delete(statement, data)

def get_subscriptor(username, topic):
    statement = "SELECT username FROM subscriptors WHERE username = %s AND topic = %s"
    data = (username, topic)

    result = query.find(statement, data)

    if len(result) > 0:
        return result[0][0]

    return None
