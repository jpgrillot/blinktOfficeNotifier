# blinktOfficeNotifier
Pi powered Home Office notification application with Pimoroni Blinkt

![PiMoroni Blinkt](https://github.com/jpgrillot/blinktOfficeNotifier/blob/main/BlinktCoupe.jpg)

Make an Office notification system using a Pi Zero W and a Pimoroni Blinkt LED strip.
This app has a web interface where y ou can connect to the Pi from your phone/tablet/computer on the same network

![App Page](https://github.com/jpgrillot/blinktOfficeNotifier/blob/main/WebPage.jpg)

Selecting a button will set the LEDs to the same color

![Illuminated](https://github.com/jpgrillot/blinktOfficeNotifier/blob/main/VideoConf.jpg)

## Installing
This install was meant for a Pi Zero W on Raspian with no desktop environment. This assumes that the Pi already has the OS installed and configured. Git, Python3, and Python3-Pip should be installed.

1. Clone this repo to the Raspberry Pi ``` git clone https://github.com/jpgrillot/blinktOfficeNotifier.git ```
1. Install the dependencies
    1. Install Python3 Blinkt Library ``` sudo apt install python3-blinkt ```
    1. Install Flask ``` sudo pip3 install flask ```
1. Create a Crontab job ``` sudo crontab -e ```
1. If prompted for an editor, select the first (nano)
1. Add this line to the end of the file, set the path to where you downloaded the Python app ``` @reboot python3 /home/pi/Github/blinktOfficeNotifier/app.py ```
1. Save and Exit ``` CTRL + X, hit Y, and enter to accept the default```
1. By default, the app will run on the 5000 port of the Pi. http://yourpi.lan:5000


