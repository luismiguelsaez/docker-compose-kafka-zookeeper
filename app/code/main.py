import mysql.connector
import socket
import time
import os
import requests
import json

MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_PORT = os.environ['MYSQL_PORT']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASS = os.environ['MYSQL_PASS']
MYSQL_CONNECTOR_USER = os.environ['MYSQL_CONNECTOR_USER']
MYSQL_CONNECTOR_PASS = os.environ['MYSQL_CONNECTOR_PASS']
MYSQL_DB = os.environ['MYSQL_DB']
CONNECTOR_ENDPOINT = os.environ['CONNECTOR_ENDPOINT']
#CONNECTOR_PORT = os.environ['CONNECTOR_P0RT']


def connWait(whost,wport):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((whost,int(wport)))
    while result != 0:
        time.sleep(1)
        print("Retrying connection ...")
        result = sock.connect_ex((whost,int(wport)))
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

def createConnector():

    with open ("/data/api/connector.json", "r") as myfile:
        payload_data = myfile.readlines()

    payload_obj = json.loads(''.join(payload_data))

    payload_obj['config']['database.hostname'] = MYSQL_HOST
    payload_obj['config']['database.port'] = str(MYSQL_PORT)
    payload_obj['config']['database.user'] = MYSQL_CONNECTOR_USER
    payload_obj['config']['database.password'] = MYSQL_CONNECTOR_PASS
    payload_obj['config']['database.include.list'] = MYSQL_DB

    headers = { "Accept":"application/json", "Content-Type":"application/json" }

    r = requests.post("http://" + CONNECTOR_ENDPOINT + ":8083/connectors/", headers=headers, data=json.dumps(payload_obj))
    
    if r.status_code == 201:
        print("Endpoint created successfully")
    else:
        print("Error creating endpoint [" + str(r.status_code) + "]: " + r.text)

def main():
    connWait(MYSQL_HOST,MYSQL_PORT)
    mysqlSchema()
    createConnector()
    connWait(CONNECTOR_ENDPOINT,"8083")

if __name__ == '__main__':
    main()