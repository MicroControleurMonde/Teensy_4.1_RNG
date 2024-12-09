# Teensy 4.1 RNG

**Date :** 09.12.2024

##### Under construction ...

![Image locale](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/NXP.jpg)
![Image locale](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/PJRC.logo.jpg)

A method for generating random numbers on a Teensy 4.1 using multiple analog inputs (_**BEWARE Not using the MCU TRNG**_)

### Context:
    I created a random number generator on Teensy (i.MX RT1062) while knowing that the MCU had its own 
    hardware TRNG. Unlike the ESP32 chip where the TRNG was relatively simple to implement in micropython, 
    on the RT1062 it is another matter. The NXP documentation does not help and the C source code of the
    RNG provided in the SDK is tearing your hair out !
    So, for the moment a more simplistic approach is preferable...

    For information: Actually, the C code itself is quite simple and straightforward. 
    However, the calls to the include file are a hellish machine. it is all about working on the multiple 
    registers of the MCU. Like a big piston-driven machine. It's real brain surgery ...

## Breakdown of Sections

1. Project Description
2. Features
3. Requirements
4. Usage
5. How it Works
6. Performance and output
7. Ent Tests
8. Diehard Test for Validation
9. Acknowledgements
10. Disclaimer

## 1. Project Description

- This script is a method to generate good quality random numbers on a **Teensy 4.1** using several analog pins and a **Fisher-Yates mixing algorithm** to improve entropy. 
- It combines the readings of several ADC inputs (analog-to-digital converters) in order to reduce the systematic noise and generate a random number of 32 bits. 
- This process is used to obtain a robust and difficult to predict random number.

## 2. Features

- **Generation of 32-bit random numbers:** By combining the readings of several analog pins.
- **Improved entropy:** Using a Fisher-Yates mixture to rearrange the pins and XOR operations to reduce bias.
- **Systematic noise reduction:** By performing several ADC readings and combining the samples using XORs and bit offsets.
- **Teensy 4.1 Compatibility:** Uses the analog pins available on the board to obtain noise samples.


## 3. Requirements

- **Microcontroller:** Teensy 4.1
- **Libraries :** 
  - `machine` (to access the ADC pins and the pins)
  - `random` (for random number generation functions)
  - `time` (for timing between generations)
- **MicroPython v1.24.0** (or a compatible environment to run the script)
  
## 4. Usage

41. **Connect the Teensy 4.1** to your computer.
42. **Download and install the script** on your Teensy using the IDE of your choice.
43. **Run the script**: The program will generate a series of 32-bit random numbers by reading the analog pins and processing the samples to obtain high-quality random numbers.
44. **Result Display:** The script will display 10 random numbers in the console.

## 5. How it Works

The script uses the following steps:

51. **Reading the analog pins:** The script uses the analog pins from A0 to A10 of the Teensy to capture noise samples.
52. **Fisher-Yates Mixing:** A mixing algorithm is applied to the pins to mix their order randomly, thus increasing the entropy of the samples.
53. **Multiple sampling:** Each analog pin is read several times (3 times for example) to reduce bias and noise.
54. **Combining samples:** Samples are combined using XOR operations and bit shifts to maximize the randomness of the results.
55. **Additional mixing of bits:** Additional mixing of bits is performed to improve the quality of the random number.
56. **Generation of the final number:** The final number is obtained by limiting the bits to 32 to obtain a random number.

**Customization:** 

In the function ***'def generate_random_number()`***, you can cahne the number of pins as desired from 2 to 10 to "_spice up the cooking recipe_". Up to you !

## 6. Performance and output

### Performance

The script produces random numbers that are uniformly distributed in the 32-bit range. The tests carried out show a rapid generation of random numbers, with improved quality thanks to multiple sampling and mixing operations. The generated values will be displayed in the console with a delay of 0.1 seconds between each generation.

Generating **681'000** random numbers (32 bits) and saving them.

- **Elapsed time**: 295.71 seconds (about 4 minutes and 55 seconds).

- **Random number generation rate**: 1.04 bytes per second.

- **Number** of random numbers generated **per second** ≈ 5'307

  The performance of the random number generator is generally good, but it may depend on the number of samples taken and the number of pins used.

  By increasing the number of pins or samples, the quality of the random number will be improved, but this may increase the latency.

### Output:
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

## 7. Ent Tests

Ent sources (www.fourmilab.ch/random/)

- Sample size: **7,1 MB**

- Total generated: **681'000 values**

[Ent Report - Raw](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/Ent_Teensy_681'000.txt)

[Ent Report Analyse](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/Ent_Teensy_681'000.md)

## 8. Diehard Test for Validation
(https://webhome.phy.duke.edu/~rgb/General/dieharder.php) Robert G. Brown

- Sample size: **7,1 MB**

- Total generated: **681'000 values**

[Diehard Report - Raw](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/Dieharder_Teensy_681'000.txt)

[Diehard Report - Analyse](https://github.com/MicroControleurMonde/Teensy_4.1_RNG/blob/main/Reports/Dieharder_Teensy_681'000.md)


## 9. Acknowledgements

The project is based on the i/MX RT1062 MCU, and its MicroPython firmware.

Tested on an original **Teensy 4.1**. [pjrc](https://www.pjrc.com/store/teensy41.html)

MicroPython v1.24.0 on 2024-10-25; Teensy 4.1 with MIMXRT1062DVJ6A

## 10. Disclaimer

The code contained in this repository is provided “as is”, without any warranty of performance, accuracy or result. The author shall not be liable for any direct or indirect damages that may result from the use of this code, including, but not limited to, loss of data or interruption of service.

Use of this code is entirely at your own risk. Please ensure that you fully understand the code before using it in a production environment or integrating it into your projects.

