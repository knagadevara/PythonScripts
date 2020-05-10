#!/usr/bin/python3.6


testbit = input("Please Enter if you want to convert Dolar to Rupee or Rupee to Dolar? \n Enter D for Dollar or R for Rupee: ")

while testbit :
    testbit = input("Please Enter if you want to convert Dolar to Rupee or Rupee to Dolar? \n Enter D for Dollar or R for Rupee: ")
    print("Please Type either D or R\n")
    if testbit == "D" or testbit == "R" :
        if testbit == "D" :
            print("\nConverting Dollar to Rupee\n")
            amount = float(input("\nKindly enter the Dollars to convert: "))
            D_ = 65
            aft_con = round(amount*D_,2)
            print(f"\n{amount}$ is around {aft_con}Rs.\n")
            testbit=''
        else:
            print("\nConverting Rupee to Dollar\n")
            amount = float(input("\nKindly enter the Rupees to convert: "))
            D_ = 65
            aft_con = round(amount/D_,2)
            print(f"\n{amount}Rs is around {aft_con}$.\n")
            testbit=''
    else:
        print("Kndly-rerun, with correct value")
        #continue