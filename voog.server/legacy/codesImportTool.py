import datetime
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
        for row in self.sheet:
            if self.header:
                self.header = False
            else:
                code = row[0].value
                voog = row[1].value
                buddy = row[2].value
                title = row[3].value
                lastname = row[4].value

                if lastname.find('\'') > -1:
                    lastname = lastname[:lastname.find('\'')] + '\'' + lastname[lastname.find('\''):]

                self.cursor.execute(f"insert into codesImport (code, voog, buddy, title, lastname) values ('{code}', '{voog}', '{buddy}', '{title}', '{lastname}')")

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
