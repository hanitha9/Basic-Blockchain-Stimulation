# Basic Blockchain Simulation in Python

This project implements a simple blockchain simulation in Python. It includes block creation, Proof-of-Work mining, and chain validation. Additionally, it demonstrates how blockchain prevents tampering by validating the chain integrity.

## Features
- Implements a basic blockchain structure with blocks and transactions.
- Uses SHA-256 hashing for security.
- Includes a Proof-of-Work mechanism with adjustable difficulty.
- Allows dynamic addition of new blocks.
- Provides a function to verify chain integrity.
- Demonstrates tampering detection.

## Prerequisites
- Python 3.x

## Installation
No additional libraries are required. Ensure you have Python installed and run the script directly.

## Usage
1. Clone or download the repository.
2. Run the Python script:
   ```sh
   python basic_stimulation.py
   ```
3. Enter transactions when prompted.
4. The program will mine blocks and print the blockchain state.
5. The integrity of the blockchain will be verified before and after tampering.

## Example Output
```
Genesis block created!

Preparing Block #1
Enter transactions: Alice sends 10 BTC to Bob, Charlie sends 5 BTC to Dave
Block #1 added to the chain!

Preparing Block #2
Enter transactions: Eve sends 2 BTC to Frank
Block #2 added to the chain!

Current Blockchain State:
...

Is chain valid? True

Tampering with Block 1...

Is chain valid after tampering? False
```
## Final Output:

   ![Screenshot 2025-03-26 002047](https://github.com/user-attachments/assets/f01baa51-9fc7-47f1-b26f-c4d255fac0db)

   ![Screenshot 2025-03-26 002106](https://github.com/user-attachments/assets/12d1afff-85b4-4179-9dfe-f17d49dab336)

   ![Screenshot 2025-03-26 002115](https://github.com/user-attachments/assets/02f2fbfb-0b43-47b2-8ce9-944fd2e88f69)



## File Structure
- `basic_stimulation.py`: The main Python script containing the blockchain logic.

## Author
Developed as a basic blockchain simulation for learning purposes.

## License
This project is open-source and free to use for educational purposes.

