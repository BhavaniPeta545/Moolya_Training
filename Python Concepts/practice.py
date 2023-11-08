list_ = [1, 2, 3, 4]
res=[i**2 for i in list_]
print(res)

# even=[i for i in range(0,10) if i%2==0]
# print(even)
# odd=[i for i in range(1,77) if i%2!=0]
# print(odd)

list_ = ['kasi' , 'jmr', 'mohana' , '123']
even=[item if len(item)%2==0 else item[::-1]for item in list_]
print(even)

