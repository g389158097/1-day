count=0
age=18

while count<3:
    user_guess=int(input('your guess'))
    if age > user_guess:
        print('low')
        count+=1
    elif age < user_guess:
        print('high')
        count+=1
    elif age == user_guess:
        print('right')
        break
    else:
        print('重新输入')
        count+=1
    if count==3:
      print('三次机会用完')
      x=input('是否还想玩,X/Y')
      if x == 'X':
       print("--------end")
      elif x== 'Y':
       count=0




