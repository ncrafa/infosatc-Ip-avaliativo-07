def  letra ( mediaAluno ): 
    if  media <= 5.0  and  media >= 0 :
        letras = "D"
    elif  media <= 7.0  and  media > 5.0 :
        letras = "C"
    elif  media < 9.0  and  media > 7.0 :
        letras = "B"
    elif  media >= 9  and  media <= 10 :
        letras = "A"
    return  letras 

notas = lambda nota1,nota2: nota1*0.4 + nota2*0.6
for i in range (0,10):
    nota1 = float(input(" 1° nota?"))
    nota2 = float(input(" 2° nota?"))
    media = notas(nota1,nota2)
    conceito = letra(media)
    print("Média :",media)
    print("Conceito:",conceito)
