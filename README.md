# Teensy_4.1_RNG
A method for generating random numbers on a Teensy 4.1 using multiple analog inputs (Not using the MCU TRNG)

### Contexte:
I created a random number generator on Teensy (i.MX RT1062) while knowing that the MCU had its own TRNG.

Unlike the ESP32 chip where the TRNG was relatively simple to implement in micropython, on the RT1062 it is another matter.

The NXP documentation does not help and the C source code of the RNG provided in the SDK is tearing your hair out!
