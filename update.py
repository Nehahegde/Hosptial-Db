import mysql.connector
import datetime
#from dateutil.relativedelta import relativedelta
def get_connection():
      connection = mysql.connector.connect(host='localhost',
                                          database='hospital',
                                          user='root',
                                          password='')
      return connection
def close_connection(connection):
      if connection:
         connection.close()

def update_doctor_experience(Experience,DID):
 # Update Doctor Experience in Years
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """update doctor set Experience = %s where DID =%s"""
        cursor.execute(sql_select_query, (Experience, DID))
        connection.commit()
        print("Doctor Id:", DID, " Experience updated to ", Experience, " years")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting doctor's data", error)
print("Question 5: Update experience of all doctors \n")
update_doctor_experience(10,1)
