from PIL import Image
path1 = "C:\\Users\\Alejandra G\\Downloads\\arbol.jpg"
path2 = "C:\\Users\\Alejandra G\\OneDrive\\Escritorio\\AleG\\scrennArbolpy.jpeg"
img = Image.open(path1).convert("1")  # convert image to 8-bit grayscale
#img = img.resize((200, 200))
#img.show()
WIDTH, HEIGHT = img.size
data = list(img.getdata()) # convert image data to a list of integers
# convert that to 2D list (list of lists of integers)
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

# At this point the image's pixels are all in memory and can be accessed
# individually using data[row][col].

# For example:
for row in data:
    print(' '.join('{:3}'.format(value) for value in row))

# Here's another more compact representation.
chars = '@%#*+=-:. '  # Change as desired.
scale = (len(chars)-1)/255.
print()
for row in data:
    print(' '.join(chars[int(value*scale)] for value in row))