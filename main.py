
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

    choose = input("Choose an effect to apply (blur / fisheye / sepia / sharpness / uv / vignette): ").strip().lower()
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
    
    
    else:
        print("Invalid choice. Please choose either 'vignette' or 'uv' or 'sharpness' or 'blur' or 'sepia' or 'fisheye'.")
        exit()

