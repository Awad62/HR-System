class Employee:
    number_of_employees = 0
    def __init__(self, first_name: str, last_name: str, job_title: str, yearly_salary: float, supervisor = None):
        self._first_name = first_name
        self._last_name = last_name
        self._job_title = job_title
        self._yearly_salary = yearly_salary
        self._supervisor = supervisor
        Employee.number_of_employees += 1
        self._reports = []

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    def get_job_title(self):
        return self._job_title

    def get_salary(self):
        return self._yearly_salary

    def get_supervisor(self):
        return self._supervisor

    def get_number_of_holidays(self):
        return 7
    
    def get_yearly_bonus(self):
        return 10000

    def get_reports(self):
        return self._reports

    def add_report(self, report):
        if report in self._reports:
            return False
        self._reports.append(report)
        return True
        
    def get_report_names(self) -> list:
        result = []
        for report in self._reports:
            result.append(report.get_full_name())
            result.extend(report.get_report_names())
        return result

    # def get_report_names(self) -> list:
    #     result = []
    #     for report in self._reports:
    #         result.append(report.get_full_name())
    #         if report.get_reports():
    #             result.extend(report.get_report_names())
    #     return result


    def set_first_name(self, name: str) -> bool:
        name = name.strip()
        if not name.isalpha():
            return False
        self._first_name = name
        return True

    def set_last_name(self, name: str) -> bool:
        name = name.strip()
        if not name.isalpha():
            return False
        self._last_name = name
        return True
    
    def set_job_title(self,job_title: str):
        job_title = job_title.strip()
        for title in job_title.split(' '):
            if not title.isalpha():
                return False
        self._job_title = job_title
        return True

    def set_salary(self, salary: float):
        if salary <= 0:
            return False
        self._yearly_salary = salary
        return True

    def set_supervisor(self, supervisor):
        self._supervisor = supervisor

    def remove_report(self, report):
        if report not in self._reports:
            return False
        self._reports.remove(report)
        return True

class Intern(Employee):
    
    number_of_interns = 0

    def __init__(self, first_name: str, last_name: str, job_title: str, yearly_salary: float, supervisor=None):
        super().__init__(first_name, last_name, job_title, yearly_salary, supervisor)
        Intern.number_of_interns += 1

    def get_yearly_bonus(self):
        return 0

class Manager(Employee):

    number_of_managers = 0

    def __init__(self, first_name: str, last_name: str, job_title: str, yearly_salary: float, supervisor=None):
        super().__init__(first_name, last_name, job_title, yearly_salary, supervisor)
        Manager.number_of_managers += 1

    def get_number_of_holidays(self):
        return 10

    def get_yearly_bonus(self):
        return 20000

class Director(Employee):

    number_of_directors = 0

    def __init__(self, first_name: str, last_name: str, job_title: str, yearly_salary: float, supervisor=None):
        super().__init__(first_name, last_name, job_title, yearly_salary, supervisor)
        Director.number_of_directors += 1

    def get_number_of_holidays(self):
        return 13

    def get_yearly_bonus(self):
        return 30000

class CEO(Employee):

    def __init__(self, first_name: str, last_name: str, job_title: str, yearly_salary: float):
        super().__init__(first_name, last_name, job_title, yearly_salary)
    
    def get_number_of_holidays(self):
        return 17

    def get_yearly_bonus(self):
        return 50000

    def set_supervisor(self, supervisor):
        return None

senior_engineer = Employee("Sulayman", "Sylla", "Senior Software Engineer", 150000)
designer = Employee("Fred", "Hampton", "Product Designer", 250000)
junior_engineer = Employee("Mustafa", "Newton", "Junior Software Engineer", 90000, senior_engineer)

assert Employee.number_of_employees == 3
assert senior_engineer.get_first_name() == "Sulayman"
assert senior_engineer.get_last_name() == "Sylla"
assert senior_engineer.get_full_name() == "Sulayman Sylla"
assert senior_engineer.get_job_title() == "Senior Software Engineer"
assert senior_engineer.get_salary() == 150000
assert senior_engineer.get_supervisor() == None
assert junior_engineer.get_supervisor() == senior_engineer
assert senior_engineer.get_number_of_holidays() == 7
assert junior_engineer.get_number_of_holidays() == 7
assert designer.get_number_of_holidays() == 7
assert senior_engineer.get_yearly_bonus() == 10000
assert junior_engineer.get_yearly_bonus() == 10000
assert designer.get_yearly_bonus() == 10000
assert senior_engineer.get_reports() == []
assert junior_engineer.get_reports() == []
assert designer.get_reports() == []

employee = Employee("Nas", "Tuf", "Principal Software Engineer", 500000)

employee1 = Employee("Malcolm", "Little", "Staff Software Engineer III", 350000)
employee2 = Employee("Fred", "Hampton", "Staff Software Engineer II", 300000)
employee3 = Employee("Marcus", "Garvey", "Staff Software Engineer", 250000)
employee4 = Employee("Jamil", "Brown", "Senior Softwaer Engineer", 200000)
employee5 = Employee("Jamil", "Al-Amin", "Software Engineer II", 150000)
employee6 = Employee("Luqman", "Hakeem", "Junior Engineer", 104000)

