## Test Results from Ent

### Distribution of Values and Occurrences
The test provides a breakdown of the values (from 0 to 9) in the file `Teensy_681'000.txt`. Below are the detailed results:

| **Value** | **Character** | **Occurrences** | **Fraction** |
|-----------|---------------|-----------------|--------------|
| 10        | (space)       | 681,000         | 9.54%        |
| 48        | 0             | 625,333         | 8.76%        |
| 49        | 1             | 660,210         | 9.25%        |
| 50        | 2             | 693,927         | 9.72%        |
| 51        | 3             | 800,337         | 11.21%       |
| 52        | 4             | 700,009         | 9.81%        |
| 53        | 5             | 592,395         | 8.30%        |
| 54        | 6             | 577,430         | 8.09%        |
| 55        | 7             | 571,586         | 8.01%        |
| 56        | 8             | 619,935         | 8.68%        |
| 57        | 9             | 616,740         | 8.64%        |

**Total occurrences**: 7,138,902  
**Total fraction**: 1.000000

### Entropy
- **Entropy**: 3.452534 bits per byte  
  Entropy measures the level of disorder or "randomization" in the data.  
  The optimal entropy for perfectly random data is 8 bits per byte.  
  Here, the entropy is 3.45 bits per byte, indicating that the data is not completely random but shows a certain degree of organization.

### Optimal Compression
- **Estimated optimal compression**: 56%  
  An effective compression algorithm could potentially reduce the file size by 56%. 
  This implies that the data contains identifiable patterns.

### Chi-Square Test
- **Chi-Square Distribution**: 160,632,211.37  
- **Probability of exceeding this value by chance**: less than 0.01%  
  The chi-square test is used to measure the "normality" or dispersion of data compared to an expected distribution.  
  The extremely low probability that this value would occur by chance suggests that the data is not random.

### Arithmetic Mean
- **Mean value of the bytes**: 48.3234  
  A value close to 127.5 would indicate truly random data.  
  Here, the mean is much closer to 48, suggesting that the data is not uniformly distributed across the entire range of possible values.

### Monte Carlo Pi Estimation
- **Pi Estimation**: 4.000000000  
- **Error**: 27.32%  
  The Monte Carlo test is a method for estimating mathematical constants (like Pi) using random simulations.  
  The Pi estimate of 4 indicates that the values generated likely do not follow a uniform distribution.  
  The error of 27.32% shows the imprecision of the calculations based on these data.

### Serial Correlation Coefficient
- **Serial correlation coefficient**: -0.095991  
  This coefficient measures the dependence between consecutive bytes in the file.  
  A value close to 0 suggests no correlation (i.e., each byte is independent of the previous one).  
  The value of -0.095991 indicates weak correlation between consecutive bytes, suggesting that the data is relatively independent from one byte to the next.

## Conclusion

- **Entropy**: Entropy: 3.45 bits per byte. It is low compared to perfect randomness – data is not fully random.
- **Compression**: The file can be reduced by 56% in size – patterns or structures in the data.
- **Statistical tests**: The chi-square and Monte Carlo tests show that the data deviates from perfect randomization – non-random organization.
- **Byte dependence**: A low serial correlation coefficient indicates a certain degree of independence between bytes.

The data in `Teensy_681'000.txt` displays characteristics that are similar to randomly generated data, but they are not completely random.  
They show detectable patterns.

---