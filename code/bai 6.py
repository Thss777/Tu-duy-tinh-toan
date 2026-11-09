a,b,c=map(float, input().split())
p=(a+b+c)/2
import math
S= math.sqrt(p*(p-a)*(p-b)*(p-c))
if a+b>c and b+c>a and a+c>b:
    print(S)
else:
    print("Khong phai 3 canh cua tam giac")