from connectDB import connectDB
class APICalls():
    def __init__(self):
        self.conn = connectDB()
        self.cursor = self.conn.cursor()

    # def useDB(func):
    #     def CreateConnection(self, *args, **kwargs):
    #         self.conn = connectDB()
    #         self.cursor = self.conn.cursor()
    #         result = func(self, *args, **kwargs)
    #         self.cursor.close()
    #         self.conn.close()
    #         return result

    #     return CreateConnection

    def formatData(self):
        columns = [column[0] for column in self.cursor.description]
        data = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        return data

    def getTeacherlessLearners(self, TeacherCode, Day):
        self.cursor.execute(f"exec TeacherAbsentLookup '{TeacherCode}', {Day}")
        return self.formatData()

    def getAbsentTeachers(self):
        self.cursor.execute(f"exec TeacherAbsentGet")
        return self.formatData()

    def setAbsentTeacher(self, TeacherCode, Day):
        self.cursor.execute(f"exec TeacherAbsentAdd '{TeacherCode}', {Day}")
        self.cursor.commit()
        return self.getAbsentTeachers()
    
    def removeAbsentTeacher(self, TeacherCode):
        self.cursor.execute(f"exec TeacherAbsentRemove '{TeacherCode}'")
        self.cursor.commit()
        return self.getAbsentTeachers()
    
    def getTeacherlessLearnersVoog(self, TeacherCode, Day):
        print(f"exec VoogLookup '{TeacherCode}', {Day}")
        self.cursor.execute(f"exec VoogLookup '{TeacherCode}', {Day}")
        return self.formatData()
    
    def getTeacherlessLearnersBuddy(self, TeacherCode, Day):
        self.cursor.execute(f"exec BuddyLookup '{TeacherCode}', {Day}")
        return self.formatData()
    
    def getVoogTeachers(self):
        self.cursor.execute(f"select VoogCode from VoogBuddyMapping")
        return self.formatData()