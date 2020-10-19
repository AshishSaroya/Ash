x1=float(input("Enter marks in C  : "))
x2=float(input("Enter marks in C++  :"))
x3=float(input("Enter marks in Java  :"))
x4=float(input("Enter marks in W.D  :" ))
x5=float(input("Enter marks in Python :"))
count=0;

t=x1+x2+x3+x4+x5 ;
percentage=(t/500.0)*100;
if(x1<33):
    count += 1
if(x2<33):
    count += 1
if(x3<33):
    count += 1
if(x4<33):
    count += 1
if (x5<33):
    count += 1
if(count==0):
     print('PASS')
     print('percentage',percentage,'%')
elif(count<=2):
    print('REAPPEAR')
else:
    print('FAIL')


