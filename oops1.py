# Initiate a class
class employee:
    # special function (method) / Magic method / dunder method - constructor
    def __init__(self):
        # print("Started Executing Attributes/data")
        print(id(self)) #id - memory location 
        self.id = 123
        self.salary = 25000
        self.designation = "SDE"
        # print("Attributes / data have been initiated")

    def travel(self):
        # print("This travel method was called manually")
        print(f"Employee is now travelling to delhi")



# Creating an Object/Instance of class
sam = employee()
sam.name = 'Sam Smith' #ate attribute from outside.
print(sam.name)
# print(id(sam))
# jak= employee()
# print(id(jak))
#printing a attribute
# print(sam.id)
#calling a method 
# sam.travel()      
# print(type(sam))