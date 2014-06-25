class wheel():
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

    def returnWheel(self):
        print "===" + str(self.model) + "==="
        print self.weight, self.cost


wheel1 = wheel("Low-Quality", 10, 25)
wheel2 = wheel("Average", 8, 50)
wheel3 = wheel("Highend", 6, 100)

#make1.returnWheel()

class frame():
    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost

    def returnFrame(self):
        print "===" + str(self.material) + "==="
        print self.weight, self.cost


frame1 = frame("Steel", 10, 100)
frame2 = frame("Aluminium", 5, 150)
frame3 = frame("Carbon", 1, 200)

#frame1.returnFrame()


class model():
    def __init__(self, name, manufacturer, wheel_type, frame_type):
        self.name = name
        self.manufacturer = manufacturer
        self.wheel = wheel_type
        self.frame = frame_type

    def returnModel(self):
        print "===" + str(self.name) + "==="
        print "===" + str(self.manufacturer) + "==="
        print self.wheel.returnWheel()
        print self.frame.returnFrame()

    def returnPrice(self):
         print ((self.wheel.cost * 2) + self.frame.cost)




model1 = model("Type1", "Topike", wheel1, frame1)
model2 = model("Type2", "Topike", wheel2, frame2)
model3 = model("Type3", "Topike", wheel3, frame3)

model4 = model("Speed1", "Nubiek", wheel1, frame1)
model5 = model("Speed2", "Nubiek", wheel2, frame2)
model6 = model("Speed3", "Nubiek", wheel3, frame3)

#model1.returnPrice()
#model2.returnModel()
#model3.returnModel()

class manufacturer():
    def __init__(self, name, upsell, mod1, mod2, mod3):
        self.name = name
        self.upsell = upsell
        self.mod1 = mod1
        self.mod2 = mod2
        self.mod3 = mod3

    def returnInventory(self):
        print self.mod1.returnModel()
        print self.mod2.returnModel()
        print self.mod3.returnModel()

    def returnPrice(self):
        print self.mod1.returnPrice()
        #print ((float(self.mod1.returnPrice()) * float(self.upsell)) + float(self.mod1.returnPrice()))

topike = manufacturer("Topike", 0.2, model1, model2, model3)
nubiek = manufacturer("Nubiek", 0.2, model4, model5, model6)

topike.returnPrice()
#topike.returnInventory()
print " "
#nubiek.returnInventory()
