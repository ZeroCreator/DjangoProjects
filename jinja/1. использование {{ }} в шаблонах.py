from jinja2 import Template

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

# name = "Федор"
# age = 28
per = Person("Федор", 33)

# tm = Template("Мне {{a*2}} лет и зовут {{ n.upper() }}.")
# tm = Template("Мне {{p.age}} лет и зовут {{ p.name }}.")
tm = Template("Мне {{p.getAge()}} лет и зовут {{ p.getName() }}.")
# msg = tm.render(n=name, a=age)
msg = tm.render(p = per)



print(msg)

# С помощью словаря
per1 = {'name': 'Федор', 'age': 34}
# tm = Template("Мне {{p1.age}} лет и зовут {{ p1.name }}.")
tm = Template("Мне {{p1['age']}} лет и зовут {{ p1['name'] }}.")
msg1 = tm.render(p1 = per1)

print(msg1)