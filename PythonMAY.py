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
"""print(type(2) is int)
num1=int(input("Digite um número:"))
if(num1>10):
    print("O valor é maior que 10!")
else:
    if(num1<5):
        print("O número é menor que 10, mas maior que 5!")
        if(num1==7):
            print("O número é igual a 7!")
    else:
        print("O valor é menor que 5.")"""
"""QUESTAO1
num1=int(input("Digite um número:"))
if(num1==0):
    print("O número é igual a 0!")
if(num1<0):
    print("O número %d é negativo" %num1)
if(num1>0):
    print("O número %d é positivo" %num1)

QUESTAO2
num1=int(input("Digite um número:"))
if(num1%2==0):
    print("O número %d é par!" %num1)
else:
    print("O número %d é impar!" %num1)
num1=int(input("digite um número:"))
num2=int(input("digite outro número:"))
if(num1>num2):
   print("%d é maior" %(num1))
else:
    print("%d é maior" %(num2))
#QUESTAO 4
num3=int(input("digite sua idade:"))
if(num3>=18):
  print("você é maior de idade hehe")
else:
  print("você é menor de idade tururu")
#QUESTAO 5
num4=int(input("digite o ano que você nasceu:"))
num5=int(input("digite o ano que sua mãe nasceu:"))
print("Dua mãe lhe teve com  %d anos," %(num4-num5) + "já você tem: %d anos" %(2022-num4))
#QUESTAO 6 
print("caractere a ser multiplicado - "*50)
#QUESTAO 7
num6=int(input("Digite um número:"))
if(num6%2==0):
    print("Este número é par!")
else:
    print("Este número é ímpar!")
#QUESTÃO 8
num7=int(input("Digite um número:"))
num8=int(input("Digite outro número:"))
if(num7>num8):
    print("O número %d é maior que %d" %(num7, num8))
else:
    print("O número %d é maior que %d" %(num8, num7))
if(num7==num8):
    print("Os números são iguais")
#QUESTAO 9
num=15.5
if type(num)==int:
    print("Este número é inteiro")
else:
    print("Este número NÃO é inteiro!")
#QUESTÃO 10
#res = isinstance(10, str)
#print(res)
val= input("Digite algo:")
if type(val)==str:
    print("É uma string")
else:
    print("Não é uma string, sorry")
#QUESTAO 11
num9=float(input("Digite um número:"))
if type(num9)==float:
    print("Este número é decimal")
else:
    print("Não é decimal")
#QUESTAO 12:
num10=float(input("Digite um número:"))
if (num10%1==0):
    print("Este número é inteiro")
else:
    print("É decimal")
#QUESTAO 13:  Faça um algoritmo que leia três números e imprima na tela o maior deles.
num11=float(input("Digite um número:"))
num12=float(input("Digite outro número:"))
num13=float(input("Digite mais um número:"))
if(num11>num12):
    maior=num11
elif(num12>num13):
    maior=num12
if(num13>num11):
    maior=num13
print("O maior número é:", maior)"""
"""#ATALHOS MATEMATICOS:
#x=(x+y) Assim ele vira com += :
x=10
x+=2
print(x)
#Tal como: -=   *=   /=  %=
#ATRIBUIÇÃO MÚLTIPLA:
a=10
b=5
a, b = b, a  #isso faz com que os valores se inverta
#ATRIBUIÇÃO CONDICIONAL:
#<variavel>=<valor1> if (true) else <valor2>
x=10
texto= "sim" if x == 10 else "não"
print(texto)"""
"""#ITERADORES: Loop (repetir qnd tal condição for atendida)/ controle de fluxo/ WHILE(enqto)
x=0
while(x<=5):
    print(x)
    x+=1
else:
    print("agora é 6")
#USANDO O FOR PARA LOOP (EXECUTAR N INSTR. EM INTV. PRÉ DEFINIDO)
#for (var) in (list):
for c in "mayara": #a lista é o ciclo -> execução de um elemento
    print(c)
#RANGE (gerar uma lista que tenha uma série de numeros em um intevalo determinado)
#range ([start], stop[,step])
]x[ intervalo aberto 
x[,]y 
0,  4
0 [1,2,3] 4
for variavel in range(0,10,2):
    print(variavel)
thislist = [0, 10, 2]
print(thislist)
print(list(range(0,10,2)))
print(list(range(10)))
print(list(range(100,0,-10)))
print(list(range(-100,0,10)))
for i in range(10):
    print(i)
for y in range(-10,0,2):
    print(y)
#BREAK= interrompe a instrução
i=10
while(i<100):
    i=i+1
    if(True):
        break"""
print("antes do loop")
for item in range(10):
    print(item)
    if(item==6): #quando chegou no 6 ele para
        break
print("depois do loop")