import json
import os


class Config:

    DEFAULT_CONFIG = {
        "app": {
            "title": "📩 Message Scheduler",
            "width": 950,
            "height": 700,
            "theme": "Dark",
            "color_theme": "blue"
        },

        "sender": {
            "delay_before_send": 5
        },

        "storage": {
            "messages_file": "messages.json"
        }
    }


    def __init__(
        self,
        filename="config.json"
    ):

        self.filename = filename

        self.data = {}

        self.load()



    # ==================================================
    # WCZYTYWANIE
    # ==================================================

    def load(self):

        if not os.path.exists(
            self.filename
        ):

            self.data = self._copy_default()

            self.save()

            return



        try:

            with open(
                self.filename,
                "r",
                encoding="utf-8"
            ) as file:

                self.data = json.load(
                    file
                )


            # uzupełnienie braków

            self._merge_defaults()


        except (
            json.JSONDecodeError,
            OSError
        ):

            self.data = self._copy_default()

            self.save()



    # ==================================================
    # ZAPIS
    # ==================================================

    def save(self):

        try:

            with open(
                self.filename,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    self.data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )


        except Exception as e:

            print(
                f"Błąd zapisu konfiguracji: {e}"
            )



    # ==================================================
    # POBIERANIE
    # ==================================================

    def get(
        self,
        section,
        key,
        default=None
    ):

        return (
            self.data
            .get(section, {})
            .get(key, default)
        )



    # ==================================================
    # USTAWIANIE
    # ==================================================

    def set(
        self,
        section,
        key,
        value
    ):

        if section not in self.data:

            self.data[section] = {}


        self.data[section][key] = value


        self.save()



    # ==================================================
    # UZUPEŁNIANIE BRAKÓW
    # ==================================================

    def _merge_defaults(self):

        changed = False


        for section, values in self.DEFAULT_CONFIG.items():

            if section not in self.data:

                self.data[section] = {}

                changed = True


            for key, value in values.items():

                if key not in self.data[section]:

                    self.data[section][key] = value

                    changed = True



        if changed:

            self.save()



    # ==================================================
    # KOPIA DOMYŚLNEJ KONFIGURACJI
    # ==================================================

    def _copy_default(self):

        return json.loads(
            json.dumps(
                self.DEFAULT_CONFIG
            )
        )