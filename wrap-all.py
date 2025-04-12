class Pessoa:
    def __init__(self, cpf: str):
        self.cpf = cpf


class CPF:
    def __init__(self, value):
        if not self._is_valid(value):
            raise ValueError("Invalid CPF")
        self._value = value

    def _is_valid(self, value):
        return len(value) == 11 and value.isdigit()

    def __str__(self):
        return self._value

    def value(self):
        return self._value


class Pessoa:
    def __init__(self, cpf: CPF):
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf