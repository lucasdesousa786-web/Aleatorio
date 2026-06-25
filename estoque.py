def cadastrar_produtos():
    """Função para cadastrar os produtos iniciais"""
    produtos = []
    try:
        quantidade = int(input("Quantos produtos deseja cadastrar? "))
        if quantidade <= 0:
            print("Quantidade deve ser maior que zero!")
            return cadastrar_produtos()
        
        for i in range(quantidade):
            print(f"\n--- Produto {i+1} ---")
            nome = input("Nome do produto: ").strip()
            if not nome:
                print("Nome não pode ser vazio!")
                continue
                
            try:
                quantidade_inicial = int(input("Quantidade inicial em estoque: "))
                if quantidade_inicial < 0:
                    print("Quantidade não pode ser negativa!")
                    continue
                    
                preco = float(input("Preço unitário: R$ "))
                if preco < 0:
                    print("Preço não pode ser negativo!")
                    continue
                    
                produtos.append({
                    'nome': nome,
                    'quantidade': quantidade_inicial,
                    'preco': preco
                })
            except ValueError:
                print("Valor inválido! Digite números válidos.")
                continue
                
    except ValueError:
        print("Valor inválido! Digite um número inteiro.")
        return cadastrar_produtos()
    
    return produtos

def adicionar_estoque(produtos):
    """Função para adicionar unidades ao estoque"""
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    
    nome = input("Nome do produto para adicionar estoque: ").strip()
    produto_encontrado = None
    
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            produto_encontrado = produto
            break
    
    if produto_encontrado:
        try:
            quantidade = int(input(f"Quantas unidades adicionar ao produto '{nome}'? "))
            if quantidade <= 0:
                print("Quantidade deve ser maior que zero!")
                return
            produto_encontrado['quantidade'] += quantidade
            print(f"✓ {quantidade} unidades adicionadas ao estoque de '{nome}'")
            print(f"Novo estoque: {produto_encontrado['quantidade']} unidades")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")
    else:
        print(f"Produto '{nome}' não encontrado!")

def retirar_estoque(produtos):
    """Função para retirar unidades do estoque com verificação de estoque suficiente"""
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    
    nome = input("Nome do produto para retirar do estoque: ").strip()
    produto_encontrado = None
    
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            produto_encontrado = produto
            break
    
    if produto_encontrado:
        try:
            quantidade = int(input(f"Quantas unidades retirar do produto '{nome}'? "))
            if quantidade <= 0:
                print("Quantidade deve ser maior que zero!")
                return
                
            if quantidade <= produto_encontrado['quantidade']:
                produto_encontrado['quantidade'] -= quantidade
                print(f"✓ {quantidade} unidades retiradas do estoque de '{nome}'")
                print(f"Estoque restante: {produto_encontrado['quantidade']} unidades")
            else:
                print(f"✗ Estoque insuficiente! Disponível: {produto_encontrado['quantidade']} unidades")
                print(f"Tentou retirar: {quantidade} unidades")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")
    else:
        print(f"Produto '{nome}' não encontrado!")

def consultar_produto(produtos):
    """Função para consultar um produto específico"""
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    
    nome = input("Nome do produto para consultar: ").strip()
    produto_encontrado = None
    
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            produto_encontrado = produto
            break
    
    if produto_encontrado:
        valor_total = produto_encontrado['quantidade'] * produto_encontrado['preco']
        print(f"\n--- Consulta do Produto: {produto_encontrado['nome']} ---")
        print(f"Quantidade em estoque: {produto_encontrado['quantidade']} unidades")
        print(f"Preço unitário: R$ {produto_encontrado['preco']:.2f}")
        print(f"Valor total em estoque: R$ {valor_total:.2f}")
    else:
        print(f"Produto '{nome}' não encontrado!")

def listar_produtos(produtos):
    """Função para listar todos os produtos com valor total"""
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    
    print("\n" + "="*60)
    print(f"{'PRODUTO':<20} {'QUANTIDADE':<12} {'PREÇO UNIT.':<12} {'VALOR TOTAL':<12}")
    print("-"*60)
    
    valor_total_geral = 0
    
    for produto in produtos:
        valor_total = produto['quantidade'] * produto['preco']
        valor_total_geral += valor_total
        
        print(f"{produto['nome']:<20} {produto['quantidade']:<12} R$ {produto['preco']:<10.2f} R$ {valor_total:<10.2f}")
    
    print("-"*60)
    print(f"{'TOTAL GERAL':<44} R$ {valor_total_geral:<10.2f}")
    print("="*60)

def exibir_menu():
    """Função para exibir o menu de opções"""
    print("\n" + "="*40)
    print("          CONTROLE DE ESTOQUE")
    print("="*40)
    print("1. Adicionar unidades ao estoque")
    print("2. Retirar unidades do estoque")
    print("3. Consultar um produto")
    print("4. Listar todos os produtos")
    print("5. Encerrar o programa")
    print("="*40)

def main():
    """Função principal do programa"""
    print("="*40)
    print("     BEM-VINDO AO CONTROLE DE ESTOQUE")
    print("="*40)
    
    # Cadastro inicial dos produtos
    produtos = cadastrar_produtos()
    
    if not produtos:
        print("Nenhum produto cadastrado. O programa será encerrado.")
        return
    
    print(f"\n✓ {len(produtos)} produtos cadastrados com sucesso!")
    
    # Loop principal do menu
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção (1-5): "))
            
            if opcao == 1:
                adicionar_estoque(produtos)
            elif opcao == 2:
                retirar_estoque(produtos)
            elif opcao == 3:
                consultar_produto(produtos)
            elif opcao == 4:
                listar_produtos(produtos)
            elif opcao == 5:
                print("\nEncerrando o programa...")
                print("Obrigado por usar o Controle de Estoque!")
                break
            else:
                print("Opção inválida! Escolha um número entre 1 e 5.")
                
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")

if __name__ == "__main__":
    main()