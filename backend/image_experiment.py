import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread(r'C:\Users\maria selciya\weather-skin-app\backend\closeup-view-human-skin-as-background-closeup-view-human-oily-skin-as-background-263476251.webp')

# Convert the image from BGR to RGB (OpenCV loads in BGR by default)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display using matplotlib
plt.imshow(img_rgb)
plt.axis('off')  # Hide axes
plt.show()
