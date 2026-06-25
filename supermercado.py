import random

def calcular_tempo_atendimento(itens):
    """
    Calcula o tempo de atendimento baseado na quantidade de itens
    Fórmula: tempo = 2 + 0,5 * quantidade_itens
    """
    return 2 + 0.5 * itens

def encontrar_caixa_menor_tempo(tempos_caixas):
    """
    Encontra o índice do caixa com menor tempo acumulado
    Em caso de empate, retorna o caixa de menor número
    """
    menor_tempo = min(tempos_caixas)
    # Retorna o primeiro caixa com o menor tempo (menor número)
    return tempos_caixas.index(menor_tempo)

def alocar_cliente(caixas, tempos_caixas, cliente, tempo):
    """
    Aloca um cliente ao caixa com menor tempo acumulado
    """
    indice_caixa = encontrar_caixa_menor_tempo(tempos_caixas)
    
    # Adiciona o cliente à fila do caixa
    caixas[indice_caixa].append(cliente)
    
    # Atualiza o tempo acumulado do caixa
    tempos_caixas[indice_caixa] += tempo
    
    return indice_caixa

def validar_quantidade(valor, mensagem, minimo=1):
    """
    Valida se a quantidade é um número inteiro positivo
    """
    while True:
        try:
            numero = int(input(mensagem))
            if numero >= minimo:
                return numero
            print(f"O valor deve ser maior ou igual a {minimo}!")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")

def validar_itens(mensagem):
    """
    Valida se a quantidade de itens é não negativa
    """
    while True:
        try:
            itens = int(input(mensagem))
            if itens >= 0:
                return itens
            print("A quantidade de itens não pode ser negativa!")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")

def cadastrar_clientes(quantidade_clientes):
    """
    Cadastra os dados de todos os clientes
    """
    clientes = []
    
    for i in range(quantidade_clientes):
        print(f"\n--- Cliente {i+1} ---")
        
        codigo = input("Código do cliente: ").strip()
        if not codigo:
            print("Código não pode ser vazio!")
            codigo = f"C{i+1:03d}"  # Gera código automático se vazio
        
        itens = validar_itens("Quantidade de itens no carrinho: ")
        
        tempo = calcular_tempo_atendimento(itens)
        
        clientes.append({
            'codigo': codigo,
            'itens': itens,
            'tempo': tempo
        })
    
    return clientes

def distribuir_clientes(clientes, num_caixas):
    """
    Distribui os clientes entre os caixas usando a estratégia de menor tempo
    """
    # Inicializa as estruturas
    caixas = [[] for _ in range(num_caixas)]
    tempos_caixas = [0.0 for _ in range(num_caixas)]
    alocacoes = []  # Para registrar onde cada cliente foi alocado
    
    print("\n" + "="*50)
    print("         DISTRIBUINDO CLIENTES")
    print("="*50)
    
    for cliente in clientes:
        indice_caixa = alocar_cliente(caixas, tempos_caixas, cliente, cliente['tempo'])
        
        print(f"Cliente {cliente['codigo']} (tempo: {cliente['tempo']:.1f} min) → Caixa {indice_caixa + 1}")
        
        alocacoes.append({
            'cliente': cliente,
            'caixa': indice_caixa + 1
        })
    
    return caixas, tempos_caixas, alocacoes

def calcular_estatisticas(clientes, caixas, tempos_caixas):
    """
    Calcula todas as estatísticas do sistema
    """
    # Tempo médio de atendimento por cliente
    tempos_clientes = [cliente['tempo'] for cliente in clientes]
    tempo_medio = sum(tempos_clientes) / len(tempos_clientes) if tempos_clientes else 0
    
    # Caixa com maior e menor tempo acumulado
    maior_tempo = max(tempos_caixas)
    menor_tempo = min(tempos_caixas)
    caixa_maior = tempos_caixas.index(maior_tempo) + 1
    caixa_menor = tempos_caixas.index(menor_tempo) + 1
    
    # Tempo total do sistema (maior tempo acumulado)
    tempo_total_sistema = max(tempos_caixas)
    
    # Médias por caixa
    medias_caixas = []
    for i, caixa in enumerate(caixas):
        if caixa:
            tempo_total_caixa = tempos_caixas[i]
            media_caixa = tempo_total_caixa / len(caixa)
            medias_caixas.append(media_caixa)
        else:
            medias_caixas.append(0)
    
    return {
        'tempo_medio': tempo_medio,
        'caixa_maior_tempo': caixa_maior,
        'caixa_menor_tempo': caixa_menor,
        'tempo_total_sistema': tempo_total_sistema,
        'medias_caixas': medias_caixas,
        'maior_tempo': maior_tempo,
        'menor_tempo': menor_tempo
    }

