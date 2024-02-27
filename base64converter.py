import base64



def CustomInMemoryBase64Converter(image_path):
    read_image = image_path.read()
    print(type(read_image))
    image_data = base64.b64encode(read_image).decode('utf-8')
    return image_data