import copy
# this doesnt make an actual copy of object
org = 5
cpy = org
cpy = 6
print(cpy)
print(org)
orgl = [0, 1, 2, 3, 4]
cpyl = orgl
cpyl[0] = -100
print(cpyl)
print(orgl)

# copy here
orgg = [0, 1, 2, 3, 4]
# same result all actual make shallow copy
# cpygg = orgg[:]
# cpygg = orgg.copy()
# cpygg = list(orgg)
cpygg = copy.copy(orgg)
cpygg[0] = -100
print(orgg)
print(cpygg)
# the disadvantage of shallow copy only copy the parent or 1 level depp
thelist = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
thecopy = thelist[:]
# if the child value changed then both the list will be changed
thecopy[0][1] = -100
print(thelist)
print(thecopy)
# use deepcopy is on all level so the value will not changed
a_list = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
deepcopyy = copy.deepcopy(a_list)
deepcopyy[0][1] = -100
print(a_list)
print(deepcopyy)


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee) -> None:
        self.boss = boss
        self.employee = employee


p1 = Person('George', 27)
p2 = Person('Joe', 18)
# shallow copy
p2 = copy.copy(p1)
p2.age = 28
print(p2.age)
print(p1.age)
# the downside of shallow copy the inside value will changed the parent value
p3 = Person('JOhn', 18)
p4 = Person('Doee', 35)
company = Company(p3, p4)
# use deepcopy to make sure copy in all level
company_clone = copy.deepcopy(company)
company_clone.boss.age = 55
print(company_clone.boss.age)
print(company.boss.age)
