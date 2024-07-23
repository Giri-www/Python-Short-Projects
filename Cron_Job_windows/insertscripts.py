# import mysql.connector 
# from mysql.connector import Error
# from datetime import datetime

# def insert_func():
#     try:
#         connection = mysql.connector.connect(host = 'localhost',database = 'world',user = 'root',password = 'admin')
#         if connection.is_connected():
#             cursor = connection.cursor()
#             select_qry = f"""SELECT name FROM world.city;"""
#             cursor.execute(select_qry)
#             rows = cursor.fetchall()
#             current_time = datetime.now()
#             insert_data = [(row,current_time) for row in rows]
#             print(insert_data) 
                

#             qry = f"""INSERT INTO world.dev_tab (name,inserted_on) VALUES (%s, %s);"""
#             cursor.executemany(qry,insert_data)
#             connection.commit()
#             print("inserted sucessfully")
#         else:
#             print("Not connected...")
#     except Error as e:
#         print(f"Error :{e}")
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("ALL CLOSE ")
# if __name__ == '__main__':
#     insert_func()
import mysql.connector
from mysql.connector import Error
from datetime import datetime

def insert_func():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='world',
            user='root',
            password='admin'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            select_qry = "SELECT name FROM city;"
            cursor.execute(select_qry)
            rows = cursor.fetchall()
            current_time = datetime.now()
            
           
            insert_data = [(row[0], current_time) for row in rows]
            print(insert_data) 

            qry = "INSERT INTO dev_tab (name, inserted_on) VALUES (%s, %s);"
            cursor.executemany(qry, insert_data)
            connection.commit()
            print("=========  Inserted successfully =========")
        else:
            print("===== OOPSS!! Not connected... ======")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("------------ ALL CLOSED --------------------")

if __name__ == '__main__':
    insert_func()
