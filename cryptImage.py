import numpy as np
from PIL import Image
import copy

def decrypt_image(encrypted_image_path):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_image)

    print(encrypted_array)
    


decrypt_image("cinza.png")