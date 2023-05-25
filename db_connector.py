from datetime import datetime
import pymysql
import sys

username = sys.argv[1]
password = sys.argv[2]

# Connect to DB and get cursor
def connect():
    conn = pymysql.connect(host='sql12.freemysqlhosting.net', port=3306, user=username, passwd=password,
                           db='sql12620882')
    conn.autocommit(True)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor

#Close Connection
def close_connection(cursor,conn):
    cursor.close()
    conn.close()

# Add user (row)
def add_user(user_id,user_name):
    conn, cursor = connect()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    sql_query = f"INSERT INTO users (user_id,user_name,creation_date)" + "\n" + f"VALUES (%s,%s,%s)"
    val = (int(user_id),user_name,dt_string)
    try:
        cursor.execute(sql_query, val)
        return "Row Added Successfully"
    except Exception as e:
        return "an error occurred" + str(e)
    close_connection(cursor, conn)

#Select all from table
def select_all_from_table():
    conn, cursor = connect()
    sql_query = f"SELECT * FROM users"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    close_connection(cursor, conn)

#Get user_name by user_id
def get_user_name_by_user_id(user_id):
    conn, cursor = connect()
    sql_query = "SELECT user_name FROM users WHERE user_id ='%s'"
    cursor.execute(sql_query % user_id)
    try:
        result = cursor.fetchone()
        return result['user_name']
    except:
        return "user_id doesn't exist"
    close_connection(cursor, conn)

#Update Username by user_id
def update_username(user_id,new_user_name):
    conn, cursor = connect()
    sql_query = "UPDATE users SET user_name=%s WHERE user_id='%s'"
    val=(new_user_name,int(user_id))
    cursor.execute(sql_query, val)
    try:
        cursor.fetchone()
        return "user_name updated successfully"
    except Exception as e:
        return "an error occurred" + str(e)
    close_connection(cursor, conn)

#Delete User (row) by user_id
def delete_user(user_id):
    conn, cursor = connect()
    sql_query = "Delete from users WHERE user_id='%s'"
    cursor.execute(sql_query % user_id)
    try:
        cursor.fetchone()
        return "User deleted successfully"
    except Exception as e:
        return "an error occurred" + str(e)
    close_connection(cursor, conn)

def main():
    select_all_from_table()

if __name__ == "__main__":
    main()
