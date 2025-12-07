#How many such routes are there through a 20 ×20 grid(only able to move to the right and down)?

def n_choose_r(n, r):
    result = 1
    for i in range(r):
         result = result * (n - i) // (i + 1)
    return result

def lattice_paths(n):
     return n_choose_r(2 * n, n)

paths = lattice_paths(20)
print(paths)