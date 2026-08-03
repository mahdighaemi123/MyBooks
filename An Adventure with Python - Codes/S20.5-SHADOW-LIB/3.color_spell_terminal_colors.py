#  pip install colorama

from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

print(Fore.RED + "Fire Spell")
print(Fore.BLUE + "Ice Spell")
