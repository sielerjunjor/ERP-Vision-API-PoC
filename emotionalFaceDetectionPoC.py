from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
  'LIKELY', 'VERY_LIKELY')
for pic in ('face_surprise.jpg', 'face_no_surprise.png'):
  image.source.image_uri = 'gs://cloud-vision-codelab/'+pic
    resp = client.face_detection(image=image)
  faces = resp.face_annotations
  for face in faces:
    print(pic + ': surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
