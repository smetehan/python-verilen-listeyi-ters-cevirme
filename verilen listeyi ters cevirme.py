x=[1,2]
y=[3,4]
z=[5,6,7]
list=[x, y, z]

def Ters(x):
  x.reverse()
  return x
def Ters(y):
  y.reverse()
  return y
def Ters(z):
  z.reverse()
  return z


def Ters(list_2):
  list_2.reverse()
  return list_2
  list_2=[Ters(x), Ters(y), Ters(z)]
print(list_2)
