from time import sleep


class CommandLineInterface:

    def __init__(self):
        self.command = None
        self.commandList = ["KAPCSOLAT", "BONTÁS", "SFTP_FELTÖLT", "SFPT_LETÖLT", "LISTA", "KÉPERNYŐKÉP", "KILÉPÉS"]
        self.cons_help = "--HELP"

    def get_command(self):
        self.command = input("Kérlek válassz egy parancsot![--help a parancsok megjelenítéséhez]: ")

    def execute_command(self):

        command = self.command.upper()

        if command in self.commandList:
            if command == "KILÉPÉS":
                self.exit()
        elif self.cons_help in command:
            self.display_help()

    def exit(self):
        print("Az alkalmazás hamarosan bezáródik.")
        sleep(5)
        exit(0)

    def display_help(self):
        print("Elérhető parancsok:\n"+
                "1. kapcsolat - Létrehoz egy új távoli kapcsolatot.\n" +
                "2. bontás - Megszakítja az aktuális kapcsolatot.\n" +
                "3. sftp_feltölt <helyi út> <távoli út> - Fájl feltöltése a távoli szerverre.\n" +
                "4. sftp_letölt <távoli út> <helyi út> - Fájl letöltése a távoli szerverről.\n" +
                "5. lista - A távoli könyvtár tartalmának listázása.\n" +
                "6. képernyőkép - Az aktuális képernyőkép elkészítése.\n" +
                "7. kilépés - Kilépés a CLI felületből.\n" +
                "További információért írd be: \"parancs_neve -help")