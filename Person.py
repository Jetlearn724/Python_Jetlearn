
class person:
    def __init__(self,n,a): 
        self.name = n
        self.age = a
    def show(self):
        print("My name is {}".format(self.name))
        print(self.age)

person1 = person("Ayush" ,13 )
person1.show()
person2 = person("Tin" , 15)
person2.show()