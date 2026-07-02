import random
pp  = random.randint(1,100)
print(int(pp))
player = 0
while player != pp:
    player = int(input("เลขของคุณ "))
    if player > pp:
        print("มากไป")
    elif player < pp:
        print("น้อยไป")
    else: 
        print("ถูกต้อง")