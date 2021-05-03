#03 출력할 구구단은? ex) '3' 입력 -> 3단 출력
num3 = int(input("출력할 구구단을 입력하세요."))

for i in range(1, 9) :
    print(str(num3) + "*" + str(i) + "=" + str(num3*i))