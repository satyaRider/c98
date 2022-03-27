def countwordsfromfile():
     filename=input("enter the file name: ")
     
     numberofwords=0
     
     file=open("satya.txt",'r')
     for line in file:
         words=line.split()
         numberofwords=numberofwords+len(words)
     
     print("number of words: ",numberofwords)     


countwordsfromfile()



