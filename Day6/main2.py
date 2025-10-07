
# File Handling
#  r = open('sample.txt')

p = open(r'C:\Users\GOD.DEBANG\Desktop\Python_Cource\Day5\main.py')
print(p.read())
# w = open('Sample2.txt','w')
q = open('Sample2.txt','w')
q.write('This is a new line')
q.close
# a = open('Sample2.txt','a')
a = open('Sample2.txt','a')
a.write('\nThis is an appended line')
a.close

# x = open('Sample3.txt','x')

#  x = open('Sample2.txt','x') # It will give an error because the file already exists.