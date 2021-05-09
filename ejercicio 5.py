def estCondicional101():
  print("Bienvenido al sistema de recomendaciones por dia de san valentin")
  c=float(input("Ingrese su cantidad de dinero:"))
  if c>=1 and c<=10:
    print("puedes comprarle tarjetas")
  elif c>=11 and c<101:
    print("puedes comprarle chocolates")
  elif c>=101 and c<251:
    print("puedes comprarle flores")
  else:
    print("puedes comprarle un anillo")
  print("pasalo bien campeon(a)")
estCondicional101()