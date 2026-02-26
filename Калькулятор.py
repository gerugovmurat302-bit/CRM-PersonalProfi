number1 = float(input("Введите первое число: "))
operation = input("Выберите операцию (+, -, * или /): ")
number2 = float(input("Введите второе число: "))
if operation == "+":
   result = number1 + number2
elif operation == "-":
   result = number1 - number2
elif operation == "*":
   result = number1 * number2
elif operation == "/":
   if number2 == 0:
       result = "На ноль делить нельзя!"
   else:
       result = number1 / number2
else:
   result = "Неверная операция!"
print("Результат:", result)