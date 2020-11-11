numero1  =  int ( input ( " 1° número:" ))
numero2  =  int ( input ( " 2° número:" ))
numero3  =  int ( input ( " 3° número:" ))
numero4  =  int ( input ( " 4° número:" ))
numero5  =  int ( input ( " 5° número:" ))
listaNumeros  = [ numero1 , numero2 , numero3 , numero4 , numero5 ]
recebe  = [ x  for  x  in  listaNumeros  if  x  >=  10 ]
print ( "Os números maiores que 10 são:" , recebe) 