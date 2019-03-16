from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = 'gs://cloud-vision-codelab/eiffel_tower.jpg'
resp = client.landmark_detection(image=image)
print(resp.landmark_annotations)
