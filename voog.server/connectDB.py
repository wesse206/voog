import pyodbc
def connectDB():
    SERVER = 'localhost\\SQLEXPRESS'
    DATABASE = 'voog'
    USERNAME = 'voog'
    PASSWORD = 'HSD@123'
    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};Encrypt=no;'
    
    conn = pyodbc.connect(connectionString) 
    return conn
