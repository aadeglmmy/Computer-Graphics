import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing Application")
        self.root.geometry("1600x900")

        self.frame = Frame(self.root)
        self.frame.pack(pady=20)

        self.load_btn = Button(self.frame, text="Load Image", command=self.load_image, width=20)
        self.load_btn.grid(row=0, column=0, padx=10, pady=10)

        self.otsu_btn = Button(self.frame, text="Otsu Thresholding", command=self.apply_otsu_threshold, state=DISABLED,
                               width=20)
        self.otsu_btn.grid(row=0, column=1, padx=10, pady=10)

        self.fixed_threshold_btn = Button(self.frame, text="Fixed Thresholding", command=self.apply_fixed_threshold,
                                          state=DISABLED, width=20)
        self.fixed_threshold_btn.grid(row=0, column=2, padx=10, pady=10)

        self.median_filter_btn = Button(self.frame, text="Median Filter", command=self.apply_median_filter,
                                        state=DISABLED, width=20)
        self.median_filter_btn.grid(row=0, column=3, padx=10, pady=10)

        self.min_filter_btn = Button(self.frame, text="Min Filter", command=self.apply_min_filter, state=DISABLED,
                                     width=20)
        self.min_filter_btn.grid(row=1, column=0, padx=10, pady=10)

        self.max_filter_btn = Button(self.frame, text="Max Filter", command=self.apply_max_filter, state=DISABLED,
                                     width=20)
        self.max_filter_btn.grid(row=1, column=1, padx=10, pady=10)

        self.display_panel = Label(self.root)
        self.display_panel.pack(pady=20)

        self.image = None
        self.processed_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            self.display_image(self.image)
            self.otsu_btn.config(state=NORMAL)
            self.fixed_threshold_btn.config(state=NORMAL)
            self.median_filter_btn.config(state=NORMAL)
            self.min_filter_btn.config(state=NORMAL)
            self.max_filter_btn.config(state=NORMAL)

    def display_image(self, img):
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.display_panel.config(image=imgtk)
        self.display_panel.image = imgtk

    def apply_fixed_threshold(self):
        _, thresh_fixed = cv2.threshold(self.image, 127, 255, cv2.THRESH_BINARY)
        self.processed_image = thresh_fixed
        self.display_image(thresh_fixed)

    def apply_otsu_threshold(self):
        _, thresh_otsu = cv2.threshold(self.image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.processed_image = thresh_otsu
        self.display_image(thresh_otsu)

    def apply_median_filter(self):
        median_filtered = cv2.medianBlur(self.image, 5)
        self.processed_image = median_filtered
        self.display_image(median_filtered)

    def apply_min_filter(self):
        kernel = np.ones((3, 3), np.uint8)
        min_filtered = cv2.erode(self.image, kernel, iterations=1)
        self.processed_image = min_filtered
        self.display_image(min_filtered)

    def apply_max_filter(self):
        kernel = np.ones((3, 3), np.uint8)
        max_filtered = cv2.dilate(self.image, kernel, iterations=1)
        self.processed_image = max_filtered
        self.display_image(max_filtered)


if __name__ == "__main__":
    root = Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
