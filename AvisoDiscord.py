import requests
from datetime import datetime

# URL del webhook de Discord
WEBHOOK_URL = 'https://discord.com/api/webhooks/1212451665072889937/e6FuoDIfBFIdDRqQqcx-SscBPAOKFZg35Xv7Lw30WzZR0tiIILLxoyJ9z0ClGnR0kRj4'

def send_message(startup=True):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = "arrancado" if startup else "apagado"
    message = f"El sistema operativo ha sido {status} a las {now}"
    data = {"content": message}
    requests.post(WEBHOOK_URL, json=data)

if __name__ == "__main__":
    import sys
    action = sys.argv[1] if len(sys.argv) > 1 else "startup"
    if action == "shutdown":
        send_message(False)
    else:
        send_message()
