def towerOfHanoi(n, dari, aux, ke):
    if n==0:
        pass
    else:
        towerOfHanoi(n-1, dari, ke, aux)
        print("Memindahkan disk {} dari {} ke {}".format(n, dari, ke))
        towerOfHanoi(n-1, aux, dari, ke)

towerOfHanoi(4, "1", "2", "3")
