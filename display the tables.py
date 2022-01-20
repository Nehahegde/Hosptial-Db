import mysql.connector
def get_connection():
      connection = mysql.connector.connect(host='localhost',
                                          database='hospital',
                                          user='root',
                                          password='')
      return connection
def close_connection(connection):
      if connection:
         connection.close()
def get_hospital_detail(HID):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where HID = %s"""
        cursor.execute(select_query, (HID,))
        records = cursor.fetchall()
        print("Printing Hospital record")
        for row in records:
            print("HOSPITAL-    ID:", row[0], )
            print("Hosp_Name:", row[1])
            print("Bed_Count:", row[2])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctor_detail(DID):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Doctor where DID = %s"""
        cursor.execute(select_query, (DID,))
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
print("Question 2: Read given hospital and doctor details \n")
get_hospital_detail(2)
print("\n")
get_doctor_detail(1)