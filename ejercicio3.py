def leibniz_pi(N: int) -> float:
    suma = 0.0
    signo = 1.0
    for n in range(N):
        suma += signo / (2 * n + 1)
        signo = -signo  # alterna +1, -1
    return 4.0 * suma

if __name__ == "__main__":
    N = 2_000_000
    aproximacion = leibniz_pi(N)