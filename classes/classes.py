from exceptions import InvalidValueError

class Bank:
    def __init__(self, name, cnpj, location, phone):
        self._name = name
        self._cnpj = cnpj
        self._location = location
        self._phone = phone
        self._branch = []

    def add_branch(self, branch):
        if not isinstance(branch, Branch):
            raise InvalidValueError("Objeto informado não é uma agência.")

        self._branch.append(branch)
        print("Branch added successfully")

class Branch:
    def __init__(self, number, name, location, phone):
        self._number = number
        self._name = name
        self._location = location
        self._phone = phone

