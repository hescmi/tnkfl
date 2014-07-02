class Wheel():
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return "[%s] [Weighs: %d] [Costs: %d]" % (self.model, self.weight, self.cost)

    def returnWheel(self):
        print "===" + str(self.model) + "==="
        print self.weight, self.cost

#    def __dir__(self):
#        return ['model', 'weight', 'cost']

wheel1 = Wheel("Low-Quality", 10, 25)
wheel2 = Wheel("Average", 8, 50)
wheel3 = Wheel("Highend", 6, 100)

#print wheel1

#make1.returnWheel()

class Frame():
    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return "[%s] [Weighs: %d] [Costs: %d]" % (self.material, self.weight, self.cost)

    def returnFrame(self):
        print "===" + str(self.material) + "==="
        print self.weight, self.cost


frame1 = Frame("Steel", 10, 50)
frame2 = Frame("Aluminium", 5, 150)
frame3 = Frame("Carbon", 1, 200)

#frame1.returnFrame()


class Model():
    def __init__(self, name, manufacturer, wheel_type, frame_type):
        self.name = name
        self.manufacturer = manufacturer
        self.wheel = wheel_type
        self.frame = frame_type

    def __str__(self):
        return "[{}] [{}] [Wheel > {}] [Frame > {}]".format(str(self.name),str(self.manufacturer),self.wheel,self.frame)

    def returnModel(self):
        print "===" + str(self.name) + "==="
        print "===" + str(self.manufacturer) + "==="
        print self.wheel.returnWheel()
        print self.frame.returnFrame()

    def returnWeight(self):
        return ((self.wheel.weight *2) + self.frame.weight)

    def returnModPrice(self):
        return ((self.wheel.cost * 2) + self.frame.cost)




model1 = Model("Type1", "Topike", wheel1, frame1)
model2 = Model("Type2", "Topike", wheel2, frame2)
model3 = Model("Type3", "Topike", wheel3, frame3)

model4 = Model("Speed1", "Nubiek", wheel1, frame1)
model5 = Model("Speed2", "Nubiek", wheel2, frame2)
model6 = Model("Speed3", "Nubiek", wheel3, frame3)

#model1.returnPrice()
#model2.returnModel()
#print model3.returnWeight()
#print model3

class Manufacturer():
    model_list = []
    def __init__(self, name, upsell, model_list):
        self.name = name
        self.upsell = upsell
        self.model_list = model_list

    def returnInventory(self):
        [model.returnModel() for model in self.model_list]

    def returnManPrice(self, number):
#        return (self.model_list[number].name, int(self.model_list[number].returnModPrice()) + (int(self.model_list[number].returnModPrice()) * self.upsell))
        return int(self.model_list[number].returnModPrice()) + (int(self.model_list[number].returnModPrice()) * self.upsell)

    def returnManPrices(self):
        nv = len(self.model_list) - 1
#        print nv
        while nv > -1:
            print int(self.model_list[nv].returnModPrice()) + (int(self.model_list[nv].returnModPrice()) * self.upsell)
            nv -= 1
#            print nv

    def returnBikesSold(self):
        nv = 0
        for mod in self.model_list:
            print "[{0}][Total Weight > {1}]".format(mod.name,mod.returnWeight()) #self.model_list[nv].returnManPrice()
            nv += 1

topike = Manufacturer("Topike", 0.2, [model1, model2, model3])
nubiek = Manufacturer("Nubiek", 0.2, [model4, model5, model6])

print topike.returnManPrices()
#print topike.returnManPrice(1)
#topike.returnPrice(1)
#topike.returnInventory()
#print " "
#nubiek.returnInventory()

class Shop():
    store_manufacturer_list = []
    def __init__(self, name, margin, store_manufacturer_list):
        self.name = name
        self.margin = margin
        self.store_manufacturer_list = store_manufacturer_list
        self.sold_list = []

    def returnStoreInventory(self):
        [model.returnBikesSold() for model in self.store_manufacturer_list]

    def removeInventory(self, man_number, mod_number):
#        print self.store_manufacturer_list[man_number].model_list[mod_number]
        self.sold_list.append(self.store_manufacturer_list[man_number].model_list[mod_number])
#        print self.sold_list[0]
        del self.store_manufacturer_list[man_number].model_list[mod_number]
        n = 0
        for x in self.store_manufacturer_list[man_number].model_list:
            print self.store_manufacturer_list[man_number].model_list[n]
            n += 1

    def returnShopPrice(self, man_number, mod_number):
        print (int(self.store_manufacturer_list[man_number].returnManPrice(mod_number)) + (self.store_manufacturer_list[man_number].returnManPrice(mod_number) * self.margin))

#    def returnShopPrices(self):
#        nv = len(self.store_manufacturer_list) - 1
#        nv2 = len(self.store_manufacturer_list.model_list) - 1
#        while nv2 > -1:
#            print int(self.store_manufacturer_list[nv].returnManPrice(mod_number)) + (self.store_manufacturer_list[nv].returnManPrice(mod_number) * self.margin)
#            nv -= 1



    def returnShopProfit(self):
        return self.sold_list[0].returnModPrice()

bikesandbikes = Shop("BnB", 0.2, [topike, nubiek])

#print bikesandbikes.returnStoreInventory()
#print bikesandbikes.returnShopPrice(0,0)

#print bikesandbikes.removeInventory(0,2)
#print bikesandbikes.returnShopPrice(1,2)
#print bikesandbikes.sold_list[0]
#print bikesandbikes.store_manufacturer_list
#print bikesandbikes.removeInventory(0,2)
#print bikesandbikes.returnStoreInventory()

#print topike.returnBikesSold()
#print nubiek.returnBikesSold()

#print bikesandbikes.returnShopProfit()

class Customer():
    bikes = []
    def __init__(self, name, funds, bikes):
        self.name = name
        self.funds = funds
        self.bikes = bikes

    def setFunds(self, change):
        self.funds += change

    def checkPrices(self):
        return self.bikes.returnStoreInventory()



jeff = Customer("Jeff", 200, [bikesandbikes])
markus = Customer("Markus", 500, [])
jules = Customer("Jules", 1000, [])

#print tom.funds
#tom.setFunds(-100)
#print tom.funds

