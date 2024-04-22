class Token:
    type: str = """"""
    value: str = """"""
    position: tuple[int, int] = (0, 0)

    def __init__(self, type: str, value: str, position: tuple[int, int]) -> None:
        self.type = type
        self.value = value
        self.position = position

    def __str__(self) -> str:
        return f"""TYPE: {self.type}\nVALUE: {self.value}\nPOSITION: {self.position}"""
