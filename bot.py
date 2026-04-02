import pyautogui
import time

print("="*60)
print("🤖 BOT WHATSAPP - ENVIO EM MASSA")
print("="*60)

# Configurações iniciais
MENSAGEM_PADRAO = "tu é beta com zero de testo"

print("\n📌 INSTRUÇÕES:")
print("1. Abra web.whatsapp.com")
print("2. Escaneie o QR Code")
print("3. Deixe a conversa ABERTA")
print("="*60)

input("\n✅ Pronto? Pressione ENTER...")

print("\n👉 Clique dentro da caixa de mensagem")
time.sleep(3)
pos = pyautogui.position()
print("✅ Posição salva!")

# Opção de escolher a mensagem
print("\n" + "="*60)
print("OPÇÕES DE MENSAGEM:")
print("2 - Digitar uma mensagem")
print("3 - Digitar mensagem personalizada para cada envio")
opcao_msg = input("\nEscolha (2 ou 3): ")

# Definir a mensagem baseada na opção
mensagem_base = ""
modo_personalizado = False
    
if opcao_msg == "2":
    mensagem_base = input("\n✏️ Digite a mensagem que será enviada: ")
    print(f"\n✅ Mensagem definida: '{mensagem_base}'")
    
elif opcao_msg == "3":
    modo_personalizado = True
    print("\n✅ Modo personalizado ativado!")
    print("   O programa vai pedir a mensagem antes de cada envio")
    
else:
    print("\n❌ Opção inválida! Usando mensagem padrão.")
    mensagem_base = "tu é beta com zero de testo"

# Configurações de envio
print("\n" + "="*60)
vezes = int(input("📊 Quantas mensagens enviar? (ex: 100): "))
intervalo = float(input("⏱️  Intervalo entre mensagens (segundos, 0 para sem intervalo): "))

print(f"\n🚀 Preparando para enviar {vezes} mensagens...")
print("⚠️ NÃO mexa no mouse durante o envio!")
print("⚠️ Para cancelar: pressione CTRL + C")
time.sleep(3)

# Função para enviar mensagem
def enviar_mensagem(texto):
    """Envia uma mensagem"""
    pyautogui.click(pos.x, pos.y)
    time.sleep(0.2)
    pyautogui.write(texto)
    time.sleep(0.2)
    pyautogui.press('enter')

# Envio das mensagens
print("\n" + "="*60)
print("🎯 INICIANDO ENVIO...")
print("="*60)

try:
    for i in range(vezes):
        # Definir qual mensagem enviar
        if modo_personalizado:
            print(f"\n📝 Mensagem {i+1}/{vezes}")
            mensagem_atual = input("Digite a mensagem (ou ENTER para repetir a última): ")
            if mensagem_atual.strip() == "" and 'ultima_mensagem' in locals():
                mensagem_atual = ultima_mensagem
            elif mensagem_atual.strip() == "":
                mensagem_atual = "tu é beta com zero de testo"
            ultima_mensagem = mensagem_atual
        else:
            mensagem_atual = mensagem_base
        
        # Enviar a mensagem
        enviar_mensagem(mensagem_atual)
        
        # Mostrar progresso
        print(f"✅ {i+1}/{vezes} - Enviado: {mensagem_atual[:50]}{'...' if len(mensagem_atual) > 50 else ''}")
        
        # Aguardar intervalo (exceto após a última mensagem)
        if intervalo > 0 and i < vezes - 1:
            time.sleep(intervalo)
    
    print("\n" + "="*60)
    print(f"🎉 COMPLETO! {vezes} mensagens enviadas com sucesso!")
    print("="*60)
    
except KeyboardInterrupt:
    print("\n\n⚠️ ENVIO INTERROMPIDO PELO USUÁRIO!")
    print(f"📊 Mensagens enviadas: {i+1}/{vezes}")
    
except Exception as e:
    print(f"\n❌ Erro inesperado: {e}")
