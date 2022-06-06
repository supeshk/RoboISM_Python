def func(ll,ul):
    for num in range(ll, ul + 1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num)

lower=int(input('Enter Lower limit:'))
upper=int(input('Enter Upper limit:'))
func(lower,upper)