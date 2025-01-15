# TODO: Make generateVoogList part of ImportTool

import connectDB

conn = connectDB.connectDB()
cursor = conn.cursor()

cursor.execute('select distinct Learner, Class from learnersImport order by Class')
learners = cursor.fetchall()

cursor.execute("select TeacherCode from TeacherCodeMapping where TeacherCode != 'N/A'")
teachers = cursor.fetchall()

print(len(learners), teachers)
for i in range(len(learners)):
    if learners[i][0].find('\'') > -1:
        learners[i][0] = learners[i][0][:learners[i][0].find('\'')] + '\'' + learners[i][0][learners[i][0].find('\''):]
    cursor.execute(f"insert into VoogList (TeacherCode, LearnerName, LearnerClass) values ('{teachers[i % len(teachers)][0]}', '{learners[i][0]}', '{learners[i][1]}') ")

cursor.commit()