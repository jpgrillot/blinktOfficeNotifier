# blinktOfficeNotifier
Pi powered Home Office notification application with Pimoroni Blinkt

Make an Office notification system using a Pi Zero W and a Pimoroni Blinkt LED strip. 

## Installing
This install was meant for a Pi Zero W on Raspian with no desktop environment. This assumes that the Pi already has the OS installed and configured. 

1. Install the dependencies
    1. Install Python3 Blinkt Library ```bash sudo apt install python3-blinkt ```
    1. Install Flask ```bash sudo pip3 install flask ```
1. Create a Crontab job
1. Add this line to the end of the file, set the path to where you downloaded the Python app @reboot python3 /home/pi/Github/blinktOfficeNotifier
1. Save and Exit
1. By default, the app will run on the 5000 port of the Pi. http://yourpi.lan:5000


