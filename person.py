class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender=gender
    def introduce(self):
        print("My name is " + self.name + ", I am " + str(self.age) + " years old" + " and I am a" + self.gender)
p=person("Rahul", 20, "Male")
p.introduce()