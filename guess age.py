# age=18
# user_guess=int(input('your guess'))
# if age>user_guess:
#     print('low')
# elif age<user_guess:
#     print('high')
# elif age==user_guess:
#     print('right')
# else:
#     print('重新输入')
grade=int(input('输入你的成绩'))
if 90<=grade<=100:
    print('A')
elif 80<=grade<90:
    print('B')
elif 60<=grade<80:
    print('C')
elif 40<=grade<60:
    print('D')
elif 0<=grade<40:
    print('E')
else:
    print('wrong')
