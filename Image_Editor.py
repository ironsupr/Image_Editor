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
        create_directory(output_dir)
        img = Image.open(path)
        file_name = os.path.basename(path)

        if way == "Quality":
            img.save(os.path.join(output_dir, file_name), quality=quality)
        elif way == "Size":
            x, y = quality
            img.save(os.path.join(output_dir, file_name), dpi=(x, y))
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


def img_crop(path, left, top, right, bottom, output_dir = "Cropped_Img"):
    try:
        create_directory(output_dir)
        img = Image.open(path)
        file_name = os.path.basename(path)
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(os.path.join(output_dir, file_name))
    except Exception as e:
        print(f"Error cropping {path}: {e}")

def img_rotate(path, angle, output_dir = "Rotated_Img"):
    try:
        create_directory(output_dir)
        img = Image.open(path)
        file_name = os.path.basename(path)
        exif_data = img._getexif()
        img_corrected = ImageOps.exif_transpose(img)
        img_corrected.save(os.path.join(output_dir, file_name))
        # rotated_img = img.rotate(angle)
        # rotated_img.save(os.path.join(output_dir, file_name))
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

