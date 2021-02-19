import pyodbc
class sql_server:

    driver = "SQL Server Native Client 11.0"
    server = "localhost"
    database = "Stock_git"
    table = "stock_day"

    def __init__(self , data):
        self.connect()
        self.data = data

    def connect(self):
        connect = pyodbc.connect(
            "Driver={" + self.driver + "};"
            f"Server={self.server};"
            f"Database={self.database};"
            "Trusted_Connection=yes;"
        )
        self.cursor = connect.cursor()
    
    def setData(self):
        self.judgment_table(self.table)
        self.commit_data()

    def judgment_table(self , table_name):
        self.cursor.execute(
            f"IF EXISTS (SELECT * FROM sys.tables WHERE name = '{table_name}')\
                BEGIN\
                    SELECT switch FROM boolean_switch\
                    WHERE switch_type = 'switch_true'\
                END\
            ELSE\
                BEGIN\
                    SELECT switch FROM boolean_switch\
                    WHERE switch_type = 'switch_false'\
                END\
            "
        )
        if not self.cursor.fetchone()[0]:
            self.cursor.execute(
                f"CREATE TABLE {table_name}(\
                ID int PRIMARY KEY , stock_name varchar(50) ,\
                stock_ID varchar(50) , date date , securities_firm varchar(50) ,\
                buy int , sell int)"
            )
            self.cursor.commit()

    def commit_data(self):
        self.cursor.execute(f"SELECT MAX(ID) FROM {self.table}")
        ID_number = self.cursor.fetchone()[0]
        if ID_number == None:
            ID_number = 0
            
        for i in self.data[2][1 :]:

            ID_number += 1

            buy = int(i[1])
            sell = int(i[2]) 
            self.cursor.execute(
                f"INSERT INTO {self.table} VALUES(\
                    {ID_number} , '{self.data[0][1]}' , '{self.data[0][0]}' , '{self.data[1]}' , '{i[0]}' , {buy} , {sell} \
                )"
            )
            self.cursor.commit()

            ID_number += 1

            buy = int(i[5])
            sell = int(i[6])

            self.cursor.execute(
                f"INSERT INTO stock_day VALUES(\
                    {ID_number} , '{self.data[0][1]}' , '{self.data[0][0]}' , '{self.data[1]}' , '{i[4]}' , {buy} , {sell} \
                )"
            )
            self.cursor.commit()

    def sql_close(self):
        self.cursor.close()