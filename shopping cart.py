basket = {}
print('''
1.Entry:
2.Remove:
3.View
0.Exit program''')
option= int(input())
while option!=0:
    if option==1:
        a=input("Enter your products:")
        b=input("Enter your quantities:")
        basket[a]=b
        print(basket[a])
    elif option==2:
      a=("Enter an item")
      del (basket[a])
    elif option==3:
        for i in basket:
          print(i,basket[a])
    elif option==0:
        print("Stop")
else:
    print("program is cancelled")


