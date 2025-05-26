import network
import socket
from machine import Pin, PWM
from time import sleep

# Wi-Fi credentials
WIFI_SSID = "HundredAcreWood"
WIFI_PASSWORD = "HeadleyGrange1115!"

# Motor control pins
IN1 = Pin(2, Pin.OUT)  # Motor A direction
IN2 = Pin(3, Pin.OUT)
ENA = PWM(Pin(4))      # Motor A speed (PWM)

IN3 = Pin(5, Pin.OUT)  # Motor B direction
IN4 = Pin(6, Pin.OUT)
ENB = PWM(Pin(7))      # Motor B speed (PWM)

# Set PWM frequency
ENA.freq(1000)
ENB.freq(1000)

# Function to control motor A
def motor_a(direction, speed):
    if direction == "forward":
        IN1.value(1)
        IN2.value(0)
    elif direction == "backward":
        IN1.value(0)
        IN2.value(1)
    elif direction == "test":
        IN1.value(1)
        IN2.value(0)
        sleep(1)
        IN1.value(0)
        IN2.value(0)
    else:  # Stop
        IN1.value(0)
        IN2.value(0)
    ENA.duty_u16(int(speed * 65535 / 100))  # Scale speed (0-100) to PWM range (0-65535)

# Function to control motor B
def motor_b(direction, speed):
    if direction == "forward":
        IN3.value(1)
        IN4.value(0)
    elif direction == "backward":
        IN3.value(0)
        IN4.value(1)
    elif direction == "test":
        IN3.value(1)
        IN4.value(0)
        sleep(1)
        IN3.value(0)
        IN4.value(0)
    else:  # Stop
        IN3.value(0)
        IN4.value(0)
    ENB.duty_u16(int(speed * 65535 / 100))  # Scale speed (0-100) to PWM range (0-65535)

def both(direction, speed):
    if direction == "forward":
        IN1.value(1)
        IN2.value(0)
        IN3.value(1)
        IN4.value(0)
    else:  # Stop
        IN3.value(0)
        IN4.value(0)
        IN1.value(0)
        IN2.value(0)
    ENB.duty_u16(int(speed * 65535 / 100))
# Connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        pass
    print("Connected to Wi-Fi:", wlan.ifconfig())
    return wlan.ifconfig()[0]  # Return IP address



# HTML template for the web interface
html = """<!DOCTYPE html>
<html>
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Mona+Sans:ital,wght@0,200..900;1,200..900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
    <title>Fan Control</title>
    <style>
        .btn {
            border: none;
            background-color: whitesmoke;
            padding: 6px 22px;
            font-size: 16px;
            cursor: pointer;
            display: inline-block;
            border-radius: 50px;
        }

        .success {color: green;}
        .success:hover {background-color: rgb(209, 255, 209);}
        .info {color: dodgerblue;}
        .info:hover {background-color: rgb(132, 193, 255);}
        .warning {color: orange;}
        .warning:hover {background-color: rgb(255, 235, 198);}
        .danger {color: red;}
        .danger:hover {background-color: rgb(255, 198, 198);}
        .default {color: black;}
        .default:hover {background-color: rgb(209, 209, 209);}
        
        body {
            font-family: "Roboto", sans-serif;
            font-weight: 100;
            font-style: normal;
        }

    </style>
</head>
<body>
    <h1>L298N Motor Controller</h1>
    <h2>Fan Left</h2>
    <form action="/" method="GET">
        <button class="btn success" name="motor_a" value="forward">Start</button>
        <button class="btn danger" name="motor_a" value="stop">Stop</button>
        <button class="btn warning" name="motor_a" value="test">Test</button>
    </form>
    <h2>Fan Right</h2>
    <form action="/" method="GET">
        <button class="btn success" name="motor_b" value="forward">Start</button>
        <button class="btn danger" name="motor_b" value="stop">Stop</button>
        <button class="btn warning" name="motor_b" value="test">Test</button>
    </form>
</body>
</html>
"""

# Start a simple web server
def start_web_server():
    motor_a("test",100)
    motor_b("test",100)
    addr = connect_to_wifi()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((addr, 80))
    s.listen(5)
    print("Web server started at http://" + addr)

    while True:
        conn, addr = s.accept()
        print("Client connected from", addr)
        request = conn.recv(1024).decode()
        print("Request:", request)
        
        # Parse HTTP GET request
        motor_a_cmd = None
        motor_b_cmd = None
        speed_a = 50
        speed_b = 50

        if "GET /?" in request:
            params = request.split(" ")[1].split("?")[1].split("&")
            for param in params:
                key, value = param.split("=")
                if key == "motor_a":
                    motor_a_cmd = value
                elif key == "speed_a":
                    speed_a = int(value)
                elif key == "motor_b":
                    motor_b_cmd = value
                elif key == "speed_b":
                    speed_b = int(value)
                elif key == "both":
                    both_cmd = value
                    
                    
        
        # Control Motor A
        if motor_a_cmd:
            speed_a = 100
            motor_a(motor_a_cmd, speed_a)
        
        # Control Motor B
        if motor_b_cmd:
            speed_b = 100
            motor_b(motor_b_cmd, speed_b)

        
        # Respond with the web page
        conn.send("HTTP/1.1 200 OK\n")
        conn.send("Content-Type: text/html\n")
        conn.send("Connection: close\n\n")
        conn.sendall(html)
        conn.close()

# Run the web server
start_web_server()