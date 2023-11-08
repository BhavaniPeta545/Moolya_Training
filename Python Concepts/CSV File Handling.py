import csv

#File handling with .csv file
with open(r'C:\Users\hp\Downloads\addresses.csv',"w") as f2:
    write_obj= csv.DictWriter(f2,["name","sname","address","country","code"])
    write_obj.writeheader()
    write_obj.writerow({"name":"hari","sname": "gadepalli","address": "hyd","country":"ind", "code":234})
    write_obj.writerow({"name": "haergri", "sname": "gadepli", "address": "hyd", "country": "and", "code": 134})


with open(r"C:\Users\hp\Downloads\addresses.csv","r") as f2:
    read_obj=csv.DictReader(f2)
    add=0
    for row in read_obj:
        add+=float(row["code"])
    print(add)

with open(r"C:\Users\hp\Downloads\addresses.csv","r") as f2:
    add=0
    read_obj=csv.reader(f2)
    next(f2)

class Cl1:
    @classmethod #when we created as classmethod we dnt need object creation
    # def data(cls):
    #     with open(r"C:\Users\hp\Downloads\addresses.csv", "r") as read:
    #         file = csv.reader(read)
    #         for i in file:
    #             print(i)
Cl1.data2()

    #output
    # ['name', 'sname', 'address', 'country', 'code']
    # []
    # ['hari', 'gadepalli', 'hyd', 'ind', '234']
    # []
    # ['haergri', 'gadepli', 'hyd', 'and', '134']
    # []
    @staticmethod
    def data1():
        with open(r"C:\Users\hp\Downloads\addresses.csv", "r") as read:
            file = csv.reader(read)
            for i in file:
                print(i)

    ['name', 'sname', 'address', 'country', 'code']
    []
    ['hari', 'gadepalli', 'hyd', 'ind', '234']
    []
    ['haergri', 'gadepli', 'hyd', 'and', '134']
    []
    @staticmethod
    def data2():
        with open(r"C:\Users\hp\Downloads\addresses.csv", "r") as read:
            file = csv.DictReader(read)
            l=list(file)
            for i in l:
                print(i)

Cl1.data2()

a=(9,12,332,"bhavani")
b=(2,3,4,"hari")
print(a)
print(type(b))
print(a[3])
print(a.index("bhavani"))
print((*a,*b))

#Regular Expressions
import re
# print(re.findall(r'[^Python]',"Bhavani is learning python in python class"))
# res=re.search(r'small',"small animals are cute")
# print(res.start())
print(re.search(r'[^a-zA-z]',"1sunil"))
print(re.search(r's.',"sunil is working sunil"))
print('Range',re.search(r'[\d{1,2}\/\d{1,2}\/\d{2,4}]',"10/22/2023 in working sunil"))

#Sets
s={1,2,3,3,3,5,4,3,6,7,6,7,-1}
# print(type(s))
# print(s)
s1=set((1,2,3,4))
# print(s1)
# print(len(s1))
c=s.symmetric_difference(s1)
d=s.intersection(s1)
print(s.difference(s1))
print(s.union(s1))
s.intersection_update(s1)
print(s)
s.remove(4)
print(s)
print(s1.issubset(s))
print(s.issubset(s1))

#Dictionary
d={"name":"bhavani","age":23,20:"mani"}
d1=(1,2,3,4)
print(d)
d[20]="nani"
print(d)
print(d["name"])
print(d.keys())
print(d.values())
print(d["name"]=="bhavani")
d[10]="raju"
print(d)
# d.update(d1)
print(d)
res=dict.fromkeys(d1)
print(res)

#Continue
for i in range(0,9):
    if i==5:
        continue
    print(i)


