from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time




subscription_key = "6d2fb313853647cca33e608f11f1b8b4"
endpoint = "https://bodega-vision.cognitiveservices.azure.com"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
#auth creds for raven88 / sudo88

"""
Bodega Face CNN Class

"""


class bodegaFaceCNN:
    def __init__(self, remote_image_url, computervision_client):
        self.remote_image_url = remote_image_url
        self.computervision_client = computervision_client
        face_log = ''
        print("Authentication Success")
        
    
    
    def faceAnalysis(self):
        print("========== BODEGA FACE CNN RUNNING ==========")
        remote_image_features = ["faces"]
        detect_faces_results = computervision_client.analyze_image(self.remote_image_url, remote_image_features)
        if len(detect_faces_results.faces) == 0 :
            pass
        else:
            for face in detect_faces_results.faces:
                self.face_log =   "'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
        face.face_rectangle.left, face.face_rectangle.top, \
        face.face_rectangle.left + face.face_rectangle.width, \
        face.face_rectangle.top + face.face_rectangle.height )
                return self.face_log
            
            
            