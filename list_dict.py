from itertools import zip_longest

#function to take two list
def two_list(lst1,lst2):
    d1=zip_longest(lst1,lst2)
    #Output:<itertools.zip_longest object at 0x00993C08>
    # Converting zip object to dict using dict() contructor.
    return dict(d1)


x = list(map(int, input("Enter the values of first list: ").split()))
y = list(map(int, input("Enter the values of second list: ").split()))
print(two_list(x,y))


