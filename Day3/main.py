#   Loops 


#  - for loop

a = range(1,21,2)
for i in a:
    print(i)

b = range(20,51)
for i in b:
    print(i)

c = range(16,1,-1)
for i in c:
    print(i)

d = range(-5,-15,-1)
for i in d:
    print(i)    

for i in range(2,21,2):
    print(i)

e = int(input("Enter a number: "))
for i in range(e,(e*10)+1,e):
    print(i)
    
f = "DEBANG KUSWAHA"
for i in range(11):
    print(f)
for i in range(len(f)):
    print(i)
    # print(f[i])
for i in f:    
    print(i)



#  break and continue

for i in range(1,11):
    if i == 5:
        break
    else:
        print("Hello World")


for i in range(1,101):
    if i == 50:
        continue        
    print(i)



# - while loop

a = 1
while a <= 10:
    print(a)
    a += 1