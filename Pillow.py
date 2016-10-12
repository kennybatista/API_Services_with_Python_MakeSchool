from PIL import Image, ImageFilter

# Read image
im = Image.open("image_sharpened.jpg")
# Display image
im.show()

# Applying a filter to the image
im_sharp = im.filter(ImageFilter.EMBOSS)
# saving the filtered image to a new filter
im_sharp.save("image_sharpened3.jpg", "JPEG")

# Splitting the image into its respective bands, i.e. Red, Green, #and Blue
r, g, b = im_sharp.split()

# Viewing EXIF data embedded in image
exif_data = im._getexif()
exif_data
