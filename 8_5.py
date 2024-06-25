from student import *

class Grades(object):

    def __init__(self):
        """空の成績ブックを生成する"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """studentをStudent型とすr
        student成績ブックへ追加する"""
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """gradeをfloat型とする
        gradeをstudentの成績リストへ追加する"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
    
    def getGrades(self, student):
        """studentの成績リストを返す"""
        try: #studentの成績リストのコピーを返す
            return self.grades[student.getIdNum()]
        except:
            raise ValueError('Student not in mapping')
        
    def getStudents(self):
        """成績ブックに収められた学生の、ソートされたリストを返す"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] # 学生のリストのコピーを返す
    

