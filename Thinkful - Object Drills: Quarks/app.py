class Quark(object):
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        self.baryon_number = 1/3

    def interact(self, q2):
        if(isinstance(q2,Quark)):
            aux = self.color
            self.color = q2.color
            q2.color = aux
        else:
            return "The objects that are interacting are not quarks!"
