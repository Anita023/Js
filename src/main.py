from src.views import trainee_view


def show_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Registrar aprendiz")
    print("2. Editar aprendiz")
    print("3. Eliminar aprendiz")
    print("4. Buscar aprendiz")
    print("5. Mostrar aprendices")
    print("6. Exportar a CSV")
    print("7. Salir")


def main():

    trainee_view.init_app_data()

    while True:

        show_menu()

        option = input("\nSeleccione una opción: ").strip()

        if option == "1":
            trainee_view.register_trainee_view()

        elif option == "2":
            trainee_view.edit_trainee_view()

        elif option == "3":
            trainee_view.delete_trainee_view()

        elif option == "4":
            trainee_view.search_trainee_view()

        elif option == "5":
            trainee_view.status_view()

        elif option == "6":
            trainee_view.export_trainees_view()

        elif option == "7":
            print("\n¡Hasta luego!")
            break

        else:
            print("\n❌ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()