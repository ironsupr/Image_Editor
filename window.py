from tkinter import *
from customtkinter import *
from Image_Editor import *  # Assuming you have an image editor module

import os

# Set up path for images
img_path = []
path = "Images"
for filename in os.listdir(path):
    img_path.append(os.path.join(path, filename))

def remove_widgets():
    """Removes all widgets from the root window except for frame1."""
    for widget in root.winfo_children():
        if widget not in [frame1]:
            widget.destroy()

def update_value_label(value, label):
    """Updates the label with the current value of the slider."""
    label.configure(text=f"{value:.2f}")  # Display the value with 2 decimal points

def create_slider(label_text, slider_range, x, y, slider_callback):
    """Creates a slider with the given parameters and returns the slider and value label."""
    label = CTkLabel(root, text=label_text, width=200, height=40)
    label.place(x=x, y=y)
    
    slider = CTkSlider(root, from_=slider_range[0], to=slider_range[1], number_of_steps=100, width=200, command=lambda value: update_value_label(value, value_label))
    slider.set(slider_range[2])  # Default value
    slider.place(x=x + 250, y=y)
    
    value_label = CTkLabel(root, text=f"{slider_range[2]:.2f}")
    value_label.place(x=x + 450, y=y)
    
    return slider, value_label

def submit():
    """Handles the submission of values from the sliders and applies the image edits."""
    brightness_value = brightness_slider.get()
    contrast_value = contrast_slider.get()
    sharpness_value = sharpness_slider.get()
    color_value = color_slider.get()
    
    # print("Brightness:", brightness_value)
    # print("Contrast:", contrast_value)
    # print("Sharpness:", sharpness_value)
    # print("Color:", color_value)
    
    for image in img_path:
        image_edit(image, brightness_value/50, contrast_value/50, sharpness_value/50, color_value/50)
    
    res = CTkLabel(root, text="Image Edited Successfully", width=200, height=40)
    res.place(x=500, y=350)

def edit():
    """Handles the 'Edit Image' functionality."""
    remove_widgets()

    # Create sliders dynamically for sharpness, brightness, contrast, and color
    global sharpness_slider, brightness_slider, contrast_slider, color_slider
    sharpness_slider, sharpness_value_label = create_slider("Sharpness:", (0, 100, 50), 250, 100, update_value_label)
    brightness_slider, brightness_value_label = create_slider("Brightness:", (0, 100, 50), 250, 150, update_value_label)
    contrast_slider, contrast_value_label = create_slider("Contrast:", (0, 100, 50), 250, 200, update_value_label)
    color_slider, color_value_label = create_slider("Color:", (0, 100, 50), 250, 250, update_value_label)

    # Create and position the Submit Button
    submit_button = CTkButton(root, text="Submit", width=200, height=40, command=submit)
    submit_button.place(x=500, y=300)

def submit_comp_qua():
    """Handles the submission of values from the sliders and applies the image compression."""
    quality_value = compress_slider.get()
    print("Quality:", quality_value)
    
    for i in img_path:
        print(quality_value/100)
        img_compress(i, float(quality_value)/100 , way = "Quality")
    
    res = CTkLabel(root, text="Image Compressed Successfully", width=200, height=40)
    res.place(x=500, y=300)

def handle_size_compression(resolution_entry):
    dpi_value = resolution_entry.get()
    print(dpi_value)

    for i in img_path:
        img_compress(i, dpi_value, way = "Size")
    
    res = CTkLabel(root, text="Image Compressed Successfully", width=200, height=40)
    res.place(x=500, y=300)

def compress():
    """Handles the 'Compress Image' functionality based on quality or size."""
    remove_widgets()

    label_compress = CTkLabel(root, text="How to Compress your Image:", fg_color="transparent", bg_color="transparent")
    label_compress.place(x=300, y=100)


    # Function to update the compression UI based on the selected option
    def update_compression_ui(selected_option=None):
        """Updates the UI based on the selected compression type (Quality or Size)."""
        # If no selection is provided, get the current dropdown selection
        if not selected_option:
            selected_option = drop_compress.get()

        # Remove all widgets except for the frame and dropdown
        for widget in root.winfo_children():
            if widget not in [frame1, label_compress, drop_compress]:
                widget.destroy()

        if selected_option == "Quality":
            # Quality-based compression: Show the quality slider
            global compress_slider
            compress_slider, compress_value_label = create_slider("Compress Quality:", (0, 100, 100), 250, 200, update_value_label)

            submit_button = CTkButton(root, text="Submit", width=200, height=40, command=submit_comp_qua)
            submit_button.place(x=500, y=250)
            

        elif selected_option == "Size":
            # Size-based compression: Show DPI input
            compress_res_label = CTkLabel(root, text="Enter Resolution (DPI):", width=200, height=40)
            compress_res_label.place(x=250, y=200)

            resolution_entry = CTkEntry(root, width=200, height=40)
            resolution_entry.place(x=500, y=200)

            # Add a submit button for the resolution-based compression
            submit_button = CTkButton(root, text="Submit", width=200, height=40, command=lambda: handle_size_compression(resolution_entry))
            submit_button.place(x=500, y=250)
        # Create the option menu for selecting "Quality" or "Size"
    drop_compress = CTkOptionMenu(root, width=200, height=40, values=["Quality", "Size"], command=update_compression_ui)
    drop_compress.place(x=500, y=100)
    # Initially trigger the UI update to handle the default "Quality"
    update_compression_ui(drop_compress.get())

