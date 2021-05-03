

# print("3*"+str(1)+"="+str(3*1))
# print("3*"+str(2)+"="+str(3*2))

a = range(2,5)
print(a[0])
print(a[1])
print(a[2])

# range를 이용하여 구구단 만들기
for i in range(1,9):
    print("3*"+str(i)+"="+str(3*(i)))
    

# print의 역할을 대신하는 것  / end=""
print("hel", end="")
print("lo")