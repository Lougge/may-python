"""
num_int= 5
num_dec= 15.5
val_str="qualquer texto"
print("o valor é:", num_int) 
print("o valor é:%i" %num_int) #i é de inteiro
print("o valor é:" + str(num_int))
print("Contatenando decimal:", num_dec)
print("Contatenando decimal: %f" %num_dec)
print("Contatenando decimal: " + str(num_dec))
print("Contatenando decimal: %.2f" %num_dec) #%.qntd de casa decimais que quer / F é de float/flutuante
#3 aspas oculta mais linhas enquanto #oculta só uma
#Float pro tipo String
print("Contatenando strings", val_str)
print("Contatenando strings %s" %val_str) #S é de string
print("Contatenando strings " + val_str)"""
"""
login=input("Login:") #input é para o usuário digitar
print(login)
senha=input("Senha:")
print(senha)
print("O usuário informado foi: %s, e a senha digitada foi: %s" %(login, senha))"""
"""
print(10//6) # 2x// é arredondar o número
print(10+(50+90)) #6%4 - A % é para saber o resto
print(6%4)"""
"""
num1= float(input("Digite um número:")) #o float é pra converter
num2= float(input("Digite outro número:"))
print() #deixa um espaço
divisao= num1 / num2
resto=num1%num2
print(num1, "dividido por", num2, "é igual a:", divisao)
print("O resto da divisão entre", num1, "e", num2, "é igual a:", resto)
5*2 #dois asteriscos significa potência"""
"""
import math  #importa da biblioteca do python
#print(dir(math)) #dir pega a lista de strings
print(math.pi)
y=10
X=2
print(5 == y)
print(X != y)
"""
"""
a=20
if(a > 20): #Só vai aparecer a condição que se encaixa, no caso (ELIF a>=20)
    print("Entrada A: R$25, não entrou")
elif(a < 10):
    print("Entrada B: R$10 antes de 00hr, não entrou ")
elif(a >= 20 ):
    print("Entrada C: R$20, entrou")
print()
a=20
if(a > 20):#para aparecer 3x, tem que ter 3 IF inves de IF/ELIF/ELIF
    print("Entrada A: R$25, não entrou")
print("Não passou no A")
if(a < 10):
    print("Entrada B: R$10 antes de 00hr, não entrou ")
print("Não entrou no B")
if(a >= 20 ):
    print("Entrada C: R$20, entrou")
acao=int(input("Digite '1' para sim e digite '2' para não:"))
if(acao==1):
    print("Você disse que sim")
#if(acao != 1):
 #   print("Você disse que não")
else:
   if(acao == 2):
       print("Você disse que não")
   else:
        print("Não é nem um e nem outro")"""
"""
idade=int(input("Informe sua idade:"))
if(idade<=0):
    print("Sua idade não pode ser menor ou igual a zero!")
else:
    if(idade>150):
        print("A sua idade não pode ser maior que 150 anos!")
    else:
        if(idade>18):
            print("Você é maior de idade")
        else:
            if(idade<18):
                print("Você precisa ser maior de 18 anos")"""
"""
numero1= input("Digite um número:")
numero1=int(numero1)
numero2= input("Digite outro número:")
numero2=int(numero2)
if(numero1==numero2):#operador de igualdade
    print("O número %d é igual a %d." %(numero1,numero2))
if(numero1!=numero2): #operador de diferença
    print("O número %d é diferente a %d." %(numero1,numero2))
if(numero1<numero2):#operador de menor que
    print("O número %d é menor que %d." %(numero1,numero2))
if(numero1>numero2):#operador de maior que
    print("O número %d é maior que %d." %(numero1,numero2))
if(numero1<=numero2):#operador de menor ou igual a
    print("O número %d é menor ou igual a %d." %(numero1,numero2))
if(numero1>=numero2):#operador de maior ou igual a
    print("O número %d é maior ou igual a %d." %(numero1,numero2))
"""
print(type(2) is int)
num1=int(input("Digite um número:"))
if(num1>10):
    print("O valor é maior que 10!")
else:
    if(num1<5):
        print("O número é menor que 10, mas maior que 5!")
        if(num1==7):
            print("O número é igual a 7!")
    else:
        print("O valor é menor que 5.")