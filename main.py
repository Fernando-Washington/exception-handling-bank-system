from classes.bank import Running

if __name__ == "__main__":
    try:
        system = Running()
        system.system_run()

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    finally:
        print("Sistema finalizado.")
