def take_order(number):
    if number == 1:
        print("Welcome to the Burger Shop!")
    
    name = input("Enter your name: ")
    greeting = "Hello", name , "I will take your order now"
    print(greeting)
    chickenBurgerMeal = ["Chicken Burger", "Fries", "Small Fizzy Drink","Ketchup"]
    veganBurgerMeal = ["Vegan Burger", "Onion Rings", "Large Water","Mayo"]
    combos = [chickenBurgerMeal, veganBurgerMeal]

    
    
    
    
    comboOrMeal = input ('Combo? yes or no?')
    if comboOrMeal == 'yes':
        print("Which Combo?")
        for count, value in enumerate(combos):
            print ( str(count) + ". " + str(value) )
        comboOrMealentry = input ('Combo 1 or combo 2?')
        foodlist = combos[int(comboOrMealentry)]
        print("-")
        print("Your combo comes with")
        for i in foodlist:
            print(i)
        print("-")
        
        
        
        
    elif comboOrMeal == 'no':
        foodlist = []
        
        burger = input("Chicken Burger or Vegan Burger?")
        if (burger == "Chicken Burger"):
            foodlist.append("Chicken Burger")
        if (burger == "Vegan Burger"):
            foodlist.append("Vegan Burger")
            
        print(foodlist)

        
        
        
        side = input ("Garden Salad, Fries or Onion Rings")
        if (side == "Garden Salad"):
            foodlist.append("Garden Salad")
        elif (side == "Fries"):
            foodlist.append("Fries")
        elif (side == "Onion Rings"):
            foodlist.append("Onion Rings")
            
        print(foodlist)

        
        
        
        drink = input ("Large Fizzy Drink, Small Fizzy Drink, Large Water or Small Water?")
        if (drink == "Large Fizzy Drink"):
            foodlist.append("Large Fizzy Drink")
        elif (drink == "Small Fizzy Drink"):
            foodlist.append("Small Fizzy Drink")
        elif (drink == "Large Water"):
            foodlist.append("Large Water")
        elif (drink == "Small Water"):
            foodlist.append("Small Water")
            
        print(foodlist)

        
        
        
        condiment = input ("Mayo or Ketchup?")
        if (condiment == "Mayo"):
            foodlist.append("Mayo")
        elif (condiment == "Ketchup"):
            foodlist.append("Ketchup")
            
        print(foodlist)



    return foodlist




class FoodItem:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        return self.name
    
class Burger(FoodItem):
    def __init__(self,name):
        super().__init__( name)
    def priceBurger(self):
        if (self.name == "Chicken Burger"):
            self.price = 3
        elif (self.name == "Vegan Burger"):
            self.price = 4
        return self.price
    
    
class Drink(FoodItem):
    def __init__(self,name):
        super().__init__( name, )
    def priceDrink(self):
        if self.name == 'Large Fizzy Drink':
            self.price = 2
        elif self.name == "Small Fizzy Drink":
            self.price = 1.5
        elif self.name == "Large Water":
            self.price = 1.5
        elif self.name == "Small Water":
            self.price = 1
        return self.price

class Side(FoodItem):
    def __init__(self,name):
        super().__init__( name)
    def priceSide(self):
        if self.name == 'Fries':
            self.price = 1
        elif self.name == "Onion Rings":
            self.price = 1
        elif self.name == "Garden Salad":
            self.price = 1
        return self.price

class Condiment(FoodItem):
    def __init__(self,name):
        super().__init__( name)
    def priceCond(self):
        if self.name == 'Mayo':
            self.price = 0
        elif self.name == "Ketchup":
            self.price = 0
        return self.price
    
    
    
number = 1
while (number != 'no'):
    foodlist = take_order(number)
    burger = foodlist[0]
    side = foodlist[1]
    drink = foodlist[2]
    condiment = foodlist[3]
    

    MyBurger = Burger(burger)
    priceOfBurger = MyBurger.priceBurger()
    print(str(burger) + " will cost £" + str(priceOfBurger))

    MySide= Side(side)
    priceOfSide = MySide.priceSide()
    print(str(side) + " will cost £" + str(priceOfSide))

    MyDrink = Drink(drink)
    priceOfDrink = MyDrink.priceDrink()
    print(str(drink) + " will cost £" + str(priceOfDrink))

    MyCond = Condiment(condiment)
    priceOfCond = MyCond.priceCond()
    print( str(condiment) + " will cost £" + str(priceOfCond))
    
  
    total=priceOfBurger+priceOfSide+priceOfDrink+priceOfCond
    print("£" + str(total) + " will be the price")
   
    number += 1
    number = input("Would you like to order again? Enter Yes or No")


