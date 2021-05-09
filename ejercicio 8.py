def estCondicional101():
  print("Transportes Power")
  t=0
  a=int(input("ingrese la cantidad de personas:"))
  print("tarifa de auto buz")
  print("si son mas de 100 personas la tarifa por personas es de 20")
  print("si son entre 100 y 50 personas la tarifa por personas es de 35")
  print("si son entre 49 y 20 personas la tarifa por personas es de 40")
  print("si son menos de 20 personas la tarifa por personas es de 70")
  if a>100:
    t=a*20
  elif a>50 and a<100:
    t=a*35
  elif a>20 and a<49:
    t=a*40
  elif a<20:
    t=a*70
  print("el costo del viaje le saldra",t,"soles")
estCondicional101()