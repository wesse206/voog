from multipledispatch import dispatch
import openpyxl
from connectDB import connectDB

class ImportTool():
    def __init__(self, path):
        self.header = True

        # Start Import Tool
        self.conn = self.connectDB()
        self.cursor = self.conn.cursor()
        self.book = openpyxl.load_workbook(path)

    def connectDB(self):
        conn = connectDB()
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

    def importLearners(self):
        print('starting import')
        fields = "grade, class, learner, learnerNumber, idnumber, subject, subjectGroup, subjectGroupEducator"
        self.loadSheet('Worksheet')
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
                values = f"'{Grade}', '{Class}', '{Learner}', '{LearnerNumber}', '{IDNumber}', '{Subject}', '{SubjectGroup}', '{SubjectGroupEducator}'"
                self.importToSQL('learnersImport', fields, values)

    def generateVoogList(self):
        self.cursor.execute('select distinct Learner, Class from learnersImport order by Class')
        learners = self.cursor.fetchall()

        self.cursor.execute("select TeacherCode from TeacherCodeMapping where TeacherCode != 'N/A'")
        teachers = self.cursor.fetchall()

        print(len(learners), teachers)
        for i in range(len(learners)):
            if learners[i][0].find('\'') > -1:
                learners[i][0] = learners[i][0][:learners[i][0].find('\'')] + '\'' + learners[i][0][learners[i][0].find('\''):]
                    

            self.cursor.execute(f"insert into VoogList (TeacherCode, LearnerName, LearnerClass) values ('{teachers[i % len(teachers)][0]}', '{learners[i][0]}', '{learners[i][1]}') ")

        self.cursor.commit()

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
