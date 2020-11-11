  
dado  =  int ( input ( "1 número para elevar ao quadrado e ao cubo:" ))
elevado  = [lambda  x : x ** 2 ,lambda  x : x ** 3 ]
for  x  in  elevado :
    print ( x ( dado ))