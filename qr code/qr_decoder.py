"""
import cv2
from pyzbar.pyzbar import decode


def decode_qr_code(image_path):
    try:
        img = cv2.imread(image_path)

        if img is None:
            print(f"Error: Could not read image from {image_path}")
            return None

        decoded_objects = decode(img)

        if decoded_objects:
            decoded_data = decoded_objects[0].data.decode('utf-8')
            return decoded_data
        else:
            print("No QR code found in the image.")
            return None

    except Exception:
        pass
"""
