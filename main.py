from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "DRINK WATER",  # Title of the Notification
            message = "Hey friend, It's time to drink water",   # Message of the Notification
            app_icon = 'Drink-Water-Notification/index.ico',  # Icon to be displayed along with the message
            timeout = 10  #notification remains on screen for 10 seconds
        )

        time.sleep(120*60)  # every 2 hours send the notification
 #icon must be .ico file       
