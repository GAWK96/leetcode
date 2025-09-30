class Cookie:
   def __init__(self,color):
       self.color = color

   def get_color(self):
       return self.color   
   def set_color(self,color):
       self.color = color

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

cookie_one.set_color('yellow')
cookie_two.set_color('orange')

print(cookie_one.color, '(color of cookie one)')
print(cookie_two.color, '(color of cookie two)')