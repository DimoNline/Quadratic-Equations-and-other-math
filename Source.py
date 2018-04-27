from math import sqrt
import sl4a
droid = sl4a.Android()
def Alert(msg):
	#title='Roots'
	droid.dialogCreateAlert(msg,msg)
	droid.dialogSetPositiveButtonText(msg)
	droid.dialogShow()

def unequalation():
 eq=input("Введите знак")
 a=float(input("x²"))
 b=float(input("x"))
 c=float(input("k"))
 d=b*b-(4*a*c)
 if d>=0:
  sqrtd=sqrt(d)
  tmpx1=(-b-sqrtd)/(2*a)
  tmpx2=(-b+sqrtd)/(2*a)
  x1=max(tmpx1,tmpx2)
  x2=min(tmpx1, tmpx2)
  
  if eq==">":
   print("x€(-∞;", x2,")", "(", x1, ";+∞)")
  elif eq==">=":
   print("x€(-∞;", x2,"]", "[", x1, ";+∞)")
  elif eq=="<":
   print("x€(", x2,";", x1,")")
  elif eq=="<=":  
   print ("x€[", x2,";", x1,"]") 
 elif d==0:
  x=(-b)/(2*a)
  if eq==">":
   print("x€(-∞;", x,")", "(", x, ";+∞)")
  elif eq==">=":
   print("x€R")
  elif eq=="<":
   print("x€(-∞;", x,")", "(", x, ";+∞)")
  elif eq=="<=":
   print ("x€R")
 else:
  print("Корней нет, значит х€R-Q")
 
def vectorLenght():
 x1=float(input("x1"))
 y1=float(input("y1"))
 x2=float(input("x2"))
 y2=float(input("y2"))
 numerator=(x1*x2)+(y1*y2)
 denominator=sqrt(x1**2+y1**2)*sqrt(x2**2+y2**2)   
 result=numerator/denominator
 return result

def equalation():
 a=float(input("x²"))
 b=float(input("x"))
 c=float(input("k"))
 d=b*b-(4*a*c)
 if d>=0:
  sqrtd=sqrt(d)
  x1=(-b-sqrtd)/(2*a)
  x2=(-b+sqrtd)/(2*a)
  print(x1)
  print(x2)
  return x1,x2
 else: print("No roots")
def main():
 choose=input()
 if choose=="v": Alert(str(vectorLenght()))
 elif choose=="e": Alert(str(equalation()))
 elif choose=="u": unequalation()
 elif choose=="m": none
while True:
 main()
