def menu():
  balance = 0
  limit = 500
  extract = ""
  withdraw_number = 0
  WITHDRAW_LIMIT = 3
  withdraw_sum = 0
  AGENCY = '0001'
  users = [] 
  accounts = []
  account_number = 0
    
  while True:
        
    option = input(f'''
===============MENU================
Por favor, selecione uma das opções:
[1] Depósito
[2] Saque
[3] Extrato
[4] Criar usuario
[5] Criar conta
[6] Sair

==> ''')
    if option == '1':
      deposit_value = float(input('\nPor favor, informe o valor que deseja depositar: '))
      extract, balance = deposit(deposit_value, balance, extract)

    elif option == '2':
      withdraw_value = float(input('\nPor favor, informe o valor que deseja sacar: '))
      balance, extract, withdraw_number, withdraw_sum = withdraw(
        withdraw_value= withdraw_value, 
        balance=balance, 
        withdraw_number=withdraw_number, 
        withdraw_sum=withdraw_sum, 
        withdraw_limit=WITHDRAW_LIMIT, 
        extract=extract, 
        limit=limit)

    elif option == '3':
      extract = see_extract(balance, extract=extract)

    elif option == '4':
      create_user(users)

    elif option == '5':
      account = create_account(AGENCY, account_number, users)

      if account:
        accounts.append(account)
        account_number += 1
    elif option == '6':
      break

    else:
        print('Operación inválida, por favor selecione novamente a opção desejada')

    

def deposit(deposit_value, balance, extract, /):
  if deposit_value <= 0:
    print('\nXXXXXx Operação falou! O valor informado é inválido XXXXXx')
  else:
    print(f'\n***** Operação realizada com sucesso. *****\n')
    balance += deposit_value
    extract += f'Deposito: R$ {deposit_value:.2f}\n'
   
  return extract, balance

def withdraw(*, withdraw_value, balance, withdraw_number, withdraw_sum, withdraw_limit, extract, limit): 
  if withdraw_number == withdraw_limit:
    print('\nXXXXX Operação falhou! Número máximo de saques diário atingido. XXXXX')
  elif withdraw_sum == limit:
    print('\nXXXXX Operação falhou! Máximo valor de saque diário atingido. XXXXX')
  elif balance < withdraw_value:
    print('\nXXXXX Operação falhou! Você não tem saldo suficiente. XXXXX')
  elif (withdraw_value + withdraw_sum)> limit:
    print('\nXXXXX Operação falhou! O valor inserido ultrapassa o límite de saque diário. XXXXX')
  elif(balance > withdraw_value):
    balance -= withdraw_value
    withdraw_number += 1
    withdraw_sum += withdraw_value
    extract += f'Saque: R$ {withdraw_value}\n'
    print(f'\n*****Saque realizado com sucesso*****\n')
  else:
    print('\nOperação falhou! Valor inserido inválido.')
 
  return balance, extract, withdraw_number, withdraw_sum

def see_extract(balance,/ ,*, extract):
  print('\n********EXTRATO********\n')
  print('\nNão foram realizadas movimentações.' if not extract else extract)
  print(f'\nSaldo R$ {balance:.2f}\n')
  print('**********************\n')

  return extract

def create_user(users):
  cpf =input('Informe o CPF (somente números): ')
  user = filter_users(cpf, users)
  
  if user:
    print('\nxxxxx Já existe usuário com esse CPF! XXXXX')
    return

  name = input('Informe o nome completo: ')
  date = input('Informe a data de nascimento (dd-mm-aaaa): ')
  endereco =input('Informe o enereço (ligrauro, nro - bairro - ciudade/UF): ')
  users.append({'name':name, 'date':date, 'cpf':cpf, 'endereco':endereco})

  print('\n*****Usuario criado com sucesso*****')

def filter_users(cpf, users):
  users_filter = [user for user in users if user['cpf'] == cpf ]
  return users_filter[0] if users_filter else None

def create_account(agency, account_number, users):
  cpf = input("Informe o número de CPF: ")
  user= filter_users(cpf, users)

  if user: 
    print('*****Cuenta creada com sucesso*****')
    return ({'agency':agency, "account_number":account_number, 'user':user})
  print('XXXXXX Usuario não encintrado, fluxo de criacção de conta encerrado XXXXXX ')

menu()
