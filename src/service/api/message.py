

from common.database import query


def add_message(topic, message):
    statement = "SELECT username FROM subscriptors WHERE topic = %s"
    data = (topic)

    users = query.find(statement, data)

    for user in users:
        statement = "INSERT INTO messages VALUES ('%s','%s')"
        data = (topic, user[0])

        query.add(statement, data)

def get_latest_messsage(username, topic):
    statement = "SELECT topic, username, message, created FROM messages WHERE username = %s AND topic = %s ORDER BY created"
    data = (username, topic)

    messages = query.find(statement, data)

    for msg in messages:
        print msg[0], msg[1], msg[2], msg[3]
