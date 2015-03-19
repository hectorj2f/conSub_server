import psycopg2
import sys

from common import resources
from common.config import settings
from common.log import logger

initialization_script="""DROP TABLE IF EXISTS "subscriptors";
                        DROP TABLE IF EXISTS "messages";
                        CREATE TABLE "subscriptors" ("topic" text, "username" text);
                        CREATE TABLE "messages" ("topic" text, "username" text, "message" text, "created" timestamp default localtimestamp);
                        INSERT INTO "subscriptors" VALUES ('football','hector');
                        INSERT INTO "messages" VALUES ('football','hector', 'Viva Real Oviedo FC');
                        """

try:
    conn_string = "host='{0}' dbname='{1}' user='{2}' password='{2}'".format(settings['postgres']['db_host'],
                                                                             settings['postgres']['db_name'],
                                                                             settings['postgres']['db_user'],
                                                                             settings['postgres']['db_pwd'])
    postgresClient = psycopg2.connect(conn_string)

    cursor = postgresClient.cursor()
    cursor.execute(initialization_script)

    postgresClient.commit()
except (psycopg2.DatabaseError, Exception) as error:
    if postgresClient:
        postgresClient.rollback()

    print(error.message)
    sys.exit(1)
