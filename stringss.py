
a="Aditya kushwaha"
# print(a[1])
# print(a[0])
# print(a[-1])
# print(a[-2])

''' slicing the string'''


# includes the start value but ignore the end value , goes from start to end-1
# a[start:end:Step_value]
# step value is just hopping 

# print(a[1:8:2])

# print(" ".join(a))


# print("...".join(["hello", "there", "my", "name","is", "Aditya", "kushwaha"]))


'''format string'''

# print("my name is {}".format("aditya"))

'''.2f and .3f let the {} know the data is float and we want only 2 and 3 decimal points as result '''

price=9.545
taxed_price=9.5*1.0954
print("The originial price is ${:.2f} and taxed_price is ${:.3f}".format(price,taxed_price))