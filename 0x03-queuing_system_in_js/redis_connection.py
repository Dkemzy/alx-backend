import redis

try:
    r = redis.Redis(host='localhost', port=6379)
    response = r.ping()
    print(response)  # Should print "True" if the connection is successful
except redis.ConnectionError:
    print("Failed to connect to Redis")

