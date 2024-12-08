# Dieharder test report

- **File tested**: Teensy_681'000.txt

## Test results
	The sequence of numbers was subjected to several statistical tests to verify its randomness. 
	The tests are divided into categories such as **Diehard**, **STS** and **RGB**.

### PASSED tests:
	The majority of tests, such as **diehard_birthdays** (p-value: 0.6707) and **diehard_bitstream** (p-value: 0.5389), passed with p-values 
	well within the acceptable range (close to 1).

### Tests with ‘WEAK’ evaluation:
- A few tests showed weak results, indicating potential problems:
  - **diehard_oqso** (p-value: 0.9974) and **diehard_3dsphere** (p-value: 0.99997), which are close to 1, but rated as ‘weak’.
  - The **rgb_lagged_sum** shows several failures with p-values close to 1 (e.g. 0.99977, 0.99957), indicating weaknesses in these subsequences.

## Conclusion
The sequence of numbers generated passes the majority of tests, but some tests showed ‘WEAK’ results, 
suggesting slight biases or non-random structures in some parts of the sequence. The sequence remains acceptable for many applications.
Tests that fail or are considered weak require further development of the number generator to ensure better quality.