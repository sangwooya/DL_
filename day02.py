vowels = 'aeiou'
letter = 'x'
if letter in vowels:
    print("실행한됨")



sum=1+\
    2+\
    3+\
    4
print(sum)  #백슬래쉬 줄변환

disaster=1      #if구문
if disaster:
    print ("yes")
else:
    print("no")

x=5
print(x<=5 and x>5)
a=[]
a.append(2)
print(bool(a))

vowels = 'aeiou'
letter = 'a                '
if letter in vowels:  #in 사용
    print("실행한됨")
else:
    print("실행됨")

limits=20 #숫자제한
tweets = "pass"*6
diff=limits - len(tweets)
if diff >= 0:
    print(tweets)
else:
    print(f'제한 글자수 {abs(diff)}')





