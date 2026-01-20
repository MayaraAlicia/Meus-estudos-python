from zxcvbn import zxcvbn

print("--- VERIFICADOR DE SENHAS PROFISSIONAL (zxcvbn) ---")
print("Nota 0: Muito Fraca | Nota 4: Muito Forte")

while True:

    senha = input("Digite a senha que deseja verificar (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Encerrando o verificador de senhas. Até mais!")
        break

    resultado = zxcvbn(senha)
    score = resultado['score']

    tempo_quebrar = resultado['crack_times_display']['offline_slow_hashing_1e4_per_second']
    feedback_aviso = resultado['feedback']['warning']
    feedback_sugestoes = resultado['feedback']['suggestions']

    print ("📊 Relatório de Segurança:")
    print (f" - Nota da Senha: {score} / 4")
    print (f" - Tempo estimado para quebra: {tempo_quebrar}")

    if feedback_aviso:
        print (f" - Aviso: {feedback_aviso}")
    if feedback_sugestoes:
        print (" - Sugestões para melhorar a senha:")
        for sugestao in feedback_sugestoes:
            print (f"    • {sugestao}")
    
    if score >= 3:
        print ("✅ Sua senha é forte! Parabéns!")
    else:
        print ("⚠️ Sua senha pode ser melhorada. Vamos tentar de novo?")
    
    print ("\n" + "-"*40 + "\n")
