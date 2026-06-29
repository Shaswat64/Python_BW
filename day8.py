# def add(*args):                 # '*args' use garye data matra linxa
#     if len(args)==0:
#         return f'Enter a valid value'
#     total = 0
#     for i in args:
#         if isinstance(i,int):
#              total = total +i
#     return total

        

# print(add(1,2,"sudna","tets"))
# print(add(1,2,3))
# print(add(1,2,3,4))
# print(add())



# def all(*args, **kwargs):                                  # '**kwargs' use garye data variable linxa
#     print(args) 
#     print(kwargs)

# all(1,2,3,4,5,6,"Hari","Tests",1,2,3, name="sudan")
# all(1,2,3,4,"hari","tests",2,4)


def marksheet(student_name, *subjects, **extra):
    total = 0
    for i in subjects:
        for j in i:
            if isinstance(j,int):
                total=total+j
    print(f"Name of student:{student_name}     Total Marks obtained:{total}      Class Teacher:{extra.get('class_teacher',"no class teacher")}      Grade Level:{extra.get('grade_level')}     Average:{total/len(subjects)}")





marksheet(
    "Sudan Bhandari",
    ("Mathematics", 92),
    ("Science", 88),
    ("English", 85),
    ("Computer", 95),
    ("Social Studies", 81),
    class_teacher="Mr. Sharma",
    grade_level="Grade 10",
    attendance="96%"
)

