from PIL import Image, ImageFilter



# filename = "Smile.png"
filename = input("Enter the image file name (with extension): ").strip()
with Image.open(filename) as img:

    filters = ["CMYK", "RGB", "L", "BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EMBOSS", "FIND_EDGES", "SHARPEN", "SMOOTH", "SMOOTH_MORE"]
    fIlter = input("Enter filter you want to apply (CMYK, RGB, L, BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EMBOSS, FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE): ").strip().upper()
    if fIlter not in filters:
        print("Invalid filter. Please choose from CMYK, RGB, or L!!!")
        exit(1)
    if fIlter == "CMYK":
        converted_img = img.convert("CMYK")
        img.save("converted_image.png", "PNG")
        converted_img.show()
    elif fIlter == "RGB":
        converted_img = img.convert("RGB")
        img.save("converted_image.png", "PNG")
        converted_img.show()
    elif fIlter == "L":
        converted_img = img.convert("L")
        img.save("converted_image.png", "PNG")
        converted_img.show()
    elif fIlter == "BLUR":
        blurred_img = img.filter(ImageFilter.BLUR)
        blurred_img.save("blurred_image.png", "PNG")
        blurred_img.show()
    elif fIlter == "CONTOUR":
        contoured_img = img.filter(ImageFilter.CONTOUR)
        contoured_img.save("contoured_image.png", "PNG")
        contoured_img.show()
    elif fIlter == "DETAIL":
        detailed_img = img.filter(ImageFilter.DETAIL)
        detailed_img.save("detailed_image.png", "PNG")
        detailed_img.show()
    elif fIlter == "EDGE_ENHANCE":
        edge_enhanced_img = img.filter(ImageFilter.EDGE_ENHANCE)
        edge_enhanced_img.save("edge_enhanced_image.png", "PNG")
        edge_enhanced_img.show()
    elif fIlter == "EMBOSS":
        embossed_img = img.filter(ImageFilter.EMBOSS)
        embossed_img.save("embossed_image.png", "PNG")
        embossed_img.show()
    elif fIlter == "FIND_EDGES":
        edges_img = img.filter(ImageFilter.FIND_EDGES)
        edges_img.save("edges_image.png", "PNG")
        edges_img.show()
    elif fIlter == "SHARPEN":
        sharpened_img = img.filter(ImageFilter.SHARPEN)
        sharpened_img.save("sharpened_image.png", "PNG")
        sharpened_img.show()
    elif fIlter == "SMOOTH":
        smoothed_img = img.filter(ImageFilter.SMOOTH)
        smoothed_img.save("smoothed_image.png", "PNG")
        smoothed_img.show()
    elif fIlter == "SMOOTH_MORE":
        smoothed_more_img = img.filter(ImageFilter.SMOOTH_MORE)
        smoothed_more_img.save("smoothed_more_image.png", "PNG")
        smoothed_more_img.show()
    else:
        print("Invalid filter. Please choose from CMYK, RGB, or L!!!")
        exit(1)


