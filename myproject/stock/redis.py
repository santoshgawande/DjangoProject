import redis
r=redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)
r.set('foo','bar')
r.set('san', 'santy')
#True
r.get('foo')
#bar