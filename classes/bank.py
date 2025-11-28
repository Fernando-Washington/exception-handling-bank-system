from exceptions import InvalidOptionError

class Running:
    def __init__(self):
        self.is_running = True
        
    def system_run(self):
        while self.is_running:
            try:
                print("Please select an option: 1, 2, 3 (3 stops the system)")
                choice = input("Choose: ")

                if choice not in ("1", "2", "3"):
                    raise InvalidOptionError("Opção inválida. Digite 1, 2 ou 3.")

                if choice == "1":
                    print("1 worked")

                if choice == "2":
                    print("2 worked")

                if choice == "3":
                    print("3 worked")
                    print("by-bye")
                    self.is_running = False

            except InvalidOptionError as e:
                print(f"Erro: {e}")

            except KeyboardInterrupt:
                print("\nExecução interrompida pelo usuário.")
                self.is_running = False
