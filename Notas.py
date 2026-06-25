def validar_nota(nota, n):
    if nota < 0 or nota > 10:
        print(f"Nota {n} deve estar entre 0 e 10!")
        return False
    return True

def cadastrar_alunos():
    alunos = []
    try:
        qtd = int(input("Quantos alunos? "))
        if qtd <= 0:
            print("Quantidade deve ser maior que zero!")
            return cadastrar_alunos()
        for i in range(qtd):
            print(f"\n--- Aluno {i+1} ---")
            nome = input("Nome: ").strip()
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
                media = sum(notas)/3
                situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
                alunos.append({'nome': nome, 'notas': notas, 'media': media, 'situacao': situacao})
    except ValueError:
        print("Valor inválido!")
        return cadastrar_alunos()
    return alunos

def exibir_tabela(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    print("\n" + "="*80)
    print(f"{'NOME':<20} {'N1':<8} {'N2':<8} {'N3':<8} {'MÉDIA':<8} {'SITUAÇÃO':<15}")
    print("-"*80)
    for a in alunos:
        print(f"{a['nome']:<20} {a['notas'][0]:<8.2f} {a['notas'][1]:<8.2f} {a['notas'][2]:<8.2f} {a['media']:<8.2f} {a['situacao']:<15}")
    print("="*80)

def exibir_estatisticas(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    print("\n" + "="*50)
    print("          ESTATÍSTICAS")
    print("="*50)
    medias = [a['media'] for a in alunos]
    print(f"Média geral: {sum(medias)/len(medias):.2f}")
    maior = max(alunos, key=lambda x: x['media'])
    menor = min(alunos, key=lambda x: x['media'])
    print(f"Maior média: {maior['nome']} - {maior['media']:.2f}")
    print(f"Menor média: {menor['nome']} - {menor['media']:.2f}")
    aprov = sum(1 for a in alunos if a['situacao'] == "Aprovado")
    recup = sum(1 for a in alunos if a['situacao'] == "Recuperação")
    reprov = sum(1 for a in alunos if a['situacao'] == "Reprovado")
    print(f"\nAprovados: {aprov}")
    print(f"Recuperação: {recup}")
    print(f"Reprovados: {reprov}")
    total = len(alunos)
    print(f"\n% Aprovação: {(aprov/total)*100:.1f}%")
    print(f"% Recuperação: {(recup/total)*100:.1f}%")
    print(f"% Reprovação: {(reprov/total)*100:.1f}%")
    print("="*50)

def main():
    print("="*40)
    print("   ANÁLISE DE NOTAS")
    print("="*40)
    alunos = []
    while True:
        print("\n1. Cadastrar\n2. Tabela\n3. Estatísticas\n4. Sair")
        try:
            opcao = int(input("Opção: "))
            if opcao == 1:
                alunos = cadastrar_alunos()
                print(f"\n✓ {len(alunos)} alunos cadastrados!")
            elif opcao == 2:
                exibir_tabela(alunos)
            elif opcao == 3:
                exibir_estatisticas(alunos)
            elif opcao == 4:
                print("\nEncerrando... Obrigado!")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número!")

if __name__ == "__main__":
    main()
