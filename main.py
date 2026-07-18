import customtkinter as ctk

from config import Config
from ui import MessageSchedulerApp


def main():

    # Wczytanie konfiguracji
    config = Config()


    # Motyw aplikacji
    appearance = config.get(
        "app",
        "theme"
    )

    if appearance:
        ctk.set_appearance_mode(
            appearance
        )
    else:
        ctk.set_appearance_mode(
            "Dark"
        )


    # Kolorystyka CustomTkinter
    ctk.set_default_color_theme(
        "blue"
    )


    # Start aplikacji
    app = MessageSchedulerApp(
        config
    )


    app.mainloop()



if __name__ == "__main__":
    main()