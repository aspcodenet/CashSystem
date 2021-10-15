from ProductRegister import ProductRegister


def getInputBetween(startval: int,endval: int)->int:
    while True:
        try:
            val=int(input("Mata in:"))
            if val >= startval and val <= endval:
                return val
            print(f"Ogiltigt val, mellan {startval} och {endval}, tack")
        except:
            print("Ange ett tal tack!")





def startNewReceipt():
    # ProductRegister 
    productReg = ProductRegister()
    productReg.readFromFile("products.txt")

    print("KASSA")
    print("--- kvitto --- ")
    print("Kommandon:")
    print("<productid> <antal>")
    print("PAY")
    kommando = input("Kommando:")
    if kommando == "PAY":
        #skriva till en fil
        return
    # 300 18
    parts = kommando.split(" ")
    productId = parts[0]

    product = productReg.find(productId)
    if product == None:
        print("Finns ej")
    else:
        print(f"Bra - adding to receipt: {product.getNamn()}")        

    # parts[0] "300"
    # parts[1] "18"





while True:
    print("KASSA")
    print("1. Ny kund")
    print("0. Avsluta")
    sel = getInputBetween(0,1)
    if sel == 0:
        break
    if sel == 1:
        startNewReceipt()
        
