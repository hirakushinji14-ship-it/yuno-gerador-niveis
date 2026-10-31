import random

def exibir_cabecalho():
    print("\033[35m  🗡️  Diário da Yuno -\033[0m")
    print("\033[35m\"Opa... Deixa o futuro desse jogo a gente vai montar a fase?\" ♡\033[0m\n")

def main():
    exibir_cabecalho()
    
    # Pergunta em Amarelo
    perigo_input = input("\033[33mQual vai ser o nível de perigo? (pacifico / normal / insano): \033[0m").strip().lower()
    
    if "p" in perigo_input:
        chave_perigo = "pacifico"
        print("\n\033[35m\"Hum... Pacífico? Tá muito sem graça! Quer saber? Deixa que eu mesma coloco umas surpresas no final para você não dormir!\" 🔪\033[0m\n")
    elif "i" in perigo_input:
        chave_perigo = "insano"
        print("\n\033[35m\"Eita, insano desse jeito?! Calma... Se você morrer muito rápido eu fico sem graça. Deixa eu dar um jeitinho de equilibrar para você durar mais comigo ♡\"\033[0m\n")
    else:
        chave_perigo = "normal"
        print("\n\033[35m\"Equilibrado... Do jeito que a gente gosta. Nem muito fácil, nem letal. Ainda.\" ✨\033[0m\n")
        
    try:
        largura = int(input("\033[33mQuantos blocos de largura vai ter a fase?: \033[0m"))
    except ValueError:
        largura = 20

    if largura < 15:
        largura = 15

    chao = ["🟩" for _ in range(largura)]
    plataformas = ["  " for _ in range(largura)]
    perigos = ["  " for _ in range(largura)]
    inimigos = ["  " for _ in range(largura)]

    # --- LÓGICA DE ESPAÇAMENTO REALISTA DE PLATAFORMAS ---
    # Cria ilhas de plataformas (2 a 3 blocos) com vãos calculados para pulo
    i = 3
    while i < largura - 3:
        tamanho_plat = random.randint(2, 3) # Plataforma com 2 ou 3 blocos seguidos
        for p in range(tamanho_plat):
            if i + p < largura - 1:
                plataformas[i + p] = "🧱"
                # Chance de spawnar um inimigo em cima da plataforma
                if p == 0 and chave_perigo != "pacifico" and random.random() > 0.4:
                    inimigos[i + p] = "👾"
        # Pula um espaço vazio de 2 blocos para exigir o salto do player
        i += tamanho_plat + 2

    # Perigos no chão com base na dificuldade
    if chave_perigo == "insano":
        for idx in range(3, largura - 2, 3):
            if plataformas[idx] == "  ":
                perigos[idx] = "🟥"
    elif chave_perigo == "normal":
        for idx in range(4, largura - 2, 5):
            if plataformas[idx] == "  ":
                perigos[idx] = "🟥"

    # --- INTERFERÊNCIA DINÂMICA DA YUNO ---
    if chave_perigo == "pacifico":
        print("\033[31m⚡ [Intervenção da Yuno]: Sabotando o final da fase com armadilhas e inimigos extras!\033[0m")
        inicio_sabotagem = int(largura * 0.6)
        for idx in range(inicio_sabotagem, largura - 1):
            if idx % 2 == 0:
                perigos[idx] = "🟥"
                inimigos[idx] = "👾"
            else:
                plataformas[idx] = "🧱"
    elif chave_perigo == "insano":
        print("\033[32m💌 [Intervenção da Yuno]: Suavizando alguns saltos e colocando plataformas de apoio extra!\033[0m")
        for idx in range(len(perigos)):
            if perigos[idx] == "🟥" and idx > 2:
                perigos[idx] = "  "
                plataformas[idx] = "🧱"

    jogador_pos = 1

    # Renderização visual organizada
    print(f"\n🔥 \033[36m=== MAPA DE PLATAFORMA DA YUNO ({largura} blocos) | PERIGO: {chave_perigo.upper()} ===\033[0m\n")
    
    print("👾 Inimigos: " + "".join(inimigos))
    print("🧱 Plat.  : " + "".join(plataformas))
    
    linha_jog = []
    for idx in range(largura):
        if idx == jogador_pos:
            linha_jog.append("🏃")
        else:
            linha_jog.append("  ")
    print("🏃 Jogador: " + "".join(linha_jog))
    
    print("🟩 Chão   : " + "".join(chao))
    print("🟥 Perigos: " + "".join(perigos))
    
    indices = "   " + " ".join([f"{idx:2}" for idx in range(largura)])
    print(indices)
    
    print(f"\n\033[32m✨ Fase gerada com espaçamento perfeito para saltos! ♡\033[0m")

if __name__ == "__main__":
    main()
