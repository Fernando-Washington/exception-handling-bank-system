class InvalidOptionError(Exception):
    """Erro para opções inválidas no menu."""
    pass


class InvalidValueError(Exception):
    """Erro para valores inválidos em operações bancárias."""
    pass


class NegativeValueError(InvalidValueError):
    def __init__(self, value):
        super().__init__(f"O valor não pode ser negativo: {value}")
