import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here

    if x == 0: 
        return -1
    m = len(g_coeffs)
    n = len(h_coeffs)
    gx = 0.0
    df_gx = 0.0
    hx = 0.0
    df_hx = 0.0
    for i in range(m):
        gx += g_coeffs[i] * (x**(m-i))
        if 1 - i >= 0:
            df_gx += (m -1 -i) * g_coeffs[i] * (x ** (m -1 -i))
    for i in range(n):
        hx += h_coeffs[i] * (x**(n-i))
        if 1 - i >= 0:
            df_hx += (n - 1 -i) * h_coeffs[i] * (x ** (n - 1 -i))

    return (df_gx * hx - gx * df_hx)/hx **2