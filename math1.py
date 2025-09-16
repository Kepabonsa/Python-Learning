import math
# x = 3.14
# y = 4
# z = 5

# result = round(x)  # redondea
# result = abs(y)  # valor absoluto
# result = pow(4,3) # potenciación
# result = max(x, y, z)
# result = min(x, y, z)
# print(result)


# Operation with math library
# x = 9.9
# print(math.pi) #Pi
# print(math.e) #Euler
# result = math.sqrt(x) #Raiz
# result = math.ceil(x) #Redondea decimal por arriba
# result = math.floor(x) #Redondea decimal por abajo 

# print(result)

# Calcular circunferencia de un circulo

# radius = float(input("Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius  # 2 * pi * r
# print(f"The cirucumference is {round(circumference, 2)}cm")

# Area de un circulo
# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2) # pi * r^2  # ^ = Alt + 94 
# print(f"The area of the circle is: {round(area, 2)}cm^2")

# Calcular hipotenusa

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c= math.sqrt(pow(a,2)+ pow(b, 2))
print(f"Side c is = {c}")