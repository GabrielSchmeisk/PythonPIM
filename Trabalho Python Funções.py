# by Gabriel Schmeisk

from datetime import datetime # pip install datetime - Módulo para puxar o horário local do computador
import time

# Etapa 1 - Boas vindas e coleta de dados (nome e idade)
def coletar_dados(): # Função de Coleta de Dados
    while True: # Loop para caso o usuário não siga os parâmetros de login
        print("\n-----------------------\n")
        nome = input("Digite seu nome:").strip().capitalize() # .strip remove os espaços em branco e o .capitalize deixa apenas a primeira letra maiúscula
        if nome.isalpha(): # Método para que só seja possível inserir letras do alfabeto na váriavel "nome"
            try: # Inicia uma verificação de erros no bloco de código e se comunica com o except.
                
                idade = int(input(f"Seja bem-vindo {nome}! Por gentileza, digite sua idade. (Apenas números): "))
                if idade < 15 or idade > 120: # Verifica se a idade é menor que 15 e maior que 120, caso seja, retornará uma mensagem e reiniciará o loop
                    print("\nDigite uma idade válida (entre 15 e 120 anos).\n")
                    continue # reinicia o loop
                    
            except ValueError: # Caso a entrada não seja númerica, ele identificará o "ValueError", executará uma mensgaem e reiniciará o loop
                print("\n\nPor favor, digite apenas números inteiros para a idade.\n\n")
                continue
                
        else: # Se comunica com o if nome, caso o nome não seja isalpha, ele executará esse else.
            print("\n\nPor favor, digite apenas letras (sem números ou símbolos ou espaços).\n\n")
            continue
            

        hora = datetime.now() # Usa o módulo datatime para criar uma váriavel que puxa o horário local
        print("\n-----------------------\n")
        print(f"Seja bem-vindo {nome}, agradecemos por usar nossa aplicação!")
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print("Horário:", hora.strftime("%H:%M\n")) # .strftime("") é um método para podermos modificar a formatação do horário.
        print("-----------------------\n")

        consentimento_usuario(nome) # Chama a proxíma função para dar continuidade
        break # Encerra o loop


 # Etapa 2 - Consentimento do usuário para coletarmos dados, caso ele aceite a coleta, será enviado para a etapa 3
# do contrário, será enviado para a etapa 1.

def consentimento_usuario(nome):
    while True:
        print(f"Bom {nome}, para prosseguirmos é necessário que você aceite nossos TERMOS DE USO.\n")
        resposta = input("Você aceita fornecer seus dados para fins de pesquisa e desenvolvimento? (Sim/Não): ")
        print("-----------------------\n")

        if resposta.lower() in ("sim", "s", "ss", "yes"): #.lower deixa toda a informação que entrar em letras minúsculas
            explicacao_TI(nome) # Se o usuário aceitar os termos, vai para a próxima função (próxima etapa)
            break
            
        elif resposta.lower() in ("nao", "n", "no", "não", "nn"):
            print("Você não aceitou os termos. Retornando ao início...\n")
            coletar_dados() # Caso o usuário recuse os temros, ele retorna para a função de coleta de dados
            break

        else:
            print("Resposta inválida, tente novamente (Sim/Não)\n")
            print("-----------------------\n")
            continue 


# Etapa 3 - Texto explicativo sobre o que é TI, caso ele digite continue, será enviado para a próxima etapa
# do contrário, o programa irá desligar.

def explicacao_TI(nome):
    while True:
        print("\n-----------------------\n")
        print("O que é tecnologia da informação??\n")
        print("A Tecnologia da Informação (TI) é a área que lida com o uso de computadores, softwares, redes e outros dispositivos para armazenar, processar, proteger e transmitir informações.\n")
        continuar = input("Pressione ENTER para dar continuidade ou digite 'sair' para encerrar o programa.\n")
        print("-----------------------\n")

        if continuar.lower() == "":
            print("Perfeito, vamos prosseguir.")
            escolha_algoritmo(nome)
            break
            
        elif continuar.lower() == "sair":
            print("Que pena, até a próxima!\n")
            exit() # Encerra o programa

        else:
            print("\nResposta inválida, tente novamente (Continuar/Sair)")
            continue


# Etapa 4 - O usuário escolhe qual a forma de algorítimo ele prefere, após a escolha, poderá ir para próxima etapa.

def escolha_algoritmo(nome):
    while True:
        print("\n-----------------------\n")
        print(f"{nome}, qual a forma de representação de algoritmo você prefere?\n")
        print("1 - Pseudocódigo")
        print("2 - Fluxograma\n")
        escolha = input("Escolha uma das opções (1/2)\n")
        print("\n-----------------------\n")

        if escolha == "1":
                continuar = input("Ótimo, Pseudocódigo é uma forma de descrever algoritmos (passo a passo para resolver um problema) usando uma linguagem informal, parecida com português (ou inglês, dependendo do caso), mas com uma estrutura parecida com a de linguagens de programação.\n\nPressione ENTER para prosseguir ou digite 'voltar' para retornar as opções. \n")
                if continuar.lower() == "":
                     finalizacao(nome)
                     break
                
                elif continuar.lower() == "voltar":
                    escolha_algoritmo(nome)
                    break
                     
                else:    
                   print("-----------------------\n")
                   print("Você não escolheu uma opção válida, pressione ENTER para prosseguir ou digite 'voltar' para retornar as opções.\n")
                   print("-----------------------\n")
                   continue

        elif escolha == "2":
                continuar = input("Fluxograma é um tipo de diagrama visual que representa um processo ou algoritmo, mostrando cada passo como caixas conectadas por setas. É como um 'mapa' que ajuda a visualizar o que acontece, em qual ordem, e quais decisões podem ser tomadas. Ele mostra o fluxo de execução de um processo, por isso o nome: fluxo + diagrama = fluxograma.\n\nPressione ENTER para prosseguir ou digite 'voltar' para voltar as opções. \n")
                if continuar.lower() == "":
                     finalizacao(nome)
                     break
                
                elif continuar.lower() == "voltar":
                    escolha_algoritmo(nome)
                    break

                else:    
                   print("-----------------------\n")
                   print("Você não escolheu uma opção válida, pressione ENTER para prosseguir ou digite 'voltar' para retornar as opções.\n")
                   print("-----------------------\n")
                   continue

        else:
            print("Resposta inválida, tente novamente (1/2)")
            continue


# Etapa 5 - Finalização do código, onde o usuário pode escolher voltar para a etapa 4, ou encerrar o programa
def finalizacao(nome):
        print("-----------------------")
        finalizacao = input(f"\nObrigado por fazer parte do nosso programa teste {nome}, caso queira sair do sistema, digite 'sair', ou pressione ENTER para voltar a etapa anterior!\n")

        if finalizacao.lower() == "sair":
            print("\nReiniciando o programa...\n")
            print("-----------------------\n")
            time.sleep(3)
            coletar_dados()

        else:
            print("\nRetornando para a etapa 4...\n")
            print("-----------------------\n")
            time.sleep(3)
            escolha_algoritmo(nome)


coletar_dados() # Inicia a função
