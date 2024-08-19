var_1 ='usama hassan'
type(var_1)


print(var_1.title())
print(var_1.find('a'))


var_list = [1,2,3,4 ,5,6,7,8,9,10]
print(var_list)

var_list = list()



list_of_all_dt =['Aplha',1,1.1, True, [1,2]]
print(list_of_all_dt)


var_list = []
print(var_list)
var_list = [1, 2, 3]
print(var_list)

var_list = list([1,2,3])
print(var_list)

# copy by reference example of list
var_list_main = [2, 4, 6, 8, 10]
print(var_list_main)
var_list_copy = var_list_main
print(var_list_copy)
var_list_copy.pop()
print(var_list_copy)
print(var_list_main)


var_str = 'awais akram'
print(var_str.title())
print(var_str)

var_list_main = [2, 4, 6, 8, 10]
print(var_list_main)
var_list_copy = var_list_main.copy()
print(var_list_copy)
var_list_copy.pop()
print(var_list_copy)
print(var_list_main)



list_of_all_dt = ['Alpha', 1, 1.1, True, [1,2]]
print(list_of_all_dt)


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

name = 'muhammad usama'
print(f'hy my name is : {name}')

string = 'abcdef ghi'
string[0]
string[6]
string[0:6]


#loop ********************************
# iterate over some things
for i in range(1,10,2):
    print(f'this is my value {i}')

for i in range(10,0,-2):
    print(f'this is my value {i}')

# foreach loop ************
#kisi list ya value per chalna 

names = ['a', 'b', 'c', 'd']
for usama in names:
    print(usama)

for char in 'Muhamamd Usama' [:10:2]:
    print(char)

# list ko index ke sath print krati hai ye function enumerate ********************************

list = ['usama', 'hassan', 'khan', 'Chapati']    

for single_value in enumerate(list):
    print(single_value)


# Multiple decractions ********************************

a,b,c = 'usama', 'hassan','riaz sign'
print(a,b,c)



# tuple ********************************
var_tuple = [1,'usama','hassan', []]
var_tuple.count(1)
var_tuple.index('hassan')

# Sets ******************************** it delete duplicates ********************************
var_list = [1,'usama','hassan','hassan']
set(var_list)

# if ********************************
cars = ["toyota","bmw","honda"]
for car in cars:
    if car == 'toyota':
        print(car.upper())

    else:
        print(car.capitalize())


# Equality********************************

age = 40

age < 19
age > 19
age == 19

var12 = ['toyota','bmw','honda']
'toyota' in var12
'hyundai' in var12

# Dictionary ****************************************************************

var_dict = {"name":"usama", "fname":"riazulhassan"}
var_dict['name']
var_dict.get('fname')

var_dict.keys()
var_dict.values()
var_dict.items()

for key, value in var_dict.items():
    print(f'for key :{key} we have the value {value}')

# replace********************************

var_dict['name'] ='fayyaz'
print(var_dict)

# add********************************

var_dict['age'] = 25
var_dict['address'] = "national park"
print(var_dict)

#****************************************************************


def usama():
    print("hello world")
usama()    

