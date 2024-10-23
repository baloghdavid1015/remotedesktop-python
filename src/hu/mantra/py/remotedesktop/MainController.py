from hu.mantra.py.remotedesktop.objects.CommandLineInterface import CommandLineInterface
from hu.mantra.py.remotedesktop.objects.GraphicalUserInterface import GraphicalUserInterface


class MainController:

    def __init__(self):
        self.mode = None
        self.components_initialized = False
        self.CLI = CommandLineInterface()
        self.GUI = GraphicalUserInterface()

    def initialize_components(self):
        self.CLI = CommandLineInterface()
        self.GUI = GraphicalUserInterface()

    def validate_environment(self):
        if isinstance(self.CLI, CommandLineInterface):
            print("CLI komponens validálva")
        else:
            print("CLI komponens validálása sikertelen")

        if isinstance(self.GUI, GraphicalUserInterface):
            print("GUI komponens validálva")
        else:
            print("GUI komponens validálása sikertelen")

    def start(self):
        print("MainController started.")
        print("-----------------------")

        while True:
            self.mode = input(
                "Kérlek válassz az alábbi lehetőségek közül! [GUI / CLI]: ").upper()

            if self.mode not in ["GUI", "CLI"]:
                print("Hibás bevitel!")
                continue
            else:

                self.validate_environment()

                if self.mode == "CLI":
                    while True:
                        self.CLI.get_command()
                        self.CLI.execute_command()
                elif self.mode == "GUI":
                    self.GUI.create_main_window()
                    break


if __name__ == "__main__":
    MainController().start()
