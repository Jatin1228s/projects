import pyodbc

from AppApplicationconfig import properties


Driver = properties["Driver"]
Server = properties["Server"]
Database = properties["Database"]
Trusted_Connection = properties["Trusted_Connection"]
db_tbl = ""
query = "SELECT * FROM " + db_tbl

outputfile = open(properties["path_output_file"], 'r+')


class Establish_conection():
    def __init__(self, properties, query):
        self.properties = properties
        self.query = query

    def make_connection(self):
        try:

            conn = pyodbc.connect(Driver = properties("Driver"), Server = properties("Server"),Database = properties("Database"), Trusted_Connection = properties("TrustedConnection"))
        except pyodbc.DatabaseError:
            print("Could not connect to Database")
            return (False,pyodbc.DatabaseError)

        cursor = conn.cursor()
        print("Connection to Database successful")
        return (True, cursor)

    def extract_data(self):
        output = self.make_connection()
        if output[0]:
            cursor = output[1]
            row_count = cursor.execute(self.query).rowcount

            rows = cursor.execute(self.query).fetchall()

            if row_count != 0:
                return rows
            else:
                return 0
        else:
            print(output[1])



db_connection = Establish_conection()
records = db_connection.extract_data()


def write_csv(self):

    if records is not  None:
        if records !=0:
            print("No Records fetched from Databse")

    for entry in records:
        outputfile.write(entry)










