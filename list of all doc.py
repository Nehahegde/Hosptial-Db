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
def get_hospital_name(HID):
 # Fetch Hospital Name using Hospital id
      try:
            connection = get_connection()
            cursor = connection.cursor()
            select_query = """select * from Hospital where Hospital_Id = %s"""
            cursor.execute(select_query, (HID,))
            record = cursor.fetchone()
            close_connection(connection)
            return record[1]
      except (Exception, mysql.connector.Error) as error:
            print("Error while getting data", error)
def get_doctors(HID):
 # Fetch Doctor Name using Hospital id
      try:
            Hosp_name = get_hospital_name(HID)
            connection = get_connection()
            cursor = connection.cursor()
            sql_select_query = """select * from Doctor where HID = %s"""
            cursor.execute(sql_select_query, (HID,))
            records = cursor.fetchall()
            print("Printing Doctors of ", Hosp_name, "Hospital")
            for row in records:
                  print("Doctor Id:", row[0])
                  print("Doctor Name:", row[1])
                  print("Hospital Id:", row[2])
                  print("Hospital Name:", hospital_name)
                  print("Specialty:", row[4])
                  print("Salary:", row[5])
                  print("Experience:", row[6], "\n")
            close_connection(connection)
      except (Exception, mysql.connector.Error) as error:
            print("Error while getting doctor's data", error)
print("Question 4: Get List of doctors of a given Hospital Id\n")
get_doctors(2)