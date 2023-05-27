# Halman 22 atas

class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is: ', cookie_one.get_color())
print('Cookie two is: ', cookie_two.get_color())

# halaman 22 bawah


class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is: ', cookie_one.get_color())
print('Cookie two is: ', cookie_two.get_color())

cookie_one.set_color('yellow')

print("\n Cookie one is now: ", cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())


#Halaman 23 atas

num1 = 11

num2 = num1

print("Before num2 value is updated: ")
print("num1 =", num1)
print("num2 = ", num2)

print("\n num1 points to: ", id(num1))
print("num2 points to: ", id(num2))

#Halaman 23 Tengah

num1 = 11

num2 = num1

print("Before num2 value is updated: ")
print("num1 =", num1)
print("num2 = ", num2)

print("\n num1 points to: ", id(num1))
print("num2 points to: ", id(num2))

num2 = 22

print("\n After num2 value is updated: ")
print("num1 = ", num1)
print("num2 = ", num2)

print("\n num1 points to: ", id(num1))
print("num 2 points to : ", id(num2))

#Halaman 23 bawah

dict1 = {
    'value' : 11
}

dict2 = dict1

print("\n Before value is updated: ")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\n dict1 points to : ", id(dict1))
print("dict2 points to: ", id(dict2))

# Halaman 24 atas
dict1 = {
    'value' : 11
}

dict2 = dict1

print("\n Before value is updated: ")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\n dict1 points to : ", id(dict1))
print("dict2 points to: ", id(dict2))

dict2['value'] = 22

print("\n After value is updated: ")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\n dict1 points to: ", id(dict1))
print("dict 2 points to: ", id(dict2))