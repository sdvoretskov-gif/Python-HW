from student import student
from course_group import CourseGroup

studen = student('Алена', 'Степанова', 20, 'инженер по тестированию')
classmate1 = student('Валерий', 'Артамонов', 18, 'инженер по тестированию')
classmate2 = student('Юрий', 'Перов', 22, 'инженер по тестированию')
classmate3 = student('Юлия', 'Ершова', 18, 'инженер по тестированию')

course_group = CourseGroup(studen, [classmate1, classmate2, classmate3])

print(course_group)
