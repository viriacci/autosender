import time
import threading

import pyautogui
import pyperclip


class MessageSender:

    def __init__(
        self,
        delay_before_send=5,
        status_callback=None
    ):

        self.delay = delay_before_send

        self.status_callback = status_callback

        self.cancel_event = threading.Event()


        # Bezpieczne tempo pyautogui
        pyautogui.PAUSE = 0.05



    # ==================================================
    # ANULOWANIE
    # ==================================================

    def cancel(self):

        self.cancel_event.set()



    # ==================================================
    # WYSYŁANIE
    # ==================================================

    def send(self, message):

        self.cancel_event.clear()


        self._status(
            f"Wysyłanie za {self.delay}s..."
        )


        # odliczanie

        for seconds in range(
            self.delay,
            0,
            -1
        ):

            if self.cancel_event.is_set():

                self._status(
                    "Wysyłanie anulowane"
                )

                return


            self._status(
                f"Wysyłanie za {seconds}s"
            )


            time.sleep(1)



        try:

            self._type_message(
                message
            )


            self._status(
                "Wiadomość wysłana"
            )


        except Exception as e:


            self._status(
                f"Błąd wysyłania: {e}"
            )

            raise



    # ==================================================
    # WPISYWANIE WIADOMOŚCI
    # ==================================================

    def _type_message(self, message):

        if not message:

            return


        lines = message.split(
            "\n"
        )


        for index, line in enumerate(lines):


            if self.cancel_event.is_set():

                return


            self._paste(
                line
            )


            # nowa linia bez wysyłania

            if index < len(lines) - 1:

                pyautogui.hotkey(
                    "shift",
                    "enter"
                )



        # właściwe wysłanie

        pyautogui.press(
            "enter"
        )



    # ==================================================
    # WKLEJANIE ZE SCHOWKA
    # ==================================================

    def _paste(self, text):

        if text == "":

            return


        old_clipboard = None


        try:

            # zapamiętanie starego schowka

            try:

                old_clipboard = pyperclip.paste()

            except Exception:

                pass



            pyperclip.copy(
                text
            )


            pyautogui.hotkey(
                "ctrl",
                "v"
            )


            # chwila na przetworzenie wklejenia

            time.sleep(
                0.05
            )


        finally:


            # przywrócenie schowka

            if old_clipboard is not None:

                try:

                    pyperclip.copy(
                        old_clipboard
                    )

                except Exception:

                    pass



    # ==================================================
    # STATUS
    # ==================================================

    def _status(self, text):

        print(
            text
        )


        if self.status_callback:

            try:

                self.status_callback(
                    text
                )

            except Exception:

                pass