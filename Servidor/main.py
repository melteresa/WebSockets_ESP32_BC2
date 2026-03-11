import tkinter as tk
from tkinter import ttk
import socket
import threading

# --- CONFIGURACIÓN ---
IP_ESP32 = "192.168.1.XX" 
PUERTO = 80

# --- CLASE DE DATOS ---
class DatosSensor:
    def __init__(self, valor):
        self.valor = valor

# --- LÓGICA DE RED ---
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conectar():
    try:
        sock.connect((IP_ESP32, PUERTO))
        print("Conectado al ESP32")
        threading.Thread(target=recibir_datos, daemon=True).start()
    except Exception as e:
        print("Error al conectar:", e)

def recibir_datos():
    # Convertimos el flujo de red en un formato de lectura por líneas
    archivo_red = sock.makefile('r')
    while True:
        try:
            # Lee exactamente hasta el salto de línea (\n)
            linea = archivo_red.readline()
            if not linea: 
                break # Si está vacío, se desconectó
            
            # Limpiamos espacios y procesamos
            valor_limpio = linea.strip()
            if valor_limpio:
                sensor = DatosSensor(int(valor_limpio))
                # Actualizar la interfaz
                progress['value'] = sensor.valor
                lbl_valor.config(text=f"Potenciómetro: {sensor.valor}")
                
        except ValueError:
            # Si llega basura ocasional, la ignoramos y el ciclo continúa
            pass
        except Exception as e:
            print("Desconectado del servidor:", e)
            break

# Agregamos manejo de errores al enviar para evitar que la app colapse si se cae la red
def led_on(): 
    try: sock.send(b'ON')
    except: print("Error enviando ON")

def led_off(): 
    try: sock.send(b'OFF')
    except: print("Error enviando OFF")

# --- INTERFAZ GRÁFICA ---
root = tk.Tk()
root.title("Control ESP32 - Instituto Cordillera")

tk.Label(root, text="CONTROL DE DISPOSITIVO", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

lbl_valor = tk.Label(root, text="Potenciómetro: 0")
lbl_valor.grid(row=1, column=0, columnspan=2)

progress = ttk.Progressbar(root, length=200, maximum=4095)
progress.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

tk.Button(root, text="Encender LED", command=led_on, bg="green", fg="white").grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Apagar LED", command=led_off, bg="red", fg="white").grid(row=3, column=1, padx=10, pady=10)

threading.Thread(target=conectar, daemon=True).start()

root.mainloop()