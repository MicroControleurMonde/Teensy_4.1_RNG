# Teensy 4.1 RNG
##### Under construction...

![Image locale](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/NXP.jpg)
![Image locale](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/PJRC.logo.jpg)
A method for generating random numbers on a Teensy 4.1 using multiple analog inputs (Not using the MCU TRNG)

### Contexte:
    I created a random number generator on Teensy (i.MX RT1062) while knowing that the MCU 
    had its own TRNG. Unlike the ESP32 chip where the TRNG was relatively simple to implement 
    in micropython, on the RT1062 it is another matter. The NXP documentation does not help 
    and the C source code of the RNG provided in the SDK is tearing your hair out !
    So, for the moment a more simplistic approach is preferable...

### Output:

    Random number (32-bit): 3323335684
    Random number (32-bit): 959659273
    Random number (32-bit): 254149946
    Random number (32-bit): 4161521706
    Random number (32-bit): 908136471
    Random number (32-bit): 536800498
    Random number (32-bit): 264766982
    Random number (32-bit): 891231253
    Random number (32-bit): 3876569099
    Random number (32-bit): 3778418214
