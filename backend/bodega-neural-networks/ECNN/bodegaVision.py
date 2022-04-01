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

computervision_client = ComputerVisionClient(
    endpoint, CognitiveServicesCredentials(subscription_key))
# auth creds for raven88 / sudo88


"""
Three broader classes  

class bodegaImageCNN --> all details of an image

class bodegaRacyCNN --> all details on racy or adult content

class bodegaNerdsCNN --> all other details
"""


class bodegaImageCNN:
    def __init__(self, remote_image_url, computervision_client):
        self.remote_image_url = remote_image_url
        self.computervision_client = computervision_client
        print("Authentication Success")

    def imageDescription(self):
        print("======== BODEGA IMAGE VISION PROCESSING =========")
        description_results = computervision_client.describe_image(
            self.remote_image_url)
        print("Description of Image: ")
        if (len(description_results.captions) == 0):
            print("No description detected.")
        else:
            for caption in description_results.captions:
                print("===== BODEGA VISION AI RESULT =======\n")
                print("'{}' with confidence {:.2f}% \n".format(
                    caption.text, caption.confidence * 100))

    def executeImageAnalysis(self):
        description_results = computervision_client.describe_image(
            self.remote_image_url)
        description_log = 'WIP'
        categories_log = 'null'
        if (len(description_results.captions) == 0):
            description_log = "No Caption"
            return description_log
        else:
            for caption in description_results.captions:
                description_log = "'{}' with confidence {:.2f}% ".format(
                    caption.text, caption.confidence * 100)
                remote_image_features = ['categories']
                categorize_results = computervision_client.analyze_image(
                    self.remote_image_url, remote_image_features)
                if (len(categorize_results.categories) == 0):
                    return categories_log
                else:
                    for category in categorize_results.categories:
                        categories_log = "'{}' with confidence {:.2f}%\n".format(
                            category.name, category.score * 100)
                        return categories_log

    def tagAnalysis(self):
        tag_results = computervision_client.tag_image(self.remote_image_url)
        tag_log = 'null'
        if (len(tag_results.tags) == 0):
            return tag_log
        else:
            for tag in tag_results.tags:
                tag_log = "'{}' with confidence {:.2f}%".format(
                    tag.name, tag.confidence * 100)
                detect_objects_location = computervision_client.detect_objects(
                    self.remote_image_url)
                for object in detect_objects_location.objects:
                    object_location_log = "object at location {} {} {}".format(
                        object.rectangle.x, object.rectangle.x + object.rectangle.w,
                        object.rectangle.y, object.rectangle.y + object.rectangle.h)
                    return object_location_log


class bodegaRacyCNN:
    def __init__(self, remote_image_url, computervision_client):
        self.remote_image_url = remote_image_url
        self.computervision_client = computervision_client
        print("Authentication Successfull")

    def racyContentAnalysis(self):
        print("========== BODEGA RACY ADULT CNN RUNNING =========")
        racy_log = 'null'
        adult_log = 'null'
        remote_image_features = ["adult"]
        detect_adult_results_remote = computervision_client.analyze_image(
            self.remote_image_url, remote_image_features)

        # Print results with adult/racy score
        print("Analyzing remote image for adult or racy content ... \n")
        print("Is adult content: {} with confidence {:.2f}".format(
            detect_adult_results_remote.adult.is_adult_content, detect_adult_results_remote.adult.adult_score * 100))
        print("Has racy content: {} with confidence {:.2f}".format(
            detect_adult_results_remote.adult.is_racy_content, detect_adult_results_remote.adult.racy_score * 100))
        adult_log = "Is adult content: {} with confidence {:.2f}".format(
            detect_adult_results_remote.adult.is_adult_content, detect_adult_results_remote.adult.adult_score * 100)
        racy_log = "Has racy content: {} with confidence {:.2f}".format(
            detect_adult_results_remote.adult.is_racy_content, detect_adult_results_remote.adult.racy_score * 100)
        analysis_log = "======== BODEGA ADULT ANALYSIS ======== " + \
            adult_log + "============ BODEGA RACY ANALYSIS ========= " + racy_log
        return analysis_log


class bodegaNerdsCNN:
    def __init__(self, remote_image_url, computervision_client):
        self.remote_image_url = remote_image_url
        self.computervision_client = computervision_client
        print("Authentication Successfull")

    def colorAnalysis(self):
        print("======== BODEGA VISION META DATA ========")
        remote_image_features = ['color']
        detect_color_results = computervision_client.analyze_image(
            self.remote_image_url, remote_image_features)
        color_analysis = "Getting color scheme of the remote image: Is black and white: {}".format(
            detect_color_results.color.is_bw_img)
        + "Accent color: {}".format(detect_color_results.color.accent_color)
        + "Dominant background color: {}".format(
            detect_color_results.color.dominant_color_background)
        + "Dominant foreground color: {}".format(
            detect_color_results.color.dominant_color_foreground)
        + "Dominant colors: {}".format(detect_color_results.color.dominant_colors)

        return color_analysis

    def publicData(self):
        print("======= BODEGA VISION PUBLIC DOMAIN =======")
        detect_domain_results_celebs = computervision_client.analyze_image_by_domain(
            "celebrities", self.remote_image_url)
        if len(detect_domain_results_celebs.result == 0):
            pass
        else:
            for celeb in detect_domain_results_celebs.result["celebrities"]:
                celeb_log = celeb["name"]
                return celeb_log

        detect_domain_results_landmarks = computervision_client.analyze_image_by_domain(
            "landmarks", self.remote_image_url)
        if len(detect_domain_results_landmarks == 0):
            pass
        else:
            for landmark in detect_domain_results_landmarks.result['landmarks']:
                landmark_log = landmark["name"]
                return landmark_log
