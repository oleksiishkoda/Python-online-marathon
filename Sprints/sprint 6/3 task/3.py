import json
class Student:
    def __init__(self, full_name, avg_rank, courses):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses
        print(self.full_name)
        print(self.avg_rank)
        print(self.courses)
    @classmethod
    def from_json(cls, json_file):
        with open(f'sprint 6/3 task/{json_file}') as f:
            data = json.load(f)
        return cls(**data)
        
# class Group:
#     def __init_(self, title, students):
#         self.title = title
#         self.students = students
#     @classmethod
#     def serialize_to_json(cls, list_of_groups, filename):
#         students = list(map(list_of_groups, filename))
#         return cls(students)
    # @classmethod
    # def create_group_from_file(cls, students_file):
user1 = Student.from_json("2020-01.json")
print(user1)
        