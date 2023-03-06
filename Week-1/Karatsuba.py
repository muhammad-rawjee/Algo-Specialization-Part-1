def Karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    else:
        string_x = str(x)
        string_y = str(y)

        n = max(len(string_x), len(string_y))
        n_divide_by_two = n // 2

        a = x // 10**(n_divide_by_two)
        b = x % 10**(n_divide_by_two)

        c = y // 10**(n_divide_by_two)
        d = y % 10**(n_divide_by_two)

        multiply_ac = Karatsuba(a, c)
        multiply_bd = Karatsuba(b, d)

        adbc = Karatsuba(a+b,c+d)

        ad_plus_bc = adbc - multiply_ac - multiply_bd

        final_result = (multiply_ac * (10**(n_divide_by_two*2))) + ((10**n_divide_by_two) * ad_plus_bc)  + multiply_bd

        return final_result
    

print(Karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))





