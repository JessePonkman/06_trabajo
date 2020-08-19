from repositorios import Repositorios


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
