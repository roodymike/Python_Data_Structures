from array import *;

array1 = array('i',[10,20,30,40,50,60]);
#insert an element into an array
array1.insert(1,70);
#delete an element in an array
array1.remove(60);
#search an element in an array
print(array1.index(40));
print("__________________");

#update an element in an array
array1[2] = 25;

for x in array1:
    print(x);