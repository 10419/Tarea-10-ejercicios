def estCondicional01():
  print("Bienvenido a tranportes Power")
  presupuesto = float (input ('Ingresa el presupuesto que tiene: '))
  km =0
  km=presupuesto
  if km>=1500 and km<=1599:
    print ("Te recomiendo viejar a M\u00E9xico con el presupuesto de",presupuesto,"te alcanza y te sobra")
  elif km>=1600 and km<=2399:
    print ("Te recomiendo viejar a Acapulco",presupuesto,"te alcanza y te sobra")
  elif km>=2400 and km<=3599:
    print ("Te recomiendo viejar a Puerto Vallarta",presupuesto,"te alcanza y te sobra")
  elif presupuesto<1500:
    print ("Te recomiendo quedarte en casa")
  elif km >=3600: 
    print ("Te recomiendo viejar a Canc\u00FAn",presupuesto,"te alcanza y te sobra")
estCondicional01()