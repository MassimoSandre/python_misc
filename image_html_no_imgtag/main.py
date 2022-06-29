from PIL import Image

im = Image.open('img.jpg')
pix = im.load()

output = open("output.html","w")

print(im.size)
for y in range(im.size[0]):
    for x in range(im.size[1]):
        r,g,b = pix[y,x]
        output.write(f"<p style='position:absolute; background-color:rgb({r},{g},{b}); height:1px;width:1px; left: {y}px;top: {x}px;'></p>\n")

output.close()