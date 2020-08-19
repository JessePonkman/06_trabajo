from repositorios import Repositorios
import random
from producto import Producto


class ProductoService:
    def add_producto(self, prod=None):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        lastKey += 1
        Repositorios.productosList[lastKey] = prod.__dict__
        return lastKey

    def delete_producto(self, key):
        if key in Repositorios.productosList:
            del Repositorios.productosList[key]
        else:
            raise ValueError

    def update_producto(self, prod, key):
        if key in Repositorios.productosList:
            del Repositorios.productosList[key]
            Repositorios.productosList[key] = prod.__dict__
        else:
            raise ValueError

    def get_productosList(self):
        pass

    def Iinsertion_sort_precio(self, insertionList, tipoOrden):
        # Este loop ingresa una tupla con la key y el precio
        listPrecios = []
        for i in insertionList:
            listPrecios.append((i, insertionList[i]["_precio"]))

        for i in range(len(listPrecios)):
            while listPrecios[i][1] > listPrecios[i-1][1]:
                listPrecios[i-1][1] = 0

        # Queda ordenar la listPrecios para poder formar el
        # nuevo diccionario
    def insertion_sort_precio(self, original, tipoOrden):
        insertionList = original

        for i in insertionList:
            if i > 0:
                iProd = insertionList[i]
                j = i - 1
                while tipoOrden == "ascendente" and\
                    j >= 0\
                        and iProd["_precio"] < insertionList[j]["_precio"]:
                    insertionList[j+1] = insertionList[j]
                    j -= 1
                while tipoOrden == "descendente" and\
                    j >= 0\
                        and iProd["_precio"] > insertionList[j]["_precio"]:
                    insertionList[j+1] = insertionList[j]
                    j -= 1
                insertionList[j + 1] = iProd
        return insertionList


if __name__ == "__main__":
    serv = ProductoService()
    for i in range(5):
        pro = Producto("A", random.randint(100, 200), "B")
        serv.add_producto(pro)

    print(serv.insertion_sort_precio(Repositorios.productosList, "ascendente"))
