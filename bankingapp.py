from pymysql import connect
import os

connection = connect(
    host = os.getenv("MYSQL_HOST"),
    user = os.getenv("MYSQL_USER"),
    password = os.getenv("MYSQL_PASSWORD"),
    db = os.getenv("MYSQL_DATABASE"),
    charset = "utf8mb4"
)

def accountCreation():
    firstName = str(input("Insert your first name")),
    lastName = str(input("Insert your last name")),  
    return firstName, lastName

def accountStatus():
    withdrawAmount = int(input("How much do you want out?")),
    depositAmount = float(input("How much do you want to put it in?"),
    totalAmount = depositAmount - withdrawAmount,
    return withdrawAmount, depositAmount, totalAmount
                                   
try:
    with connection.cursor() as cursor:
        query = "SELECT * FROM accountDetail";
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)


    with connection.cursor() as cursor:
        query = "SELECT * FROM withdraw";
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)


    with connection.cursor() as cursor:
        query = "SELECT * FROM deposit";
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()
