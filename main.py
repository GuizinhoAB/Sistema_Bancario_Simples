# Módulo para manipular as datas
from datetime import date, datetime

# Módulo utilizado na função Investir (Operação Livre)
import random

# Módulo utilizado para validar o nome na função novo_cliente
import re

# Autor: Guilherme de Abreu Guimarães
# RA: 22.222.028-7

# Arquivos para armazenar dados de clientes e operações
cliente_txt = "clientes.txt"
operacoes_txt = "operacoes.txt"

# Obtém a data atual formatada dd/mm/aaaa
today = date.today()
data = today.strftime("%d/%m/%Y")


# Função para criar um novo cliente
def novo_cliente(cliente_txt):
    # Inicia um loop infinito para validação do nome
    while True:
        # Pede o nome do cliente
        nome = input("Digite o nome do cliente: ")
    
        # Verifica se o nome é vazio ou contém qualquer caractere que não seja uma letra ou espaço
        if nome == "" or not re.match("^[A-Za-z ]*$", nome):
            # Se o nome for inválido, imprime uma mensagem de erro
            print("Nome inválido! Por favor, insira um nome que contenha apenas letras e espaços.")
        else:
            # Se o nome for válido, sai do loop
            break

    # Inicia um loop infinito para a validação do CPF.
    while True:
        # Solicita que o usuário insira o CPF do cliente.
        cpf = input("Digite o CPF do cliente (Ex: 38534309833): ")
        
        # Verifica se o CPF inserido tem 11 dígitos e se todos os caracteres são numéricos.
        if len(cpf) == 11 and cpf.isdigit():
            # Inicia a flag 'cpf_em_uso' como False. Ela será usada para verificar se o CPF já está em uso.
            cpf_em_uso = False
            
            # Abre o arquivo que contém os dados do cliente para leitura.
            with open(cliente_txt, 'r') as f:
                # Lê todas as linhas do arquivo e as armazena na variável 'linhas'.
                linhas = f.readlines()
            
            # Itera sobre cada linha do arquivo.
            for linha in linhas:
                # Separa os dados em cada linha por vírgula e remove os espaços em branco.
                dados = linha.strip().split(',')
                
                # Verifica se o CPF na linha corresponde ao CPF inserido pelo usuário.
                if dados[2].strip() == cpf:
                    # Se o CPF na linha corresponder ao CPF inserido, altera a flag 'cpf_em_uso' para True e interrompe o loop.
                    cpf_em_uso = True
                    break
            
            # Verifica se a flag 'cpf_em_uso' é True.
            if cpf_em_uso:
                # Se for, imprime uma mensagem.
                print("CPF já está em uso, digite novamente.")
            
            # Se a flag 'cpf_em_uso' for False, isso significa que o CPF passou em todas as verificações e o loop é interrompido.
            else:
                break
        
        # Se o CPF inserido não tiver 11 dígitos ou não for totalmente numérico, imprime uma mensagem.
        else:
            print("CPF inválido, digite novamente.")

    # Inicia um loop infinito para validar o tipo de conta
    while True:
        # Pede o tipo de conta (comum ou plus)
        tipo_conta = input("Digite o tipo de conta (comum ou plus): ")
    
        # Verifica se o tipo de conta é válido
        if tipo_conta.lower() not in ["comum", "plus"]:
            # Se o tipo de conta não for válido, imprime uma mensagem de erro
            print("Tipo de conta inválido! Por favor, insira 'comum' ou 'plus'.")
        else:
            # Se o tipo de conta for válido, sai do loop
            break

    # Inicia um loop infinito para validar se o valor contém apenas números
    while True:
        try:
            # Pede o valor inicial para depósito na conta
            valor_inicial = float(input("Digite o valor inicial da conta: "))
            # Se o valor for corretamente convertido para float, sai do loop
            break
        except ValueError:
            # Se ocorrer um erro ao tentar converter o valor para float, imprime uma mensagem de erro
            print("Valor inválido! Por favor, insira um número.")

    # Inicia um loop infinito para validar a senha
    while True:
        # Pede a senha do cliente
        senha = input("Digite a senha do cliente: ")
    
        # Verifica se a senha é vazia ou contém apenas espaços em branco
        if senha.strip() == "":
            # Se a senha for vazia, imprime uma mensagem de erro
            print("Senha inválida! Por favor, insira uma senha que não esteja vazia.")
        else:
            # Se a senha for válida, sai do loop
            break

    # Abre o arquivo de clientes para adicionar um novo cliente
    with open(cliente_txt, "a") as arquivo:
        # Adiciona as informações do novo cliente no arquivo
        arquivo.write(f"{data},{nome},{cpf},{tipo_conta},{valor_inicial:.3f},{senha}\n")
        # Fecha o arquivo
        arquivo.close()
      
    # Imprime uma mensagem de confirmação
    print("Cliente inserido no sistema!\n")




