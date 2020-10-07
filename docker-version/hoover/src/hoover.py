import os
import time


class Hoover():

    def __init__(self):
        self.rabbitmqUser = os.environ['RABBITMQ_DEFAULT_USER']
        self.rabbitmqPasswd = os.environ['RABBITMQ_DEFAULT_USER']
        self.srv = ('camera')

    def start(self):
        print("toto")
        print(self.rabbitmqUser)
        print(self.rabbitmqPasswd)
        time.sleep(3600)



if __name__ == '__main__':
    hoover = Hoover()
    hoover.start()
