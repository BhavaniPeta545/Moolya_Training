f=open("file.txt")
l=f.readlines()
for i in l:
    print(i.strip())
f.close()
l=[]


with open("file.txt") as f:
    for i in f.readlines():
       l.append(i.strip())
print(l)
rev=l[::-1]


with open("file.txt","a") as f:
    for i in rev:
        f.write(i)
        f.write('\n')

with open("file.txt","r") as f:
    print(f.read(5))

with open("file.txt","a+") as f:
    print()
    f.write("hiarhduirmd")

with open("file.txt","r") as f:
    print(f.readlines())









