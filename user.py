class User:
    def __init__(self, name, age, country):
        # インスタンス変数
        self.name = name
        self.age = age
        self.country = country

    def display_profile(self):
        # display_profile()はUserクラスのインスタンスメソッド
        print(f"私は{self.name}です。{self.country}出身の{self.age}歳です。")

    def change_nationality(self, coutry_name):
        self.country = coutry_name

if __name__ == '__main__':
    bob = User("Bob", 15, "USA")
    bob.display_profile()
    bob.change_nationality("China")
    bob.display_profile()

    tom = User("Tom", 57, "USA")
    tom.display_profile()
    tom.change_nationality("US")
    tom.display_profile()

    ken = User("Ken", 49, "JP")
    ken.display_profile()
    ken.change_nationality("Italy")
    ken.display_profile()
