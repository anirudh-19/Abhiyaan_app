m= int(input("M "))
n= int(input("N "))
k= int(input("K "))
p= m*n
l=[] #Outer list to host the matrix
b=[] #creating a second list that does not have segmenting, rather contains just the values (easier to sort)

for i in range(m):
    c=[]
    for j in range(n):
        val=int(input("Value "))
        c.append(val)
        b.append(val)
    l.append(c)

b.sort()

for j in range(m*n):
    if b[j]==k:
        print("True")
        break

else:
    print("False")
    
    