# Função para remover um cliente específico do arquivo
def apagar_cliente(cliente_txt):
    # Inicia o loop para solicitar o CPF até que o correto seja inserido
    while True:
        # Solicita ao usuário para inserir o CPF do cliente
        cpf = input("Digite o CPF do cliente (Ex: 38534309833): ")
    
        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena na variável 'linhas'
            linhas = f.readlines()
    
        # Inicializa a flag 'cpf_valido' como False
        cpf_valido = False
        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Se o CPF corresponder, o CPF é válido
            if dados[2].strip() == cpf:
                cpf_valido = True
                break
    
        # Se o CPF não foi válido, imprime a mensagem
        if not cpf_valido:
            print("CPF não encontrado!")
        else:
            break
    # Abre o arquivo txt que contém os dados dos clientes para leitura
    with open(cliente_txt, 'r') as f:
        # Lê todas as linhas do arquivo e armazena na variável 'linhas'
        linhas = f.readlines()

    # Inicializa uma lista vazia que armazenará as linhas do novo arquivo
    nova_linha = []
    # Variável flag que indica se o cliente foi encontrado
    encontrado = False

    # Itera sobre cada linha do arquivo
    for linha in linhas:
        # Se o cpf está na linha, marca a variável 'encontrado' como verdadeira
        if cpf in linha:
            encontrado = True
        # Se o cpf não está na linha, adiciona a linha à nova lista
        else:
            nova_linha.append(linha)

    # Se o cliente não foi encontrado, imprime uma mensagem e encerra a função
    if not encontrado:
        print(f"Cliente com CPF: {cpf} não encontrado!")
        return

    # Abre o arquivo txt e substitui seu conteúdo pela nova lista, efetivamente removendo o cliente
    with open(cliente_txt, 'w') as f:
        f.writelines(nova_linha)
        # Imprime uma mensagem confirmando que o cliente foi removido
        print(f'O cliente com o CPF: {cpf} foi removido!\n')  




# Função para listar todos os clientes no arquivo
def listar_clientes(cliente_txt):
    # Abre o arquivo txt que contém os dados dos clientes para leitura
    with open(cliente_txt, 'r') as f:
        # Lê todas as linhas do arquivo e armazena na variável 'linhas'
        linhas = f.readlines()

    # Itera sobre cada linha do arquivo
    for linha in linhas:
        # Separa os dados na linha por vírgula e remove os espaços em branco
        dados = linha.strip().split(',')
        # Imprime as informações do cliente de maneira formatada
        print(f"\nData: {dados[0]}  Nome: {dados[1]}  CPF: {dados[2]}  Tipo de conta: {dados[3]}  Saldo: {dados[4]}  Senha: {dados[5]}\n")




