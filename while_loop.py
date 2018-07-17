string = input("Enter your name:")
print(string)

num=int(input("Enter the value of n:"))
if(num<=0):
    print("Please enter the valid number")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
    print(sum)
