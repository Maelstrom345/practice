# list datastructure
#list are mutable/Changable

my_list = ["Banana","Mangoes","Oranges","Apples"]

print(my_list)

my_list[1] ="Banana"

print(f"I love eating {my_list[1]}")

list =[9,5,1,4,2,3,8,6,7]
list.sort()

print(list)

#tuple
my_tuple = (9,5,1,4,2,3,8,6,7)

print(my_tuple)

#set
my_set={"Kenya","Uganda","Nigeria","Tanzania"}
print(my_set)
my_set.add("Senegal")
print(my_set)

#dictionaries
my_dic = {"name":"Joseph","age":"17","Gender":"Male","profession":"jobless person"}
print(my_dic)
print(f"My name is {my_dic['name']}")
print(f"I am {my_dic['age']} years")
print(f"I am a {my_dic['Gender']}")
print(f"I am a {my_dic['profession']}")