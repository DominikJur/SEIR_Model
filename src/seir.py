def SEIR(
    y: tuple[int], t, n: int, beta: float, sigma: float, gamma: float
) -> list[float]:
    s, e, i, r = y
    ds_dt = -beta * s * i / n
    de_dt = beta * s * i / n - sigma * e
    di_dt = sigma * e - gamma * i
    dr_dt = gamma * i
    return [ds_dt, de_dt, di_dt, dr_dt]
