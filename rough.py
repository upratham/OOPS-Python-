# list = [1,2,3]
# my_str = "ml ops"
# my_int =122

# print(type(my_str))

# my_str=my_str.capitalize()
# print(my_str)

from oops_proj import chatbook

user1=chatbook()

# Calling function
# lst=[1,2,3]
# print(len(lst))

#Calling Method
#user1=chatbook()
#print(user1._chatbook__name)  # conventio to use the encapsulated attribute 'obj._classname__attribute'

## Getter and Setter

# print(user1.get_name())
# user1.set_name("Vinod")
# print(user1.get_name())
# user2=chatbook()
# print(user2.get_name())

# # Static Method

# user1=chatbook()
# print(user1.user_id)

# user2=chatbook()
# print(user2.user_id)

# user3=chatbook()
# print(user3.user_id)

# Use setter

chatbook.set_id(10)
user1=chatbook()
print(user1.user_id)

user2=chatbook()
print(user2.user_id)