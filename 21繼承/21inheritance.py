#繼承 inherritance(用student.py繼承person)可以少寫許多程式碼
from student import Student

student1 = Student("小明",15,"XX國中")
student1.print_name()
student1.print_age()