employee1.add_report(employee2)
employee2.add_report(employee3)
employee3.add_report(employee4)
employee4.add_report(employee5)

employee.add_report(employee1)
employee.add_report(employee6)

assert sorted(employee.get_report_names()) == sorted([
'Malcolm Little', 
'Fred Hampton', 
'Marcus Garvey', 
'Jamil Brown', 
'Jamil Al-Amin', 
'Luqman Hakeem'
])

assert senior_engineer.set_first_name("Yusuf  ")
assert senior_engineer.get_first_name() == "Yusuf"

assert not senior_engineer.set_first_name("Yusuf@")
assert not senior_engineer.set_first_name("")
assert not senior_engineer.set_first_name(" ")
assert senior_engineer.get_first_name() == "Yusuf"

assert senior_engineer.set_last_name("Drame  ")
assert senior_engineer.get_last_name() == "Drame"

assert not senior_engineer.set_last_name("Drame@")
assert not senior_engineer.set_last_name("")
assert not senior_engineer.set_last_name(" ")
assert senior_engineer.get_last_name() == "Drame"

assert designer.set_job_title("Senior Product Designer")
assert designer.get_job_title() == "Senior Product Designer"

assert designer.set_job_title(" Senior Product Designer ")
assert designer.get_job_title() == "Senior Product Designer"

assert not designer.set_job_title("")
assert not designer.set_job_title("  ")
assert designer.get_job_title() == "Senior Product Designer"

assert junior_engineer.set_salary(40000)
assert junior_engineer.get_salary() == 40000

assert not junior_engineer.set_salary(-10000)
assert junior_engineer.get_salary() == 40000

assert senior_engineer.get_supervisor() == None
senior_engineer.set_supervisor(designer)
assert senior_engineer.get_supervisor() == designer

senior_engineer.set_supervisor(None)
assert senior_engineer.get_supervisor() == None

assert senior_engineer.add_report(junior_engineer)
assert not senior_engineer.add_report(junior_engineer)
assert senior_engineer.get_reports() == [junior_engineer]
assert senior_engineer.get_report_names() == ["Mustafa Newton"]

assert not senior_engineer.remove_report(designer)

assert senior_engineer.remove_report(junior_engineer)
assert senior_engineer.get_reports() == []
assert senior_engineer.get_report_names() == []

engineer_intern = Intern("Hakeem", "Luqman", "Software Engineer Intern", 100000)
assert Intern.number_of_interns == 1
assert engineer_intern.get_yearly_bonus() == 0

engineering_manager = Manager("Rakim", "Wise", "Software Engineering Manager", 250000)
assert Manager.number_of_managers == 1
assert engineering_manager.get_number_of_holidays() == 10
assert engineering_manager.get_yearly_bonus() == 20000 

engineering_director = Director("Marcus", "Garv", "Director of Engineering", 650000)
assert Director.number_of_directors == 1
assert engineering_director.get_number_of_holidays() == 13
assert engineering_director.get_yearly_bonus() == 30000
ceo = CEO("Malcolm", "Little", "CEO", 650000)
assert ceo.get_yearly_bonus() == 50000
assert ceo.get_number_of_holidays() == 17

employee = Employee("Mansa", "Musa", "Software Engineer", 150000)

assert employee.get_first_name() == "Mansa"
assert employee.get_last_name() == "Musa"
assert employee.get_full_name() == "Mansa Musa"
assert employee.get_job_title() == "Software Engineer"
assert employee.get_salary() == 150000
assert employee.get_number_of_holidays() == 7


manager = Manager("Mansa", "Sulayman", "Software Engineering Manager", 250000)

assert manager.get_first_name() == "Mansa"
assert manager.get_last_name() == "Sulayman"
assert manager.get_full_name() == "Mansa Sulayman"
assert manager.get_job_title() == "Software Engineering Manager"
assert manager.get_salary() == 250000
assert manager.get_number_of_holidays() == 10
assert manager.get_yearly_bonus() == 20000

director = Director("Man", "Mohamed", "Director of Engineering", 350000)

assert director.get_first_name() == "Man"
assert director.set_first_name("Mansa")
assert director.get_first_name() == "Mansa"
assert director.get_last_name() == "Mohamed"
assert director.get_full_name() == "Mansa Mohamed"
assert director.get_job_title() == "Director of Engineering"
assert not director.set_salary(-100000)
assert director.get_salary() == 350000
assert director.get_number_of_holidays() == 13
assert director.get_yearly_bonus() == 30000

ceo = CEO("Malcolm", "Little", "CEO", 1000000)
director = Director("Huey", "Newton", "Senior Director", 450000, supervisor=ceo)
manager = Manager("Jamil", "Al-Amin", "Engineering Manager", 320000, supervisor=director)

assert ceo.add_report(director)
assert director.add_report(manager)

assert ceo.get_number_of_holidays() == 17
assert director.get_number_of_holidays() == 13

assert director.get_yearly_bonus() == 30000
assert manager.get_yearly_bonus() == 20000

assert ceo.get_report_names() == [
    'Huey Newton', 
    'Jamil Al-Amin', 
]

assert manager.get_report_names() == []
assert director.get_supervisor() == ceo

lssst = [1]
for x in lssst:
    print('hey')


assert ''.isalpha()