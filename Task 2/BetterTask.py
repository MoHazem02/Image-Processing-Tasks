import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the image
image_path = 'Task 2\monkey.jpg'
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get the dimensions of the image
M, N, _ = image.shape

# Display the original image
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')
plt.show()

# Req 2: Generate Bayer Filter ✅
BAYER_FILTER = np.zeros((M, N, 3), dtype=np.uint8)

# Red channel
BAYER_FILTER[0::2, 0::2, 0] = 255
# Green channel
BAYER_FILTER[0::2, 1::2, 1] = 255
BAYER_FILTER[1::2, 0::2, 1] = 255
# Blue channel
BAYER_FILTER[1::2, 1::2, 2] = 255

# Display Bayer Filter
plt.imshow(BAYER_FILTER)
plt.title('Bayer Filter')
plt.axis('off')
plt.show()

# Req 3: Apply Bayer Filter to the image ✅
FILTERED_MATRIX = BAYER_FILTER * image

# Display Filtered Matrix
plt.imshow(FILTERED_MATRIX)
plt.title('Filtered Matrix')
plt.axis('off')
plt.show()

# Convert to single channel Bayer pattern
BAYER_PATTERN = np.zeros((M, N), dtype=np.uint8)
BAYER_PATTERN[0::2, 0::2] = image[0::2, 0::2, 0]  # Red
BAYER_PATTERN[0::2, 1::2] = image[0::2, 1::2, 1]  # Green
BAYER_PATTERN[1::2, 0::2] = image[1::2, 0::2, 1]  # Green
BAYER_PATTERN[1::2, 1::2] = image[1::2, 1::2, 2]  # Blue

# Req 3.2: Perform Demosaicing using OpenCV ✅
INTERPOLATED_IMAGE = cv2.cvtColor(BAYER_PATTERN, cv2.COLOR_BAYER_RG2RGB)

# Display Interpolated Image
plt.imshow(INTERPOLATED_IMAGE)
plt.title('Interpolated Image')
plt.axis('off')
plt.show()

# Req 4: Transform to HSV color space ✅
HSV_IMAGE = cv2.cvtColor(INTERPOLATED_IMAGE, cv2.COLOR_RGB2HSV)

# Display HSV Image
plt.imshow(HSV_IMAGE)
plt.title('HSV Image')
plt.axis('off')
plt.show()