# Função para debitar um valor da conta de um cliente
def debitar(cliente_txt, operacoes_txt):
    # Inicia um loop infinito para solicitar o CPF até que o correto seja inserido
    while True:
        # Solicita ao usuário para inserir o CPF do cliente
        cpf = input("Digite o CPF do cliente (Ex: 38534309833): ")

        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena na variável 'linhas'
            linhas = f.readlines()

        # Inicializa a flag 'cpf_valido' como False
        cpf_valido = False
        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Se o CPF corresponder, o CPF é válido
            if dados[2].strip() == cpf:
                cpf_valido = True
                break

        # Se o CPF não foi válido, imprime a mensagem
        if not cpf_valido:
            print("CPF não encontrado!")
        # Se o CPF foi válido, sai do loop
        else:
            break

    # Inicia um loop infinito para solicitar a senha até que a correta seja inserida
    while True:
        # Solicita ao usuário para digitar a senha do cliente
        senha = input("Digite a senha do cliente: ")

        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena em uma lista
            linhas = f.readlines()

        # Inicializa a variável para verificar se a senha está correta
        senha_correta = False

        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Verifica se o CPF e a senha na linha atual correspondem aos dados inseridos pelo usuário
            if dados[2].strip() == cpf and dados[5].strip() == senha:
                # Se o CPF e a senha correspondem, define a variável de verificação da senha como True
                senha_correta = True
                break

        # Se a senha não foi correta, imprime a mensagem e continua o loop
        if not senha_correta:
            print("Senha incorreta!")
        # Se a senha foi correta, sai do loop
        else:
            break

    # Inicia um loop infinito para validar se o valor contém apenas números
    while True:
        try:
            # Pede o valor para debitar da conta
            valor_debito = float(input("Digite o valor a ser debitado da conta: "))
            # Se o valor for corretamente convertido para float, sai do loop
            break
        except ValueError:
            # Se ocorrer um erro ao tentar converter o valor para float, imprime uma mensagem de erro
            print("Valor inválido! Por favor, insira um número.")

    # Abre o arquivo do cliente para leitura
    with open(cliente_txt, 'r') as f:
        # Lê todas as linhas do arquivo e armazena na variável 'linhas'
        linhas = f.readlines()

    # Inicializa a lista 'novo_conteudo' que vai armazenar as novas linhas do arquivo
    novo_conteudo = []
    # Inicializa a variável 'cliente_encontrado' como False
    cliente_encontrado = False

    # Itera sobre cada linha do arquivo
    for linha in linhas:
        # Separa os dados na linha por vírgula e remove os espaços em branco
        dados = linha.strip().split(',')
        # Verifica se o CPF na linha atual corresponde ao CPF inserido pelo usuário
        if dados[2].strip() == cpf:
            # Se o CPF corresponder, define a variável 'cliente_encontrado' como True
            cliente_encontrado = True
            # Pega o saldo atual do cliente
            saldo_atual = float(dados[4])
            # Pega o tipo da conta do cliente
            tipo_conta = dados[3]

            # Define as taxas e o saldo negativo máximo permitido de acordo com o tipo de conta
            if tipo_conta == 'plus':
                taxa = 0.03
                saldo_negativo_max = -5000
            else:
                taxa = 0.05
                saldo_negativo_max = -1000
            
            # Inicia um loop infinito para validar se o valor a ser debitado não excederá o saldo permitido
            while True:
                # Calcula o valor total a ser debitado, incluindo a taxa
                valor_total = valor_debito * (1 + taxa)

                # Verifica se o saldo atual menos o valor total a ser debitado é menor que o saldo negativo máximo permitido
                if saldo_atual - valor_total < saldo_negativo_max:
                    # Se for, imprime uma mensagem de saldo insuficiente e pede novo valor
                    print("Saldo insuficiente. Insira um valor válido.")
                    valor_debito = float(input("Digite o valor a ser debitado da conta: "))
                else:
                    # Se não for, sai do loop
                    break

            # Subtrai o valor total do saldo atual
            novo_saldo = saldo_atual - valor_total
            # Atualiza o saldo na lista 'dados'
            dados[4] = str(novo_saldo)
            # Junta os dados em uma nova linha e a adiciona à lista 'novo_conteudo'
            nova_linha = ",".join(dados) + "\n"
            novo_conteudo.append(nova_linha)

            # Abre o arquivo de operações para adicionar a operação de débito
            with open(operacoes_txt, 'a') as op:
                # Grava a operação no arquivo de operações
                op.write(f"{data},{cpf},-{valor_debito},{taxa * valor_debito},{tipo_conta},{novo_saldo}\n")

        else:
            # Se o CPF na linha atual não corresponder ao CPF inserido pelo usuário, adiciona a linha atual à lista 'novo_conteudo'
            novo_conteudo.append(linha)

    # Se o cliente não foi encontrado, imprime uma mensagem e retorna a função
    if not cliente_encontrado:
        print("Cliente não encontrado!")
        return

    # Abre o arquivo do cliente para escrita
    with open(cliente_txt, 'w') as f:
        # Substitui as linhas do arquivo pelas linhas na lista 'novo_conteudo'
        f.writelines(novo_conteudo)

    # Imprime uma mensagem de sucesso e o novo saldo do cliente
    print(f'\nValor debitado com sucesso! \nO novo saldo do cliente com CPF {cpf} é {novo_saldo}\n')
  



