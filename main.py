from interface.main_menu import run_main_menu_interface
from database.database import initialize_databases


def main():
    initialize_databases()
    run_main_menu_interface()


if __name__ == '__main__':
    main()
