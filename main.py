import customtkinter as ctk

from config import Config
from ui import MessageSchedulerApp



def main():

    # ==============================================
    # KONFIGURACJA
    # ==============================================

    config = Config()



    # ==============================================
    # TRYB WYŚWIETLANIA
    # ==============================================

    appearance = config.get(
        "app",
        "theme",
        "Dark"
    )


    ctk.set_appearance_mode(
        appearance
    )



    # ==============================================
    # KOLOR MOTYWU
    # ==============================================

    color_theme = config.get(
        "app",
        "color_theme",
        "blue"
    )


    ctk.set_default_color_theme(
        color_theme
    )



    # ==============================================
    # START APLIKACJI
    # ==============================================

    app = MessageSchedulerApp(
        config
    )


    app.mainloop()



if __name__ == "__main__":

    main()