def estCondicional01():
  print("Bienvenido al estacionamiento Luis")
  horasapagarporprestamoaestacional=0
  horas=int(input("ingrese la cantidad de horas:"))
  print("tarifas")
  print("por 2 horas usted pagara 5 soles por hora")
  print("por 3 a 4 horas usted pagara 4 soles por hora")
  print("por 5 a 9 horas usted pagara 3 soles por hora ")
  print("por mas de 10 horas usted pagara 2 soles por hora")
  if horas>=1 and horas<3:
    horasapagarporprestamoaestacional=horas*5.00
  elif horas>=3 and horas<5:
    horasapagarporprestamoaestacional=horas*4.00
  elif horas>=5 and horas<10:
    horasapagarporprestamoaestacional=horas*3.00
  else:
    horasapagarporprestamoaestacional=horas*2.00
  print("Usted debe:",horasapagarporprestamoaestacional,", gracias por confiar en nosotros")
estCondicional01()