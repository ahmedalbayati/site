bind = '0.0.0.0:80'
backlog = 2048
workers = 12
worker_class = 'geventwebsocket.gunicorn.workers.GeventWebSocketWorker'
worker_connections = 1000
timeout = 30
keepalive = 2
accesslog = '-'
