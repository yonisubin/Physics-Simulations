from PIL import Image
im=Image.open("C:\\Users\\yonis\\Documents\\Python Scripts\\Physics Simulations\\SampleJPGImage_30mbmb.jpg")
print(im.format, im.size, im.mode)
c=list(im.split())