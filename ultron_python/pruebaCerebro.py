import os
from google import genai

# 1. Recuperar nuestra credencial de Lagan
api_key = os.environ.get("LAGAN_API_KEY")

if not api_key:
    raise ValueError("Error de Seguridad: No se encontró la variable LAGAN_API_KEY.")

# 2. Inicializar el Cliente
cliente = genai.Client(api_key=api_key)

print("Iniciando conexión con el cerebro de Ultron...")

# 3. Crear una sesión de Chat (Interactions API) con el modelo actualizado
# Esto prepara un canal de comunicación continuo en lugar de un disparo único
chat = cliente.chats.create(model='gemini-3.6-flash')

# 4. Enviar el mensaje dentro de esa sesión
print("Enviando señal...")
respuesta = chat.send_message('Hola. Responde únicamente con la palabra: "Conectado".')

# 5. Mostrar la respuesta limpia
print(f"Respuesta del modelo: {respuesta.text.strip()}")