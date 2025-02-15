import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")  # Read from the PNG file

# Read the stored password
with open("key.txt", "r") as f:
    saved_password = f.read().strip()

# Get passcode for decryption
pas = input("Enter passcode for Decryption: ")

if saved_password == pas:
    # Read the message length from the first pixel
    msg_len = img[0, 0, 0]

    n, m = 0, 1  # Start from (0,1)
    message = ""

    for _ in range(msg_len):
        message += chr(img[n, m, 0])  # Retrieve from blue channel
        m += 1
        if m >= img.shape[1]:  # Move to next row if end of width is reached
            m = 0
            n += 1

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
