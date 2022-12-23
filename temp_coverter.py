def to_celsuis(temp):
    return (temp-32)*5/9

for i in range(0,101,10):
    print("{:>3} F  |  {:>6.2f}  C".format(i,to_celsuis(i)))