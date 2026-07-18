import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from scheduler import MessageScheduler
from storage import MessageStorage

from widgets import (
    CardFrame,
    TitleLabel,
    SectionLabel,
    ModernButton,
    StatusBar,
    MessageItem
)


class MessageSchedulerApp(ctk.CTk):

    def __init__(self, config):

        super().__init__()

        self.config = config

        self.title(
            self.config.get(
                "app",
                "title",
                "📩 Message Scheduler"
            )
        )


        width = self.config.get(
            "app",
            "width",
            950
        )

        height = self.config.get(
            "app",
            "height",
            700
        )


        self.geometry(
            f"{width}x{height}"
        )


        self.storage = MessageStorage(
            self.config.get(
                "storage",
                "messages_file",
                "messages.json"
            )
        )


        self.message_widgets = []


        self.scheduler = MessageScheduler(
            status_callback=self.update_status,
            change_callback=self.scheduler_changed,
            delay_before_send=self.config.get(
                "sender",
                "delay_before_send",
                5
            )
        )


        self.create_ui()

        self.load_messages()

        self.scheduler.start()


        self.protocol(
            "WM_DELETE_WINDOW",
            self.close
        )



    # ==================================================
    # UI
    # ==================================================

    def create_ui(self):

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            1,
            weight=1
        )


        header = CardFrame(self)

        header.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20,10),
            sticky="ew"
        )


        TitleLabel(
            header,
            text="📩 Planer wiadomości"
        ).pack(
            pady=15
        )



        content = CardFrame(self)

        content.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )


        content.grid_columnconfigure(
            0,
            weight=3
        )

        content.grid_columnconfigure(
            1,
            weight=1
        )

        content.grid_rowconfigure(
            1,
            weight=1
        )



        SectionLabel(
            content,
            text="Treść wiadomości"
        ).grid(
            row=0,
            column=0,
            padx=20,
            pady=(20,5),
            sticky="w"
        )



        self.message_box = ctk.CTkTextbox(
            content,
            corner_radius=12,
            wrap="word",
            font=ctk.CTkFont(
                size=14
            )
        )


        self.message_box.grid(
            row=1,
            column=0,
            padx=20,
            pady=5,
            sticky="nsew"
        )



        side = CardFrame(
            content
        )


        side.grid(
            row=0,
            column=1,
            rowspan=2,
            padx=15,
            pady=15,
            sticky="nsew"
        )



        SectionLabel(
            side,
            text="Godzina wysłania"
        ).pack(
            pady=(20,5)
        )


        self.time_entry = ctk.CTkEntry(
            side,
            placeholder_text="HH:MM:SS"
        )


        self.time_entry.pack(
            padx=20
        )



        ModernButton(
            side,
            text="➕ Zaplanuj",
            command=self.add_message
        ).pack(
            padx=20,
            pady=20,
            fill="x"
        )



        ModernButton(
            side,
            text="🗑 Usuń ostatnią",
            command=self.delete_last,
            fg_color="#8b0000",
            hover_color="#b22222"
        ).pack(
            padx=20,
            pady=5,
            fill="x"
        )



        SectionLabel(
            side,
            text="Harmonogram"
        ).pack(
            pady=(20,5)
        )


        self.list_frame = ctk.CTkScrollableFrame(
            side,
            height=300
        )


        self.list_frame.pack(
            padx=15,
            pady=5,
            fill="both",
            expand=True
        )



        self.status = StatusBar(
            self
        )


        self.status.grid(
            row=2,
            column=0,
            padx=20,
            pady=(0,15),
            sticky="ew"
        )



    # ==================================================
    # NORMALIZACJA CZASU
    # ==================================================

    def normalize_time(self, value):

        if not value:
            return ""


        parts = value.split(":")


        try:

            if len(parts) == 1:

                hour = int(parts[0])
                minute = 0
                second = 0


            elif len(parts) == 2:

                hour = int(parts[0])
                minute = int(parts[1])
                second = 0


            elif len(parts) == 3:

                hour = int(parts[0])
                minute = int(parts[1])
                second = int(parts[2])


            else:

                return value



            return (
                f"{hour:02d}:"
                f"{minute:02d}:"
                f"{second:02d}"
            )


        except ValueError:

            return value



    # ==================================================
    # DODAWANIE
    # ==================================================

    def add_message(self):

        text = self.message_box.get(
            "1.0",
            "end-1c"
        )


        send_time = self.normalize_time(
            self.time_entry.get().strip()
        )



        if not text.strip():

            messagebox.showwarning(
                "Brak tekstu",
                "Wpisz wiadomość."
            )

            return



        try:

            datetime.strptime(
                send_time,
                "%H:%M:%S"
            )


        except ValueError:

            messagebox.showwarning(
                "Błędna godzina",
                "Podaj czas np. 3:42 albo 03:42:00"
            )

            return



        self.scheduler.add_message(
            {
                "time": send_time,
                "message": text
            }
        )


        self.message_box.delete(
            "1.0",
            "end"
        )


        self.time_entry.delete(
            0,
            "end"
        )



    # ==================================================
    # RESZTA FUNKCJI BEZ ZMIAN
    # ==================================================

    def refresh_messages(self):

        for widget in self.message_widgets:
            widget.destroy()


        self.message_widgets.clear()


        for index, msg in enumerate(
            self.scheduler.messages
        ):

            widget = MessageItem(
                self.list_frame,
                msg["message"],
                msg["time"],
                delete_callback=lambda i=index:
                    self.delete_message(i)
            )


            widget.pack(
                fill="x",
                pady=5
            )


            self.message_widgets.append(
                widget
            )



    def delete_message(self, index):

        self.scheduler.remove_message(
            index
        )



    def delete_last(self):

        if self.scheduler.messages:

            self.scheduler.remove_message(
                len(self.scheduler.messages)-1
            )



    def load_messages(self):

        messages = self.storage.load()

        self.scheduler.messages = messages

        self.refresh_messages()



    def scheduler_changed(self, messages):

        self.storage.save(
            messages
        )


        self.after(
            0,
            self.refresh_messages
        )



    def update_status(self, text):

        self.after(
            0,
            lambda:
                self.status.set(text)
        )



    def close(self):

        self.scheduler.stop()

        self.storage.save(
            self.scheduler.messages
        )

        self.destroy()