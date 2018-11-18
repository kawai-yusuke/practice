class User:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

if __name__ == '__main__':
    bob = User("Bob", 15, "USA")
    print(bob)
    print(bob.name)
    print(bob.age)
    print(bob.country)

    tom = User("Tom", 57, "USA")
    print(tom)
    print(tom.name)
    print(tom.age)

    ken = User("Ken", 49, "JP")
    print(ken)
    print(ken.name)
