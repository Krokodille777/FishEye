
from PIL import Image, ImageFilter, ImageEnhance

import numpy as np





# filename = "Smile.png"
filename = input("Enter the image file name (with extension): ").strip()
with Image.open(filename) as img:

    def apply_uv_filter(image_path):

        Image.open(image_path)
        strength  = float( input("Enter the strength of the UV filter in % (1% = 0.01) (0.01 to 1.00): ").strip())
        r, g, b, _ = img.split()
        b = ImageEnhance.Brightness(b).enhance(strength)
        r = ImageEnhance.Brightness(r).enhance(0.85) 

        
        
        

        filtered_img = Image.merge("RGB", (r, g, b))
        filtered_img.show()


        return filtered_img

    def apply_vignette(image_path):
            
            imgv = Image.open(image_path).convert("RGBA")
            radius = float(input("Enter the radius for the vignette effect in % (1% = 0.01) (0.01 to 1.00): ").strip())
            width, height = imgv.size

           

    
            # Create a vignette mask
            mask = Image.new("L", (width, height), 0)
            for x in range (width):
                for y in range (height):
                    distance = np.sqrt((x - width / 2) ** 2 + (y - height / 2) ** 2)
                    mask.putpixel((x, y), int(255 * (1 - min(distance / (radius * min(width, height)), 1))))

            mask = mask.filter(ImageFilter.GaussianBlur(radius=radius * 10))
            imgv.putalpha(mask)
    
            imgv.show()
            
        
            return img
    
    def apply_sharpness(image_path):
        img2 = Image.open (image_path).convert("RGBA")
        sharpness = float(input("Enter the sharpness level in % (1% = 0.01): (0.01 to 1.00): ").strip())
        enhancer = ImageEnhance.Sharpness(img2)
        sharpened_img = enhancer.enhance(sharpness)
        
        sharpened_img.show()
       

        return sharpened_img
    
    def apply_blur(image_path):
        img1 = Image.open(image_path).convert("RGBA")
        blur = float(input("Enter the blur level in % (1% = 0.01): (0.01 to 1.00): ").strip())
        blurred_img = img1.filter(ImageFilter.BLUR)
        blurred_img.show()
        return blurred_img
    
    def apply_sepia(image_path):
        img3 = Image.open(image_path).convert("RGB") 
    
        sepia_filter = np.array([[0.393, 0.769, 0.189],
                            [0.349, 0.686, 0.168],
                            [0.272, 0.534, 0.131]])

        img_array = np.array(img3)
    
        sepia_img = img_array @ sepia_filter.T
    
        sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)
    
        sepia_result = Image.fromarray(sepia_img, "RGB")
        sepia_result.show()
        return sepia_result
    def apply_fishEye(image_path):
        img4 = Image.open(image_path).convert("RGB")
        img_array = np.array(img4)
        height, width = img_array.shape[:2]
        y, x = np.ogrid[:height, :width]
        center_x, center_y = width // 2, height // 2

        dx = x- center_x
        dy = y - center_y
        distance = np.sqrt(dx**2 + dy**2)
        max_distance = min(center_x, center_y)
        normalised_distance = distance / max_distance
        strength = float(input("Enter the strength of the fisheye effect in % (1% = 0.01) (0.01 to 1.00): ").strip())
        distorted_distance = normalised_distance * (1 + strength * normalised_distance**2)

        scale = np.where(distance > 0, distorted_distance / normalised_distance, 1)
        new_x = (dx * scale + center_x).astype(int)
        new_y = (dy * scale + center_y).astype(int)

        new_x = np.clip(new_x, 0, width - 1)
        new_y = np.clip(new_y, 0, height - 1)

        fisheye_array = img_array[new_y, new_x]
        fisheye_result = Image.fromarray(fisheye_array, "RGB")
        fisheye_result.show()
        return fisheye_result

    def apply_pixelate(image_path):
        img5 = Image.open(image_path).convert("RGB")
        img_array = np.array(img5)
        pixel_size = int(input("Enter the pixelation size (e.g., 10 for 10x10 pixels): ").strip())
        height, width = img_array.shape[:2]
        pixelated_array = img_array.copy()
        for y in range(0, height, pixel_size):
            for x in range(0, width, pixel_size):
                block = img_array[y:y + pixel_size, x:x + pixel_size]
                avg_color = block.mean(axis=(0, 1)).astype(int)
                pixelated_array[y:y + pixel_size, x:x + pixel_size] = avg_color
        pixelated_result = Image.fromarray(pixelated_array, "RGB")
        pixelated_result.show()
        return pixelated_result
        

    def apply_colorblind(image_path):
        img6 = Image.open(image_path).convert("RGB")
        colorblind_filter = np.array([[0.567, 0.433, 0],
                                     [0.558, 0.442, 0],
                                     [0.241, 0.759, 0]])
        img_array = np.array(img6)

        colorblind_img = img_array @ colorblind_filter.T
        colorblind_img = np.clip(colorblind_img, 0, 255).astype(np.uint8)
        colorblind_result = Image.fromarray(colorblind_img, "RGB")
        colorblind_result.show()
        return colorblind_result

    def apply_grayscale(image_path):
        img7 = Image.open(image_path).convert("L")
        grayscale_result = img7.convert("RGB")
        grayscale_result.show()
        return grayscale_result
    
    def apply_negative (image_path):
        img8 = Image.open(image_path).convert("RGB")
        img_array = np.array(img8)
        negative_array = 255 - img_array
        negative_array = np.clip(negative_array, 0, 255).astype(np.uint8)
        negative_result = Image.fromarray(negative_array, "RGB")
        negative_result.show()
        return negative_result
    
    def apply_opium(image_path):
        img9 = Image.open(image_path).convert("RGB")
        img_array = np.array(img9)
        height, width = img_array.shape[:2]

        y,x = np.ogrid[:height, :width]
        center_x, center_y = width // 2, height // 2

        max_distance = np.sqrt((width/2)**2 + (height/2)**2)
        distance = np.sqrt((x - center_x)**2 + (y - center_y)**2) / max_distance
        power = float(input("Enter the power of the opium effect in % (1% = 0.01) (0.01 to 1.00): ").strip())
        

        red_stain = distance**2 * power* 80

        angle = np.arctan2(y - center_y, x - center_x)
        pink_stain = (distance**1.5) * power * 60 * (1 + 0.5 * np.sin(angle * 3))

        orange_stain = (distance ** 1.5) * power * 70 * (1 + 0.3 * np.cos(angle * 2))
        blue_stain = (distance ** 1.5) * power * 50 * (1 + 0.4 * np.sin(angle * 4))

        img_array[:, :, 0] = np.clip(img_array[:,:,0] +red_stain  + orange_stain * 0.8 + blue_stain * 0.5, 0, 255)
        img_array[:, :, 1] = np.clip(img_array[:,:,1] + pink_stain * 0.4 + orange_stain * 0.8, 0, 255)
        img_array[:, :, 2] = np.clip(img_array[:,:,2] * 0.8 + pink_stain * 0.3, 0, 255)

        result_array = img_array.astype(np.uint8)
        opium_result = Image.fromarray(result_array, "RGB")
        opium_result.show()
        return opium_result

    choose = input("Choose an effect to apply (blur / colorblind / fisheye / grayscale / negative / opium / pixelate / sepia / sharpness / uv / vignette): ").strip().lower()
    if choose == "blur":
        apply_blur(filename)
    if choose == "sharpness":
        apply_sharpness(filename)
    elif choose == "uv":
        apply_uv_filter(filename)
    elif choose == "vignette":
        apply_vignette(filename)
    elif choose == "sepia":
        apply_sepia(filename)
    elif choose == "fisheye":
        apply_fishEye(filename)
    elif choose == "pixelate":
        apply_pixelate(filename)
    elif choose == "colorblind":
        apply_colorblind(filename)
    elif choose == "grayscale":
        apply_grayscale(filename)
    elif choose == "negative":
        apply_negative(filename)
    elif choose == "opium":
        apply_opium(filename)
    
    
    else:
        print("Invalid choice. Please choose either 'vignette' or 'uv' or 'sharpness' or 'blur' or 'sepia' or 'fisheye'or 'pixelate' or 'colorblind'.")
    save_choice = input("Do you want to save the modified image? (yes/no): ").strip().lower()
    if save_choice == "yes":
        save_filename = input("Enter the name to save the modified image (with extension): ").strip()
        exit()