def handle_resize(height_entry, width_entry):
    height = height_entry.get()
    width = width_entry.get()

    for i in img_path:
        img_resize(i, int(height), int(width))
    
    res = CTkLabel(root, text="Image Resized Successfully :  {} by {}".format(height, width), width=200, height=40)
    res.place(x=500, y=300)

def resize():
    remove_widgets()

    label_hieght = CTkLabel(root, text="Enter Height:", width=200, height=40)
    label_hieght.place(x=250, y=150)

    height_entry = CTkEntry(root, width=200, height=40)
    height_entry.place(x=500, y=150)

    label_width = CTkLabel(root, text="Enter Width:", width=200, height=40)
    label_width.place(x=250, y=200)

    width_entry = CTkEntry(root, width=200, height=40)
    width_entry.place(x=500, y=200)

    submit_button = CTkButton(root, text="Submit", width=200, height=40, command=lambda: handle_resize(height_entry, width_entry))
    submit_button.place(x=500, y=250)

def crop():
    remove_widgets()

    label_warn = CTkLabel(root, text="Ensure left < right and top < bottom.", width=200, height=40)
    label_warn.place(x=500, y=50)

    label_left = CTkLabel(root, text="Enter Left:", width=200, height=40)
    label_left.place(x=250, y=150)

    left_entry = CTkEntry(root, width=200, height=40)
    left_entry.place(x=500, y=150)

    label_top = CTkLabel(root, text="Enter Top:", width=200, height=40)
    label_top.place(x=250, y=200)

    top_entry = CTkEntry(root, width=200, height=40)
    top_entry.place(x=500, y=200)

    label_right = CTkLabel(root, text="Enter Right:", width=200, height=40)
    label_right.place(x=250, y=250)

    right_entry = CTkEntry(root, width=200, height=40)
    right_entry.place(x=500, y=250)

    label_bottom = CTkLabel(root, text="Enter Bottom:", width=200, height=40)
    label_bottom.place(x=250, y=300)

    bottom_entry = CTkEntry(root, width=200, height=40)
    bottom_entry.place(x=500, y=300)

    def handle_crop(left_entry, top_entry, right_entry, bottom_entry):
        try:
            left = int(left_entry.get())
            top = int(top_entry.get())
            right = int(right_entry.get())
            bottom = int(bottom_entry.get())

            print(f"Cropping with coordinates: top={top}, left={left}, right={right}, bottom={bottom}")

            for i in img_path:
                img_crop(i, left, top, right, bottom)
        
            res = CTkLabel(root, text="Image Cropped Successfully", width=200, height=40)
            res.place(x=500, y=400)
    
        except Exception as e:
            print(f"Error in handle_crop: {e}")

    submit_button = CTkButton(root, text="Submit", width=200, height=40, command=lambda: handle_crop(left_entry, top_entry, right_entry, bottom_entry))
    submit_button.place(x=500, y=350)

def rotate():
    remove_widgets()

    label_angle = CTkLabel(root, text="Enter Angle (in degrees):", width=200, height=40)
    label_angle.place(x=250, y=150)

    angle_entry = CTkEntry(root, width=200, height=40)
    angle_entry.place(x=500, y=150)

    def handle_rotate(angle_entry):
        angle = angle_entry.get()

        for i in img_path:
            img_rotate(i, int(angle))
        
        res = CTkLabel(root, text="Image Rotated Successfully", width=200, height=40)
        res.place(x=500, y=250)
    
    submit_button = CTkButton(root, text="Submit", width=200, height=40, command=lambda: handle_rotate(angle_entry))
    submit_button.place(x=500, y=200)

