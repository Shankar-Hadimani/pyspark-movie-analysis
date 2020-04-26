a = [10.1,10979799.2,10.3]
s = sum(a)
c = len(a)
m = max(a)

mean = s/c
print("avg is  :"+ str(mean), m)

z = a.__ge__(10.0)
print(z)