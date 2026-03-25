from collections.abc import Iterable, Iterator

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


def add_matter_4(cls):
    original_init = cls.__init__
    def new_init(self, name, matter_1, matter_2, matter_3, matter_4=0):
        original_init(self, name, matter_1, matter_2, matter_3)
        self.matter_4 = matter_4
    cls.__init__ = new_init
    return cls


def add_matter_4_iterator(cls):
    def get_matter_4_iter(self):
        return Matter4Iterator(self.students)
    cls.get_matter_4_iter = get_matter_4_iter
    return cls


@add_matter_4
class Student:
    def __init__(self, name, matter_1, matter_2, matter_3):
        self.name = name
        self.matter_1 = matter_1
        self.matter_2 = matter_2
        self.matter_3 = matter_3
class Matter1Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter_1, reverse=True)
        self.index = 0
    def __next__(self):
        if self.index < len(self.students):
            res = self.students[self.index]
            self.index += 1
            return res
        raise StopIteration
    
class Matter2Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter_2, reverse=True)
        self.index = 0
    def __next__(self):
        if self.index < len(self.students):
            res = self.students[self.index]
            self.index += 1
            return res
        raise StopIteration

class Matter3Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter_3, reverse=True)
        self.index = 0
    def __next__(self):
        if self.index < len(self.students):
            res = self.students[self.index]
            self.index += 1
            return res
        raise StopIteration
    
class Matter4Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter_4, reverse=True)
        self.index = 0
    def __next__(self):
        if self.index < len(self.students):
            res = self.students[self.index]
            self.index += 1
            return res
        raise StopIteration

@singleton
@add_matter_4_iterator
class SchoolClass(Iterable):
     def __init__(self):
         self.students = []
     def add_student(self, student):
        self.students.append(student)
     def __iter__(self):
        return Matter1Iterator(self.students)

# def rank_matter_1(self):
#         self.students.sort(key=lambda s: s.matter_1, reverse=True)
#         for s in self.students:
#             print(f"{s.name}: {s.matter_1}")
        
# def rank_matter_2(self):
#         self.students.sort(key=lambda s: s.matter_2, reverse=True)
#         for s in self.students:
#             print(f"{s.name}: {s.matter_2}")

# def rank_matter_3(self):
#         self.students.sort(key=lambda s: s.matter_3, reverse=True)
#         for s in self.students:
#             print(f"{s.name}: {s.matter_3}")

if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13,15))
    school_class.add_student(Student('A', 8, 2, 17,10))
    school_class.add_student(Student('V', 9, 14, 14, 12))
    school_class_2 = SchoolClass() # On essaie d'en créer une deuxième pour le résultat finale
    
    # school_class.rank_matter_1()
    # school_class.rank_matter_2()
    # school_class.rank_matter_3()*

    for s in school_class:
        print(f"{s.name}: {s.matter_1}")
    for s in Matter2Iterator(school_class.students):
        print(f"{s.name}: {s.matter_2}")
    for s in Matter3Iterator(school_class.students):
        print(f"{s.name}: {s.matter_3}")
    
    for s in school_class.students:
        print(f"{s.name}: {s.matter_4}")
    for s in school_class.get_matter_4_iter():
        print(f"{s.name}: {s.matter_4}")

    if school_class is school_class_2:
        print("Succès : school_class et school_class_2 sont la même instance (Singleton).")
    else:
        print("Erreur : Ce sont deux instances différentes.")