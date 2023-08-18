# Caesar Cipher Project Documentation

## Introduction

The Caesar Cipher Project is a Python-based tool that allows users to encrypt and decrypt text using the Caesar cipher algorithm. It provides a user-friendly graphical user interface (GUI) for ease of use.

## Features

- Text Encryption: Encrypt input text using a specified shift key.
- Text Decryption: Decrypt input text using a specified shift key.
- File Encryption: Encrypt text content from input files and save the encrypted content to output files.
- File Decryption: Decrypt text content from input files and save the decrypted content to output files.

## How to Use

1. Launch the program by running the `caesar_cipher_gui.py` script.
2. The GUI window will open, providing the following options:

   - Input Text: Enter the text you want to encrypt or decrypt.
   - Shift Key: Set the shift key for encryption or decryption.
   - Encrypt Button: Encrypt the input text using the specified shift key.
   - Decrypt Button: Decrypt the input text using the specified shift key.
   - Open Input File Button: Open an input file to load text for encryption or decryption.
   - Save Output File Button: Save the output text to an output file.

3. Choose the appropriate options, and the GUI will display the results in the output text area.

## Dependencies

- Python (>=3.6)
- tkinter library

## Examples

### Text Encryption

1. Enter the input text in the "Input Text" area.
2. Set the shift key using the "Shift Key" field.
3. Click the "Encrypt" button.
4. The encrypted text will be displayed in the "Output Text" area.

### Text Decryption

1. Enter the encrypted text in the "Input Text" area.
2. Set the shift key using the "Shift Key" field (using the same shift value used for encryption).
3. Click the "Decrypt" button.
4. The decrypted text will be displayed in the "Output Text" area.

### File Encryption

1. Click the "Open Input File" button to select an input file.
2. Set the shift key using the "Shift Key" field.
3. Click the "Encrypt" button.
4. The encrypted text will be displayed in the "Output Text" area.
5. Click the "Save Output File" button to save the encrypted text to an output file.

### File Decryption

1. Click the "Open Input File" button to select an input file containing encrypted text.
2. Set the shift key using the "Shift Key" field (using the same shift value used for encryption).
3. Click the "Decrypt" button.
4. The decrypted text will be displayed in the "Output Text" area.
5. Click the "Save Output File" button to save the decrypted text to an output file.

## License

This project is licensed under the [MIT License](LICENSE).
