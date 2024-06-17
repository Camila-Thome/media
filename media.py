#media.py
'''
tera uma lista de alunos, com notas de b1 e b2,
um menu para selecionar a opção
1- adicionar aluno
2- listar aluno
3- remover aluno
4- procurar aluno
5- aprovados
6- reprovados
7- procurar nome
8- media da turma na B1
9- media da turma na B2
10- media geral da turma
11- diario da turma
0- sair
OBS:
Item 11 do menu: 11 Diario da turma
Deve imprimir na tela neste padrão exatamente, com os alinhamentos igual ao exemplo abaixo:
56 colunas
RA: 5 CARACTERES
Nome: 27 CARACTERES
B1, B2, Média: 5 CARACTERES CADA
DICA: var.ljust(QTD, CHAR) | var.rjust (QTD, CHAR)
'''
alunos = {}

def menu():
    print("1 - adicionar aluno")
    print("2 - listar aluno")
    print("3 - remover aluno")
    print("4 - procurar aluno")
    print("5 - aprovados")
    print("6 - reprovados")
    print("7 - procurar nome")
    print("8 - media da turma B1")
    print("9 - media da turma B2")
    print("10 - Média da turma GERAL")
    print('11 - diario')
    print("0 - sair")
    try:
        opt = int(input('digite uma opção: '))
        return opt
    #except KeyboardInterrupt:
    #   print('deu pau no teclado!!')
    #except ValueError:
    #   print('numero digitado errado!!')
    except Exception as e:
        print(f'Opção inválida: {e}')
    return 9
    #finally:
    #print('mostra isso!')

def add_aluno():
    try:
        ra = input('digite o RA do aluno: ')
        nome = input('digite o nome do aluno: ')
        nota_b1 = float(input('digite a nota B1 do aluno: '))
        nota_b2 = float(input('digite a nota B2 do aluno: '))
        dados = {"nome": nome, "b1": nota_b1, "b2": nota_b2}
        alunos [ra]= dados
    except Exception as e:
       print('alguma coisa foi digitado errado!! {e}')

def listar_alunos():
    for ra, dados in alunos.items():
        print(f'RA: {ra} - Aluno: {dados['nome']} - B1: {dados['b1']} - B2:{dados['b2']} ')
    input('pressione qualquer tecla para continuar')

def remover_alunos():
   ra = input('digite o RA do Aluno: ')
   if ra in alunos:
      aluno = alunos.pop(ra)
      print(f'O aluno:{aluno['nome']} foi removido')
   else:
      print('aluno não encontrado')
      input('pressione qualquer tecla para continuar')

def procurar_aluno():
   ra = input('digite o RA do aluno: ')
   if ra in alunos:
      dados = alunos[ra]
      print(f'RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2:{dados['b2']}')
   else:
      print('aluno não encontrado')
      input('pressione qualquer tecla para continuar')

def aprovados():
    for ra, dados in alunos.items():
        if ((dados['b1'] + dados['b2'])/ 2) >= 7.0:
            aluno = f'RA: {ra} - '
            aluno += f'Nome: {dados['nome']} -'
            aluno += f'B1: {dados['b1']} - '
            aluno += f'B2: {dados['b2']}'
            print(aluno)
    input('pressione qualquer tecla para continuar')

def reprovados():
   for ra, dados in alunos.items():
       if ((dados['b1'] + dados['b2'])/ 2) <= 6.9:
        aluno = f'RA: {ra} - '
        aluno += f'Nome: {dados['nome']}'
        aluno += f'B1: {dados['b1']}'
        aluno += f'B2: {dados['b2']}'
        print(aluno)
   input('pressione qualquer tecla para continuar')

def procurar_nome():
  nome = input('digite o nome do aluno')
  nome = nome.upper
  for ra, dados in alunos.items():
     if (dados['nome'].upper() == nome):
      aluno = f'RA: {ra} - '
      aluno += f'Nome: {dados['nome']}'
      aluno += f'B1: {dados['b1']}'
      aluno += f'B2: {dados['b2']}'
      print(aluno)
      break
     input('pressione qualquer tecla para continuar')

def media_b1():
   total_notas = 0
   total_alunos = 0
   for dados in alunos.values():
      total_notas += dados['b1']
      total_alunos += 1
   media_b1 = total_notas / total_alunos
   print(f'Média da turma na B1: {media_b1:.2f}')
   input('Pressione qualquer tecla para continuar')

def media_b2():
   total_notas = 0
   total_alunos = 0
   for dados in alunos.values():
      total_notas += dados['b2']
      total_alunos += 1
   media_b1 = total_notas / total_alunos
   print(f'Média da turma na B2: {media_b2:.2f}')
   input('Pressione qualquer tecla para continuar')

def media_GERAL():
   total_notas = 0
   total_alunos = 0
   for dados in alunos.values():
      total_notas += (dados['b1'] + dados['b2']) / 2
      total_alunos += 1
   media_geral = total_notas / total_alunos
   print(f'Média geral da turma: {media_geral:.2f}')
   input('Pressione qualquer tecla para continuar')

def calcular_media():
   soma_medias = 0
   for ra, dados in alunos.items():
        media = calcular_media(dados['b1'], dados['b2'])
        soma_medias += media
        print(f"{ra.ljust(15)}{dados['nome'].ljust(25)}{str(dados['b1']).ljust(12)}{str(dados['b2']).ljust(12)}{media:.2f}")

def diario():
    c1 =("-") 
    print(c1.ljust(56, "-"))
    print("                  Diário da turma")
    print(c1.ljust(56, "-"))
    print("RA    Nome                      Nota B1  Nota B2  Média")
    print(c1.ljust(56, "-"))
    
    soma_b1 = soma_b2 = soma_geral = 0
    contador = 0
    
    for ra, dados in alunos.items():
        media = (dados['b1'] + dados['b2']) / 2
        soma_b1 += dados['b1']
        soma_b2 += dados['b2']
        soma_geral += media
        contador += 1
        print(f"{ra.rjust(5, '0')} {dados['nome'].ljust(27)} {dados['b1']:5.2f}  {dados['b2']:7.2f}   {media:4.2f}")
    
    if contador > 0:
        media_b1 = soma_b1 / contador
        media_b2 = soma_b2 / contador
        media_geral = soma_geral / contador
    else:
        media_b1 = media_b2 = media_geral = 0
    
    print(c1.ljust(56, "-"))
    print(f"{'Médias da Turma'.rjust(33)}  {media_b1:4.2f}  {media_b2:7.2f}   {media:4.2f}")
    print(c1.ljust(56, "-"))
    input("fecha os olhos e clica em qualquer lugar, para continuar ") 

if __name__ == "__main__":
   while True:
    match menu():
       case 1:
          add_aluno()
       case 2:
          listar_alunos()
       case 3:
          remover_alunos()
       case 4:
          procurar_aluno()
       case 5:
           aprovados()
       case 6:
          reprovados ()
       case 7:
          procurar_nome()
       case 8:
          media_b1()
       case 9:
          media_b2()
       case 10:
          media_GERAL()
       case 11:
          diario()
       case 0:
          break