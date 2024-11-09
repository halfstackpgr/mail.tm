from colorama import Fore
import datetime

text = r"""
{mail} __  __       _ _  _{reset}                           {ssb}Server-Side Build{reset}
{mail}|  \/  |     (_) || |{reset}
{mail}| \  / | __ _ _| || |_ _ __ ___{reset}    {info}Developed: halfstackpgr     Website: https://mail.tm{reset}
{mail}| |\/| |/ _` | | || __| '_ ` _ \{reset}                        
{mail}| |  | | (_| | | || |_| | | | | |{reset}  {info}Documentation: https://github.com/halfstackpgr/Mail.tm{reset}
{mail}|_|  |_|\__,_|_|_(_)__|_| |_| |_|{reset}                       
        {sdk} ____  ____  _  __{reset}         {issues}Issues: https://github.com/halfstackpgr/Mail.tm/Issues{reset}
        {sdk}/ ___||  _ \| |/ /{reset}        
        {sdk}\___ \| | | | ' /{reset}          {version}Version: 0.1.3                            Coverage: 98%{reset}  
        {sdk} ___) | |_| | . \{reset}       
        {sdk}|____/|____/|_|\_\{reset}         {dateandtime}Time: {time}                             Date:{date}{reset}
"""


def version() -> None:
    """
    Version information and general banner for Mail.TM.
    """
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
