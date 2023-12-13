equation = input("Enter the quadratic equation (in the form 'ax^2-bx-c'): ")


def has_real_roots(y):
    # Split the equation into a, b, and c
    a_str, b_str, c_str = y.split(',')

    # Convert string coefficients to integers
    a = int(a_str.strip())
    b = int(b_str.strip())
    c = int(c_str.strip())

    # Calculate the discriminant
    disc = b * b - 4 * a * c

    # Check if the discriminant is non-negative
    return disc >= 0


print(has_real_roots(equation))