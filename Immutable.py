# tuples are immutable
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)

# strings are immutable
message = "Hi devdatta!!!"
message[0] = 'peepppep'
print(message)

# range are immutable
myrange  = range(0,1,10)
myrange[0] = 3
print(myrange)

# id is imuutable
a = 1
b = 1
print(id(a))
print(id(b))
a = 2
print(id(a))
