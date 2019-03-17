from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = 'https://cloud.google.com/vision/docs/images/bicycle.jpg'

objects = client.object_localization(
        image=image).localized_object_annotations

print('Number of objects found: {}'.format(len(objects)))

for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
