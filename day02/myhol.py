import random

mine = input("홀/짝을 선택하세요.")

com = random.randint(1,100)

print("내가 예상한 결과 : " + str(mine))
print("컴퓨터가 출력한 숫자 : " + str(com))

if mine == "홀":
    if (com%2) == 1:
        print("정답입니다.")
    if (com%2) == 0:
        print("오답입니다.")

elif mine == "짝":
    if (com%2) == 1:
        print("오답입니다.")
    if (com%2) == 0:
        print("정답입니다.")


