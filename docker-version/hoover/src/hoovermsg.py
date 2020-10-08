import pika

class msg():
  
    def __init__(self, msgName)::
        self.rabbitmqUser = os.environ['RABBITMQ_DEFAULT_USER']
        self.rabbitmqPasswd = os.environ['RABBITMQ_DEFAULT_USER']
        self.msgName = msgName
        channel.queue_declare(queue=self.msgName)
        
    def listen(self, callback):
        channel.basic_consume(queue=self.msgName,
                      auto_ack=True,
                      on_message_callback=callback)
                      
    def send(seld, msg):
        channel.basic_publish(exchange='',
                      routing_key=self.msgName,
                      body=msg)
        
        
  
