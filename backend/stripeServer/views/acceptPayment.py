from rest_framework import status, generics, mixins, request, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import exception_handler
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
import datetime
from django.utils import timezone
import requests
from rest_framework.request import Request
import stripe
import jsonify

@api_view(['POST'])
def paymentSheet():
    stripe.api_key = 'sk_test_51L08MiHqfk1hk8aABrqHYR0aGbxNY3YkKdSmX8VRRSKEVUTmYnvfxert4KnNnAh1R2qSbyRpKiohlYpG8Nfk89vB00W13HuLdg'
    customer = stripe.Customer.create() 
    ephermalKey = stripe.EphemeralKey.create(
        customer = customer['id'],
        stripe_version='2020-08-27',
    )

    paymentIntent = stripe.PaymentIntent.create(
        amount = 19999,
        currency = 'usd',
        customer = customer['id'],
        automatic_payment_methods ={
            'enabled': True,
        },
    )

    return jsonify(paymentIntent= paymentIntent.client_secret,
                    ephermalKey=ephermalKey.secret,
                    customer=customer.id, 
                    publishableKey = 'pk_test_51L08MiHqfk1hk8aAaDVQJEgT327VqDZawac4lYNOzcMxD6q1YFaZzxZhAWnZjRkMkBESSX5x0Rn8wOrTnltQmueD00VW6O02dT')