import vinlib
import time
t1=time.time()
a=vinlib.decode_vin('1ZVBP8JZ9E5265717')
t2=time.time()
print(vinlib.Vin('1ZVBP8JZ9E5265717').year)
t3=time.time()
print(t2-t1)
print(t3-t2)

print(a.vin)
print(a.check)
print(a.year)
print(a.wmi)

a.year
print('doing tests ')
print(vinlib.Vin('1ZVBP8JZ9E5265717').year)
print(vinlib.Vin('1ZVBP8JZ9E5265717').check)
print(vinlib.Vin('1G3EZ57Y2FE330903').year)
print(vinlib.decode_vin('1G3EZ57Y2FE330903').year)
