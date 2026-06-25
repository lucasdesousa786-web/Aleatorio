def cadastrar_produtos():
    produtos = []
    try:
        qtd = int(input("Quantos produtos? "))
        if qtd <= 0:
            print("Quantidade deve ser maior que zero!")
            return cadastrar_produtos()
        for i in range(qtd):
            print(f"\n--- Produto {i+1} ---")
            nome = input("Nome: ").strip()
            if not nome:
                print("Nome não pode ser vazio!")
                continue
            try:
                qtd_ini = int(input("Quantidade inicial: "))
                if qtd_ini < 0:
                    print("Quantidade não pode ser negativa!")
                    continue
                preco = float(input("Preço unitário: R$ "))
                if preco < 0:
                    print("Preço não pode ser negativo!")
                    continue
                produtos.append({'nome': nome, 'quantidade': qtd_ini, 'preco': preco})
            except ValueError:
                print("Valor inválido!")
                continue
    except ValueError:
        print("Valor inválido!")
        return cadastrar_produtos()
    return produtos

def adicionar_estoque(produtos):
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    nome = input("Nome do produto: ").strip()
    for p in produtos:
        if p['nome'].lower() == nome.lower():
            try:
                qtd = int(input(f"Quantas unidades adicionar? "))
                if qtd <= 0:
                    print("Quantidade deve ser maior que zero!")
                    return
                p['quantidade'] += qtd
                print(f"✓ {qtd} unidades adicionadas. Novo estoque: {p['quantidade']}")
                return
            except ValueError:
                print("Valor inválido!")
                return
    print(f"Produto '{nome}' não encontrado!")

def retirar_estoque(produtos):
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    nome = input("Nome do produto: ").strip()
    for p in produtos:
        if p['nome'].lower() == nome.lower():
            try:
                qtd = int(input(f"Quantas unidades retirar? "))
                if qtd <= 0:
                    print("Quantidade deve ser maior que zero!")
                    return
                if qtd <= p['quantidade']:
                    p['quantidade'] -= qtd
                    print(f"✓ {qtd} unidades retiradas. Estoque restante: {p['quantidade']}")
                else:
                    print(f"✗ Estoque insuficiente! Disponível: {p['quantidade']}")
                return
            except ValueError:
                print("Valor inválido!")
                return
    print(f"Produto '{nome}' não encontrado!")

def consultar_produto(produtos):
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    nome = input("Nome do produto: ").strip()
    for p in produtos:
        if p['nome'].lower() == nome.lower():
            valor_total = p['quantidade'] * p['preco']
            print(f"\n--- {p['nome']} ---")
            print(f"Quantidade: {p['quantidade']} unidades")
            print(f"Preço unitário: R$ {p['preco']:.2f}")
            print(f"Valor total: R$ {valor_total:.2f}")
            return
    print(f"Produto '{nome}' não encontrado!")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    print("\n" + "="*60)
    print(f"{'PRODUTO':<20} {'QTD':<8} {'PREÇO':<10} {'TOTAL':<10}")
    print("-"*60)
    total_geral = 0
    for p in produtos:
        total = p['quantidade'] * p['preco']
        total_geral += total
        print(f"{p['nome']:<20} {p['quantidade']:<8} R$ {p['preco']:<9.2f} R$ {total:<9.2f}")
    print("-"*60)
    print(f"{'TOTAL GERAL':<40} R$ {total_geral:<9.2f}")
    print("="*60)

def main():
    print("="*40)
    print("     CONTROLE DE ESTOQUE")
    print("="*40)
    produtos = cadastrar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado. Encerrando...")
        return
    print(f"\n✓ {len(produtos)} produtos cadastrados!")
    while True:
        print("\n1. Adicionar\n2. Retirar\n3. Consultar\n4. Listar\n5. Sair")
        try:
            opcao = int(input("Opção: "))
            if opcao == 1:
                adicionar_estoque(produtos)
            elif opcao == 2:
                retirar_estoque(produtos)
            elif opcao == 3:
                consultar_produto(produtos)
            elif opcao == 4:
                listar_produtos(produtos)
            elif opcao == 5:
                print("\nEncerrando... Obrigado!")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número!")

if __name__ == "__main__":
    main()
