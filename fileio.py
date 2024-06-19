                    #write the file
#f=open("myfile.txt","w")
#f.write("I am from bhopal.")
#f.close()

                    #append the file
#f=open("myfile.txt","a")
#f.write("\nI am from bhopal")
#f.close()

#f=open("myfile.txt","w")
#f.write("How are you.")
#f.close()

                    #read the file
#f=open("myfile.txt","r")
#data=f.read()
#print(data)
#f.close()

#a=str(input("Enter:-"))
#f=open("myfile.txt","r")
#data=f.read()
#if a in data:
#   print("yes")
#else:
#   print("no")
#f.close() 

#num=int(input("Enter the number:-"))
#f.open("myfile.txt","w")
#for i in range(1,11):
#    f.write(f,"{num} x {i} ={num*i}\n")
#f.close()

#num=int(input("Enter the number:-"))
#f.open("myfile_{num}.txt","w")
#for i in range(1,11):
#    f.write(f,"num*i={num*i}")
#    f.close()

#f=open("myfile.txt","w")
#f.write("How are you guys!")
#f.close() 

#f=open("myfile.txt","w")
#f.write("How are you guys!----")
#f.close()

#f=open("myfile.txt","r")
#data=f.read()
#print(data)
#f.close()

a=str(input("Enter:-"))
f=open("myfile.txt","w")
f.write(a)
f.close()

#abc=int(input("Enter the number:-"))
#f=open("myfile.txt","r")
#data=f.read()
#f.close()

        #readline the file of only first line 
f=open("file.txt","r")
data=f.readline()
print(data)
f.close()







