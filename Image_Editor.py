import os

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

img_path = []
path = "D:\Project\Image_Editor\Images"
for filename in os.listdir(path):
    img_path.append(os.path.join(path, filename))

def image_edit(path, brightness, contrast, sharpness, color, output_dir = "Edited_Img"):
    try:
        create_directory(output_dir)
        file_name = os.path.basename(path)
        img = Image.open(path)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(sharpness)
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(color)
        img.save(f"{output_dir}/{file_name}")
    except Exception as e:
        print(f"Error editing {path}: {e}")


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def img_compress(path, quality, way, output_dir = "Image_Compressed"):
    try:
        # Create the output directory if it doesn't exist
        create_directory(output_dir)
        
        # Open the image file
        img = Image.open(path)
        file_name = os.path.basename(path)

        # Handle "Quality" compression
        if way == "Quality":
            # Ensure quality is an integer between 0 and 100
            quality = int(quality * 100)  # Scale from 0-1 to 0-100
            img.save(os.path.join(output_dir, file_name), quality=quality)
        
        # Handle "Size" compression (DPI)
        elif way == "Size":
            # Assuming quality is a string like "300,300" for DPI
            dpi = quality.split(",")
            dpi = tuple(map(int, dpi))  # Convert to tuple of integers (x, y)
            img.save(os.path.join(output_dir, file_name), dpi=dpi)
    except Exception as e:
        print(f"Error compressing {path}: {e}")


def img_resize(path, height, width, output_dir = "Resized_Img"):
    try:
        create_directory(output_dir)
        img = Image.open(path)
        file_name = os.path.basename(path)
        resized_img = img.resize((width, height))
        resized_img.save(os.path.join(output_dir, file_name))
    except Exception as e:
        print(f"Error resizing {path}: {e}")


def img_crop(path, left, top, right, bottom, output_dir="Cropped_Img"):
    try:
        create_directory(output_dir)
        img = Image.open(path)
        
        # Check if the coordinates are valid
        if left < 0 or top < 0 or right > img.width or bottom > img.height:
            raise ValueError(f"Invalid crop coordinates for {path}. Coordinates must be within the image bounds.")
        
        # Perform the crop
        cropped_img = img.crop((left, top, right, bottom))

        # Ensure the cropped image is not empty
        if cropped_img.width == 0 or cropped_img.height == 0:
            raise ValueError(f"The crop resulted in an empty image for {path}.")
        
        # Save the cropped image
        file_name = os.path.basename(path)
        cropped_img.save(os.path.join(output_dir, file_name))
    except Exception as e:
        print(f"Error cropping {path}: {e}")

def img_rotate(path, angle, output_dir = "Rotated_Img"):
    try:
        create_directory(output_dir)
        img = Image.open(path)
        file_name = os.path.basename(path)
        # exif_data = img._getexif()
        # img_corrected = ImageOps.exif_transpose(img)
        # img_corrected.save(os.path.join(output_dir, file_name))
        rotated_img = img.rotate(angle)
        rotated_img.save(os.path.join(output_dir, file_name))
    except Exception as e:
        print(f"Error rotating {path}: {e}")

def img_blur(path, radius, output_dir = "Blurred_Img"):
    try:
        create_directory(output_dir)
        img = Image.open(path)
        file_name = os.path.basename(path)
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius))
        blurred_img.save(os.path.join(output_dir, file_name))
    except Exception as e:
        print(f"Error blurring {path}: {e}")

def img_sharpen(path, output_dir = "Sharpened_Img"):
    try:
        create_directory(output_dir)
        img = Image.open(path)
        file_name = os.path.basename(path)
        sharpened_img = img.filter(ImageFilter.SHARPEN)
        sharpened_img.save(os.path.join(output_dir, file_name))
    except Exception as e:
        print(f"Error sharpening {path}: {e}")

def img_edge(path, output_dir = "Edge_Detected_Img"):
    try:
        create_directory(output_dir)
        img = Image.open(path)
        file_name = os.path.basename(path)
        edge_detected_img = img.filter(ImageFilter.EDGE_ENHANCE)
        edge_detected_img.save(os.path.join(output_dir, file_name))
    except Exception as e:
        print(f"Error edge detecting {path}: {e}")

def img_show_metadata(path):
    try:
        img = Image.open(path)
        file_name = os.path.basename(path)
        print(f"Image metadata for {file_name} is:")
        exif_data = img._getexif()
        print(exif_data)
    except Exception as e:
        print(f"Error getting metadata for {path}: {e}")

for i in img_path:
    img_crop(i, 100, 100, 200, 200)