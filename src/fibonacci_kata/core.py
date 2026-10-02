def fibonacci(n: int) -> int:
    """
    Compute the n-th term of the Fibonacci sequence using the Fast Doubling Algorithm.

    Args:
        n (int): Index of the desired term (must be a positive integer or zero)

    Returns:
        int: Value of F(n)

    Raises:
        TypeError: If n is not an integer or a boolean
        ValueError: If n is negative
    """

    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be positive or null")

    a, b = 0, 1

    for bit in bin(n)[2:]:
        a2 = a * a
        b2 = b * b

        c = a * (2 * b - a)
        d = a2 + b2

        if bit == "0":
            a, b = c, d
        else:
            a, b = d, c + d

    return a
