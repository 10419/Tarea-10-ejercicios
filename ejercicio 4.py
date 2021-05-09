def estCondicional01():
  print("Bienvenido ")
  n01=input("ingrese su nombre:")
  e01=int(input("ingrese su edad:"))
  n02=input("ingrese su nombre:")
  e02=int(input("ingrese su edad:"))
  n03=input("ingrese su nombre:")
  e03=int(input("ingrese su edad:"))
  if e01<e02:
    print(n01,"es menor porqu\u00eA tiene",e01)
  elif e01<e03:
    print(n01,"es menor porqu\u00eA tiene",e01)
  elif e03<e02:
    print(n03,"es menor porqu\u00eA tiene",e03)
  elif e03<e01:
    print(n03,"es menor porqu\u00eA tiene",e03)
  elif e02<e01:
    print(n02,"es menor porqu\u00eA tiene",e02)
  elif e02<e03:
    print(n02,"es menor porqu\u00eA tiene",e02) 
estCondicional01()