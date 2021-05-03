import random

mine = input("가위/바위/보를 입력하세요.")

com = ""
result = ""

rand = random.random()

if rand > 0.66:
    com = "가위"
elif rand > 0.33:
    com = "바위"
else:
    com = "보"

# 쌤 방법
# if mine == "가위" and com == "가위":
#     result = "비겼습니다."
    
if mine == "가위":
    if com == "가위":
        result = "비겼습니다."
    if com == "바위": 
        result = "졌습니다."
    if com == "보": 
        result = "이겼습니다."

elif mine == "바위":
    if com == "가위": 
        result = "사용자가 이겼습니다."
    if com == "바위":
        result = "사용자가 비겼습니다."
    if com == "보":
        result = "졌습니다."

elif mine == "보":
    if com == "가위": 
        result = "사용자가 졌습니다."
    if com == "바위": 
        result = "사용자가 이겼습니다."
    if com == "보": 
        result = "비겼습니다."
        
print("사용자가 입력한 값 : ", mine)
print("컴퓨터가 입력한 값 : ", com)
print("결과 : ", result)
