import mysql.connector
import socket
import time
import os

MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_PORT = os.environ['MYSQL_PORT']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASS = os.environ['MYSQL_PASS']
MYSQL_DB = os.environ['MYSQL_DB']


def mysqlWait():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((MYSQL_HOST,int(MYSQL_PORT)))
    while result != 0:
        time.sleep(1)
        print("Retrying connection ...")
        result = sock.connect_ex((MYSQL_HOST,int(MYSQL_PORT)))
    sock.close()

def mysqlSchema():

    db_connection = mysql.connector.connect(
        host=MYSQL_HOST,
        port=int(MYSQL_PORT),
        user=MYSQL_USER,
        password=MYSQL_PASS,
        database=MYSQL_DB,
        auth_plugin="mysql_native_password"
    )

    db_cursor = db_connection.cursor()

    with open('/data/sql/schema-setup.sql') as fp:
        line = fp.readline()
        while line:
            if len(line) > 2:
                print("Executing line: " + line)
                db_cursor.execute(line)
            line = fp.readline()

def main():
    mysqlWait()
    mysqlSchema()

if __name__ == '__main__':
    main()