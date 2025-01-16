import datetime
import pyodbc
import openpyxl

class ImportTool():
    def __init__(self, path=None):
        # SQL Connection String
        self.SERVER = 'localhost\\SQLEXPRESS'
        self.DATABASE = 'voog'
        self.USERNAME = 'Voog'
        self.PASSWORD = 'HSD@123'
        self.connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.SERVER};DATABASE={self.DATABASE};UID={self.USERNAME};PWD={self.PASSWORD};Encrypt=no;'
        
        # File Selector
        self.path = path
        self.header = True

        # Start Import Tool
        print('Starting import of', path)
        self.conn = self.connectDB()
        self.cursor = self.conn.cursor()
        self.sheet = self.loadSheet()
        self.importToSQL()
        print('Completed import of', path)

        # Cleanup
        self.conn.close()
        self.book.close()

    def connectDB(self):
        conn = pyodbc.connect(self.connectionString) 
        return conn
    
    def loadSheet(self):
        self.book = openpyxl.load_workbook(self.path)
        sheet = self.book.active
        return sheet

    def importToSQL(self):
        now = datetime.datetime.now()
        now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        for row in self.sheet:
            if self.header:
                self.header = False
            else:
                Grade = row[0].value
                Class = row[1].value
                Learner = row[2].value
                LearnerNumber = row[3].value
                IDNumber = row[4].value
                Subject = row[16].value
                SubjectGroup = row[18].value
                SubjectGroupEducator = row[19].value

                if Learner.find('\'') > -1:
                    Learner = Learner[:Learner.find('\'')] + '\'' + Learner[Learner.find('\''):]
                if SubjectGroupEducator.find('\'') > -1:
                    SubjectGroupEducator = SubjectGroupEducator[:SubjectGroupEducator.find('\'')] + '\'' + SubjectGroupEducator[SubjectGroupEducator.find('\''):]

                self.cursor.execute(f"insert into learnersImport (Grade, Class, Learner, LearnerNumber, IDNumber, Subject, SubjectGroup, SubjectGroupEducator) values ('{Grade}', '{Class}', '{Learner}', '{LearnerNumber}', '{IDNumber}', '{Subject}', '{SubjectGroup}', '{SubjectGroupEducator}')")

                self.cursor.commit()

    def __str__(self):
        self.cursor.execute('select * from test')
        records = self.cursor.fetchall()

        table = ''
        for row in records:
            for field in row:
                table += f'{field}' + '\t'
            table += '\n'
        
        return f'{table}'
