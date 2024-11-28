import datetime
from multipledispatch import dispatch
import pyodbc
import openpyxl

class ImportTool():
    def __init__(self, path):
        # SQL Connection String
        self.SERVER = 'localhost\\SQLEXPRESS'
        self.DATABASE = 'voog'
        self.USERNAME = 'Voog'
        self.PASSWORD = 'HSD@123'
        self.connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.SERVER};DATABASE={self.DATABASE};UID={self.USERNAME};PWD={self.PASSWORD};Encrypt=no;'
        
        self.header = True

        # Start Import Tool
        self.conn = self.connectDB()
        self.cursor = self.conn.cursor()
        self.book = openpyxl.load_workbook(path)

    def connectDB(self):
        conn = pyodbc.connect(self.connectionString) 
        return conn
    
    @dispatch()
    def loadSheet(self):       
        sheet = self.book.active
        self.sheet = sheet
        return sheet
    
    @dispatch(str)
    def loadSheet(self, sheetname):
        sheet = self.book[sheetname]
        self.sheet = sheet
        return sheet

    def importToSQL(self, table, fields, values):
        self.cursor.execute(f"insert into {table} ({fields}) values ({values})")
        self.cursor.commit()

    def importTimeTable(self):
        fields = 'code, day, P1, P2, P3, P4, P5, P6'
        for i in range(8):
            self.loadSheet('Edu CTT D' + str(i + 1))
            for row in self.sheet:
                if self.header:
                    self.header = False
                else:
                    code = row[0].value
                    day = i + 1
                    P1 = row[1].value
                    P2 = row[2].value
                    P3 = row[3].value
                    P4 = row[4].value
                    P5 = row[5].value
                    P6 = row[6].value
                    values = f"'{code}', '{day}', '{P1}', '{P2}', '{P3}', '{P4}', '{P5}', '{P6}'"
                    self.importToSQL('timetableImport', fields, values)

    def importTeacherCodes(self):
        fields = "code, lastname"
        self.loadSheet()
        for row in self.sheet:
            if self.header:
                self.header = False
            else:
                code = row[0].value
                lastname = row[1].value
                if lastname.find('\'') > -1:
                    lastname = lastname[:lastname.find('\'')] + '\'' + lastname[lastname.find('\''):]
                values = f"'{code}', '{lastname}'"
                self.importToSQL('codesImport', fields, values)
                
    def cleanup(self):
        self.conn.close()
        self.book.close()

    def __str__(self):
        # self.cursor.execute('select * from test')
        # records = self.cursor.fetchall()

        # table = ''
        # for row in records:
        #     for field in row:
        #         table += f'{field}' + '\t'
        #     table += '\n'
        
        # return f'{table}'
        pass
