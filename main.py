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
    
    choose = input("Choose an effect to apply (blur / sharpness / uv / vignette): ").strip().lower()
    if choose == "blur":
        apply_blur(filename)
    if choose == "sharpness":
        apply_sharpness(filename)
    elif choose == "uv":
        apply_uv_filter(filename)
    elif choose == "vignette":
        apply_vignette(filename)
    
    
    else:
        print("Invalid choice. Please choose either 'vignette' or 'uv' or 'sharpness' or 'blur' .")
        exit()

