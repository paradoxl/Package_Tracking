#Michael Evans
import packages


print("")
print("Welcome to WGU UPS!")
print("What can blue do for you?")
print("1: Package lookup")
print("2: Truck stats")
print("3: Exit")
menuSelection  = input("Please select a menu: ")
print("You have selected ", menuSelection)

if menuSelection == '1':
    packageId = input("Please enter the package ID you are looking for: ")
    packages.getPackages(packageId)