from PIL import Image, ImageFilter, ImageEnhance
import numpy as np




# filename = "Smile.png"
filename = input("Enter the image file name (with extension): ").strip()
with Image.open(filename) as img:

    def apply_uv_filter(image_path, save_path):

        Image.open(image_path)
        strength  = float( input("Enter the strength of the UV filter (0.1 to 2.0): ").strip())
        r, g, b, _ = img.split()
        b = ImageEnhance.Brightness(b).enhance(strength)
        r = ImageEnhance.Brightness(r).enhance(0.85) 

        
        
        

        filtered_img = Image.merge("RGB", (r, g, b))
        filtered_img.save(save_path)
        filtered_img.show()
        print(f"UV filter applied and saved to {save_path}")


        return filtered_img

    def apply_vignette(image_path, save_path):
            
            img = Image.open(image_path).convert("RGBA")
            radius = float(input("Enter the radius for the vignette effect (0.1 to 1.0): ").strip())
            width, height = img.size

           

    
            # Create a vignette mask
            mask = Image.new("L", (width, height), 0)
            for x in range (width):
                for y in range (height):
                    distance = np.sqrt((x - width / 2) ** 2 + (y - height / 2) ** 2)
                    mask.putpixel((x, y), int(255 * (1 - min(distance / (radius * min(width, height)), 1))))

            mask = mask.filter(ImageFilter.GaussianBlur(radius=radius * 10))
            img.putalpha(mask)
            img.save(save_path)
            img.show()
            print(f"Vignette effect applied and saved to {save_path}")
        
            return img
    
    choose = input("Choose an effect to apply (vignette/uv): ").strip().lower()
    if choose == "vignette":
        apply_vignette(filename, "vignette_image.png")
    elif choose == "uv":
        apply_uv_filter(filename, "uv_filtered_image.png")
    else:
        print("Invalid choice. Please choose either 'vignette' or 'uv'.")
        exit()

