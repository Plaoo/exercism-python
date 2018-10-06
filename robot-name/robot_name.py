import random
import string
import datetime

class Robot(object):

    def __init__(self):
        self.reset()
    
    def reset(self):
        self.name = Robot.random_name()

    def random_name():
        random.seed(datetime.datetime.now())
        alf = string.ascii_uppercase
        prefix = ''.join(random.sample(alf, 2))
        suffix = str(random.randrange(100,999))
        name = prefix + suffix
        return name