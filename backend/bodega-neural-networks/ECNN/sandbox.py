"""
Bodega Vision Source Code

Three modules:

1. Collection -- Collecting response data from Azure Congnitive Services
2. Processing & Storage -- Cleaning the data + Storing data by productID keys on metauserID key
3. Analysis -- Showing actionable insights 


Collection:
1. Build a boilerplate CNN Ui which takes images and shows metadata

Processing & Storage:
1. Fetch all product images by metauserID key
2. Make this a 30 day cron job 
3. Store all the data in BodegaVision Table by metauserID 
4. Acheive 3rd point via a POST request to keep data flow clean and independent

Analysis:
1. Sort data based on most used buckets 
2. Show data on what other BodegaVision tables / metausers are creating 
"""


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
endpoint = "https://bodega-vision.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(
    endpoint, CognitiveServicesCredentials(subscription_key))

remote_image_url = "https://i.guim.co.uk/img/media/fad91f7c52cfeb31ac395dabf11307d0afe52c4d/79_119_4491_2695/master/4491.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=2e5fa0230bfb87df7c859239651356cf"

'''
Describe an Image - remote
This example describes the contents of an image with the confidence score.
'''
print("===== BODEGA VISION AI PROCESSING! ======= \n")
# Call API
description_results = computervision_client.describe_image(remote_image_url)

# Get the captions (descriptions) from the response, with confidence level
print("Description of Image: ")
if (len(description_results.captions) == 0):
    print("No description detected.")
else:
    for caption in description_results.captions:
        print("===== BODEGA VISION AI RESULT =======\n")
        print("'{}' with confidence {:.2f}% \n".format(
            caption.text, caption.confidence * 100))


'''
Categorize an Image - remote
This example extracts (general) categories from a remote image with a confidence score.
'''
print("===== Doing further computation - hold on =====\n")
# Select the visual feature(s) you want.
remote_image_features = ["categories"]
# Call API with URL and features
categorize_results_remote = computervision_client.analyze_image(
    remote_image_url, remote_image_features)

# Print results with confidence score
print("Sorting Image in buckets: ")
if (len(categorize_results_remote.categories) == 0):
    print("No categories detected.")
else:
    for category in categorize_results_remote.categories:
        print("'{}' with confidence {:.2f}%\n".format(
            category.name, category.score * 100))


'''
Tag an Image - remote
This example returns a tag (key word) for each thing in the image.
'''
print("===== TAGGING IMAGE NOW=====\n")
# Call API with remote image
tags_result_remote = computervision_client.tag_image(remote_image_url)

# Print results with confidence score
print("Here's what I think this image is: \n")
if (len(tags_result_remote.tags) == 0):
    print("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}%".format(
            tag.name, tag.confidence * 100))


'''
Detect Objects - remote
This example detects different kinds of objects with bounding boxes in a remote image.
'''
print("===== Detect Location of Objects - ===== \n")
# Get URL image with different objects
remote_image_url_objects = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg"
# Call API with URL
detect_objects_results_remote = computervision_client.detect_objects(
    remote_image_url_objects)

# Print detected objects results with bounding boxes
print("Detecting objects in remote image:")
if len(detect_objects_results_remote.objects) == 0:
    print("No objects detected.")
else:
    for object in detect_objects_results_remote.objects:
        print("object at location {}, {}, {}, {}".format(
            object.rectangle.x, object.rectangle.x + object.rectangle.w,
            object.rectangle.y, object.rectangle.y + object.rectangle.h))


'''
Detect Brands - remote
This example detects common brands like logos and puts a bounding box around them.
'''
print("\n===== Detect Brands - remote =====\n")
# Get a URL with a brand logo

# Select the visual feature(s) you want
remote_image_features = ["brands"]
# Call API with URL and features
detect_brands_results_remote = computervision_client.analyze_image(
    remote_image_url, remote_image_features)

print("Detecting brands in remote image: ")
if len(detect_brands_results_remote.brands) == 0:
    print("No brands detected.")