# Função para depositar um valor no saldo do cliente
def depositar(cliente_txt, operacoes_txt):
    # Inicia o loop para solicitar o CPF até que o correto seja inserido
    while True:
        # Solicita ao usuário para inserir o CPF do cliente
        cpf = input("Digite o CPF do cliente (Ex: 38534309833): ")
    
        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena na variável 'linhas'
            linhas = f.readlines()
    
        # Inicializa a flag 'cpf_valido' como False
        cpf_valido = False
        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Se o CPF corresponder, o CPF é válido
            if dados[2].strip() == cpf:
                cpf_valido = True
                break
    
        # Se o CPF não foi válido, imprime a mensagem
        if not cpf_valido:
            print("CPF não encontrado!")
        else:
            break

    # Inicia um loop infinito para validar se o valor contém apenas números
    while True:
        try:
            # Pede o valor para depósito na conta
            valor_deposito = float(input("Digite o valor a ser depositado na conta: "))
            # Se o valor for corretamente convertido para float, sai do loop
            break
        except ValueError:
            # Se ocorrer um erro ao tentar converter o valor para float, imprime uma mensagem de erro
            print("Valor inválido! Por favor, insira um número.")

    # Abre o arquivo do cliente para leitura
    with open(cliente_txt, 'r') as f:
        linhas = f.readlines()

    # Inicializa uma lista vazia para armazenar as novas linhas do arquivo
    novo_conteudo = []

    # Flag para verificar se o cliente foi encontrado no arquivo
    cliente_encontrado = False

    # Itera sobre cada linha do arquivo
    for linha in linhas:

        # Separa os dados na linha por vírgula e remove os espaços em branco
        dados = linha.strip().split(',')

        # Verifica se o CPF na linha atual corresponde ao CPF inserido pelo usuário
        if dados[2].strip() == cpf:
            cliente_encontrado = True
            saldo_atual = float(dados[4])
            tipo_conta = dados[3]

            # Calcula o novo saldo adicionando o valor do depósito ao saldo atual
            novo_saldo = saldo_atual + valor_deposito

            # Atualiza o saldo na lista de dados
            dados[4] = str(novo_saldo)

            # Junta os dados em uma nova linha e adiciona ao novo conteúdo do arquivo
            nova_linha = ",".join(dados) + "\n"
            novo_conteudo.append(nova_linha)

            # Grava a operação no arquivo de operações
            with open(operacoes_txt, 'a') as op:
                op.write(f"{data},{cpf},+{valor_deposito},0,{tipo_conta},{novo_saldo}\n")

        else:
            # Se o CPF não corresponder, simplesmente adiciona a linha atual ao novo conteúdo
            novo_conteudo.append(linha)

    # Se o cliente não foi encontrado, imprime uma mensagem e encerra a função
    if not cliente_encontrado:
        print("Cliente não encontrado!")
        return

    # Abre o arquivo do cliente para escrita
    with open(cliente_txt, 'w') as f:
        f.writelines(novo_conteudo)

    # Imprime uma mensagem indicando que o valor foi depositado com sucesso e mostra o novo saldo
    print(f'Valor depositado com sucesso! \nO novo saldo do cliente com CPF {cpf} é {novo_saldo}\n')




