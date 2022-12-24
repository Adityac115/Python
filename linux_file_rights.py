def converter(octal):
    rights=""
    values=[(4,'r'),(2,'w'),(1,'x')]
    for i in [int(n) for n in octal]:      #when 755 comes
        for num,letter in values:           #this loop is only going to run 3 times so if 7 comes as first num this will happen 
            if i>=num:              #1st:7   # i=7 comes , 7>=4 then, " "+'r' ,then i=7-4 ,gives i=3 for next iteration
                rights+=letter                # i=3 comes , 3>=2 then, "r"+'w' ,then i=3-2 ,gives i=1 for next iteration
                i-=num                         # i=1 comes , 1>=1 then, "rw"+'x' ,then i=1-1, gives i=0 for next iteration  
            else:                               # but here iteration stops because we already done 3 iterations,now comes 2nd           
                rights+='-'         #2nd:5   # i=5 comes , 5>=4 then, "rwx"+'r' , then i=5-4 ,gives i=1 for next iteration         
    return rights                             # i=1 comes , 1>=2 here condition is false , so we add "rwxr"+'-',i=1 for next iteration
                                               # i=1 comes , 1>=1 then, "rwxr-"+'x' , then i=1-1, gives i=0 for next iteration
                                                # but here iteration stops because we already done 3 iterations,now comes 3rd
                                    #3rd:5   # i=5 comes , 5>=4 then, "rwxr-x"+'r' ,then i=5-4, gives i=1 for next iteration
                                              # i=1 comes , 1>=2 here condition is false ,so we add "rwxr-xr"+'-',i=1 for next iteration
                                               # i=1 comes , 1>=1 then, "rwxr-xr-"+'x' ,then i=1-1, gives i=0 for next iteration
                                                ## but here iteration stops because we already done 3 iterations, and we iterated over the given octal

                                    ##  result is : "rwxr-xr-x"                                                


print(converter(input('Enter the octal number for which you want to see rights: ')))



