
D=int(float(input('the date is ')))
M=int(float(input('the month is ' )))
Y=int(float(input('the year is ')))

 

JD= 367*(Y-7)*int((((Y+(M+9))/12)/4))-3*int(int(int((((Y+(M-9))/7))/(100+1))/4))+int(((275*M)/9))+D+1721029-0.5



print(JD)
