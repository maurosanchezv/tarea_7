from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DIC Almacenar")
for i in range(10):
    Item("SSD de 2.5 pulgadas", 13370, seller)
    Item("HDD de 3.5 pulgadas", 10980, seller)
    Item("CPU", 40830, seller)
    Item("Refrigerador de CPU", 13400, seller)
    Item("SSD M.2", 12980, seller)
    Item("Caja de PC", 8727, seller)
    Item("Tarjeta gráfica", 23800, seller)
    Item("Placa madre", 28980, seller)
    Item("Memoria", 13880, seller)
    Item("Fuente de alimentación", 8980, seller)

print("🤖 Por favor, introduce tu nombre")
customer = Customer(input())

print("🏧 Por favor, introduce la cantidad a recargar en tu billetera")
customer.wallet.deposit(int(input()))

print("🛍️ Comenzando compras")
end_shopping = False

while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Por favor, introduce el número del producto")
    number = int(input())

    print("⛏ Por favor, introduce la cantidad del producto")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)

    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Monto total: {customer.cart.total_amount()}")

    if customer.wallet.balance < customer.cart.total_amount():
        print("No tienes suficiente saldo en la billetera para comprar más productos.")
        print("¿Deseas recargar tu billetera? (si/no)")
        if input().lower() == "si":
            print("🏧 Por favor, introduce la cantidad a recargar en tu billetera")
            customer.wallet.deposit(int(input()))
            continue 

        break

    print("😭 ¿Deseas finalizar las compras? (si/no)")
    end_shopping = input().lower() == "si"

if end_shopping:
    print("💸 ¿Deseas confirmar la compra? (si/no)")
    if input().lower() == "si":
        customer.cart.check_out()

    print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultados ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
    print(f"️🛍️ ️Productos de {customer.name}")
    customer.show_items()
    print(f"😱👛 Saldo en la billetera de {customer.name}: {customer.wallet.balance}")

    print(f"📦 Estado del inventario de {seller.name}")
    seller.show_items()
    print(f"😻👛 Saldo en la billetera de {seller.name}: {seller.wallet.balance}")

    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🌚 Monto total: {customer.cart.total_amount()}")

print("🎉 Fin")