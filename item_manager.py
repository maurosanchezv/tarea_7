# Este módulo te permite manejar las instancias de Item que posees.

from item import Item
from tabulate import tabulate
from itertools import groupby

def items_list(self):   # Devuelve todas las instancias de Item que posees (donde eres el propietario).
    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):   # Devuelve las instancias de Item que posees correspondientes al número especificado, en la cantidad indicada.
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):   # Muestra el estado del inventario de las instancias de Item que posees en formato de tabla con las columnas ["Número", "Nombre del Producto", "Precio", "Cantidad"].
    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["Número", "Nombre del Producto", "Precio", "Cantidad"], tablefmt="grid"))   #Imprime los resultados en formato de tabla utilizando el módulo 'tabulate
def _stock(self):   # Devuelve el estado del inventario de las instancias de Item que posees.
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name): # Clasifica las instancias de Item que devuelven el mismo valor con Item#name.
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})   # En la lista 'items' se almacenan las instancias de Item clasificadas.
    return stock