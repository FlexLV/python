
class Address:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def display(self):
        print("First Name:", self.fname)
        print("Last Name:", self.lname)
        print("Email:", self.email)

a = Address("Ernests", "Dejus", "ernests@gmail.com")
a.display()
