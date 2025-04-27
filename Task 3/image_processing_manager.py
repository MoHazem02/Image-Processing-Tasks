import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from image_processing_ui import ImageProcessingUI
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImageProcessingManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ImageProcessingUI()
        self.setCentralWidget(self.ui)

        # Connect buttons to their respective functions
        self.ui.load_button.clicked.connect(self.load_image_tab1)
        self.ui.detect_button.clicked.connect(self.detect_features)
        self.ui.load_button_tab2.clicked.connect(self.load_image_tab2)
        self.ui.transform_button.clicked.connect(self.transform_dft)

        # Initialize variables
        self.image_tab1 = None
        self.gray_image_tab1 = None
        self.image_tab2 = None

    def load_image_tab1(self):
        # Open file dialog to select an image for Tab 1
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.webp)", options=options)

        if file_path:
            # Load the image
            self.image_tab1 = cv2.imread(file_path)
            self.image_tab1 = cv2.cvtColor(self.image_tab1, cv2.COLOR_BGR2RGB)

            # Resize the image to fit the display area
            self.image_tab1 = cv2.resize(self.image_tab1, (300, 200))

            # Display the original image
            self.display_image(self.ui.original_image_label, self.image_tab1)

            # Reset other components
            self.ui.grayscale_image_label.clear()
            self.ui.harris_builtin_label.clear()
            self.ui.harris_manual_label.clear()

    def detect_features(self):
        if self.image_tab1 is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please load an image first.")
            return

        # Convert to grayscale
        self.gray_image_tab1 = cv2.cvtColor(self.image_tab1, cv2.COLOR_RGB2GRAY)
        self.display_image(self.ui.grayscale_image_label, self.gray_image_tab1, cmap='gray')

        # Harris Corner Detection (Built-in)
        gray_float = np.float32(self.gray_image_tab1)
        dst = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04)
        dst = cv2.dilate(dst, None)
        harris_builtin = self.image_tab1.copy()
        harris_builtin[dst > 0.01 * dst.max()] = [255, 0, 0]
        self.display_image(self.ui.harris_builtin_label, harris_builtin)

        # Harris Corner Detection (Manual)
        Ix = cv2.Sobel(self.gray_image_tab1, cv2.CV_64F, 1, 0, ksize=3)
        Iy = cv2.Sobel(self.gray_image_tab1, cv2.CV_64F, 0, 1, ksize=3)
        Ixx = cv2.GaussianBlur(Ix * Ix, (3, 3), sigmaX=1)
        Iyy = cv2.GaussianBlur(Iy * Iy, (3, 3), sigmaX=1)
        Ixy = cv2.GaussianBlur(Ix * Iy, (3, 3), sigmaX=1)
        k = 0.04
        det_M = (Ixx * Iyy) - (Ixy * Ixy)
        trace_M = Ixx + Iyy
        R = det_M - k * (trace_M ** 2)
        manual_corners = self.image_tab1.copy()
        manual_corners[R > 0.01 * R.max()] = [255, 0, 0]
        self.display_image(self.ui.harris_manual_label, manual_corners)

    def load_image_tab2(self):
        # Open file dialog to select an image for Tab 2
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.webp)", options=options)

        if file_path:
            # Load the image
            self.image_tab2 = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

            # Resize the image to fit the display area
            self.image_tab2 = cv2.resize(self.image_tab2, (300, 200))

            # Display the grayscale image
            self.display_image(self.ui.image1_label, self.image_tab2, cmap='gray')

            # Reset other components
            self.ui.image1_magnitude_label.clear()
            self.ui.image1_phase_label.clear()

    def transform_dft(self):
        if self.image_tab2 is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please load an image first.")
            return

        # Perform DFT on the image
        dft = cv2.dft(np.float32(self.image_tab2), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        magnitude = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
        phase = np.angle(dft_shift[:, :, 0] + 1j * dft_shift[:, :, 1])

        # Display magnitude and phase images
        self.display_image(self.ui.image1_magnitude_label, magnitude, cmap='gray')
        self.display_image(self.ui.image1_phase_label, phase, cmap='gray')

    def display_image(self, label, image, cmap=None):
        # Convert the image to QPixmap and display it in the QLabel
        if cmap == 'gray':
            image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QtGui.QImage(image.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_image)
        label.setPixmap(pixmap)
        label.setScaledContents(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = ImageProcessingManager()
    main_window.show()
    sys.exit(app.exec_())