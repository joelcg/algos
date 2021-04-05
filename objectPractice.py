class Vehicle:
    name = ''
    kind = 'car'
    color = ''
    value = 100.00
    def description(self):
        desc_string = "%s is a %s %s worth $%.2f. " % (self.name, self.color, self.kind, self.value)
        return desc_string
    
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00        

print(car1.description())
print(car2.description())

##############################################################################

class squad:
    codeName = ''
    roleType = ''
    role = ''
    primary = ''
    def desc(self):
        desc = "Codename %s act as the %s unit, specifically as the %s for the squad and armed with %s as his/her primary." % (self.codeName, self.roleType, self.role, self.primary,)
        return desc
    def unit(self, codeName, roleType, role, primary):
        self.codeName = codeName
        self.roleType = roleType
        self.role = role
        self.primary = primary
        return self.codeName, self.roleType, self.role, self.primary

def alphaTeamDesc():
    squad.unit(squad, 'A-1', "command", "MOS 0365", "M4A1 with Tracer, Vertical Grip, ACOG, and 7 mags")
    print(squad.desc(squad))
    squad.unit(squad, 'A-2', "support", "HM-8404", "M4 with M68 and 7 mags")
    print(squad.desc(squad))
    squad.unit(squad, 'A-3', "direct fire", "MOS 0311", "M4A1 with M68 and 7 mags")
    print(squad.desc(squad))
    squad.unit(squad, 'A-4', "fire support", "designated marksman", "M110 SASS and 8 mags")
    print(squad.desc(squad))
    squad.unit(squad, 'A-5', "specialist", "MOS 0331", "M240B with M145 and 7 ammo pouches")
    print(squad.desc(squad))
    
alphaTeamDesc()

##############################################################################
