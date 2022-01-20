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
def get_specialist_doctors_list(Speciality, Salary): 
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sql_select_query = """select * from doctor where Speciality=%s and Salary > %s"""
            cursor.execute(sql_select_query, (Speciality, Salary))
            records = cursor.fetchall()
            print("Printing doctors whose specialty is", Speciality, "and salary greater than or equal to", Salary, "\n")
            for row in records:
                print("Doctor Id: ", row[0])
                print("Doctor Name:", row[1]) 
                print("Hospital Id:", row[2])
                print("Specialty:", row[3])
                print("Salary:", row[4])
                print("Experience:", row[5], "\n")
            close_connection(connection)
        except (Exception, mysql.connector.Error) as error:
            print("Error while getting data", error)
            
print("Question 3: Get Doctors as per given Speciality\n")
get_specialist_doctors_list("Cardiologist", 50000)