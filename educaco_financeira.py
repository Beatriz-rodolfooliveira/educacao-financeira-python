# Educacao financeira 
from datetime import datetime
import locale

salario = 0
saldo = salario
calcular_despesas = {}
investimentos = 0 
porcentagem = 0

 
while True: 
    print(""" 
        [1] - Salario 
        [2] - adicionar Despesas 
        [3] - Investir 
        [4] - Editar informaçoes
        [5] - Relatorio 
        [6] - Sair 
   """ ) 
    opcao = input(": ") 
    if opcao == "6":
        sair = input("Tem certeza que deseja sair? [S/N]")
        if sair.strip().lower() == "s":
            print("Saindo do sistema... 👋")
            break
        else:
            continue

    elif opcao == "1": 
        print("Salario")
        salario +=  float(input("Digite seu salario desse mês: "))
        saldo += salario
        print(f"Salario Adicinado: {salario:,.2f}") 
        print(f"Saldo: R${saldo:,.2f}")
     
    elif opcao == "2": 
        print("Adicionando Despesas") 
        despesa = str(input("Despesa: ")) 
        valor_despesa = float(input("Valor: R$ "))   

        if valor_despesa >= saldo:
            print("⚠ Saldo insuficiente! Não é possível adicionar essa despesa.")
            
        else: 
            calcular_despesas.update({despesa: valor_despesa})
            saldo -= valor_despesa
            print(f"Despesa '{despesa.capitalize()}' adicionada: R$ {valor_despesa:,.2f}")
            print(f"Saldo restante: R$ {saldo:,.2f}")
            
    elif opcao == "3": 
        print("investir!") 
        valor_aplicacao = float(input("Digite valor que deseja investir: ")) 
        
        if valor_aplicacao > saldo:
            print("⚠ Saldo insuficiente!")
            
        else: 
            investimentos += valor_aplicacao
            saldo -= valor_aplicacao
            print(f"Valor investido: R$ {investimentos}")
            print(f"Saldo restante: R$ {saldo:,.2f}")

    elif opcao == "4":
        print("Editando informaçoes!")
        print("""
            Qual opção você deseja editar?
              [1] - Salario
              [2] - Despesa - Editar/Excluir
              [3] - investimento - Editar / Resgatar
              """)
        editar = input("Escolha: ")
        if editar == "1":
            editar_salario = float(input("Digite o novo salario: R$ "))
            diferenca = editar_salario - salario
            salario = editar_salario
            saldo += diferenca
            print(f"✅ Salário atualizado para R$ {salario:,.2f}")
        
        elif editar == "2":
                print("Despesas Atuais:")
                if calcular_despesas:
                    for nome, valor in calcular_despesas.items():
                        print(f"{nome.capitalize()}: R$ {valor:,.2f}")
                else:
                    print("Nenhuma despesa cadastrada.")
                    continue
                pergunta = input("Deseja excluir esta despesa? (sim)(nao)").strip().lower()
            
                if pergunta == "sim":
                    chave_valor_excluir = input("Qual despesa deseja excluir?")

                    if chave_valor_excluir in calcular_despesas:
                        valor_excluido = calcular_despesas.pop(chave_valor_excluir)
                        saldo += valor_excluido  
                        print(f"\n✅ Despesa '{chave_valor_excluir}' excluída com sucesso!")
                        print(f"💰 Valor devolvido ao saldo: R$ {valor_excluido:,.2f}")
                        print(f"Saldo atual: R$ {saldo:,.2f}")
                    else:
                        print("⚠️ Despesa não encontrada.")

                elif pergunta == "nao": 
                    nome = input("Qual despesa deseja editar? ")
                    
                    if nome in calcular_despesas:
                        novo_valor = float(input("Novo valor: R$ "))
                        saldo += calcular_despesas[nome] - novo_valor
                        calcular_despesas[nome] = novo_valor
                        print("✅ Despesa atualizada!")
                        
                    else: 
                        print("⚠ Despesa não encontrada.")
                        
        elif editar == "3":
            print("Investimento Atual:")
            print(investimentos)
            print("""
            Deseja Resgatar ou Editar seu investimento?      
                [1] - Resgatar 
                [2] - Editar
                """)
            restagar_editar = input(": ")
            
            if restagar_editar == "1":
                resgatar = float(input("Qual valor deseja resgatar?"))
                
                if resgatar > investimentos:
                    print("⚠ Valor de resgate maior que o investimento total.")
                    
                else:
                    investimentos -= resgatar
                    saldo += resgatar
                    print(f"✅ Valor resgatado: R$ {resgatar:,.2f}\nInvestimento Atualizado: R${investimentos:,.2f}")
                    
            elif restagar_editar == "2":
                editar_investimento = float(input("Digite o novo valor que deseja editar: "))
                dif_editar = editar_investimento - investimentos
                investimentos = editar_investimento
                saldo -= dif_editar
                print(f"Valor Atualizado: R${investimentos}")
            
    elif opcao == "5":
        if salario <= 0:
            print("⚠ Impossível gerar relatório: Salário ainda não foi adicionado (ou é zero).")
            continue 
            
        porcentagem_despesa = sum(calcular_despesas.values()) / salario
        lazer = saldo
        porcentagem_lazer = lazer / salario if salario > 0 else 0
        porcentagem_investimento = investimentos / salario

        # Gera automaticamente a data completa (dia da semana, dia, mês e ano) no momento em que o usuário interage com o sistema.
        locale.setlocale(locale.LC_TIME, 'pt_BR')
        agora = datetime.now().strftime("%A %d. %B %Y").title()
        
        print(
            f"📊 Resumo Financeiro\n"
            f"--------------------------\n"
            f"{agora}\n"
            f"💰 Salário: R$ {salario:.2f}\n"
            f"💸 Despesas: R$ {sum(calcular_despesas.values()):.2f}  ({porcentagem_despesa:.1%} do salário)\n"
            f"📈 Investimentos: R$ {investimentos:.2f} ({porcentagem_investimento:.1%} do salário)\n"
            f"🎉 Lazer: R$ {lazer:,.2f} ({porcentagem_lazer:.1%} do salário)"
        )

