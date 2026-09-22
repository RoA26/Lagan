# Arquitectura de Lagan

## 1. Identidad del proyecto

### Lagan

Lagan es el ecosistema tecnológico que contiene la infraestructura, los sistemas y los componentes necesarios para construir y operar a Ultron.

Lagan no es la inteligencia artificial en sí misma. Es el sistema que permite que Ultron exista, evolucione y se conecte con otros componentes.

### Ultron

Ultron es el agente de Inteligencia Artificial que se desarrolla dentro del ecosistema Lagan.

Su objetivo inicial es comprender entradas de texto, procesarlas y responder mediante una arquitectura modular.

A medida que el proyecto avance, Ultron podrá incorporar memoria, herramientas, percepción, voz y comunicación con otros sistemas.

### Principio fundamental

Lagan y Ultron se desarrollarán de forma incremental.

Cada componente debe ser comprendido, probado y documentado antes de convertirse en una dependencia de otros componentes.

## 2. Componentes del sistema (V1 - Fase Inicial)

Para garantizar un crecimiento progresivo y comprensible, la primera versión de Ultron operará exclusivamente en texto. El objetivo de la V1 es establecer el flujo básico de comunicación sin introducir dependencias complejas.

Los componentes de esta fase inicial son:

* **Interfaz (Entrada/Salida):** Un ciclo de ejecución en la terminal. Actúa como el punto de contacto básico, capturando el texto del usuario (`input`) y mostrando las respuestas del agente (`print`).
* **Memoria de Trabajo (Contexto Temporal):** Una estructura de datos en RAM (como una lista) que almacena el historial de la conversación activa. Dado que los modelos de lenguaje no tienen memoria intrínseca, Ultron debe inyectar este contexto en cada interacción para mantener el hilo de la charla.
* **Cerebro (Procesamiento/Decisión):** El módulo que conecta el sistema con un LLM (Large Language Model) a través de una API. El agente Ultron no *es* el LLM, sino que lo orquesta; utiliza el modelo exclusivamente como su motor de razonamiento y generación de lenguaje.

### Flujo de ejecución V1

1. La **Interfaz** recibe un mensaje del usuario.
2. El sistema añade este mensaje a la **Memoria de Trabajo**.
3. El **Cerebro** toma el historial completo y lo envía al LLM.
4. El LLM devuelve una respuesta.
5. El sistema registra la respuesta en la **Memoria de Trabajo** y la **Interfaz** la muestra en pantalla.## 2. Componentes del sistema (V1 - Fase Inicial)

Para garantizar un crecimiento progresivo y comprensible, la primera versión de Ultron operará exclusivamente en texto. El objetivo de la V1 es establecer el flujo básico de comunicación sin introducir dependencias complejas.

Los componentes de esta fase inicial son:

* **Interfaz (Entrada/Salida):** Un ciclo de ejecución en la terminal. Actúa como el punto de contacto básico, capturando el texto del usuario (`input`) y mostrando las respuestas del agente (`print`).
* **Memoria de Trabajo (Contexto Temporal):** Una estructura de datos en RAM (como una lista) que almacena el historial de la conversación activa. Dado que los modelos de lenguaje no tienen memoria intrínseca, Ultron debe inyectar este contexto en cada interacción para mantener el hilo de la charla.
* **Cerebro (Procesamiento/Decisión):** El módulo que conecta el sistema con un LLM (Large Language Model) a través de una API. El agente Ultron no *es* el LLM, sino que lo orquesta; utiliza el modelo exclusivamente como su motor de razonamiento y generación de lenguaje.

### Flujo de ejecución V1

1. La **Interfaz** recibe un mensaje del usuario.
2. El sistema añade este mensaje a la **Memoria de Trabajo**.
3. El **Cerebro** toma el historial completo y lo envía al LLM.
4. El LLM devuelve una respuesta.
5. El sistema registra la respuesta en la **Memoria de Trabajo** y la **Interfaz** la muestra en pantalla.