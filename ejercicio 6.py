def estCondicional101():
  print("Bienvnido tienda el garoto")
  d=0 
  p=int(input("ingrese el precio del articulos:"))
  if p>0 and p<100:
    d=p*0.10
  elif p>100 and p<200:
    d=p*0.12
  else:
    d=p*0.15
  print("El precio del articulo es",d)
estCondicional101()