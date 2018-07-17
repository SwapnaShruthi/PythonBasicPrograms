for quant in range(99, 0, -1):
    if quant>1:
        print(quant, "Bottles of beer on the wall", quant," bottles of beer")
        if quant==50:
            break
        elif quant>2:
            continue
            suffix= str(quant)+" bottles of beer on the wall"
        else:
            suffix="1 bottle of beer in the wall"
    elif quant==1:
        print("1 Bottle of beer on the wall 1 bottle of beer")
        suffix="No more beer on the wall"
    
    print("Take one down and pass it around", suffix)
    print("--------")