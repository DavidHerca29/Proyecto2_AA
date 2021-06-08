from PIL import Image
path1 = "Siluetas\\silueta1.jpg"
path2 = "Siluetas\\silueta2.jpg"
pathFitness = "imagenes\\imagen-"

def obtenerSilueta(path):
    img = Image.open(path).convert("1")  # convert image to 8-bit grayscale
    img = img.resize((600, 600))

    WIDTH, HEIGHT = img.size
    data = list(img.getdata()) # convert image data to a list of integers
    # convert that to 2D list (list of lists of integers)
    data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
    return data
# At this point the image's pixels are all in memory and can be accessed
# individually using data[row][col].
