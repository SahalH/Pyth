# Sahal  03/05/2022

Cost = 0

#Sizes
Small = 2
Medium = 3
Large = 4

#Type
Brewed = 0
Espresso = 0.5
Coldbrew = 1

#Flavouring
none = 0
Other = 0.50


Size = input("What size do you want? Small, Medium, or Large?")

Size = Size.upper()

if Size == "LARGE":
    Cost = Cost + Large
    print("Okay. Large for you!")
elif Size == "MEDIUM":
    Cost = Cost + Medium
    print("Okay. Medium for you!")
elif Size == "SMALL":
    Cost = Cost + Small
    print("Okay. Small for you!")
else:
    print("This isnt a size")
    exit()

    
    
Type = input("How do you want your coffee? Brewed, Espresso or Cold brew?")

Type = Type.upper()

if Type == "BREWED":
    Cost = Cost + Brewed
    print("Okay. Brewed for you!")
    
elif Type == "ESPRESSO":
    Cost = Cost + Espresso
    print("Okay. Expresso for you!")
    
elif Type == "COLD BREW":
    Cost = Cost + Coldbrew
    print("Okay. Cold brew for you!")
    
else:
    print("This isnt a type") 
    exit()
    
    
Flavour = input("What Flavour do you want? None, Vanilla, Hazelnut or Caramel?")

Flavour = Flavour.upper()

if Flavour == "NONE":
    Cost = Cost + none
    print("Okay. I wont add any Flavour!")
    
elif (Flavour == "VANILLA") or (Flavour == "HAZELNUT") or (Flavour == "CARAMEL"):
    Cost = Cost + Other
    print("Okay. We will add this Flavour for you!")
    
else:
    print("This isnt a Flavour")
    exit()
    

print("You have placed an order for a", Size , Type , "with", Flavour, "flavour.")

tip = (Cost / 100) * 15

Cost = Cost + tip

print("The total will be", Cost)

