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

## Breakdown of Sections

## Project Description

## Features

## Requirements

## Usage

## How it Works

## Performance and output

#### Performance:
Generating 681'000 random numbers (32 bits) and saving them.

- **Elapsed time**: 295.71 seconds (about 4 minutes and 55 seconds).

- **Random number generation rate**: 1.04 bytes per second.

- **Number** of random numbers generated **per second** ≈ 5'307

#### output:
- The final output is a 32-bit random number that is periodically generated and can be used in applications requiring randomness.
  
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

## Ent Tests

Ent sources (www.fourmilab.ch/random/)

- Sample size: **7,1 MB**

- Total generated: **681'000 values**

[Ent Report - Raw](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/Ent_Teensy_681'000.txt)

[Ent Report Analyse](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/Ent_Teensy_681'000.md)

## Diehard Test for Validation
(https://webhome.phy.duke.edu/~rgb/General/dieharder.php) Robert G. Brown

- Sample size: **7,1 MB**

- Total generated: **681'000 values**

[Diehard Report - Raw](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/Dieharder_Teensy_681'000.txt)

[Diehard Report - Analyse](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/Dieharder_Teensy_681'000.md)


## Acknowledgements

## Disclaimer

The code contained in this repository is provided “as is”, without any warranty of performance, accuracy or result. The author shall not be liable for any direct or indirect damages that may result from the use of this code, including, but not limited to, loss of data or interruption of service.

Use of this code is entirely at your own risk. Please ensure that you fully understand the code before using it in a production environment or integrating it into your projects.

