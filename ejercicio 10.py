def estCondicional01():
  print("beca estudiaPeru")
  e=int(input("ingrese su edad:"))
  n=float(input("ingrese su nota promedio:"))
  if e>18 and n>=9:
    print("la beca sera de 2000.00 dolares")
  elif e>18 and n>=7.5:
    print("la beca sera de 1000.00 dolares")
  elif e>18 and n>=6 and n<7.5:
    print("la beca sera de 500.00 dolares")
  elif e<18 and n>=9:
    print("la beca sera de 3000.00 dolares")
  elif e<18 and n>=8 and n<9:
    print("la beca sera de 2000.00 dolares")
  elif e<18 and n>=6 and n<8:
    print("la beca sera de 100.00 dolares")
  else:
    print("sigue estudiando campeon")
estCondicional01()