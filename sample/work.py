from PIL import Image
import os

filename = "ganesh.jpeg"

img = Image.open(filename)

if img.mode == "RGBA":
    img = img.convert("RGB")

output = "output.pdf"
image = img.save(output, "PDF", resolution=100.0)
