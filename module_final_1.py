grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#формирую средние значения вместо оценок
grades = [sum(grades[0])/len(grades[0]),
              sum(grades[1])/len(grades[1]),
              sum(grades[2])/len(grades[2]),
             sum(grades[3])/len(grades[3]),
             sum(grades[4])/len(grades[4])]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#сортировка по алфавиту
students = list(students) #перевод в изменяемый формат
students.sort() #сортировка по алфавиту
list_students = {tuple(students[0]): grades[0],
                 tuple(students[1]): grades[1],
                 tuple(students[2]): grades[2],
                 tuple(students[3]): grades[3],
                 tuple(students[4]): grades[4]}
print({tuple(students): grades})