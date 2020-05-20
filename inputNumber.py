import sys #sytem import
def BinaryConversion():
   
    i1 = input("Enter First Decimal Number?") #Input integer i1
    n1=list(i1) #Creates new list ie seperates the digits(eg 55=[5,5])
    while 1:
        try:
            while int(i1):
                if int(i1)>255:
                    print("Error! Input must be between 0-255")
                    i1 = input("Enter First Decimal Number?") #Input integer i1
                else:
                    break
            break
        except:
            print("Error! Input cannot be string")
            i1 = input("Enter First Decimal Number?") #Input integer i1
        
    i2 = input("Enter Second Decimal Number?") #Input integer i2
    while 1:
        try:
            while int(i2):
                if int(i2)>255:
                    print("Error! Input must be between 0-255")
                    i2 = input("Enter second Decimal Number?") #Input integer i2
                else:
                    break
            break
        except:
            print("Error! Input cannot be String,")        
            i2 = input("Enter second Decimal Number?") #Input integer i2
    n2=list(i2)
    if int(i1)>255 or int(i2)>255:
        print("Error! Input must not be between 0-255")
        sys.exit()
    
    
    
    
            
    no3=int(i1) #adding no3 and no3 int 
    no4=int(i2)
    list1=[] #Creating empty list1 and list2
    list2=[]
    if int(no3)<=255 and int(no3)>=0 and int(no4)<=255 and int(no4)>=0 and (no3+no4)<=255:#check condition
        db1=bin(no3) #Conversion of integer to binary number
        db2=bin(no4)
        l1=list(db1) #Adding binary number in lists
        l2=list(db2)
        l1F=l1[2::] #only add content after 2 index
        l2F=l2[2::]
        print("The first number to binary is :",''.join(l1F))
        print("The second number to binary is :",''.join(l2F))
        while len(l1F) < 8: #Adding zeroes values if list is less than 8 to match 8 bit binary numbers
            l1F.insert(0,0)
        while len(l2F) <8:
            l2F.insert(0,0)
        
        

        for i in range(len(l1F)):
            l=int(l1F[i]) #Converting string values to Integer
            m=int(l2F[i])
            list1.append(l) #Adding Integer in list
            list2.append(m)
           
    else : #Display error message if input doesn't match if loop condition
            print("ERROR! The sum value must not exceed or less than the actual size of byte-coded integer 0 and 255")
            sys.exit()
    return list1, list2 #Returns list1 and list 2
