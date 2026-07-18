import threading
import time
from datetime import datetime

from sender import MessageSender


class MessageScheduler:

    def __init__(
        self,
        status_callback=None,
        change_callback=None,
        delay_before_send=5
    ):

        self.messages = []

        self.running = False

        self.thread = None

        self.lock = threading.Lock()

        self.status_callback = status_callback

        self.change_callback = change_callback

        self.sending = False

        # zapamiętane wykonane wiadomości
        self.sent_messages = set()


        self.sender = MessageSender(
            delay_before_send=delay_before_send,
            status_callback=self._send_status
        )



    # ==================================================
    # START
    # ==================================================

    def start(self):

        if self.running:
            return


        self.running = True


        self.thread = threading.Thread(
            target=self._worker,
            daemon=True
        )


        self.thread.start()



    # ==================================================
    # STOP
    # ==================================================

    def stop(self):

        self.running = False

        self.sender.cancel()



    # ==================================================
    # DODAWANIE
    # ==================================================

    def add_message(self, message):

        with self.lock:

            self.messages.append(
                message
            )


        self._notify_change()


        self._send_status(
            f"Dodano wiadomość na {message['time']}"
        )



    # ==================================================
    # USUWANIE
    # ==================================================

    def remove_message(self, index):

        with self.lock:

            if index < 0 or index >= len(self.messages):
                return


            removed = self.messages.pop(
                index
            )


        self._notify_change()


        self._send_status(
            f"Usunięto wiadomość {removed['time']}"
        )



    # ==================================================
    # WORKER
    # ==================================================

    def _worker(self):

        while self.running:


            now = datetime.now().strftime(
                "%H:%M:%S"
            )


            message_to_send = None


            with self.lock:


                # blokada podczas wysyłania

                if not self.sending:


                    for msg in list(self.messages):


                        unique_id = (
                            msg["time"],
                            msg["message"]
                        )


                        if msg["time"] == now:


                            # już wykonana

                            if unique_id in self.sent_messages:
                                continue



                            # natychmiast blokujemy

                            self.sending = True


                            self.sent_messages.add(
                                unique_id
                            )


                            message_to_send = msg


                            self.messages.remove(
                                msg
                            )


                            break



            if message_to_send:


                self._notify_change()


                self._send_status(
                    f"Wysyłanie {now}"
                )


                try:

                    self.sender.send(
                        message_to_send["message"]
                    )


                except Exception as e:

                    self._send_status(
                        f"Błąd wysyłania: {e}"
                    )


                finally:


                    with self.lock:

                        self.sending = False



            time.sleep(
                1
            )



    # ==================================================
    # CALLBACK LISTY
    # ==================================================

    def _notify_change(self):

        if self.change_callback:

            try:

                self.change_callback(
                    self.messages.copy()
                )

            except Exception:

                pass



    # ==================================================
    # STATUS
    # ==================================================

    def _send_status(self, text):

        print(text)


        if self.status_callback:

            try:

                self.status_callback(
                    text
                )

            except Exception:

                pass