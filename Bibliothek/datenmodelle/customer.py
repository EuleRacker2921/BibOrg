

class Customer:
    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
    


class youthCostumer(Customer):
    def __init__(self, id, name, username, email, age):
        super().__init__(id, name, username, email)
        self.age = age

    def age_check(self):
        if self.age < 18:
            return True
        else:
            return False
