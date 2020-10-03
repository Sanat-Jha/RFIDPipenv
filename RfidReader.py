from BarCode import BarCode                 #Importing barcodemodule
from Rfid import Rfid                 #Importing Rfid module

def main():                     #Defining the main function
    while True:
        reader= Rfid()         #initiate
        barcodeStore= BarCode()  #initiate
        reader.read()
        barcodeStore.add_product()

if __name__ == "__main__":     #code will only run in main file
    main()      #calling the main function


