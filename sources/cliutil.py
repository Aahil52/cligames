from random import randint
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def delete_output(n=1):
        for i in range(n):
            sys.stdout.write("\x1b[1A")
            sys.stdout.write("\x1b[2K")

def print_list(list: list, title: str):
    print(f"\n{title}\n")
    for item in list:
        print(f"• {item}")
    print("")

def get_valid_choice(list: list, prompt: str, warning=""):
    choice = input(f"{warning}{prompt}").lower()
    if choice in list:
        return choice
    else:
        delete_output()
        return get_valid_choice(list, prompt, warning="(Invalid Input) ")

def ask_for_choice_in_list(list: list, title, prompt):
    print_list(list, title)
    choice = get_valid_choice(list, f"{prompt}")
    delete_output(len(list) + 5)
    return choice

def ask_for_int_between(prompt: str, lower_bound: int, upper_bound: int, default: int = None, random_option: bool = False, warning=f"") -> int:
    # Print additional specified options only on initial call
    if warning == "" and (default or random_option):
        print_list([f"default - {default} (enter)", "random"] if default and random_option else [f"default - {default} (enter)"] if default else ["random (enter)"], "Other Options:")

    choice = input(f"{warning}{prompt}").lower()

    # Check for "default", "random", and "" choices depending on what was specified
    if default and (choice == "default" or choice == ""):
        delete_output(7 if default and random_option else 6)
        return default
    if random_option and (choice == "random" or (not default and choice == "")):
        delete_output(7 if default and random_option else 6)
        return randint(lower_bound, upper_bound)

    # Catch exception if choice is not an int
    try:
        # Check if choice is within specified lower and upper bounds
        if int(choice) in range(lower_bound, upper_bound + 1):
            delete_output(7 if default and random_option else 6 if default or random_option else 5)
            return int(choice)
        else:
            delete_output()
            return ask_for_int_between(prompt, lower_bound, upper_bound, default, random_option, warning=f"(Not in Range) ")
    except Exception:
        delete_output()
        return ask_for_int_between(prompt, lower_bound, upper_bound, default, random_option, warning="(Invalid Input) ")
