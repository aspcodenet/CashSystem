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
    print("KASSA")
    print("--- kvitto --- ")
    print("Kommandon:")
    print("<productid> <antal>")
    print("PAY")
    kommando = input("Kommando:")
    if kommando == "PAY":
        #skriva till en fil
        return
    





while True:
    print("KASSA")
    print("1. Ny kund")
    print("0. Avsluta")
    sel = getInputBetween(0,1)
    if sel == 0:
        break
    if sel == 1:
        startNewReceipt()
        