else:
    for brand in detect_brands_results_remote.brands:
        print("'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}".format(
            brand.name, brand.confidence *
            100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w,
            brand.rectangle.y, brand.rectangle.y + brand.rectangle.h))


'''
Detect Adult or Racy Content - remote
This example detects adult or racy content in a remote image, then prints the adult/racy score.
The score is ranged 0.0 - 1.0 with smaller numbers indicating negative results.
'''
print("\n===== Detect Adult or Racy Content - remote =====\n")
# Select the visual feature(s) you want
remote_image_features = ["adult"]
# Call API with URL and features
detect_adult_results_remote = computervision_client.analyze_image(
    remote_image_url, remote_image_features)

# Print results with adult/racy score
print("Analyzing remote image for adult or racy content ... \n")
print("Is adult content: {} with confidence {:.2f}".format(
    detect_adult_results_remote.adult.is_adult_content, detect_adult_results_remote.adult.adult_score * 100))
print("Has racy content: {} with confidence {:.2f}".format(
    detect_adult_results_remote.adult.is_racy_content, detect_adult_results_remote.adult.racy_score * 100))


'''
Detect Color - remote
This example detects the different aspects of its color scheme in a remote image.
'''
print("\n===== Detect Color - remote =====\n")
# Select the feature(s) you want
remote_image_features = ["color"]
# Call API with URL and features
detect_color_results_remote = computervision_client.analyze_image(
    remote_image_url, remote_image_features)

# Print results of color scheme
print("Getting color scheme of the remote image:\n ")
print("Is black and white: {}".format(
    detect_color_results_remote.color.is_bw_img))
print("Accent color: {}".format(detect_color_results_remote.color.accent_color))
print("Dominant background color: {}".format(
    detect_color_results_remote.color.dominant_color_background))
print("Dominant foreground color: {}".format(
    detect_color_results_remote.color.dominant_color_foreground))
print("Dominant colors: {}".format(
    detect_color_results_remote.color.dominant_colors))


'''
Detect Domain-specific Content - remote
This example detects celebrites and landmarks in remote images.
'''
print("\n===== Detect Domain-specific Content - remote =====\n")
# URL of one or more celebrities
remote_image_url_celebs = remote_image_url
# Call API with content type (celebrities) and URL
detect_domain_results_celebs_remote = computervision_client.analyze_image_by_domain(
    "celebrities", remote_image_url_celebs)

# Print detection results with name
print("Celebrities in the remote image:")
if len(detect_domain_results_celebs_remote.result["celebrities"]) == 0:
    print("No celebrities detected.")
else:
    for celeb in detect_domain_results_celebs_remote.result["celebrities"]:
        print(celeb["name"])

# Call API with content type (landmarks) and URL
detect_domain_results_landmarks = computervision_client.analyze_image_by_domain(
    "landmarks", remote_image_url)
print()

print("\nLandmarks in the remote image:")
if len(detect_domain_results_landmarks.result["landmarks"]) == 0:
    print("No landmarks detected.")
else:
    for landmark in detect_domain_results_landmarks.result["landmarks"]:
        print(landmark["name"])


'''
Detect Image Types - remote
This example detects an image's type (clip art/line drawing).
'''
print("===== Detect Image Types - remote =====")
# Get URL of an image with a type
remote_image_url_type = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/type-image.jpg"
# Select visual feature(s) you want
remote_image_features = [VisualFeatureTypes.image_type]
# Call API with URL and features
detect_type_results_remote = computervision_client.analyze_image(
    remote_image_url_type, remote_image_features)

# Prints type results with degree of accuracy
print("Type of remote image:")
if detect_type_results_remote.image_type.clip_art_type == 0:
    print("Image is not clip art.")
elif detect_type_results_remote.image_type.line_drawing_type == 1:
    print("Image is ambiguously clip art.")
elif detect_type_results_remote.image_type.line_drawing_type == 2:
    print("Image is normal clip art.")
else:
    print("Image is good clip art.")

if detect_type_results_remote.image_type.line_drawing_type == 0:
    print("Image is not a line drawing.")
else:
    print("Image is a line drawing")
