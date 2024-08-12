from django.shortcuts import render
from constants import *
import os, logging
import redis
logger = logging.getLogger(__name__)
# Create your views here.
class Redis:
    # redis = Redis()
    def __init__(self):
        self.redis_client = redis.Redis(host=REDISHOST, port=REDISPORT, password=REDISPASSWORD, charset=UTF8, decode_responses=True)
    def redis_connect(self,email_address,phone,city):
        try:
            result = None
            logger.info("Trying to connect Redis Cluster")
            # HOW TO CONNECT
            # r = redis.Redis(host=REDISHOST, port=REDISPORT, password=REDISPASSWORD, charset=UTF8, decode_responses=True)
            r = redis.Redis(host=REDISHOST, port=REDISPORT, password=REDISPASSWORD, charset=UTF8, decode_responses=True)
    
            # Elasticache
            # r = redis.Redis(host=REDISHOST, port=REDISPORT, ssl=True, username=REDISUSERNAME, password=REDISPASSWORD, charset=UTF8, decode_responses=True)
            if r.ping():
                logger.info("Connected to Redis Server")
            if email_address is None and phone is None and city is None:
                raise Exception("Email / Phone Not Provided for Redis")
            # r.set(email_address, phone)
            lop = "ok"
            # r.set(email_address,city,phone,lop)
            self.redis_client.hmset(email_address, {
                'city': city,
                'phone': phone,
                'email_address': email_address
            })
            # r.set(email_address,city)
            # r.set(city,phone)
            result = True
            return r
        except Exception as e:
            logger.exception(e)
            return 1
        finally:
            r.close()
            return result
            
    # def get_data_redis(self, email_address=None):
    #     try:
    #         if email_address is None:
    #             raise Exception("Email Not Provided for Redis")

    #         r = redis.Redis(host=REDISHOST, port=REDISPORT, password=REDISPASSWORD, charset=UTF8, decode_responses=True)
            
    #         if not r.ping():
    #             raise Exception("Redis server is not reachable")
    #         logger.info("Connected to Redis Server")
    #         # result = r.get(email_address)
    #         result = r.hgetall(email_address)
    #         logger.info(result)
    #     except Exception as e:
    #         logger.exception(e)
    #         result = None
    #     finally:
    #         r.close()
    #         return result

    def get_data_redis(self, email_address=None):
        try:
            if email_address is None:
                raise Exception("Email Not Provided for Redis")

            if not self.redis_client.ping():
                raise Exception("Redis server is not reachable")
            
            logger.info("Connected to Redis Server")

            # Check key type
            key_type = self.redis_client.type(email_address)
            logger.info(f"Key type for {email_address}: {key_type}")

            if key_type == 'hash':
                result = self.redis_client.hgetall(email_address)
            elif key_type == 'string':
                result = {"value": self.redis_client.get(email_address)}
            else:
                raise Exception(f"Unsupported key type: {key_type}")

            logger.info(result)
            return result
        except Exception as e:
            logger.exception(e)
            return None
        finally:
            self.redis_client.close()