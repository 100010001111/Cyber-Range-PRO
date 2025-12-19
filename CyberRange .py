#vou importar as bibliotecas necessárias 
import random #aleatoriedade
import time #pausas, delays entre os textos 
import os #faz uma limpezinha na tela, reinício

#textos para o efeito visual
TEXTOS = [
    "\033[ OK ] Conectando ao servidor remoto..\033[0m",
    "\033[ !! ] Firewall detectado\033[0m",
    "\033[ >> ] Forçando autenticação..\033[0m",
    "\033[ OK ] Acesso concedido\033[0m",
    "\033[ >> ] Injetando payload falso..\033[0m",
    "\033[ ## ] Criptografando pacotes..\033[0m",
    "\033[ OK ] Extraindo dados simulados..\033[0m",
    "\033[ !! ] Bypass concluído com sucesso\033[0m",
    "\033[92m[+] Sincronizando osciladores de frequência\033[0m",
    "\033[92m[+] Estabelecendo conexão entrelaçada\033[0m",
    "\033[92m[+] Criptografia ativada\033[0m",
    "\033[92m[+] Canal seguro estabelecido\033[0m",
    "\033[92m[+] Transmitindo dados não-locais...\033[0m",
    "\033[92m[0x01x00x1x00] Inicializando payload assimétrico...\033[0m",
    "\033[92m[0x00x01x1x00] Sincronizando osciladores de frequência\033[0m",
    "\033[92m[0x00x00x1x00] Calibrando matriz de interferência\033[0m",
    "\033[92m[0x00x00x1x00] Estabelecendo conexão entrelaçada\033[0m",
    "\033[92m[0x10x00x1x00] Protocolo 0x00x00x1x00: FASE 1 COMPLETA\033[0m",
    "\033[92m[0x00x00x1x00] ERRO: Dessincronização detectada\033[0m",
    "\033[92m[0x00x00x1x01] Recalibrando... 87 por cento de estabilidade\033[0m",
    "\033[92m[0x00x00x1x00] Pulso de verificação: 01001011 01001111\033[0m",
    "\033[92m[1x00x00x1x00] Criptografia fractal ativada\033[0m",
    "\033[92m[1x01x00x1x00] Canal seguro estabelecido: 0x00x00x1x00\033[0m",
    "\033[92m[1x00x00x1x10] Transmitindo dados não-locais...\033[0m",
    "\033[92m[0x00x00x1x00] Payload carregado\033[0m",
    "\033[92m[0x00x00x1x00] Colapsando função de onda...\033[0m",
    "\033[92m[0x00x11x1x00] Resultado: 0x00x00x1x000x00x00x1x00 \033[0m",
    "\033[92m[0x00x00x1x00] Leitura NFC em progresso\033[0m",
    "\033[92m[0x11x00x1x00] Fidelidade: 0.997 acima do limiar\033[0m",
    "\033[92m[0x00x00x1x00] Protocolo 0x00x00x1x00: CONCLUSÃO BEM-SUCEDIDA\033[0m",
    "\033[92m[1x10x11x10x1] inicializado\033[0m",
    "\033[92m[0x00x00x1x00] Estado final: Superposição mantida\033[0m",
    "\033[92m[1x00x10x1x10] [SISTEMA] Pronto para próximo ciclo\033[0m"
]

#função de limpar a tela
def limpar_tela():
    os.system('clear')

#gera um hash falso
def gerar_hash_falso():
    tipos = ['MD5', 'SHA1', 'SHA256', 'NTLM']
    tipo = random.choice(tipos)
    dados = os.urandom(16).hex()
    return tipo, dados[:32] if tipo != 'NTLM' else dados.upper()

#cria senha falsa
def gerar_senha():
    tipos = ['Android', 'Mobile', 'Wi-Fi', 'Wireless' , 'system' ]
    return random.choice(tipos), f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"

# IP
def gerar_ip():
    ips = ['192.168.1.', '10.0.0.0', '172.160.0.1' , '10.0.0.1' , '192.168.0.1' , '1.1.1.1' , '252.168.100' , '200.100.50']
    locais = ['RJ', 'BR', 'Centro RJ' , 'Net Fibra' , 'Telecom internet' ]
    return random.choice(ips) + str(random.randint(1, 254)), random.choice(locais)

