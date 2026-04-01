import pyautogui
import time

print("="*60)
print("🤖 BOT WHATSAPP - ENVIO EM MASSA")
print("="*60)

MENSAGEM = "tu é beta com zero de testo"

print("\n📌 INSTRUÇÕES:")
print("1. Abra web.whatsapp.com")
print("2. Escaneie o QR Code")
print("3. Abra a conversa 'roth zero testo'")
print("4. Deixe a conversa ABERTA")
print("="*60)

input("\n✅ Pronto? Pressione ENTER...")

print("\n👉 Clique dentro da caixa de mensagem")
time.sleep(3)
pos = pyautogui.position()
print("✅ Posição salva!")

# Configurações
vezes = int(input("\nQuantas mensagens enviar? (ex: 100): "))
intervalo = float(input("Intervalo entre mensagens (segundos, 0 para sem intervalo): "))

print(f"\n🚀 Enviando {vezes} mensagens...")
print("⚠️ NÃO mexa no mouse!")
time.sleep(2)

for i in range(vezes):
    pyautogui.click(pos.x, pos.y)
    time.sleep(0.2)
    pyautogui.write(MENSAGEM)
    time.sleep(0.2)
    pyautogui.press('enter')
    
    print(f"✅ {i+1}/{vezes} - Mensagem enviada")
    
    if intervalo > 0 and i < vezes - 1:
        time.sleep(intervalo)

print(f"\n🎉 COMPLETO! {vezes} mensagens enviadas!")