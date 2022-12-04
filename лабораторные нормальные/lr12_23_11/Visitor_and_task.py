from __future__ import generators
import random
# The shoping_center hierarchy cannot be changed:
class Project(object):
    def accept(self, visitor):
        visitor.visit(self)
    def working(self, employer):
        print(self, 'выполняет поручение от', employer)
    def communication(self, interaction):
        print(self, 'общается с', interaction)
    def fight(self, hit):
        print(self, 'критует на', hit)
    def __str__(self):
        return self.__class__.__name__

class Dwarf(Project): pass
class Elf(Project): pass
class Troll(Project): pass

class Visitor:
    def __str__(self):
        return self.__class__.__name__
class Engineer(Visitor): pass
class Marketing(Visitor): pass
class Manager(Visitor): pass


class Dwarf(Engineer):
    def visit(self, shoping_center):
        shoping_center.working(self)

class Elf(Marketing):
    def visit(self, shoping_center):
        shoping_center.communication(self)

class Troll(Manager):
    def visit(self, shoping_center):
        shoping_center.fight(self)

def Workers(n):
        workers_in_shoping_center = Project.__subclasses__()
        for i in range(n):
            yield random.choice(workers_in_shoping_center)()


if __name__ == '__main__':
    dwarf = Dwarf()
    elf = Elf()
    troll = Troll()
    for workers_in_shoping_center in Workers(4):
        workers_in_shoping_center.accept(dwarf)
        workers_in_shoping_center.accept(elf)
        workers_in_shoping_center.accept(troll)
