# Import the tkinter library with an alias 'tk'
import tkinter as tk
# Import the filedialog module from tkinter
from tkinter import filedialog


# Encryption logic function
def encrypt(plain_text, shift):
    encrypted_chars = []

    # Loop through each character in the plain text
    for char in plain_text:
        # Check if the character is alphabetic
        if char.isalpha():
            # Shift the character by the specified amount
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % (ord('z') - ord('a') + 1) + ord('a'))
            # Append the shifted character in uppercase if the original was uppercase, else in lowercase
            encrypted_chars.append(shifted_char.upper() if char.isupper() else shifted_char)
        else:
            # Append non-alphabetic characters unchanged
            encrypted_chars.append(char)
    
    # Join the encrypted characters into a string and return
    return ''.join(encrypted_chars)


# Decryption logic function
def decrypt(encrypted_text, shift):
    decrypted_chars = []

    # Loop through each character in the encrypted text
    for char in encrypted_text:
        # Check if the character is alphabetic
        if char.isalpha():
            # Shift the character back by the specified amount
            shifted_char = chr((ord(char.lower()) - ord('a') - shift) % (ord('z') - ord('a') + 1) + ord('a'))
            # Append the shifted character in uppercase if the original was uppercase, else in lowercase
            decrypted_chars.append(shifted_char.upper() if char.isupper() else shifted_char)
        else:
            # Append non-alphabetic characters unchanged
            decrypted_chars.append(char)
    
    # Join the decrypted characters into a string and return
    return ''.join(decrypted_chars)


# Encryption of a file
def encrypt_file(input_filename, output_filename, shift):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as input_file:
            # Read the plain text from the input file
            plain_text = input_file.read()
            # Encrypt the plain text
            encrypted_text = encrypt(plain_text, shift)
        
        # Open the output file for writing
        with open(output_filename, 'w') as output_file:
            # Write the encrypted text to the output file
            output_file.write(encrypted_text)
        
        # Print a success message
        print(f"Encryption successful. Encrypted text saved to {output_filename}")
    except FileNotFoundError:
        # Print an error message if the input file is not found
        print("Error: Input file not found.")


# Decryption of a file
def decrypt_file(input_filename, output_filename, shift):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as input_file:
            # Read the encrypted text from the input file
            encrypted_text = input_file.read()
            # Decrypt the encrypted text
            decrypted_text = decrypt(encrypted_text, shift)
        
        # Open the output file for writing
        with open(output_filename, 'w') as output_file:
            # Write the decrypted text to the output file
            output_file.write(decrypted_text)
        
        # Print a success message
        print(f"Decryption successful. Decrypted text saved to {output_filename}")
    except FileNotFoundError:
        # Print an error message if the input file is not found
        print("Error: Input file not found.")


# Encryption of input text
def encrypt_text():
    # Get the input text from the text widget
    text = input_text.get("1.0", "end-1c")
    # Get the shift key from the entry widget
    shift = int(shift_entry.get())
    # Encrypt the input text
    encrypted_text = encrypt(text, shift)
    # Delete the current content of the output text widget
    output_text.delete("1.0", "end")
    # Insert the encrypted text into the output text widget
    output_text.insert("1.0", encrypted_text)


# Decryption of input text
def decrypt_text():
    # Get the input text from the text widget
    text = input_text.get("1.0", "end-1c")
    # Get the shift key from the entry widget
    shift = int(shift_entry.get())
    # Decrypt the input text
    decrypted_text = decrypt(text, shift)
    # Delete the current content of the output text widget
    output_text.delete("1.0", "end")
    # Insert the decrypted text into the output text widget
    output_text.insert("1.0", decrypted_text)

# Open an input file and display its content in the input text widget
def open_input_file():
    # Ask the user to select an input file using a file dialog
    input_filename = filedialog.askopenfilename(title="Select Input File")
    # If a file was selected
    if input_filename:
        # Open the selected input file for reading
        with open(input_filename, 'r') as input_file:
            # Delete the current content of the input text widget
            input_text.delete("1.0", "end")
            # Insert the content of the input file into the input text widget
            input_text.insert("1.0", input_file.read())

# Save the content of the output text widget to an output file
def save_output_file():
    # Ask the user to select an output file using a file dialog
    output_filename = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".txt")
    # If an output file was selected
    if output_filename:
        # Open the selected output file for writing
        with open(output_filename, 'w') as output_file:
            # Write the content of the output text widget to the output file
            output_file.write(output_text.get("1.0", "end-1c"))

# GUI Setup
# Create the main window
window = tk.Tk()
# Set the title of the main window
window.title("Caesar Cipher GUI")

# Create a label for input text
input_label = tk.Label(window, text="Input Text:")
# Pack the label into the window
input_label.pack()

# Create a text widget for input text
input_text = tk.Text(window, height=10, width=40)
# Pack the text widget into the window
input_text.pack()

# Create a label for shift key
shift_label = tk.Label(window, text="Shift Key:")
# Pack the label into the window
shift_label.pack()

# Create an entry widget for shift key
shift_entry = tk.Entry(window)
# Pack the entry widget into the window
shift_entry.pack()

# Create a button for encryption with a callback to encrypt_text
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_text)
# Pack the button into the window
encrypt_button.pack()

# Create a button for decryption with a callback to decrypt_text
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text)
# Pack the button into the window
decrypt_button.pack()

# Create a label for output text
output_label = tk.Label(window, text="Output Text:")
# Pack the label into the window
output_label.pack()

# Create a text widget for output text
output_text = tk.Text(window, height=10, width=40)
# Pack the text widget into the window
output_text.pack()

# Create a button to open an input file with a callback to open_input_file
open_file_button = tk.Button(window, text="Open Input File", command=open_input_file)
# Pack the button into the window
open_file_button.pack()

# Create a button to save an output file with a callback to save_output_file
save_file_button = tk.Button(window, text="Save Output File", command=save_output_file)
# Pack the button into the window
save_file_button.pack()

# Start the GUI event loop
window.mainloop()
