from plyer import notification
import requests
def notifyme(title, message):
    notification.notify(
        title=title, 
        message=message,
        timeout=3
    )
def getdata(url):
    a=requests.get(url)
    return a.text

notifyme("instagram", "Hello how are you")
