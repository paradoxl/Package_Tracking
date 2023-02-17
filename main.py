#Michael Evans
import packages

print("")
print("Welcome to WGU UPS!")
print("What can blue do for you?")
print("1: Show all packages")
print("2: Truck stats")
print("3: Exit")
menuSelection  = input("Please select a menu: ")
print("You have selected ", menuSelection)

if menuSelection == '1':
        print(packages.getPackages())