from ownable import Ownable
from user import User
from cart import Cart

class Customer(User, Ownable):

    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)  # Cuando se crea una instancia de Cliente, tiene un carrito con sí mismo como propietario.