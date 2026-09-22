import os
import sys
from groq import Groq

class Ultron:
    def __init__(self):
        """Constructor: Se ejecuta al 'nacer' el agente."""
        # 1. Buscamos tu variable agnóstica de Lagan
        self.api_key = os.environ.get("LAGAN_API_KEY")
        if not self.api_key:
            print("Error: No se encontró la variable LAGAN_API_KEY en el sistema.")
            sys.exit(1)
            
        # 2. Instanciamos el cliente de Groq pasándole tu clave de Lagan
        self.cliente = Groq(api_key=self.api_key)
        
        # 3. MEMORIA DE TRABAJO (Construida desde cero sin abstracciones mágicas)
        self.memoria = [
            {"role": "system", "content": "Eres Ultron, el agente de IA del ecosistema Lagan. Tu creador es Roa (Royata). Responde de manera útil, técnica y concisa."}
        ]

    def procesar(self, entrada_texto):
        """CEREBRO: Recibe texto, lo guarda, lo procesa y devuelve texto."""
        try:
            # A. Guardamos lo que dijo el usuario
            self.memoria.append({"role": "user", "content": entrada_texto})
            
            # B. Enviamos TODA la lista de memoria al modelo Llama 3
            respuesta = self.cliente.chat.completions.create(
                messages=self.memoria,
                model="openai/gpt-oss-20b" 
            )
            
            # C. Extraemos el texto
            texto_respuesta = respuesta.choices[0].message.content.strip()
            
            # D. Guardamos la respuesta de Ultron
            self.memoria.append({"role": "assistant", "content": texto_respuesta})
            
            return texto_respuesta
        except Exception as e:
            return f"[Error en procesamiento cognitivo]: {e}"

# ==========================================
# INTERFAZ 
# ==========================================
if __name__ == "__main__":
    print("Iniciando ecosistema Lagan...")
    agente = Ultron() 
    print("Ultron V1 (Cerebro Llama 3.1) en línea. Escribe 'salir' para apagar.\n")
    
    while True:
        try:
            texto_usuario = input("Tú: ")
            
            if texto_usuario.lower().strip() in ['salir', 'exit', 'quit']:
                print("Ultron: Apagando sistemas. Hasta luego, Roa.")
                break
                
            if texto_usuario.strip() == "":
                continue 
                
            respuesta_ultron = agente.procesar(texto_usuario)
            print(f"Ultron: {respuesta_ultron}\n")
            
        except KeyboardInterrupt:
            print("\nUltron: Interrupción forzada. Apagando...")
            break