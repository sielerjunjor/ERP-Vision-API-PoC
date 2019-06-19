from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
#image.source.image_uri = 'gs://cloud-vision-codelab/eiffel_tower.jpg'
image.source.image_uri = 'https://www.leipzig.de/fileadmin/_processed_/0/c/csm_Voelkerschlachtdenkmal-blauer-Himmel_LTM_andreas_schmidt-themenbild_eee72a3423.jpg'
resp = client.landmark_detection(image=image)
print(resp.landmark_annotations)
