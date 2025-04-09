import sqlite3 as sql
from tkinter import messagebox


class Student:

    def __init__(self, id, lastName, firstName, middleName, phone, email, grades):
        self.id = id
        self.lastName = lastName
        self.firstName = firstName
        self.middleName = middleName
        self.email = email
        self.phone = phone
        self.grades = grades if grades is not None else []

    def calculateAttendance(self):

        quantity = 0
        sum = 0
        marks = 0.0
        miss = 0

        for grade in self.grades:
            if grade[2] != 0:
                quantity += 1
                sum += grade[2]
            if grade[1] > 0:
                miss += grade[1]

        if quantity != 0:
            marks = sum / quantity

        return marks, miss

    def __repr__(self):
        return (f"{self.id}, {self.lastName}, {self.firstName}, {self.middleName},"
                f" {self.email}, {self.phone}, {self.grades}")


class Database:

    def __init__(self):
        try:
            self.conn = sql.connect('database/journal.db')
            self.curs = self.conn.cursor()

        except Exception as e:
            messagebox.showerror("Error", e)

    def createTable(self):
        self.curs.execute("""
                        CREATE TABLE IF NOT EXISTS `auth` (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        studentID INTEGER NOT NULL,
                        accessLvl INTEGER NOT NULL DEFAULT 0,
                        userName TEXT NOT NULL,
                        hash TEXT NOT NULL,
                        salt TEXT NOT NULL)
                        """)

        self.curs.execute('''
                        CREATE TABLE IF NOT EXISTS students (
                            studentID INTEGER PRIMARY KEY AUTOINCREMENT,
                            lastName TEXT,
                            firstName TEXT,
                            middleName TEXT,
                            groupID INTEGER,
                            phone TEXT,
                            email TEXT)
                            ''')

        self.curs.execute('''
                        CREATE TABLE IF NOT EXISTS groups (
                            groupID INTEGER PRIMARY KEY AUTOINCREMENT,
                            groupName TEXT)
                            ''')

        self.curs.execute('''
                        CREATE TABLE IF NOT EXISTS subjects (
                            subjectID INTEGER PRIMARY KEY AUTOINCREMENT,
                            subjectName TEXT)
                            ''')

        self.curs.execute('''
                        CREATE TABLE IF NOT EXISTS schedules (
                            scheduleID INTEGER PRIMARY KEY AUTOINCREMENT,
                            groupID INTEGER,
                            subjectID INTEGER,
                            date TEXT,
                            FOREIGN KEY (groupID) REFERENCES groups(groupID),
                            FOREIGN KEY (subjectID) REFERENCES subjects(subjectID))
                            ''')

        self.curs.execute('''
                        CREATE TABLE IF NOT EXISTS attendance (
                            attendanceID INTEGER PRIMARY KEY AUTOINCREMENT,
                            studentID INTEGER,
                            subjectID INTEGER,
                            date TEXT,
                            attendance INTEGER DEFAULT 0,
                            grade INTEGER DEFAULT 0,
                            FOREIGN KEY (studentID) REFERENCES students(studentID),
                            FOREIGN KEY (subjectID) REFERENCES subjects(subjectID))
                            ''')

    def dropTable(self, key):
        try:
            if key == 1:
                self.curs.execute("DROP TABLE IF EXISTS `students`")
            elif key == 2:
                self.curs.execute("DROP TABLE IF EXISTS `groups`")
            elif key == 3:
                self.curs.execute("DROP TABLE IF EXISTS `subjects`")
            elif key == 4:
                self.curs.execute("DROP TABLE IF EXISTS `schedules`")
            elif key == 5:
                self.curs.execute("DROP TABLE IF EXISTS `attendance`")

        except Exception as e:
            messagebox.showerror("Error", e)

    def addSchedule(self, groupID, subjectID, date):
        try:
            self.curs.execute(f"INSERT INTO schedules (groupID, subjectID, date) VALUES (?, ?, ?)",
                              (groupID, subjectID, date))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def addGroup(self, groupName):
        try:
            self.curs.execute("INSERT INTO groups (groupName) VALUES (?)", (groupName,))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def addSubject(self, subject):
        try:
            self.curs.execute("INSERT INTO subjects (subjectName) VALUES (?)", (subject,))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def addShedule(self, groupID, subjectID, date):
        try:
            self.curs.execute("INSERT INTO schedules (groupID, subjectID, date) VALUES (?, ?, ?)",
                              (groupID, subjectID, date))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def addStudent(self, lastName, firstName, middleName, groupID, phone, email):
        try:
            self.curs.execute("INSERT INTO students (lastName, firstName, middleName, groupID, phone, email) VALUES (?, ?, ?, ?, ?, ?)",
                              (lastName, firstName, middleName, groupID, phone, email))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def editStudentAsObject(self, student, groupID):
        try:
            self.curs.execute("UPDATE students SET lastName = ?, firstName = ?, middleName = ?, groupID = ?, phone = ?, email = ? WHERE studentID = ?",
                              (student.lastName, student.firstName, student.middleName, groupID, student.phone, student.email, student.id))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def removeStudent(self, studentID):
        try:
            self.curs.execute("DELETE FROM students WHERE studentID = ?", (studentID,))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def removeShedule(self, sheduleID):
        try:
            self.curs.execute("DELETE FROM schedules WHERE scheduleID = ?", (sheduleID,))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def addStudentAsObject(self, student, groupID):
        try:
            self.curs.execute("INSERT INTO students (lastName, firstName, middleName, groupID, phone, email) VALUES (?, ?, ?, ?, ?, ?)",
                              (student.lastName, student.firstName, student.middleName, groupID, student.phone, student.email))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def addAttendance(self, studentID, subjectID, date, attendance, grade=None):
        try:
            self.curs.execute(
                "INSERT INTO attendance (studentID, subjectID, date, attendance, grade) VALUES (?, ?, ?, ?, ?)",
                (studentID, subjectID, date, attendance, grade))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def saveStudents(self, students):
        for student in students:
            try:
                self.curs.execute("""
                    INSERT OR REPLACE INTO students
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (student.studentID, student.lastName, student.firstName, student.middleName, student.groupID, student.phone, student.email))
            except Exception as e:
                messagebox.showerror("Error", e)

            self.conn.commit()

    def getStudents(self, groupID, subjectID):

        students = []
        countOfStudents = 0

        self.curs.execute("""
            SELECT studentID, lastName, firstName, middleName, phone, email
            FROM students 
            WHERE groupID = ?
            ORDER BY lastName, firstName, middleName
        """, (groupID,))

        studentsData = self.curs.fetchall()

        for studentData in studentsData:
            studentID, lastName, firstName, middleName, phone, email = studentData

            self.curs.execute("""
                SELECT date, attendance, grade 
                FROM attendance 
                WHERE studentID = ? AND subjectID = ?
                ORDER BY date
            """, (studentID, subjectID))

            performance = self.curs.fetchall()

            students.append(Student(studentID, lastName, firstName, middleName, phone, email, performance))
            countOfStudents += 1

        return students, countOfStudents

    def getStudentsToEdit(self, groupID):

        self.curs.execute("""
            SELECT studentID, lastName, firstName, middleName, phone, email
            FROM students 
            WHERE groupID = ?
            ORDER BY lastName, firstName, middleName
        """, (groupID,))

        return self.curs.fetchall()

    def deleteGroup(self, groupID):
        try:
            self.curs.execute("DELETE FROM groups WHERE groupID = ?", (groupID,))
            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", e)

    def getGroups(self):
        self.curs.execute("""
            SELECT groupID, groupName
            FROM groups
            ORDER BY groupName
        """)

        return self.curs.fetchall()

    def getShedules(self, groupID, subjectID):
        self.curs.execute("""
            SELECT date
            FROM schedules
            WHERE groupID = ? AND subjectID = ?
            ORDER BY date
        """, (groupID, subjectID))

        return self.curs.fetchall()

    def getShedulesToEdit(self, groupID, subjectID):
        self.curs.execute("""
            SELECT date, scheduleID
            FROM schedules
            WHERE groupID = ? AND subjectID = ?
            ORDER BY date
        """, (groupID, subjectID))

        return self.curs.fetchall()

    def getSubjects(self):
        self.curs.execute("""
            SELECT subjectID, subjectName
            FROM subjects
            ORDER BY subjectName
        """)

        return self.curs.fetchall()

    def updateStudents(self, students, subjectID):
        try:
            for student in students:
                if student.grades:
                    for grade in student.grades:
                        self.curs.execute("""
                            SELECT attendanceID FROM attendance
                            WHERE studentID = ? AND subjectID = ? AND date = ?
                        """, (student.id, subjectID, grade[0]))
                        result = self.curs.fetchone()

                        if result:
                            self.curs.execute("""
                                UPDATE attendance
                                SET attendance = ?, grade = ?
                                WHERE studentID = ? AND subjectID = ? AND date = ?
                            """, (grade[1], grade[2], student.id, subjectID, grade[0]))
                        else:
                            self.curs.execute("""
                                INSERT INTO attendance (studentID, subjectID, date, attendance, grade)
                                VALUES (?, ?, ?, ?, ?)
                            """, (student.id, subjectID, grade[0], grade[1], grade[2]))

            self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error", f"Ошибка при обновлении данных: {e}")
        finally:
            self.conn.close()

    def close(self):
        self.conn.close()


##########################################################

test = Database()

test.close()
