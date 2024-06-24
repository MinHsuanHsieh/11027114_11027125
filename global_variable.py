from flask import g, Flask, request, abort, session
import redis
global_user_id = None
SESSION = redis.Redis(host='localhost', port=6379, decode_responses=True, db=0)