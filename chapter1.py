import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# Read the image
image = cv2.imread('chapter1.jpg')

# Convert the image from BGR (OpenCV default) to RGB (for displaying with Matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Display the original image using Matplotlib
# plt.imshow(image_rgb)
# plt.axis('off')  # Hide axis
# plt.title('Original Image')
# # plt.show()

# Print the shape of the image
# print(f"Image shape: {image.shape}")

# Get the current time as a number
current_time = int(time.time())

# Generate a number based on current time
generated_number = (current_time % 100) + 50

# Ensure generated_number is even
if generated_number % 2 == 0:
    generated_number += 10

# print(f"Generated number: {generated_number}")

# Add the generated number to each channel and clip the values must between 0 to 255
new_image_rgb = np.clip(image_rgb + generated_number, 0, 255).astype(np.uint8)

# Display the modified image using Matplotlib
plt.imshow(new_image_rgb)
plt.axis('off')  # Hide axis
plt.title('chapter1out.png')
plt.show()

# Sum all red (R) pixel values in the new image
red_channel_sum = np.sum(new_image_rgb[:, :, 0])

# Output the sum of red pixel values
print(f"Sum of all red pixel values: {red_channel_sum}")
