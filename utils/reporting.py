import math

def print_dim (dim_name, dim):
    dim = round(dim, 2)
    dim_ft = math.floor(dim/12)
    dim_in = round(dim - dim_ft * 12, 2)
    print(f'{dim_name}: {dim}"\t|\t{dim_ft}\'{dim_in}"')
