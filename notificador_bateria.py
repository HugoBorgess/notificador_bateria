# pip install psutil
import psutil

bateria = psutil.sensors_battery()
conectado = bateria.power_plugged
percentual = bateria.percent

if percentual >= 30:

    # pip install py-notifier
    # pip install win10toast
    from pynotifier import Notification

    Notification(
        title="Bateria Fraca",
        description=str(percentual) + "% de bateria restante!",
        duration=5,  # Duração em segundos
        urgency=Notification.URGENCY_CRITICAL,
    ).send()
