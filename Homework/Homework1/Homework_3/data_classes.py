class Person(object):
    """Architecture for Person Data"""

    def __init__ (self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
    
    def AssignName (self):
        """A Person's Name"""

        print(self.name.title() + "is now in the system.")

    def ApplyAge(self):
        """The Person's Age"""

        print(str(self.age) + "is" + self.name.title() + "'s" + "age")

    def person_email (self):
        """Person's Email"""
        print(self.name.title() + "'s email: " + self.email.title())

class Student(Person):
    """A person that is a student"""

    def __init__ (self,name,age,email,student_id):

        super().__init__(name,age,email)

        self.student_id = student_id

def save_student(Save):
    """Saving in a JSON File"""
    import json

    json_info = Save.__dict__

    Student_data = []

    Student_data.append(json_info)

    with open('student_saves.json','w') as f:
        json.dump(Student_data,f)

def show_content():
    import json
    
    with open('student_saves.json','r') as f:
        json_display = json.load(f)

    print(json.dumps(json_display,indent=2))

        