#mostra os resultados
def mostrar_resultados():
    print("\n" + "="*60)
    print("\033[92m" + " " * 20 + "RESULTADOS ENCONTRADOS" + " " * 20 + "\033[0m")
    print("="*60)
    
    tipo_hash, hash_valor = gerar_hash_falso()
    print(f"\n\033[93m[+] HASH CRACKED:\033[0m")
    print(f"   Tipo: {tipo_hash}")
    print(f"   Hash: {hash_valor}")
    
    tipo_senha, senha = gerar_senha()
    print(f"\n\033[93m[+] SENHA ENCONTRADA:\033[0m")
    print(f"   Alvo: {tipo_senha}")
    print(f"   \033[91mSenha: {senha}\033[0m")
    
    ip, local = gerar_ip()
    print(f"\n\033[93m[+] ENDEREÇO IP:\033[0m")
    print(f"   IP: {ip}")
    print(f"   Local: {local}")
    
    print(f"\n\033[93m[+] DADOS ADICIONAIS:\033[0m")
    print(f"   Usuário: {random.choice(['admin', 'root', 'user'])}")
    print(f"   Porta: {random.choice([22, 80, 443, 3389])}")
    print(f"   Data: {random.randint(1,28):02d}/{random.randint(1,12):02d}/2024")
    
    print("="*60 + "\n")

def executar_ataque(duracao, velocidade):
    limpar_tela()
    print(f">>> ATAQUE EM EXECUÇÃO ({duracao}s)...\n")
    
    inicio = time.time()
    mensagens_exibidas = 0
    
    while time.time() - inicio < duracao:
        print(random.choice(TEXTOS))
        mensagens_exibidas += 1
        
        #mostra progresso a cada 3 mensagens
        if mensagens_exibidas % 3 == 0:
            progresso = ((time.time() - inicio) / duracao) * 100
            barra = "●●" * int(progresso/5) + " " * (20 - int(progresso/5))
            print(f"\033[94m[{barra}] {progresso:.1f}%\033[0m\n")
        
        time.sleep(velocidade)
    
    print("\n\033[92m>>> PENTEST FINALIZADO\033[0m")
    time.sleep(1)
    mostrar_resultados()
    input("\n\033[93mPressione Enter para voltar ao menu...\033[0m")

#menu principal
def menu():
    opcoes = {
        "1": ("Ataque padrão (2 segundos)", 2, 0.1),
        "2": ("Ataque rápido (2 segundos)", 2, 0.03),
        "3": ("Ataque RÁPIDO de 10 segundos", 10, 0.03),
        "4": ("Ataque LENTO de 10 segundos", 10, 0.3),
    }
    
    while True:
        limpar_tela()
        print("""
              

                .;´                   `;.                   
              .;'  ,;'             `;,  `;,                  
             .;'  ,;   ,;´     `;,  `;,  `;,                
             ::   ::   :   ( )   :   ::   ::                   
             ':.  ':   ':. /_\ .:'   :'  ,:'                  
              ':.  ':.    /___\    .:'  ,:'                  
               ':.       /_____\      .:'                    
                        /       \
   ____      _               ____                         
  / ___|   _| |__   ___ _ __|  _ \ __ _ _ __   __ _  ___  
 | |  | | | | '_ \ / _ \ '__| |_) / _` | '_ \ / _` |/ _ \ 
 | |__| |_| | |_) |  __/ |  |  _ < (_| | | | | (_| |  __/ 
  \____\__, |_.__/ \___|_|  |_| \_\__,_|_| |_|\__, |\___| 
  ____ |___/   ___                            |___/       
 |  _ \|  _ \ / _ \                                       
 | |_) | |_) | | | |                                      
 |  __/|  _ <| |_| |                                      
 |_|   |_| \_\\___/

╔══════════════════════════════════════════════╗
║        DICTIONARY/BRUTE FORCE PENTEST        ║
╚══════════════════════════════════════════════╝

[1] Ataque padrão (2 segundos)
[2] Ataque rápido (2 segundos)
[3] Ataque RÁPIDO de 10 segundos
[4] Ataque LENTO de 10 segundos
[0] Sair
""")
        
        escolha = input("\nEscolha: ")
        
        if escolha == "0":
            print("Saindo...")
            time.sleep(1)
            limpar_tela()
            break
        elif escolha in opcoes:
            nome, duracao, velocidade = opcoes[escolha]
            executar_ataque(duracao, velocidade)
        else:
            print("Opção inválida")
            time.sleep(1)

if __name__ == "__main__":
    menu()