# Função para transferência
def transferir(cliente_txt, operacoes_txt):
    # Inicia o loop para solicitar o CPF até que o correto seja inserido
    while True:
        # Solicita ao usuário para inserir o CPF do cliente
        cpf_origem = input("Digite o CPF do cliente de origem (Ex: 38534309833): ")
    
        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena na variável 'linhas'
            linhas = f.readlines()
    
        # Inicializa a flag 'cpf_valido' como False
        cpf_valido = False
        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Se o CPF corresponder, o CPF é válido
            if dados[2].strip() == cpf_origem:
                cpf_valido = True
                break
    
        # Se o CPF não foi válido, imprime a mensagem
        if not cpf_valido:
            print("CPF não encontrado!")
        else:
            break
    # Inicia o loop para solicitar a senha até que a correta seja inserida
    while True:
        # Solicita ao usuário para inserir a senha do cliente de origem
        senha = input("Digite a senha do cliente de origem: ")

        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena na variável 'linhas'
            linhas = f.readlines()

        # Inicializa a flag 'senha_correta' como False
        senha_correta = False
        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Se o CPF e a senha correspondem, a senha está correta
            if dados[2].strip() == cpf_origem and dados[5].strip() == senha:
                senha_correta = True
                break

        # Se a senha não foi correta, imprime a mensagem
        if not senha_correta:
            print("Senha incorreta!")
        else:
            break
    # Inicia o loop para solicitar o CPF até que o correto seja inserido
    while True:
        # Solicita ao usuário para inserir o CPF do cliente
        cpf_destino = input("Digite o CPF do cliente de destino (Ex: 38534309833): ")
    
        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena na variável 'linhas'
            linhas = f.readlines()
    
        # Inicializa a flag 'cpf_valido' como False
        cpf_valido = False
        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Se o CPF corresponder, o CPF é válido
            if dados[2].strip() == cpf_destino:
                cpf_valido = True
                break
    
        # Se o CPF não foi válido, imprime a mensagem
        if not cpf_valido:
            print("CPF não encontrado!")
        else:
            break
    # Inicia um loop infinito para validar se o valor contém apenas números
    while True:
      try:
          # Pede o valor para transferencia na conta
          valor_transferencia = float(input("Digite o valor a ser transferido: "))
          # Se o valor for corretamente convertido para float, sai do loop
          break
      except ValueError:
          # Se ocorrer um erro ao tentar converter o valor para float, imprime uma mensagem de erro
          print("Valor inválido! Por favor, insira um número.")
  
    # Abre o arquivo do cliente para leitura
    with open(cliente_txt, 'r') as f:
      # Lê todas as linhas do arquivo e armazena na variável 'linhas'
      linhas = f.readlines()
    
    # Cria uma lista vazia para armazenar o novo conteúdo do arquivo do cliente
    novo_conteudo = []
    
    # Cria duas flags para verificar se os clientes de origem e destino foram encontrados no arquivo
    cliente_origem_encontrado = False
    cliente_destino_encontrado = False
    
    # Itera sobre cada linha do arquivo
    for linha in linhas:
        # Separa os dados na linha por vírgula e remove os espaços em branco
        dados = linha.strip().split(',')
        
        # Se o CPF na linha corresponder ao CPF de origem...
        if dados[2].strip() == cpf_origem:
            # Define que o cliente de origem foi encontrado
            cliente_origem_encontrado = True
            # Converte o saldo atual para float
            saldo_atual = float(dados[4])
            # Armazena o tipo de conta do cliente de origem
            tipo_conta_origem = dados[3].strip()
            # Define a taxa de transferência e o saldo negativo máximo de acordo com o tipo de conta
            if tipo_conta_origem == 'comum':
              # Para comum
                taxa_transf = 0.05
                saldo_negativo_max = -1000
            else:
              # Para plus
                taxa_transf = 0.03
                saldo_negativo_max = -5000
    
            # Inicia um loop para validar se o valor a ser transferido não excederá o saldo permitido
            while True:
                # Calcula o valor total da transferência, incluindo a taxa
                valor_total_transf = valor_transferencia + valor_transferencia * taxa_transf
                # Verifica se o saldo atual menos o valor total da transferência é menor que o saldo negativo máximo permitido
                if saldo_atual - valor_total_transf < saldo_negativo_max:
                    print("Saldo insuficiente. Insira um valor válido.")
                    valor_transferencia = float(input("Digite o valor a ser transferido: "))
                else:
                    # Se não for, sai do loop
                    break
    
            # Calcula o novo saldo subtraindo o valor total da transferência do saldo atual
            novo_saldo = saldo_atual - valor_total_transf
            # Atualiza o saldo no array de dados
            dados[4] = str(novo_saldo)
            # Cria uma nova linha com os dados atualizados
            nova_linha = ",".join(dados) + "\n"
            # Adiciona a nova linha ao novo conteúdo
            novo_conteudo.append(nova_linha)
    
            # Adiciona registro de transferência para o cliente de origem no arquivo de operações
            data = datetime.now().strftime('%d/%m/%Y')
            with open(operacoes_txt, 'a') as op:
                op.write(f"{data},{cpf_origem},-{valor_transferencia},{valor_transferencia * taxa_transf},{tipo_conta_origem},{novo_saldo}\n")
        # Se o CPF na linha corresponder ao CPF de destino...
        elif dados[2].strip() == cpf_destino:
            # Define que o cliente de destino foi encontrado
            cliente_destino_encontrado = True
            # Converte o saldo atual para float
            saldo_atual = float(dados[4])
            # Armazena o tipo de conta do cliente de destino
            tipo_conta_destino = dados[3].strip()
            # Calcula o novo saldo do cliente de destino, somando o valor da transferência ao saldo atual
            novo_saldo_destino = saldo_atual + valor_transferencia
            # Atualiza o saldo no array de dados
            dados[4] = str(novo_saldo_destino)
            # Cria uma nova linha com os dados atualizados
            nova_linha = ",".join(dados) + "\n"
            # Adiciona a nova linha ao novo conteúdo
            novo_conteudo.append(nova_linha)
    
            # Adiciona registro de transferência para o cliente de destino no arquivo de operações
            data = datetime.now().strftime('%d/%m/%Y')
            with open(operacoes_txt, 'a') as op:
                op.write(f"{data},{cpf_destino},{valor_transferencia},0,{tipo_conta_destino},{novo_saldo_destino}\n")
        else:
            # Se a linha não corresponder nem ao cliente de origem nem ao cliente de destino, adiciona a linha ao novo conteúdo sem modificá-la
            novo_conteudo.append(linha)
    
    # Se um ou ambos os clientes não foram encontrados, imprime uma mensagem de erro
    if not cliente_origem_encontrado or not cliente_destino_encontrado:
      print("Um ou ambos os clientes não foram encontrados!")
    
    # Abre o arquivo do cliente para escrita
    with open(cliente_txt, 'w') as f:
        # Escreve o novo conteúdo no arquivo
        f.writelines(novo_conteudo)
    
    # Imprime uma mensagem de sucesso e o novo saldo do cliente de origem
    print(f'Transferência realizada com sucesso! \nO novo saldo do cliente com CPF {cpf_origem} é {novo_saldo}\n')




