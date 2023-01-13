import random

a= random.randint(1,10)  # randint 함수 1에서 10까지 아무거나 나옴

limits = 20
diff= limits - 4*a
if diff >= 0:
    print("1에서5사이 나옴")
else:
    print("6에서 10 나옴")

    #과제 1에서 10까지
    #연습문제 4.8 책 105쪽

secret=random.randint(1,10)
guess=random.randint(1.10)
diff= secret-guess
if diff>0:
    print('too low')
elif diff<0:
    print('too low')
else:
    print('just right')
