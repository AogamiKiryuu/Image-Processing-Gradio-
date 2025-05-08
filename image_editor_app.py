import gradio as gr
import numpy as np
import cv2
from PIL import Image

def process_image(image, grayscale=0.0, denoise=10, brightness=0, contrast=1.0, rotation=0.0):
    # Convert PIL image to NumPy array
    image_np = np.array(image.convert('RGB'))

    # Jika grayscale slider 0, maka tidak perlu blending
    if grayscale > 0:
        # Grayscale blending (dari gambar asli)
        gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
        gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        blended = cv2.addWeighted(image_np, 1 - grayscale, gray_rgb, grayscale, 0)
    else:
        blended = image_np

    # Denoising menggunakan mean filter (blur) tanpa mengubah warna
    kernel_size = max(3, int(denoise) // 2 * 2 + 1)  # Pastikan kernel size ganjil
    denoised = cv2.blur(blended, (kernel_size, kernel_size))

    # Brightness and contrast adjustment
    adjusted = cv2.convertScaleAbs(denoised, alpha=contrast, beta=brightness)

    # Rotation (Operasi Geometri)
    if rotation != 0.0:
        height, width = adjusted.shape[:2]
        center = (width // 2, height // 2)
        rot_matrix = cv2.getRotationMatrix2D(center, rotation, 1.0)
        rotated = cv2.warpAffine(adjusted, rot_matrix, (width, height), flags=cv2.INTER_LINEAR)
    else:
        rotated = adjusted

    return Image.fromarray(rotated)

iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="pil", label="Upload Gambar"),
        gr.Slider(0, 1, step=0.05, label="Grayscale Blend"),
        gr.Slider(0, 20, step=1, label="Denoise Strength"),
        gr.Slider(-100, 100, step=1, label="Brightness"),
        gr.Slider(0.1, 3.0, step=0.1, label="Contrast"),
        gr.Slider(-180, 180, step=1, label="Rotation (Degrees)")
    ],
    outputs=gr.Image(type="pil"),
    title="UTP PC - Faqih Fathurrachman 065122103",
    description="Upload gambar untuk bisa diubah menjadi grayscale, denoise dengan mean filter, brightness and contrast adjustment, dan rotasi (Operasi Pixel dan Geometri)."
)

if __name__ == "__main__":
    iface.launch()