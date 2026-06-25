import random

def calcular_tempo(itens):
    return 2 + 0.5 * itens

def encontrar_caixa(tempos):
    return tempos.index(min(tempos))

def alocar_cliente(caixas, tempos, cliente, tempo):
    idx = encontrar_caixa(tempos)
    caixas[idx].append(cliente)
    tempos[idx] += tempo
    return idx

def validar_num(mensagem, minimo=1):
    while True:
        try:
            n = int(input(mensagem))
            if n >= minimo:
                return n
            print(f"Valor deve ser >= {minimo}!")
        except ValueError:
            print("Digite um número!")

def validar_itens(mensagem):
    while True:
        try:
            n = int(input(mensagem))
            if n >= 0:
                return n
            print("Não pode ser negativo!")
        except ValueError:
            print("Digite um número!")

def cadastrar_clientes(qtd):
    clientes = []
    for i in range(qtd):
        print(f"\n--- Cliente {i+1} ---")
        codigo = input("Código: ").strip() or f"C{i+1:03d}"
        itens = validar_itens("Itens no carrinho: ")
        tempo = calcular_tempo(itens)
        clientes.append({'codigo': codigo, 'itens': itens, 'tempo': tempo})
    return clientes

def distribuir_clientes(clientes, num_caixas):
    caixas = [[] for _ in range(num_caixas)]
    tempos = [0.0 for _ in range(num_caixas)]
    alocacoes = []
    print("\n" + "="*50)
    print("         DISTRIBUINDO CLIENTES")
    print("="*50)
    for c in clientes:
        idx = alocar_cliente(caixas, tempos, c, c['tempo'])
        print(f"Cliente {c['codigo']} ({c['tempo']:.1f}min) → Caixa {idx+1}")
        alocacoes.append({'cliente': c, 'caixa': idx+1})
    return caixas, tempos, alocacoes

def exibir_resultados(caixas, tempos, clientes, alocacoes):
    print("\n" + "="*60)
    print("         RESULTADOS")
    print("="*60)
    for i, caixa in enumerate(caixas):
        print(f"\n--- Caixa {i+1} ---")
        if caixa:
            cods = [c['codigo'] for c in caixa]
            print(f"Clientes: {', '.join(cods)}")
            print(f"Tempo total: {tempos[i]:.1f}min")
            print(f"Clientes: {len(caixa)}")
            print(f"Média: {tempos[i]/len(caixa):.2f}min")
        else:
            print("Nenhum cliente")
    
    # Estatísticas
    temps = [c['tempo'] for c in clientes]
    print("\n" + "="*60)
    print("         ESTATÍSTICAS")
    print("="*60)
    print(f"Média por cliente: {sum(temps)/len(temps):.2f}min")
    maior = max(tempos)
    menor = min(tempos)
    print(f"Caixa mais ocupado: {tempos.index(maior)+1} ({maior:.1f}min)")
    print(f"Caixa menos ocupado: {tempos.index(menor)+1} ({menor:.1f}min)")
    print(f"Tempo total: {max(tempos):.1f}min")
    
    print("\nMédias por caixa:")
    for i, t in enumerate(tempos):
        if caixas[i]:
            print(f"  Caixa {i+1}: {t/len(caixas[i]):.2f}min/cliente")
        else:
            print(f"  Caixa {i+1}: Sem clientes")
    
    print("\nEficiência:")
    for i, t in enumerate(tempos):
        if caixas[i]:
            print(f"  Caixa {i+1}: {(t/max(tempos))*100:.1f}%")
    
    print("\n" + "="*60)

def exibir_resumo(alocacoes):
    print("\n" + "="*50)
    print("         RESUMO")
    print("="*50)
    print(f"{'CLIENTE':<10} {'ITENS':<10} {'TEMPO':<10} {'CAIXA':<10}")
    print("-"*50)
    for a in alocacoes:
        c = a['cliente']
        print(f"{c['codigo']:<10} {c['itens']:<10} {c['tempo']:<10.1f} {a['caixa']:<10}")
    print("="*50)

def main():
    print("="*50)
    print("   SIMULADOR DE CAIXA")
    print("="*50)
    while True:
        print("\n1. Simular\n2. Sair")
        try:
            opcao = int(input("Opção: "))
            if opcao == 1:
                print("\n" + "="*50)
                print("   SIMULADOR")
                print("="*50)
                caixas_num = validar_num("Caixas: ", 1)
                clientes_num = validar_num("Clientes: ", 1)
                clientes = cadastrar_clientes(clientes_num)
                caixas, tempos, alocacoes = distribuir_clientes(clientes, caixas_num)
                exibir_resumo(alocacoes)
                exibir_resultados(caixas, tempos, clientes, alocacoes)
            elif opcao == 2:
                print("\nEncerrando... Obrigado!")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número!")

if __name__ == "__main__":
    main()
