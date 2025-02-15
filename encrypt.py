import cv2
import os

# Load the image
img = cv2.imread("mypic.jpg")  # Ensure the image exists

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Save the password in a text file
with open("key.txt", "w") as f:
    f.write(password)

# Convert message to ASCII and store in the blue channel
msg_len = len(msg)
img[0, 0, 0] = msg_len  # Store the length of the message

n, m = 0, 1  # Start from (0,1) to avoid overwriting the length

for i in range(msg_len):
    img[n, m, 0] = ord(msg[i])  # Store ASCII values in the blue channel
    m += 1
    if m >= img.shape[1]:  # Move to next row if end of width is reached
        m = 0
        n += 1

# Save the encrypted image in PNG format to prevent OpenCV compression issues
cv2.imwrite("encryptedImage.png", img)

print("Encryption Done. Use 'decrypt.py' to decrypt the message.")
