import mysql.connector

def mysqlSchema():

    db_connection = mysql.connector.connect(
        host="mysql",
        user="debezium",
        password="debeziumpass",
        database="communication",
        auth_plugin="mysql_native_password"
    )

    db_cursor = db_connection.cursor()

    with open('/data/sql/schema-setup.sql') as fp:
        line = fp.readline()
        while line:
            if len(line) < 2:
                db_cursor.execute(line)
            line = fp.readline()

def main():
    mysqlSchema()

if __name__ == '__main__':
    main()