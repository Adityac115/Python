limit=int(input('enter number: '))
print([x for x in range(2, limit+1) if 0 not in [x%n for n in range(2, x)]])

'''how it's actually working
   
   or what my understanding is

for x in range(2,limit+1):
    if 0 not in list_values:                               |||| list_values=for n in range(2,x):
        print(x)                                                                  list_values.append(x%n)

             
this one checks if there is 0 so
 dont print number becuase it has factors available
                                                                         this list contains the remainder of x/n and if this list contains 0 that means there is a factor of that number is available hence dont print it
''' 
