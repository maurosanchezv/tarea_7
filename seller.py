
from ownable import Ownable
from user import User

class Seller(User, Ownable):
    def __init__(self, name):
        super().__init__(name)