# Função para investimento
def investir(cliente_txt, operacoes_txt):
    # Inicia o loop para solicitar o CPF até que o correto seja inserido
    while True:
        # Solicita ao usuário para inserir o CPF do cliente
        cpf = input("Digite o CPF do cliente (Ex: 38534309833): ")
    
        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena na variável 'linhas'
            linhas = f.readlines()
    
        # Inicializa a flag 'cpf_valido' como False
        cpf_valido = False
        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Se o CPF corresponder, o CPF é válido
            if dados[2].strip() == cpf:
                cpf_valido = True
                break
    
        # Se o CPF não foi válido, imprime a mensagem
        if not cpf_valido:
            print("CPF não encontrado!")
        else:
            break

    # Inicia o loop para solicitar a senha até que a correta seja inserida
    while True:
        # Solicita ao usuário para inserir a senha do cliente de origem
        senha = input("Digite a senha do cliente: ")

        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena na variável 'linhas'
            linhas = f.readlines()

        # Inicializa a flag 'senha_correta' como False
        senha_correta = False
        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Se o CPF e a senha correspondem, a senha está correta
            if dados[2].strip() == cpf and dados[5].strip() == senha:
                senha_correta = True
                break

        # Se a senha não foi correta, imprime a mensagem
        if not senha_correta:
            print("Senha incorreta!")
        else:
            break
    # Inicia um loop infinito para validar se o valor contém apenas números
    while True:
        try:
            # Pede o valor para investir
            valor_investimento = float(input("Digite o valor a ser investido: "))
            # Se o valor for corretamente convertido para float, sai do loop
            break
        except ValueError:
            # Se ocorrer um erro ao tentar converter o valor para float, imprime uma mensagem de erro
            print("Valor inválido! Por favor, insira um número.")

    # Abre o arquivo de texto do cliente para leitura
    with open(cliente_txt, 'r') as f:
        # Lê todas as linhas do arquivo e armazena na variável 'linhas'
        linhas = f.readlines()
    
    # Cria uma lista vazia chamada 'novo_conteudo'
    novo_conteudo = []
    # Define a variável 'cliente_encontrado' como False
    cliente_encontrado = False
    # Itera sobre cada linha em 'linhas'
    for linha in linhas:
        # Divide a linha em elementos separados por vírgulas e remove espaços em branco
        dados = linha.strip().split(',')
        # Verifica se o CPF e a senha na linha correspondem aos dados fornecidos
        if dados[2].strip() == cpf and dados[5].strip() == senha:
            # Define que o cliente foi encontrado
            cliente_encontrado = True
            # Converte o saldo atual para float
            saldo_atual = float(dados[4])
            # Armazena o tipo de conta
            tipo_conta = dados[3].strip()
            # Define a taxa com base no tipo de conta
            taxa = 0.05 if tipo_conta == 'comum' else 0.03
            # Define o limite negativo com base no tipo de conta
            limite_negativo = -1000 if tipo_conta == 'comum' else -5000
            # Calcula o valor da taxa de investimento
            valor_taxa = valor_investimento * taxa
    
            # Inicia um loop infinito para validar se o valor a ser investido não excederá o saldo permitido
            while True:
                # Calcula o valor total do investimento
                valor_total_invest = valor_investimento + valor_investimento * taxa
                # Verifica se o saldo atual menos o valor total do investimento é menor que o limite negativo
                if saldo_atual - valor_total_invest < limite_negativo:
                    print("Saldo insuficiente. Insira um valor válido.")
                    valor_investimento = float(input("Digite o valor a ser investido: "))
                else:
                    # Se não for, sai do loop
                    break
    
            # Atualiza o saldo atual subtraindo o valor total do investimento
            novo_saldo = saldo_atual - valor_total_invest
            # Atualiza o saldo no array de dados
            dados[4] = str(novo_saldo)
            # Cria uma nova linha com os dados atualizados
            nova_linha = ",".join(dados) + "\n"
            # Adiciona a nova linha ao novo conteúdo
            novo_conteudo.append(nova_linha)
    
            # Adiciona registro de investimento para o cliente no arquivo de operações
            data = datetime.now().strftime('%d/%m/%Y')
            with open(operacoes_txt, 'a') as op:
                op.write(f"{data},{cpf},-{valor_investimento},{valor_taxa},{tipo_conta},{novo_saldo}\n")
        else:
            # Se a linha não corresponder ao cliente, adiciona a linha ao novo conteúdo sem modificá-la
            novo_conteudo.append(linha)
    
    # Se o cliente não foi encontrado, imprime uma mensagem de erro e retorna
    if not cliente_encontrado:
        print("Cliente não encontrado!")
        return
    
    # Abre o arquivo do cliente para escrita
    with open(cliente_txt, 'w') as f:
        # Escreve as linhas do 'novo_conteudo' no arquivo
        f.writelines(novo_conteudo)
    
    # Lendo novamente o arquivo do cliente para obter os valores atualizados
    with open(cliente_txt, 'r') as f:
        linhas = f.readlines()
        
    # Imprime uma mensagem informando que o investimento foi realizado com sucesso
    print(f'\nInvestimento realizado com sucesso! \nO novo saldo do cliente com CPF {cpf} é {novo_saldo}\n')
    
    # Pega a data atual formatada
    data_operacao = datetime.now().strftime("%d/%m/%Y")
    
    # Gera um número aleatório entre -20 e 20 para simular a mudança percentual no valor do investimento
    percentual_mudanca = random.randint(-20, 20)
    # Calcula o resultado do investimento com base na mudança percentual
    resultado_investimento = valor_investimento * (1 + percentual_mudanca / 100)
    
    # Se a mudança percentual for maior ou igual a zero, imprime uma mensagem de sucesso
    if percentual_mudanca >= 0:
        print(f'Parabéns!\nSeu investimento aumentou em {percentual_mudanca}% e agora vale R${resultado_investimento}\n')
    # Caso contrário, imprime uma mensagem informando que o investimento diminuiu
    else:
        print(f'Infelizmente,\nseu investimento diminuiu em {-percentual_mudanca}% e agora vale R${resultado_investimento}\n')
    
    # Inicia um novo loop para depositar o resultado do investimento de volta na conta do cliente
    novo_conteudo = []
    for linha in linhas:
        # Divide a linha em elementos separados por vírgulas e remove espaços em branco
        dados = linha.strip().split(',')
        # Verifica se o CPF e a senha na linha correspondem aos dados fornecidos
        if dados[2].strip() == cpf and dados[5].strip() == senha:
            # Converte o saldo atual para float
            saldo_atual = float(dados[4])
            # Atualiza o saldo adicionando o resultado do investimento
            novo_saldo = saldo_atual + resultado_investimento
            # Atualiza o saldo no array de dados
            dados[4] = str(novo_saldo)
            # Cria uma nova linha com os dados atualizados
            nova_linha = ",".join(dados) + "\n"
            # Adiciona a nova linha ao novo conteúdo
            novo_conteudo.append(nova_linha)
        else:
            # Se a linha não corresponder ao cliente, adiciona a linha ao novo conteúdo sem modificá-la
            novo_conteudo.append(linha)
    
    # Abre o arquivo do cliente para escrita
    with open(cliente_txt, 'w') as f:
        # Escreve as linhas do 'novo_conteudo' no arquivo
        f.writelines(novo_conteudo)
    
    # Imprime uma mensagem informando que o resultado do investimento foi depositado de volta na conta do cliente
    print(f'O resultado do investimento foi depositado de volta na sua conta. O novo saldo é R${novo_saldo}\n')

    # Prepara a linha de operação de retorno do investimento
    operacao_retorno = f"{data_operacao},{cpf},+{resultado_investimento},0,{tipo_conta},{novo_saldo}\n"
    # Abre o arquivo de operações para adicionar o retorno do investimento
    with open(operacoes_txt, 'a') as f:
        # Escreve a operação de retorno no arquivo de operações
        f.write(operacao_retorno)




