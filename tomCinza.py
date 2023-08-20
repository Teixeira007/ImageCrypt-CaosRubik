from PIL import Image

# Carregue a imagem colorida
image_path = "image.png"
color_image = Image.open(image_path)

# Converta a imagem para tons de cinza
gray_image = color_image.convert("L")

# Salve a imagem em tons de cinza
gray_image.save("cinza.png")

# Mostre a imagem em tons de cinza
gray_image.show()
