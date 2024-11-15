import random
import string
import time
import RPi.GPIO as GPIO
from Adafruit_SSD1306 import SSD1306_128_32
from PIL import Image, ImageDraw, ImageFont

# GPIO setup
BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Display setup
display = SSD1306_128_32(rst=None)
display.begin()
display.clear()
display.display()

# Font setup
font = ImageFont.load_default()

# Easy password generator
def generate_easy_password(length=8):
    characters = string.ascii_letters  # Only letters (uppercase + lowercase)
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Strong password generator
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Display message on the screen
def display_message(message):
    image = Image.new('1', (display.width, display.height))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), message, font=font, fill=255)
    display.image(image)
    display.display()

# Main function
try:
    while True:
        display_message("Press button:\n1: Easy\n2: Strong")
        time.sleep(0.5)

        # Wait for button press
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == GPIO.LOW:
            time.sleep(0.2)  # Debounce delay

            # Ask user for password type
            choice = input("Enter 'easy' for easy password or 'strong' for strong password: ").lower()

            if choice == 'easy':
                password = generate_easy_password()
                display_message(f"Easy Password:\n{password}")
                print(f"Generated Easy Password: {password}")

            elif choice == 'strong':
                password = generate_strong_password()
                display_message(f"Strong Password:\n{password}")
                print(f"Generated Strong Password: {password}")

            else:
                display_message("Invalid Choice")
                print("Invalid choice! Please enter 'easy' or 'strong'.")

            time.sleep(2)  # Wait before next action

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.cleanup()
    display.clear()
    display.display()
