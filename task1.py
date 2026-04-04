#hello teacher
def evaluate_polynomial(poly_dict, x):
    p=0
    for key, value in poly_dict.items():
        p=p+value*(x**key)
    return p

