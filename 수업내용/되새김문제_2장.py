# 1번
a = 80
b = 75
c = 55
(a+b+c)/3

# 2번
num = 13
num % 2 == 0

# 3번
pin = '881120-1068234'
yyyymmdd = '19' + pin[:pin.find('-')]
num = pin[pin.find('-')+1:]
print(yyyymmdd)
print(num)

#4번
pin = '881120-1068234'
pin[pin.find('-')+1]

#5번
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#6번
a=[1,3,5,4,2]
a.sort()
a.reverse()
a


#7번
a=["Life","is","too","short"]    
result = " ".join(a)
result

#8번
a=(1,2,3)
a+= (4,)
a

#9번
"""3번 / 키는 변경 불가능해야함"""

# 10번
a = {'A':90,'B':80,'C':70}




a=["Life","is","too","short"]
a.index("Life")



# 12번
a = b = [1,2,3]
a
b
a[1] = 4
print(b)

# a와 b 모두 동일한 [1,2,3] 리스트 객체를 가르키고 있기 때문이다.
