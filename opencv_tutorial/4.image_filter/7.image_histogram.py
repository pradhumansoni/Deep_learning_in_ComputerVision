import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("4.image_filter/test_img.jpg")

# Colors corresponding to OpenCV channel order (BGR)
colors = ('b', 'g', 'r')
labels = ('Blue', 'Green', 'Red')

plt.figure(figsize=(8, 5))

for i, (color, label) in enumerate(zip(colors, labels)):
    # Calculate histogram
    hist = cv2.calcHist(
        images=[img],      # Source image
        channels=[i],      # 0=Blue, 1=Green, 2=Red
        mask=None,         # Use entire image
        histSize=[256],    # 256 bins (0-255)
        ranges=[0, 256]    # Pixel intensity range
    )

    plt.plot(hist, color=color, label=label)

plt.title("RGB Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.xlim([0, 256])
plt.legend()
plt.grid(alpha=0.3)

plt.show()