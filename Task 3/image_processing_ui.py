from PyQt5 import QtWidgets, QtGui, QtCore

class ImageProcessingUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up the main layout
        self.setWindowTitle("Harris & DFT")
        self.setFixedSize(800, 600)  # Medium size and non-resizable

        # Create tab widget
        self.tabs = QtWidgets.QTabWidget()

        # Tab 1: Harris Corner Detection
        self.tab1 = QtWidgets.QWidget()
        self.init_tab1()
        self.tabs.addTab(self.tab1, "Harris Detection")

        # Tab 2: DFT
        self.tab2 = QtWidgets.QWidget()
        self.init_tab2()
        self.tabs.addTab(self.tab2, "DFT")

        # Main layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def init_tab1(self):
        # Layout for Tab 1
        self.tab1_layout = QtWidgets.QVBoxLayout()

        # Button layout
        self.button_layout = QtWidgets.QHBoxLayout()

        # Image loading button
        self.load_button = QtWidgets.QPushButton("Load Image")
        self.load_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px; padding: 10px; border-radius: 5px;")
        self.button_layout.addWidget(self.load_button)

        # Detect button
        self.detect_button = QtWidgets.QPushButton("Detect")
        self.detect_button.setStyleSheet("background-color: #2196F3; color: white; font-size: 14px; padding: 10px; border-radius: 5px;")
        self.button_layout.addWidget(self.detect_button)

        self.tab1_layout.addLayout(self.button_layout)

        # Image display grid layout
        self.image_grid = QtWidgets.QGridLayout()

        # Labels and Image display areas
        self.original_image_label_text = QtWidgets.QLabel("Original Image")
        self.original_image_label_text.setAlignment(QtCore.Qt.AlignCenter)
        self.image_grid.addWidget(self.original_image_label_text, 0, 0)

        self.original_image_label = QtWidgets.QLabel()
        self.original_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.original_image_label.setFixedSize(300, 200)
        self.image_grid.addWidget(self.original_image_label, 1, 0)

        self.grayscale_image_label_text = QtWidgets.QLabel("Grayscale Image")
        self.grayscale_image_label_text.setAlignment(QtCore.Qt.AlignCenter)
        self.image_grid.addWidget(self.grayscale_image_label_text, 0, 1)

        self.grayscale_image_label = QtWidgets.QLabel()
        self.grayscale_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.grayscale_image_label.setFixedSize(300, 200)
        self.image_grid.addWidget(self.grayscale_image_label, 1, 1)

        self.harris_builtin_label_text = QtWidgets.QLabel("Built-In Harris")
        self.harris_builtin_label_text.setAlignment(QtCore.Qt.AlignCenter)
        self.image_grid.addWidget(self.harris_builtin_label_text, 2, 0)

        self.harris_builtin_label = QtWidgets.QLabel()
        self.harris_builtin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.harris_builtin_label.setFixedSize(300, 200)
        self.image_grid.addWidget(self.harris_builtin_label, 3, 0)

        self.harris_manual_label_text = QtWidgets.QLabel("Manual Harris")
        self.harris_manual_label_text.setAlignment(QtCore.Qt.AlignCenter)
        self.image_grid.addWidget(self.harris_manual_label_text, 2, 1)

        self.harris_manual_label = QtWidgets.QLabel()
        self.harris_manual_label.setAlignment(QtCore.Qt.AlignCenter)
        self.harris_manual_label.setFixedSize(300, 200)
        self.image_grid.addWidget(self.harris_manual_label, 3, 1)

        self.tab1_layout.addLayout(self.image_grid)
        self.tab1.setLayout(self.tab1_layout)

    def init_tab2(self):
        # Layout for Tab 2
        self.tab2_layout = QtWidgets.QVBoxLayout()

        # Button layout
        self.button_layout = QtWidgets.QHBoxLayout()

        # Load button
        self.load_button_tab2 = QtWidgets.QPushButton("Load Image")
        self.load_button_tab2.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px; padding: 10px; border-radius: 5px;")
        self.button_layout.addWidget(self.load_button_tab2)

        # Transform button
        self.transform_button = QtWidgets.QPushButton("Transform")
        self.transform_button.setStyleSheet("background-color: #2196F3; color: white; font-size: 14px; padding: 10px; border-radius: 5px;")
        self.button_layout.addWidget(self.transform_button)

        self.tab2_layout.addLayout(self.button_layout)

        # Image display vertical layout for DFT
        self.dft_layout = QtWidgets.QVBoxLayout()

        # Grayscale image display
        self.image1_label = QtWidgets.QLabel("Grayscale Image")
        self.image1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image1_label.setFixedSize(300, 200)
        self.dft_layout.addWidget(self.image1_label)

        # Magnitude spectrum display
        self.image1_magnitude_label = QtWidgets.QLabel("Magnitude Spectrum")
        self.image1_magnitude_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image1_magnitude_label.setFixedSize(300, 200)
        self.dft_layout.addWidget(self.image1_magnitude_label)

        # Phase spectrum display
        self.image1_phase_label = QtWidgets.QLabel("Phase Spectrum")
        self.image1_phase_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image1_phase_label.setFixedSize(300, 200)
        self.dft_layout.addWidget(self.image1_phase_label)

        self.tab2_layout.addLayout(self.dft_layout)
        self.tab2.setLayout(self.tab2_layout)