def exibir_resultados(caixas, tempos_caixas, clientes, alocacoes):
    """
    Exibe todos os resultados do sistema
    """
    print("\n" + "="*60)
    print("         RESULTADOS DO SIMULADOR")
    print("="*60)
    
    # Exibe a fila de cada caixa
    for i, caixa in enumerate(caixas):
        print(f"\n--- Caixa {i+1} ---")
        if caixa:
            codigos = [cliente['codigo'] for cliente in caixa]
            print(f"Clientes atendidos: {', '.join(codigos)}")
            print(f"Tempo total: {tempos_caixas[i]:.1f} minutos")
            print(f"Quantidade de clientes: {len(caixa)}")
            if caixa:
                media_caixa = tempos_caixas[i] / len(caixa)
                print(f"Tempo médio no caixa: {media_caixa:.2f} minutos")
        else:
            print("Nenhum cliente atendido")
            print(f"Tempo total: 0.0 minutos")
    
    # Estatísticas
    stats = calcular_estatisticas(clientes, caixas, tempos_caixas)
    
    print("\n" + "="*60)
    print("         ESTATÍSTICAS DO SISTEMA")
    print("="*60)
    print(f"\nTempo médio de atendimento por cliente: {stats['tempo_medio']:.2f} minutos")
    print(f"Caixa com maior tempo acumulado: Caixa {stats['caixa_maior_tempo']} ({stats['maior_tempo']:.1f} min)")
    print(f"Caixa com menor tempo acumulado: Caixa {stats['caixa_menor_tempo']} ({stats['menor_tempo']:.1f} min)")
    print(f"Tempo total necessário para encerrar todos os atendimentos: {stats['tempo_total_sistema']:.1f} minutos")
    
    # Exibe médias por caixa
    print("\nMédias de atendimento por caixa:")
    for i, media in enumerate(stats['medias_caixas']):
        if media > 0:
            print(f"  Caixa {i+1}: {media:.2f} minutos/cliente")
        else:
            print(f"  Caixa {i+1}: Sem clientes")
    
    # Exibe eficiência dos caixas
    print("\nEficiência dos caixas:")
    for i, caixa in enumerate(caixas):
        if caixa:
            eficiencia = (tempos_caixas[i] / stats['tempo_total_sistema']) * 100
            print(f"  Caixa {i+1}: {eficiencia:.1f}% do tempo total")
    
    print("\n" + "="*60)

def exibir_resumo_alocacao(alocacoes):
    """
    Exibe um resumo de onde cada cliente foi alocado
    """
    print("\n" + "="*50)
    print("         RESUMO DE ALOCAÇÃO")
    print("="*50)
    print(f"{'CLIENTE':<10} {'ITENS':<10} {'TEMPO':<10} {'CAIXA':<10}")
    print("-"*50)
    
    for alocacao in alocacoes:
        cliente = alocacao['cliente']
        print(f"{cliente['codigo']:<10} {cliente['itens']:<10} {cliente['tempo']:<10.1f} {alocacao['caixa']:<10}")
    
    print("="*50)

def menu_principal():
    """
    Exibe o menu principal do programa
    """
    print("\n" + "="*50)
    print("    SIMULADOR DE CAIXA DE SUPERMERCADO")
    print("="*50)
    print("1. Executar simulação")
    print("2. Sair")
    print("="*50)

def simular_atendimento():
    """
    Função principal para simular o atendimento
    """
    print("\n" + "="*50)
    print("    SIMULADOR DE CAIXA DE SUPERMERCADO")
    print("="*50)
    
    # Solicita dados iniciais
    num_caixas = validar_quantidade(0, "Quantidade de caixas disponíveis: ", 1)
    num_clientes = validar_quantidade(0, "Quantidade de clientes: ", 1)
    
    print(f"\n✓ {num_caixas} caixas disponíveis")
    print(f"✓ {num_clientes} clientes serão atendidos")
    
    # Cadastra os clientes
    print("\n--- CADASTRO DE CLIENTES ---")
    clientes = cadastrar_clientes(num_clientes)
    
    # Distribui os clientes
    caixas, tempos_caixas, alocacoes = distribuir_clientes(clientes, num_caixas)
    
    # Exibe os resultados
    exibir_resumo_alocacao(alocacoes)
    exibir_resultados(caixas, tempos_caixas, clientes, alocacoes)

def main():
    """
    Função principal do programa
    """
    print("="*50)
    print("   BEM-VINDO AO SIMULADOR DE CAIXA")
    print("="*50)
    
    while True:
        menu_principal()
        
        try:
            opcao = int(input("Escolha uma opção (1-2): "))
            
            if opcao == 1:
                simular_atendimento()
            elif opcao == 2:
                print("\nEncerrando o simulador...")
                print("Obrigado por usar o Simulador de Caixa de Supermercado!")
                break
            else:
                print("Opção inválida! Escolha 1 ou 2.")
                
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")

if __name__ == "__main__":
    main()