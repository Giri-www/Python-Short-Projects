from django.shortcuts import render

# Create your views here.

from constants import *
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import request
from django.db import transaction, connection
import os, logging, requests
from myapp.views import Redis
from rest_framework import status
# from api_app.models import Redis
logger = logging.getLogger(__name__)


@api_view(['POST'])
def add_data(request):
    ec = []
    try:
        data = request.data
        email_address = data.get('email_address')
        phone = data.get('phone')
        city = data.get('city')
        # id = data.get('id')
        logger.info("============= Starting ==========")
        redis_obj = Redis()
        logger.info("object creations")
        connect = redis_obj.redis_connect(email_address,phone,city)
        if connect:
            logger.info("Connect SucessFully")
            return Response("Connection Successfulyy Established....")
    except Exception as e:
        ec.append("THIS IS COONECTION ERROR EXCEPTION")
        logger.exception("========= CONNECTION Error Exception ==========")
        
        return Response({"Errors": ec}, status=status.HTTP_400_BAD_REQUEST)
    finally:    
        logger.info("Database connection is closed")


@api_view(['POST'])
def fetch_data(request):
    ec = []
    try:
        data = request.data
        email_address = data.get('email_address')
        # phone = data.get('phone')
        # city = data.get('city')
        # # id = data.get('id')
        logger.info("============= Starting ==========")
        redis_obj = Redis()
        logger.info("object creations")
        connect = redis_obj.get_data_redis(email_address)
        if connect:
            logger.info(connect)
            
            return Response(connect)
    except Exception as e:
        ec.append("THIS IS COONECTION ERROR EXCEPTION")
        logger.exception("========= CONNECTION Error Exception ==========")
        
        return Response({"Errors": ec}, status=status.HTTP_400_BAD_REQUEST)
    finally:    
        logger.info("Database connection is closed")
