
from common.log import logger
from common.database.connection import postgresClient


def find(query, data):
    try:
        cursor = postgresClient.cursor()
        cursor.execute(query, data)
        values = cursor.fetchall()

        logger.debug(values)

        return values

    except Exception as error:
        logger.error(error.message)
        raise

def add(query, data):
    try:
        cursor = postgresClient.cursor()
        cursor.execute(query, data)
        postgresClient.commit()

    except Exception as error:
        postgresClient.rollback()
        logger.error(error.message)
        raise

def delete(query, data):
    try:
        cursor = postgresClient.cursor()
        cursor.execute(query, data)
        postgresClient.commit()

    except Exception as error:
        postgresClient.rollback()
        logger.error(error.message)
        raise
