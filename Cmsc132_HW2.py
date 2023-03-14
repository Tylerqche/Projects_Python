# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.cid = cid
        self.cname = cname
        self.credits = credits

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"{self.cid}({self.credits}): {self.cname}"
    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(other, str):
            return self.cid == other
        elif isinstance(other, Course):
            return self.cid == other.cid
        else:
            return self.cid == None

class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        if cid not in self.courseOfferings:
            c = Course(cid,cname,credits)
            self.courseOfferings[cid] = c
            return "Course added successfully"
        else:
            return "Course already added"


    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return "Course removed successfully"
        else:
            return "Course not found"

    def _loadCatalog(self, file):
        with open(file, "r") as f:
            course_info = f.read()
        # YOUR CODE STARTS HERE
        course_info = course_info.split("\n")
        for course in course_info:
            cid, cname, credits = course.split(",")
            c = Course(cid,cname,credits)
            self.courseOfferings[cid] = c
        
class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''

    def __init__(self):
        # --- YOUR CODE STARTS HERE
        self.courses = {}

    def __str__(self):
        # YOUR CODE STARTS HERE
        if len(self.courses) == 0:
            return "No courses"
        else:
            return "; ".join(self.courses.keys())
       
    __repr__ = __str__

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid not in self.courses:
            self.courses[course.cid] = course
        else:
            return "Course already added"

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid in self.courses:
            del self.courses[course.cid]
        else:
            return "No such course"

    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        total = 0
        for course in self.courses:
            total += int(self.courses[course].credits)
        return total

    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        return self.totalCredits >= 12

class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.amount = amount
        self.loan_id = self.__getloanID


    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Balance: ${}".format(self.amount)

    __repr__ = __str__


    @property
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        self.loan_id = random.randrange(10000, 99999)
        return self.loan_id

class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.__ssn = ssn
        self.name = name

    def __str__(self):
        # YOUR CODE STARTS HERE
        temp_ssn = list(self.get_ssn())
        for number in range(0, len(temp_ssn) - 4):
            if temp_ssn[number] != "-":
                temp_ssn[number] = "*"
        temp_ssn = "".join(temp_ssn)
        return "Person({}, {})".format(self.name, temp_ssn)

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return self.__ssn

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        return self.get_ssn() == other.get_ssn()

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        super().__init__(name, ssn) # Initiates main class
        #self.name = name
        #self.__ssn = ssn
        self.__supervisor = supervisor


    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Staff({}, {})".format(self.name, self.id)

    __repr__ = __str__


    @property
    def id(self):
        # YOUR CODE STARTS HERE

        #Gets last four ssn
        temp_ssn = ""
        for number in range(7, len(self.get_ssn())): 
            temp_ssn += self.get_ssn()[number]
        
        #Gets initials
        initials = ""
        for ch in self.name.title():
            if ch.isupper():
                initials += ch
        
        return "905{}{}".format(initials.lower(), temp_ssn)

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        return self.__supervisor

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        self.__supervisor = new_supervisor


    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student): # Checks instnace
            student.hold = True # Changes to True
            return "Completed!"

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = False # Changes to False
            return "Completed!" 

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.active = False # Changes to False
            return "Completed!"

    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        name = person.name
        ssn = person.get_ssn()
        year = "Freshman"
        return Student(name, ssn, year) # Creates student sub class

class Student(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        super().__init__(name,ssn)
        self.classCode = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()

    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Student({}, {}, {})".format(self.name, self.id, self.classCode) 

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        return StudentAccount(self) # Creates StudentAccount object

    @property
    def id(self):
        # YOUR CODE STARTS HERE

        #Gets last four ssn
        temp_ssn = ""
        for number in range(7, len(self.get_ssn())): 
            temp_ssn += self.get_ssn()[number]
        
        #Gets initials
        initials = ""
        for ch in self.name.title():
            if ch.isupper():
                initials += ch
        
        return "{}{}".format(initials.lower(), temp_ssn)

    def registerSemester(self):
        # YOUR CODE STARTS HERE

        # Dict of years
        yearRecord = {1 : "Freshman", 2 : "Freshman", 
                      3 : "Sophomore", 4 : "Sophomore",
                      5 : "Junior", 6 : "Junior"}

        if self.hold == False and self.active == True:
            self.key = len(self.semesters) + 1

            if self.key <= 6:
                self.classCode = yearRecord[self.key]
            else:
                self.classCode = "Senior" # Changes senior code if over 6 semesters

            self.semesters[self.key] = Semester() # Creates Semester class
        else:
            return "Unsuccessful operation"

    def enrollCourse(self, cid, catalog):
        # YOUR CODE STARTS HERE

        if self.hold == True or self.active == False:
            return "Unsuccessful operation"

        if cid in self.semesters[self.key].courses:
            return "Course already enrolled"

        if self.hold == False and self.active == True:
            if cid in catalog.courseOfferings:
                self.semesters[self.key].addCourse(catalog.courseOfferings[cid]) # Adds Course to Semester

                #Adds credit price
                self.credits = int(self.semesters[self.key].courses[cid].credits) # Checks semester class credits
                self.account.chargeAccount(self.credits * self.account.CREDIT_PRICE)

                return "Course added successfully"
            elif cid not in catalog.courseOfferings:
                return "Course not found"

    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE

        if self.hold == True or self.active == False:
            return "Unsuccessful operation"
        
        if cid in self.semesters[self.key].courses:
            
            #Removes credit price
            self.account.makePayment((int(self.semesters[self.key].courses[cid].credits) * self.account.CREDIT_PRICE)/2) # Finds Semester credits and divides by 2
            del self.semesters[self.key].courses[cid]

            #Updates amount of credits
            self.credits = self.semesters[self.key].totalCredits # Updates credit amount from Semester
            

            return "Course dropped successfully"
        else:
            return "Course not found"
        
    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        if self.active == False:
            return "Unsuccessful operation"
        elif self.semesters[self.key].isFullTime == False:
            return "Not full-time"
        elif self.active == True and self.semesters[self.key].isFullTime == True: # Check if active and FullTime
            #self.account.loans[Loan.__getloanID] = amount
            x = Loan(amount)
            self.account.makePayment(x.amount) # Sets balance
            self.account.loans[x.loan_id] = x # Creates loan object into dict

class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    
    CREDIT_PRICE = 1000

    def __init__(self, student):
        # YOUR CODE STARTS HERE
        self.student = student
        self.balance = 0
        self.loans = {}


    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Name: {}\nID: {}\nBalance: ${}".format(self.student.name, self.student.id, self.student.account.balance)

    __repr__ = __str__


    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        self.balance = self.balance - amount
        return self.balance


    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        self.balance = self.balance + amount
        return self.balance

def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Course with the name of the function you want to test
    doctest.run_docstring_examples(Staff, globals(), name='HW2',verbose=True)   

if __name__ == "__main__":
    run_tests()