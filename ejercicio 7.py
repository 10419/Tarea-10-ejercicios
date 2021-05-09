def estCondicional101():
  print("Bienvendio querido empleado(a)")
  pm=2000
  ps=0
  print("te daremos un pequeño regalo por tu antiguedad")
  A=int(input("ingrese los años que viene trabajand con nosotros:"))
  A==0
  if A>=1 and A<2:
    ps=pm+100
  elif A>=2 and A<3:
    ps=pm+200
  elif A>=3 and A<4:
    ps=pm+300
  elif A>=4 and A<5:
    ps=pm+400
  elif A>=5 and A<6:
    ps=pm+500
  else:
    ps=pm+1000
  print("Su pago por este mes sera",ps,"gracias por trabajar con nosotros.")
estCondicional101()