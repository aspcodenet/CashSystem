from product import Product

class ProductRegister:

    def __init__(self) :
        self._listOfProducts = []

    def find(self, productid) -> Product:
        for product in self._listOfProducts:
            if product.getProductId() == productid:
                return product
        return None

    def readFromFile(self, path:str):
        pass
        # läs från fil och stoppa in i listan

    def saveToFile(self, path:str):
        pass
        # sparar alla i listan till fil