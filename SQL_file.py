import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="netthmvopidli123",
    database="yoma"
)

# Initialise the cursor
mycursor = mydb.cursor()


# CREATE TABLE customerInfo
# (
# id INT AUTO_INCREMENT PRIMARY KEY,
# firstName VARCHAR(255),
# lastName VARCHAR(255),
# contactNumber VARCHAR(255),
# program VARCHAR(255),
# PTName VARCHAR(255)
# )

# mycursor.execute("CREATE DATABASE yoma1")

# mycursor.execute("""CREATE TABLE customerInfo18
#                      (
#                      id INT AUTO_INCREMENT PRIMARY KEY,
#                      firstName VARCHAR(255),
#                      lastName VARCHAR(255),
#                      contactNumber VARCHAR(255),
#                      program VARCHAR(255),
#                      PTName VARCHAR(255)
#                      )"""
#                  )


def createRecord(details):
    """
    Arguments:
         details: A dictionary with all the information of the newly registered user except the PRIMARY KEY.
    Returns:
    """

    # details = ["firstName", "lastName", "contactNumber", "program", "PTName"]

    insertCommand = """INSERT INTO customerInfo18 
                    (firstName, lastName, contactNumber, program, PTName) 
                    VALUES (%s, %s, %s, %s, %s)"""

    details = tuple(detail for detail in details.values())
    mycursor.execute(insertCommand, details)
    mydb.commit()

    selectCommand = """SELECT MAX(id)
                        FROM customerInfo18
                        """

    mycursor.execute(selectCommand)

    results = mycursor.fetchall()

    for result in results:
        uniqueGymCode = result[0]

    return uniqueGymCode


def validateCode(code):
    code = int(code)

    selectCommand = """SELECT COUNT(id)
                        FROM customerInfo18
                        WHERE id = %s """

    mycursor.execute(selectCommand, (code,))
    data = mycursor.fetchall()

    if len(data) != 0:
        return True


def retrieveDetails(uniqueGymCode):

    columns = ("id", "firstName", "lastName", "contactNumber", "program", "PTName")
    selectCommand = """SELECT *
                            FROM customerInfo18
                            WHERE id = %s"""

    mycursor.execute(selectCommand, (uniqueGymCode,))
    results = mycursor.fetchall()

    details = {}
    for result in results:
        for idx in range(len(result)):
            print(f"{columns[idx]} =  {result[idx]}")
            details[columns[idx]] = result[idx]

    return details


def updateRecord(details):
    """
    Arguments:
         details: A dictionary with all the information of the newly registered user.
    Returns:
    """

    colsExceptKey = ["firstName", "lastName", "contactNumber", "program", "PTName"]

    insertCommand = """UPDATE customerInfo18 
                        SET firstName = %s, lastName = %s, contactNumber = %s, program = %s, PTName = %s 
                        WHERE id = %s"""

    detailsAndKey = tuple(details[col] for col in colsExceptKey) + (details["id"],)
    mycursor.execute(insertCommand, detailsAndKey)
    mydb.commit()


