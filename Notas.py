def validar_nota(nota, numero_nota):
    """Função para validar se a nota está entre 0 e 10"""
    if nota < 0 or nota > 10:
        print(f"Nota {numero_nota} deve estar entre 0 e 10!")
        return False
    return True

def cadastrar_alunos():
    """Função para cadastrar os alunos e suas notas"""
    alunos = []
    
    try:
        quantidade = int(input("Quantos alunos deseja cadastrar? "))
        if quantidade <= 0:
            print("Quantidade deve ser maior que zero!")
            return cadastrar_alunos()
        
        for i in range(quantidade):
            print(f"\n--- Aluno {i+1} ---")
            
            nome = input("Nome do aluno: ").strip()
            if not nome:
                print("Nome não pode ser vazio!")
                continue
            
            notas = []
            for j in range(1, 4):
                while True:
                    try:
                        nota = float(input(f"Nota {j}: "))
                        if validar_nota(nota, j):
                            notas.append(nota)
                            break
                    except ValueError:
                        print("Valor inválido! Digite um número.")
            
            if len(notas) == 3:
                media = calcular_media(notas)
                situacao = classificar_situacao(media)
                
                alunos.append({
                    'nome': nome,
                    'notas': notas,
                    'media': media,
                    'situacao': situacao
                })
                
    except ValueError:
        print("Valor inválido! Digite um número inteiro.")
        return cadastrar_alunos()
    
    return alunos

def calcular_media(notas):
    """Função para calcular a média aritmética das notas"""
    return sum(notas) / len(notas)

def classificar_situacao(media):
    """Função para classificar a situação do aluno baseado na média"""
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def calcular_media_geral(alunos):
    """Função para calcular a média geral da turma"""
    if not alunos:
        return 0
    soma_medias = sum(aluno['media'] for aluno in alunos)
    return soma_medias / len(alunos)

def encontrar_melhores_notas(alunos):
    """Função para encontrar o aluno com maior e menor média"""
    if not alunos:
        return None, None
    
    maior_media = max(alunos, key=lambda x: x['media'])
    menor_media = min(alunos, key=lambda x: x['media'])
    
    return maior_media, menor_media

def contar_situacoes(alunos):
    """Função para contar quantos alunos estão em cada situação"""
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    
    for aluno in alunos:
        if aluno['situacao'] == "Aprovado":
            aprovados += 1
        elif aluno['situacao'] == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1
    
    return aprovados, recuperacao, reprovados

def exibir_tabela_alunos(alunos):
    """Função para exibir a tabela com todos os alunos"""
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    
    print("\n" + "="*80)
    print(f"{'NOME':<20} {'NOTA 1':<10} {'NOTA 2':<10} {'NOTA 3':<10} {'MÉDIA':<10} {'SITUAÇÃO':<15}")
    print("-"*80)
    
    for aluno in alunos:
        print(f"{aluno['nome']:<20} {aluno['notas'][0]:<10.2f} {aluno['notas'][1]:<10.2f} {aluno['notas'][2]:<10.2f} {aluno['media']:<10.2f} {aluno['situacao']:<15}")
    
    print("="*80)

def exibir_estatisticas(alunos):
    """Função para exibir as estatísticas da turma"""
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    
    print("\n" + "="*50)
    print("          ESTATÍSTICAS DA TURMA")
    print("="*50)
    
    # Média geral
    media_geral = calcular_media_geral(alunos)
    print(f"Média geral da turma: {media_geral:.2f}")
    
    # Melhor e pior aluno
    maior_media, menor_media = encontrar_melhores_notas(alunos)
    if maior_media and menor_media:
        print(f"Aluno com maior média: {maior_media['nome']} - {maior_media['media']:.2f}")
        print(f"Aluno com menor média: {menor_media['nome']} - {menor_media['media']:.2f}")
    
    # Contagem de situações
    aprovados, recuperacao, reprovados = contar_situacoes(alunos)
    print(f"\nQuantidade de aprovados: {aprovados}")
    print(f"Quantidade em recuperação: {recuperacao}")
    print(f"Quantidade de reprovados: {reprovados}")
    
    # Percentuais
    total = len(alunos)
    if total > 0:
        print(f"\nPercentual de aprovação: {(aprovados/total)*100:.1f}%")
        print(f"Percentual em recuperação: {(recuperacao/total)*100:.1f}%")
        print(f"Percentual de reprovação: {(reprovados/total)*100:.1f}%")
    
    print("="*50)

def menu_alunos():
    """Função para exibir o menu de opções"""
    print("\n" + "="*40)
    print("          ANÁLISE DE NOTAS")
    print("="*40)
    print("1. Cadastrar alunos")
    print("2. Exibir tabela de notas")
    print("3. Exibir estatísticas")
    print("4. Sair")
    print("="*40)

def main():
    """Função principal do programa"""
    print("="*40)
    print("   BEM-VINDO À ANÁLISE DE NOTAS")
    print("="*40)
    
    alunos = []
    
    while True:
        menu_alunos()
        
        try:
            opcao = int(input("Escolha uma opção (1-4): "))
            
            if opcao == 1:
                alunos = cadastrar_alunos()
                if alunos:
                    print(f"\n✓ {len(alunos)} alunos cadastrados com sucesso!")
                
            elif opcao == 2:
                exibir_tabela_alunos(alunos)
                
            elif opcao == 3:
                exibir_estatisticas(alunos)
                
            elif opcao == 4:
                print("\nEncerrando o programa...")
                print("Obrigado por usar a Análise de Notas!")
                break
                
            else:
                print("Opção inválida! Escolha um número entre 1 e 4.")
                
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")

if __name__ == "__main__":
    main()