def extrato(cliente_txt, operacoes_txt):
    # Inicia o loop para solicitar o CPF até que o correto seja inserido
    while True:
        # Solicita ao usuário para inserir o CPF do cliente
        cpf = input("Digite o CPF do cliente (Ex: 38534309833): ")
    
        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena na variável 'linhas'
            linhas = f.readlines()
    
        # Inicializa a flag 'cpf_valido' como False
        cpf_valido = False
        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Se o CPF corresponder, o CPF é válido
            if dados[2].strip() == cpf:
                cpf_valido = True
                break
    
        # Se o CPF não foi válido, imprime a mensagem
        if not cpf_valido:
            print("CPF não encontrado!")
        else:
            break

    # Inicia o loop para solicitar a senha até que a correta seja inserida
    while True:
        # Solicita ao usuário para inserir a senha do cliente de origem
        senha = input("Digite a senha do cliente: ")

        # Abre o arquivo do cliente para leitura
        with open(cliente_txt, 'r') as f:
            # Lê todas as linhas do arquivo e armazena na variável 'linhas'
            linhas = f.readlines()

        # Inicializa a flag 'senha_correta' como False
        senha_correta = False
        # Itera sobre cada linha do arquivo
        for linha in linhas:
            # Separa os dados na linha por vírgula e remove os espaços em branco
            dados = linha.strip().split(',')
            # Se o CPF e a senha correspondem, a senha está correta
            if dados[2].strip() == cpf and dados[5].strip() == senha:
                senha_correta = True
                break

        # Se a senha não foi correta, imprime a mensagem
        if not senha_correta:
            print("Senha incorreta!")
        else:
            break

    # Abre o arquivo do cliente para leitura
    with open(cliente_txt, 'r') as f:
        # Lê todas as linhas do arquivo e armazena na variável 'linhas'
        linhas = f.readlines()
    
    # Inicia a variável 'cliente_encontrado' como False para verificar se o cliente foi encontrado no arquivo
    cliente_encontrado = False
    
    # Itera sobre cada linha do arquivo
    for linha in linhas:
        # Remove espaços no início e no fim da linha e divide cada linha por ','
        dados = linha.strip().split(',')
        # Verifica se o CPF na linha corresponde ao CPF que estamos procurando
        if dados[2].strip() == cpf:
            # Se encontrou o cliente, define 'cliente_encontrado' como True
            cliente_encontrado = True
            # Armazena o nome e a conta do cliente
            nome = dados[1]
            conta = dados[4]
            # Sai do loop uma vez que o cliente foi encontrado
            break
    
    # Se o cliente não foi encontrado, imprime uma mensagem e termina a execução da função
    if not cliente_encontrado:
        print("Cliente não encontrado!")
        return
    
    # Imprime as informações do cliente
    print(f"\nNome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Conta: {conta}\n")
    
    # Abre o arquivo de operações para leitura
    with open(operacoes_txt, 'r') as f:
        # Lê todas as linhas do arquivo e armazena na variável 'linhas'
        linhas = f.readlines()
    
    # Inicia a variável 'extrato_encontrado' como False para verificar se foram encontradas operações para o cliente
    extrato_encontrado = False
    
    # Itera sobre cada linha do arquivo de operações
    for linha in linhas:
        # Remove espaços no início e no fim da linha e divide cada linha por ','
        dados = linha.strip().split(',')
        # Verifica se o CPF na linha corresponde ao CPF do cliente
        if dados[1] == cpf:
            # Se encontrou operações do cliente, define 'extrato_encontrado' como True
            extrato_encontrado = True
            # Armazena os detalhes da operação
            data = dados[0]
            operacao = dados[2]  # mantenha como string
            tarifa = float(dados[3])
            saldo = float(dados[5])
            # Se a operação começa com '-', é um débito
            if operacao.startswith('-'):  # verifica se é um débito
                print(f"Data: {data}\t\t{operacao}\t\tTarifa: {tarifa}\t\tSaldo: {saldo}\n")
            else:  # caso contrário, é um crédito
                print(f"Data: {data}\t\t{operacao}\t\tTarifa: {tarifa}\t\tSaldo: {saldo}\n")
    
    # Se nenhuma operação foi encontrada para o cliente, imprime uma mensagem
    if not extrato_encontrado:
        print("Nenhuma operação encontrada para este CPF!")




