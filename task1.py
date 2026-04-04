#hello teacher
def evaluate_polynomial(poly_dict, x):
    p=0
    for key, value in poly_dict.items():
        p=p+value*(x**key)
    return p
my_poly = {0: -10, 2: 3, 4: 1}
print (evaluate_polynomial(my_poly, 2))
print (evaluate_polynomial(my_poly, -1.5))
