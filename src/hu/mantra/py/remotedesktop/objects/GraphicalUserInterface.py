import tkinter as tk

class GraphicalUserInterface:

    def __init__(self):
        self.window = tk.Tk()
        self.notification = None
        self.entry = tk.Entry()

    def create_main_window(self):
        self.window.title("Remote Desktop Controller")
        self.window.geometry("400x720")

        # Címke a felhasználó üdvözlésére
        title_label = tk.Label(self.window, text="Remote Desktop Kezelő", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Kapcsolat gomb létrehozása
        connect_button = tk.Button(self.window, text="Kapcsolat", width=20, command=self.connect_to_host)
        connect_button.pack(pady=5)

        # Bontás gomb létrehozása
        disconnect_button = tk.Button(self.window, text="Bontás", width=20, command=self.disconnect_from_host)
        disconnect_button.pack(pady=5)

        # Képernyőkép készítése gomb
        screenshot_button = tk.Button(self.window, text="Képernyőkép", width=20, command=self.create_screenshot)
        screenshot_button.pack(pady=5)

        # Értesítések megjelenítése
        self.notification_label = tk.Label(self.window, text="Kapcsolat állapota: Nincs kapcsolat", fg="red")
        self.notification_label.pack(pady=10)

        # Bezáró gomb létrehozása
        close_button = tk.Button(self.window, text="Bezárás", width=20, command=self.close_window)
        close_button.pack(pady=20)

        self.window.mainloop()

    def close_window(self):
        self.window.destroy()

    def display_notification(self, message, color):
        self.notification_label.config(text=message, fg=color)

    def update_connection_status(self, status):
        self.notification_label.config(text=f"Kapcsolat állapota: {status}",
                                       fg="green" if status == "Kapcsolat létrejött" else "red")
    def read_entry(self):
        # Beolvassuk az Entry mező tartalmát
        user_input = self.entry.get()
        print(f"Beolvasott szöveg: {user_input}")

    def connect_to_host(self):
        # Itt lehet meghívni a megfelelő RemoteDesktopManager metódusokat
        #self.window.destroy()

        title_label = tk.Label(self.window, text="Remote Desktop Kezelő Login", font=("Helvetica", 16))
        title_label.pack(pady=10)

        self.entry = tk.Entry(self.window)
        self.entry.pack(pady=10)

        # Kapcsolat gomb létrehozása
        connect_button = tk.Button(self.window, text="Bejelentkezés", width=20, command=self.read_entry)
        connect_button.pack(pady=5)

        self.update_connection_status("Kapcsolat létrejött")

    def disconnect_from_host(self):
        # Itt lehet meghívni a megfelelő RemoteDesktopManager metódusokat
        self.update_connection_status("Nincs kapcsolat")

    def create_screenshot(self):
        # Itt hívhatod meg a ScreenCapture metódusokat
        self.display_notification("Képernyőkép készült és elmentve.", "green")

