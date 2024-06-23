from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self.name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self._yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self._yob} - Subject: {self.subject}"
        )


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - YoB: {self._yob} - Specialist: {self.specialist}"
        )


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__listpeople = list()

    def add_person(self, person: Person):
        self.__listpeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__listpeople:
            p.describe()

    def count_doctor(self):
        cnt = 0
        for person in self.__listpeople:
            if isinstance(person, Doctor):
                cnt += 1
        return cnt

    def sort_age(self):  # sort theo tuoi
        self.__listpeople.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):  # tinh trung binh nam sinh cua teachers
        cnt = 0
        total_year = 0
        for p in self.__listpeople:
            if isinstance(p, Teacher):
                cnt += 1
                total_year += p.get_yob()
        return total_year / cnt


print("2(a)")
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()

print("\n2(b)")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

print("\n2(c)")
print(f"Number of doctors: {ward1.count_doctor()}")

print("\n2(d)")
print("After sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

print("\n2(e)")
print(f"Average year of birth (teachers): {ward1.compute_average()}")
