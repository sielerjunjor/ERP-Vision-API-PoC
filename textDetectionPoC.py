from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = 'https://cdn.shopify.com/s/files/1/0229/0851/products/YAB_Large_Yard_Sign_1024x1024.JPG?v=1494952307'
resp = client.text_detection(image=image)
print('\n'.join([d.description for d in resp.text_annotations]))
