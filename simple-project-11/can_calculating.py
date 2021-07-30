import math

def paint_calc(height, width, cover):
  no_of_cans =round((height*width)/cover)
  return no_of_cans





h = int(input("Height of wall"))
w = int(input("Width of wall"))
persq = 5
x= paint_calc(height=h, width=w, cover=persq)
print(x)

print(range(1,11))