import json
import os


class MessageStorage:

    def __init__(self, filename="messages.json"):

        self.filename = filename



    # ==================================================
    # ZAPIS
    # ==================================================

    def save(self, messages):

        try:

            temp_file = self.filename + ".tmp"


            with open(
                temp_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    messages,
                    file,
                    indent=4,
                    ensure_ascii=False
                )


            # bezpieczna zamiana pliku

            os.replace(
                temp_file,
                self.filename
            )


            return True


        except Exception as e:

            print(
                f"Błąd zapisu wiadomości: {e}"
            )

            return False



    # ==================================================
    # ODCZYT
    # ==================================================

    def load(self):

        if not os.path.exists(
            self.filename
        ):

            return []


        try:

            with open(
                self.filename,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(
                    file
                )


            if not isinstance(
                data,
                list
            ):

                return []


            return self._validate(
                data
            )


        except json.JSONDecodeError:

            print(
                "Plik wiadomości jest uszkodzony."
            )

            return []


        except Exception as e:

            print(
                f"Błąd odczytu wiadomości: {e}"
            )

            return []



    # ==================================================
    # WALIDACJA
    # ==================================================

    def _validate(self, messages):

        valid = []


        for item in messages:

            if not isinstance(
                item,
                dict
            ):

                continue


            if (
                "time" not in item
                or
                "message" not in item
            ):

                continue


            valid.append(
                {
                    "time": str(
                        item["time"]
                    ),

                    "message": str(
                        item["message"]
                    )
                }
            )


        return valid



    # ==================================================
    # CZYSZCZENIE
    # ==================================================

    def clear(self):

        try:

            if os.path.exists(
                self.filename
            ):

                os.remove(
                    self.filename
                )


            return True


        except Exception as e:

            print(
                f"Błąd usuwania pliku: {e}"
            )

            return False