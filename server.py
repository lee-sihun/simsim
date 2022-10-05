import pymysql


def db_connect():
    conn = pymysql.connect(host='127.0.0.1', user='root',
                           password='0000', db='simsim', charset='utf8')
    return conn


def insert_data(conn, qs, ans):
    cursor = conn.cursor()
    query = "INSERT INTO Text VALUES ('"+qs+"','"+ans+"')"
    cursor.execute(query)
    conn.commit()


def search_data(conn):
    cursor = conn.cursor()
    query = "SELECT qs,ans FROM Text"
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def db_disconnect(conn):
    conn.close()
