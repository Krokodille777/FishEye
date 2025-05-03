from PIL import Image

filename = "Smile.png"
with Image.open(filename) as img:

    img.load()  # Load the image data
    img.show()  # Display the image