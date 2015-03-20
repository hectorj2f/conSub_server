#import psycopg2
import sqlite3
import sys

from common import resources
from common.config import settings
from common.log import logger

#CREATE TABLE "messages" ("topic" text, "username" text, "message" text, "created" timestamp default localtimestamp);
initialization_script="""DROP TABLE IF EXISTS "subscriptors";
                        DROP TABLE IF EXISTS "messages";
                        CREATE TABLE "subscriptors" ("topic" text, "username" text);
                        CREATE TABLE "messages" ("topic" text, "username" text, "message" text, "created" timestamp default current_timestamp not null);
                        INSERT INTO "subscriptors" VALUES ('football','hector');
                        INSERT INTO "messages" VALUES ('football','hector', 'Viva Real Oviedo FC', '2010-08-28T13:40:02.200');
                        """

try:
    conn_string = "host='{0}' dbname='{1}' user='{2}' password='{2}'".format(settings['postgres']['db_host'],
                                                                             settings['postgres']['db_name'],
                                                                             settings['postgres']['db_user'],
                                                                             settings['postgres']['db_pwd'])
    #postgresClient = psycopg2.connect(conn_string)
    postgresClient = sqlite3.connect(settings['sqlite']['db_name'])
    cursor = postgresClient.cursor()
    cursor.executescript(initialization_script)

    postgresClient.commit()
except Exception as error:
    #if postgresClient:
    #    postgresClient.rollback()

    print(error.message)
    sys.exit(1)
#except (psycopg2.DatabaseError, Exception) as error:
