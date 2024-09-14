#Latihan 1 slide 27
print ("Hello, world!")
print ("Nama saya Alfaris")
print ("NIM saya 2023071028")
#Latihan 1 s.28
if 5>2:
    print("Five is greater than two!")
#Latihan 1 s.29
x = 5
y = "John"
print (x)
print (y)
#Latihan 1 s.30
x = 4 
x = "Agus"
print(x)
#
def getfirst(mylist):
    return (mylist[0])

print (getfirst([1,2,3]))

print (getfirst([1,2,3]))

print (getfirst([1,2,3,4,5,6,7,8,9]))

#memperoleh getsecond

def getsecond(mylist):
    return (mylist[1])

print (getsecond([1,2,3]))

#memperoleh getlast 
def getlast(mylist):
    return (mylist[-1])

print (getlast([1,2,3,4,5]))

#analisis performa: notasi big 0
def getsum(mylist):
    sum = 0
    for item in mylist:
        sum = sum+item
    return sum 

print (getsum([1,2,3,4]))
print (getsum([1,2,3]))
print (getsum([1,2,3,4]))

#latihan s.36
def getkali(mylist):
    hasil = 1  # mulai dengan 1 agar perkalian berjalan
    for item in mylist:
        hasil = hasil * item
    return hasil

print(getkali([1, 2, 3, 4]))   
print(getkali([1, 2, 3, 4, 5])) 

#s.37
def getbagi(mylist):
    hasil = 1  # mulai dengan 1 agar perkalian berjalan
    for item in mylist:
        hasil = hasil / item
    return hasil

print(getbagi([1, 2, 3, 4]))   
print(getbagi([1, 2, 3, 4, 5]))

#s.38
def getsum(mylist):
    sum = 0  
    for row in mylist:
        for item in row:
            sum += item
    return sum

print(getsum([[1, 2, 5],[3, 4, 7]]))
print(getsum([[1, 2], [3, 4]]))

#s.39
hm1 = [1, 2, 3, 4, 5]
hm2 = [1, 2, 3]

getSum1 = 0
for num in hm1:
    getSum1 += num

getSum2 = 0
for num in hm2:
    getSum2 += num

print(getSum1/getSum2)

#s.40
hm1 = [1, 2, 3, 4, 5]
hm2 = [1, 2, 3]

getSum1 = 0
for num in hm1:
    getSum1 += num

getSum2 = 0
for num in hm2:
    getSum2 += num

print(getSum1-getSum2)   

#link github https://github.com/AlFaris2211