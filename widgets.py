import customtkinter as ctk


# ==================================================
# KARTA / PANEL FLUENT
# ==================================================

class CardFrame(ctk.CTkFrame):

    def __init__(
        self,
        master,
        **kwargs
    ):

        super().__init__(
            master,
            corner_radius=16,
            fg_color=("#f2f2f2", "#1c1c1c"),
            **kwargs
        )



# ==================================================
# NAGŁÓWEK
# ==================================================

class TitleLabel(ctk.CTkLabel):

    def __init__(
        self,
        master,
        text,
        **kwargs
    ):

        super().__init__(
            master,
            text=text,
            font=ctk.CTkFont(
                size=26,
                weight="bold"
            ),
            **kwargs
        )



# ==================================================
# PODTYTUŁ / LABEL
# ==================================================

class SectionLabel(ctk.CTkLabel):

    def __init__(
        self,
        master,
        text,
        **kwargs
    ):

        super().__init__(
            master,
            text=text,
            font=ctk.CTkFont(
                size=15,
                weight="bold"
            ),
            **kwargs
        )



# ==================================================
# NOWOCZESNY PRZYCISK
# ==================================================

class ModernButton(ctk.CTkButton):

    def __init__(
        self,
        master,
        text,
        command,
        **kwargs
    ):

        super().__init__(
            master,
            text=text,
            command=command,
            height=42,
            corner_radius=12,
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            **kwargs
        )



# ==================================================
# PASEK STATUSU
# ==================================================

class StatusBar(ctk.CTkFrame):

    def __init__(
        self,
        master,
        **kwargs
    ):

        super().__init__(
            master,
            corner_radius=12,
            height=40,
            **kwargs
        )


        self.label = ctk.CTkLabel(
            self,
            text="Gotowy",
            anchor="w"
        )

        self.label.pack(
            padx=15,
            pady=8,
            fill="x"
        )



    def set(
        self,
        text
    ):

        self.label.configure(
            text=text
        )



# ==================================================
# ELEMENT LISTY WIADOMOŚCI
# ==================================================

class MessageItem(ctk.CTkFrame):

    def __init__(
        self,
        master,
        message,
        time,
        delete_callback=None,
        **kwargs
    ):

        super().__init__(
            master,
            corner_radius=12,
            **kwargs
        )


        self.message = message
        self.time = time



        self.selected = False



        self.time_label = ctk.CTkLabel(
            self,
            text=f"🕒 {time}",
            font=ctk.CTkFont(
                weight="bold"
            )
        )

        self.time_label.pack(
            anchor="w",
            padx=10,
            pady=(8,0)
        )



        preview = message.replace(
            "\n",
            " "
        )


        if len(preview) > 60:

            preview = preview[:60] + "..."



        self.text_label = ctk.CTkLabel(
            self,
            text=preview,
            anchor="w"
        )

        self.text_label.pack(
            anchor="w",
            padx=10,
            pady=5
        )



        if delete_callback:

            self.delete_button = ModernButton(
                self,
                text="🗑",
                command=delete_callback,
                width=45
            )

            self.delete_button.pack(
                padx=10,
                pady=(0,8),
                anchor="e"
            )



    def get_data(self):

        return {
            "time": self.time,
            "message": self.message
        }