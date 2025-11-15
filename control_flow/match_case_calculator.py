numb1 = int(input("enter the first number "))
numb2 = int(input("enter the second number "))
operation = input ("chooose the operation (+,-,*,/)""")
if operation == "+":
     sum= numb1 + numb2 
     print (f"the result is {sum }")

elif operation == "-":
  diff = numb1- numb2
  print (f"the result  is :{diff}")
elif operation == "*":
  product = numb1* numb2
  print (f"the result is {product }")
elif operation == "/":
    if numb2 == 0:
      print ("math error")
    else :
          div = numb1 / numb2
          print(f"the result is {div}")
else :
   print ("invalid input operation ")