def blur():
    remove_widgets()

    label_radius = CTkLabel(root, text="Enter Radius:", width=200, height=40)
    label_radius.place(x=250, y=150)

    radius_entry = CTkEntry(root, width=200, height=40)
    radius_entry.place(x=500, y=150)

    def handle_blur(radius_entry):
        radius = radius_entry.get()

        for i in img_path:
            img_blur(i, int(radius))
        
        res = CTkLabel(root, text="Image Blurred Successfully", width=200, height=40)
        res.place(x=500, y=250)
    
    submit_button = CTkButton(root, text="Submit", width=200, height=40, command=lambda: handle_blur(radius_entry))
    submit_button.place(x=500, y=200)

def sharp():
    remove_widgets()

    label_sharpness = CTkLabel(root, text="Do you want to Sharpen your Image:", width=200, height=40)
    label_sharpness.place(x=500, y=150)

    def handle_sharp():

        for i in img_path:
            img_sharpen(i)
        
        res = CTkLabel(root, text="Image Sharpened Successfully", width=200, height=40)
        res.place(x=500, y=250)

    submit_button = CTkButton(root, text="Yes", width=200, height=40, command=lambda: handle_sharp())
    submit_button.place(x=500, y=200)

def edge_enhance():
    remove_widgets()

    label_edge = CTkLabel(root, text="Do you want to Enhance Edges in your Image:", width=200, height=40)
    label_edge.place(x=500, y=150)

    def handle_edge():

        for i in img_path:
            img_edge(i)
        
        res = CTkLabel(root, text="Edges Enhanced Successfully", width=200, height=40)
        res.place(x=500, y=250)

    submit_button = CTkButton(root, text="Yes", width=200, height=40, command=lambda: handle_edge())
    submit_button.place(x=500, y=200)

def mirror():
    remove_widgets()

    label_mirror = CTkLabel(root, text="Do you want to Mirror your Image:", width=200, height=40)
    label_mirror.place(x=500, y=150)

    def handle_mirror():

        for i in img_path:
            img_mirror(i)
        
        res = CTkLabel(root, text="Image Mirrored Successfully", width=200, height=40)
        res.place(x=500, y=250)

    submit_button = CTkButton(root, text="Yes", width=200, height=40, command=lambda: handle_mirror())
    submit_button.place(x=500, y=200)

# Set up the Tkinter root window
root = CTk()  # Create the main window
root.geometry("1000x800")
root.title("Image Editor")
set_default_color_theme("green")
set_appearance_mode("dark")

# Create the left frame containing buttons and labels
frame1 = CTkFrame(root, width=200, height=800)
frame1.pack(side=LEFT, fill=Y)

welcome = CTkLabel(root, text="Welcome to Image Editor", fg_color="transparent", bg_color="transparent", font=("Arial", 30))
welcome.place(x=450, y=300)

# Add a label at the top of the frame
label = CTkLabel(frame1, text="Image Editor", fg_color="transparent", bg_color="transparent", font=("Arial", 20))
label.pack(side=TOP, pady=10)

# Create the 'Edit Image' button
button_edit = CTkButton(frame1, text="Edit Image", width=200, height=40, command=edit)
button_edit.pack(side=TOP, pady=10)

# Create a 'Compress Image' button
button_compress = CTkButton(frame1, text="Compress Image", width=200, height=40, command=compress)
button_compress.pack(side=TOP, pady=10)

button_resize = CTkButton(frame1, text="Resize Image", width=200, height=40, command=resize)
button_resize.pack(side=TOP, pady=10)

button_crop = CTkButton(frame1, text="Crop Image", width=200, height=40, command=crop)
button_crop.pack(side=TOP, pady=10)

button_rotate = CTkButton(frame1, text="Rotate Image", width=200, height=40, command=rotate)
button_rotate.pack(side=TOP, pady=10)

button_blur = CTkButton(frame1, text="Blur Image", width=200, height=40, command=blur)
button_blur.pack(side=TOP, pady=10)

button_sharp = CTkButton(frame1, text="Sharpen Image", width=200, height=40, command=sharp)
button_sharp.pack(side=TOP, pady=10)

button_edge = CTkButton(frame1, text="Edge Detection", width=200, height=40, command=edge_enhance)
button_edge.pack(side=TOP, pady=10)

button_mirror = CTkButton(frame1, text="Mirror Image", width=200, height=40, command=mirror)
button_mirror.pack(side=TOP, pady=10)

root.mainloop()
