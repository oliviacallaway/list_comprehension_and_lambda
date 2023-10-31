remainder=lambda num: num % 2
print(type(remainder))
print(remainder(5))


product=lambda x,y: x*y
print(product(2,3))

def testfunc(num):
    return lambda x:x *num

result10=testfunc(10) #assigns 10 to num
result100=testfunc(100)

print(type(result10))
print(type(result100))

print(result10(9))
print(result100(9))

result10=lambda num: num*10  #also assigns 10 to num but hard coding
result100=lambda num: num*100

numbers_list=[2,6,7,10,11,4,12,7,13,17,0,3,21]

filtered_list=list(filter(lambda num: (num>7), numbers_list))

print(filtered_list)

def divide2(num):
    return num % 2


#both below have the same output
mapped_list=list(map(divide2, numbers_list)) #wrapping this in a list makes it readable 
print(mapped_list)
mapped_list=list(map(lambda num: num %2, numbers_list))
print(mapped_list)

