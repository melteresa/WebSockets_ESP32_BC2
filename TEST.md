# Cuestionario de Evaluación: Comunicación por Sockets 📝

**Nombre del Estudiante:**  Melany Terán
**Fecha:** 11/03/2026

*Instrucciones: Responde a las siguientes preguntas basándote en la teoría de redes y en el análisis del código de nuestro proyecto. Sube este archivo con tus respuestas a tu repositorio como evidencia de trabajo.*

1. **¿Qué es una Dirección IP y para qué sirve en nuestro proyecto?**
   > *La Dirección IP identifica al dispositivo en la red y permite saber a qué equipo debemos conectarnos para consumir su servicio.*

2. **¿Qué es un Puerto de red? (Menciona qué puerto estamos usando en el código de la ESP32).**
   > *El puerto indica a qué servicio del dispositivo queremos conectarnos, y en este proyecto usamos el puerto 80 para la comunicación entre la PC y el ESP32.*

3. **Define con tus propias palabras qué es un Servidor en informática.**
   > *Un servidor es una unidad informática que proporciona diversos servicios a computadoras conectadas a ella a través de una red, respondiendo a las solicitudes que estas le envían.*

4. **¿Cuál es la diferencia entre un "Servidor" (Hardware/Software) y un "Servicio" (Service)?**
   > *Servidor:
      Es el equipo o programa que está preparado para recibir conexiones de otros dispositivos en la red y responder a sus solicitudes (quien sirve).
      Servicio:
      Es la función o recurso específico que el servidor ofrece a los clientes que se conectan (lo que sirve).*

5. **Investigación: ¿Cuál es la diferencia técnica entre un "Socket TCP" normal y un "WebSocket"?**
   > *Un Socket TCP es una conexión básica para transmitir datos entre dispositivos en una red, mientras que un WebSocket es un protocolo basado en TCP que permite comunicación bidireccional en tiempo real entre cliente y servidor.*

6. **Analizando nuestro código: ¿Quién actúa como Servidor y quién actúa como Cliente? (Justifica tu respuesta mencionando qué funciones del código lo demuestran, ej. `bind()`, `connect()`).**
   > *ESP32: Servidor.
      Porque espera conexiones y atiende solicitudes de la PC. Se demuestra en funciones como: *

7. **En el código de la computadora (Python), importamos la librería `threading` (Hilos). ¿Qué pasaría con la ventana de Tkinter si no usáramos hilos para recibir los datos de la red?**
   > *Tu respuesta aquí*

8. **¿Por qué es necesario usar bloques `try...except` cuando trabajamos con conexiones de red e Internet?**
   > *Tu respuesta aquí*

9. **En la función de encender el LED en Python, enviamos el comando así: `sock.send(b'ON')`. ¿Qué significa esa letra `b` antes de las comillas y por qué no enviamos un texto normal?**
   > *Tu respuesta aquí*

10. **Describe brevemente el flujo de datos: ¿Qué camino recorre la información desde que giras el potenciómetro físicamente hasta que la barra se mueve en la pantalla de la computadora?**
    > *Tu respuesta aquí*
