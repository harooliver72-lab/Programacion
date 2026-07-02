def Pollo_gus(nombre, opcion_menu):
 factura = 0
 detalle = ""

 print("***** Bienvenido a Asadero GUstambo, ganas de un gusto?", nombre, "? te lo mereces *****\n")

 if opcion_menu == "1":
  print("**** Menu pollo asado GUStambo ****")
  print("1. ***** 1 pollo entero con papas y cola ***** ($12)")
  print("2. ***** medio pollo con papas y cola ***** ($6)")
  print("3. ***** plato con presa personal ***** ($3)")
  print("4. ***** 1 pollo entero con papas 2 consome y cola de 1LT ****** ($14)")
  pollog = input("Ingresa tu orden: ")

  if pollog == "1":
   factura = 12
   detalle = "pollo entero papas y cola"
  elif pollog == "2":
   factura = 6
   detalle = "medio pollo"
  elif pollog == "3":
   factura = 3
   detalle = "plato personal"
  elif pollog == "4":
   factura = 14
   detalle = "pollo entero, consome, papas y cola"

 elif opcion_menu == "2":
  print("**** Menu Alitas GUStambo ****")
  print("1. ***** 7 Alitas picantes ***** ($5)")
  print("2. ***** 20 Alitas con salsa de maracuya **** ($17)")
  print("3. ***** 15 Alitas con salsa especial de la casa ***** ($14)")
  print("4. ***** 45 Alitas locura extrema ******* ($32)")
  alitas = input("Ingresa tu orden: ")

  if alitas == "1":
   factura = 5
   detalle = "7 alitas picantes"
  elif alitas == "2":
   factura = 17
   detalle = "20 alitas salsa maracuya"
  elif alitas == "3":
   factura = 14
   detalle = "15 alitas salsa especial"
  elif alitas == "4":
   factura = 32
   detalle = "45 alitas locura extrema"

 if factura > 0:
  print("\n---------------------------------")
  print("Gracias por tu compra,", nombre, "!")
  print("Tu pedido:", detalle)
  print("Total a pagar: $", factura)
  print("---------------------------------")
 else:
  print("Opcion no valida.")

nombre_cliente = input("***** Ayudame con tu nombre *****\n")

print("Perfecto", nombre_cliente, "¿Que deseas ordenar?")
print("***** Te presento nuestro menu, escoge lo que mas te GUSte *****")
print("1. **** Pollo Asado ****")
print("2. **** Alitas ****")
print("3. **** Hamburguesas ***")
print("*---------------------------------*")
opcion_elegida = input("Escoge una opción (1, 2 o 3): ")

Pollo_gus(nombre_cliente, opcion_elegida)