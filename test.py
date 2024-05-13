from colorama import Fore
import datetime


def version() -> None:
    with open(r"./b.txt", "r", encoding="utf-8") as f:
        text = f.read()
        details = text.format(
            time=datetime.datetime.now().time().strftime("%H:%M:%S"),
            date=f"{datetime.date.today()}",
            mail=Fore.CYAN,
            reset=Fore.RESET,
            sdk=Fore.MAGENTA,
            ssb=Fore.GREEN,
            version=Fore.LIGHTBLUE_EX,
            info=Fore.LIGHTMAGENTA_EX,
            issues=Fore.RED,
            warning=Fore.LIGHTYELLOW_EX,
            dateandtime=Fore.GREEN,
        )

        print(details)

version()