#Funcao sair
def sair():
  # Apenas imprime "Operação Finalizada",
  # pois o loop é encerrado com o While na função principal "banco()"
  print("\nOperacao finalizada!\n")




#Menu de opcoes do banco
def menu():

  # Interface
  print("1 - Novo cliente")
  print("2 - Apagar cliente")
  print("3 - Listar clientes")
  print("4 - Debito")
  print("5 - Deposito")
  print("6 - Extrato")
  print("7 - Transferencia entre contas")
  print("8 - Investimento")
  print("9 - Sair")

  # Armazena a opção escolhida na variável "opcao"
  opcao = int(input("Digite a opcao: "))

  # Retorna a variável
  return opcao



# Função principal do programa
def banco():

  # Declara a variável "opcao" como 0
  opcao = 0

  # Loop para retornar o menu até o usuário digitar 9 para sair
  while opcao != 9:

    # Declara a variável opcao como "menu()", pois o menu retorna a opcao escolhida
    opcao = menu()

    # Com base na opçao escolhida pelo usuário, a determinada função será iniciada
    match opcao:
      case 1:
        # Novo cliente
        novo_cliente(cliente_txt)
  
      case 2:
        # Apagar cliente
        apagar_cliente(cliente_txt)
  
      case 3:
        # Listar cliente
        listar_clientes(cliente_txt)
  
      case 4:
        # Debito
        debitar(cliente_txt, operacoes_txt)
  
      case 5:
        # Depósito
        depositar(cliente_txt, operacoes_txt)
  
      case 6:
        # Extrato
        extrato(cliente_txt, operacoes_txt)
  
      case 7:
        # Transferência entre contas
        transferir(cliente_txt, operacoes_txt)
  
      case 8:
        # Investimento
        investir(cliente_txt, operacoes_txt)
  
      case 9:
        # Sair
        sair()

# Inicializa a função principal do programa
banco()