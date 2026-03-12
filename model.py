
def produit(T):
    S = 1
    for t in T:
        S *= t
    return S
Data = [1,3,5]
Prod = math.prod(Data)
print("le produit est :", Prod)

