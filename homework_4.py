
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def fly(self):
        print(self.name,'fly')
    def __str__(self):
        return f'{self.name} {self.age}'
class Fly:
    def fly(self):
        print('fly')
class Name:
    def names(self):
        print(self)

    def run(self):
        print('Name')
class Forco:
    def __init__(self,definite):
        self.definite=definite

    def fly(self):
        print(self.definite, 'fly')
    def __str__(self):
        return self.definite


class Human(People,Fly,Name,Forco):
    def __init__(self, name, age, definite):
        People.__init__(self, name, age)
        Forco.__init__(self,definite)

    def __str__(self):
        return f'{self.name} {self.age} {self.definite}'

superhuman=Human('BetMen',45,'money')
superhuman.run()
# superhuman.names
# print(superhuman)

      
# human="Asadullox"
# # print(human)