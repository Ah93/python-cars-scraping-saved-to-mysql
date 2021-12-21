import pymysql
import mysql.connector

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='cars',
    port=3306
)


def insertScrapedCars(CarsToInsert):
    try:
        mySql_insert_query = """INSERT INTO cars_details (name, mileage, dealer_name, rating, rating_count, price) 
                            VALUES (%s, %s, %s, %s, %s, %s) """

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, CarsToInsert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into cars_details table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        connection.close()