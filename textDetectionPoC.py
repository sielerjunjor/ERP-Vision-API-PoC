from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = 'gs://cloud-vision-codelab/otter_crossing.jpg'
resp = client.text_detection(image=image)
print('\n'.join([d.description for d in resp.text_annotations]))
