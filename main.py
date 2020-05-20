import sys #sytem import
import iterator as m1 #import as m1
from inputNumber import BinaryConversion #import BinaryConversion
no3=[] #list variable
global n5 #global variables
def output(): #output function
    n=''
    for i in range (len(m1.sumF)): #length sum
        no = str(m1.sumF[i]) #change to string
        n=n+no #add no list

        no3.append(no)
    print("The binary sum is:",int(n))

def magic(no3): #magic function             
    no3 = map(str, no3) #map string and no3
    no3 = ''.join(no3) #join empty string with no3
    
    no3 = int(no3,2) #convert no3

    return no3 #return no3


m1.totalSum() #total sum
output() #output
n=magic(no3) #sum of lists
print("Decimal output is",n) #display m
i3 = input("Do you want to Continued the program? (Y/N)") #take input
while i3=="y" or i3=="Y": #if yes
    m1.li1.clear() #clear lil1 and li2
    m1.li2.clear()
    m1.sumF.clear()
    no3.clear()
    m1.totalSum() #display total sum
    output()
    n=magic(no3) #print n
    print("Decimal output is",n) #print n
    i3 = input("Do you want to Continued the program? (Y/N)")  
    
else: #if no
    print("Thank you for using this program! The program will now terminate")
    sys.exit() #exit the program
