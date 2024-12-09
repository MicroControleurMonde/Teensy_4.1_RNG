'''
	This script demonstrates a method for generating high-quality random numbers on a Teensy 4.1
	using multiple analog pins and a Fisher-Yates shuffle algorithm to improve entropy.
	It combines multiple ADC readings to reduce systematic noise and generate a 32-bit random number.
	Author: [MicroControleurMonde]
	File name: Teensy_RNG_Demo.py
	Date: 08.12.2024
'''
import random
from machine import ADC, Pin
import time

# List of available analog pins on Teensy 4.1 (A0 to A10)
analog_pins = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']

# Create ADC objects for each pin
adcs = {pin: ADC(Pin(pin)) for pin in analog_pins}

def fisher_yates_shuffle(lst):
    """
    Perform Fisher-Yates shuffle on the list to randomize the order of elements.
    """
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

def generate_random_number():
    """
    Generate a 32-bit random number by sampling multiple analog pins and combining 
    the ADC readings using bitwise operations to improve entropy.
    The function shuffles the analog pin list, reads multiple samples from the selected pins, 
    and combines them using XOR and bit shifting to enhance randomness.
    Returns:
        int: A 32-bit random number.
    """
    # Shuffle the list of pins to randomly select which pins to use
    fisher_yates_shuffle(analog_pins)
    
    random_bits = 0

    # Read multiple pins to increase entropy
    for pin in analog_pins[:6]:  # Select more pins for higher entropy (Customization)
        adc = adcs[pin]
        
        # Take multiple samples from the ADC and combine them with XOR to reduce systematic noise
        sample = adc.read_u16() ^ adc.read_u16() ^ adc.read_u16()
        
        # Shift the bits and add the new ones
        random_bits = (random_bits << 8) | (sample >> 8)  # Use the 8 most significant bits
    
    # Apply an additional XOR operation to further mix the bits
    random_bits = random_bits ^ (random_bits >> 16)  # Mix with the upper bits
    
    return random_bits & 0xFFFFFFFF  # Limit to 32 bits

# Generate and display 10 random 32-bit numbers
for i in range(10):
    try:
        random_number = generate_random_number()
        print(f"Random number (32-bit): {random_number}")  # Display in decimal
        time.sleep(0.1)  # Wait a bit before generating another number
    except Exception as e:
        print(f"Error occurred: {e}")
        break  # Stop the program if an error occurs to avoid infinite restarts

