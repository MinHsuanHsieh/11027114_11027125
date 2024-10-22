from flask import g, Flask, request, abort, session
import redis
global_user_id = None
BUBBLE_MAX_PAGE = 7
SESSION = redis.Redis(host='localhost', port=6379, decode_responses=True, db=0)