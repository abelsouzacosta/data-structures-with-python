class Fraction:
    def __init__(self, top, bottom) -> None:
        self.num = top
        self.den = bottom

    # Prints the fraction in a/b format
    def __str__(self) -> str:
        return f"{self.num}/{self.den}"
