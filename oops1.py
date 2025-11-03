# Initiate a class
class employee:
    # special function (method) / Magic method / dunder method - constructor
    def __init__(self):
        # print("Started Executing Attributes/data")
        self.id = 123
        self.salary = 25000
        self.designation = "SDE"
        # print("Attributes / data have been initiated")

    def travel(self,destination):
        # print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")




# Creating an Object/Instance of class
sam = employee()
#printing a attribute
# print(sam.id)
#calling a method 
# sam.travel('Kerala')

print(type(sam))