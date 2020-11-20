""" 
    Class for handling all python errors:
    |
    |- • AssertionError
    |- • AttributeError
    |- • EOFError
    |- • FileNotFoundError
    x FloatingPointError    	Raised when a floating point operation fails.
    x GeneratorExit         	Raised when a generator's close() method is called.
    |- • ImportError
    |- • IndexError
    |- • KeyError
    |- • KeyboardInterrupt
    |- • MemoryError
    |- • NameError
    |- • NotImplementedError
    |- • ModuleNotFoundError
    |- • OSError
    |- • OverflowError
    |- • ReferenceError
    |- • RuntimeError
    |- • StopIteration
    |- • SyntaxError
    |- • IndentationError
    |- • TabError
    |- • SystemError
    |- • TypeError
    |- • UnboundLocalError
    |- • ValueError
    |- • ZeroDivisionError
"""

from colorama import Fore, Style
import re


class Handler:
    def SyntaxErr(self, line: int, contex: str):
        template = "[×] An error of type SyntaxError occurred, the error is at line: {0} [ {1} ]"
        message = template.format(
            line, contex)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[i] Try the following:\n[-] Check for missing brackets, braces or curly braces. \n[-] Missing quotes or characters.\n[-] Mistaking dictionary syntax\n[-] Using the wrong indentation \
                                \n[-] Defining and calling functions" + Style.RESET_ALL)

    def StopIterationErr(self, line: int):
        template = "[✓] Your next() method is done [ LINE {0}]. Script is OK!"
        message = template.format(line)
        print(
            Fore.GREEN + message + Style.RESET_ALL)

    def AssertionErr(self, line: int):
        template = "[×] An error of type AssertionError occurred, the error is at line: {0}"
        message = template.format(
            line)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[i] Try the following:\n[-] This error is usually caused by the assert statement, check your statement and try again. \n[-] This error is sometimes caused by unittest module, if you're using functions like 'failIf()' check your code and try again." + Style.RESET_ALL)

    def ZeroDivisionErr(self, line: int):
        template = "[×] An error of type ZeroDivisionError occurred at line {0}, you cannot devide by zero."
        message = template.format(line)
        print(
            Fore.RED + message + Style.RESET_ALL)

    def AttributeErr(self, line: int, contex: str):
        template = "[×] An error of type AttributeError occurred at line: {0}, {1}"
        message = template.format(
            line, contex)
        print(
            Fore.RED + message + Style.RESET_ALL)

    def TypeErr(self, line: int, contex: str):
        template = "[×] An error of type TypeError occurred at line: {0}."
        message = template.format(
            line)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] Check the error message: {}.".format(contex) + Style.RESET_ALL)

    def EOFErr(self, line: int):
        template = "[×] An error of type EOFError occurred at line: {0}."
        message = template.format(
            line)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] You need to provide user value for your input or you can remove it if you don't want to use it" + Style.RESET_ALL)

    def ModuleNotFoundErr(self, line: int, contex: str):
        template = "[×] An error of type ModuleNotFoundError occurred at line: {0}."
        message = template.format(line)
        module_name = re.findall("'([^']*)'", contex)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] There is {} installed in your machine, use [ pip install {} ] in your terminal to install it and try again".format(contex, *module_name) + Style.RESET_ALL)

    def ImportErr(self, line: int, contex: str):
        template = "[×] An error of type ImportError occurred at line: {0}."
        message = template.format(line)
        module_name = re.findall("'([^']*)'", contex)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] '{}' cannot be imported from '{}', check your syntax and try again.".format(module_name[0], module_name[1]) + Style.RESET_ALL)

    def IndexErr(self, line: int):
        template = "[×] An error of type IndexError occurred at line: {0}."
        message = template.format(line)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] This one is easy to fix, you are trying to access an index of the list that doesn't exist." + Style.RESET_ALL)

    def KeyErr(self, line: int, contex: str):
        template = "[×] An error of type KeyError occurred at line: {0}."
        message = template.format(line)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] There is no key named {} in your dictionary.".format(contex) + Style.RESET_ALL)

    def TabErr(self, line: int):
        template = "[×] An error of type TabError occurred at line: {0}."
        message = template.format(line)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] Fix your tabs spacing." + Style.RESET_ALL)

    def UnboundLocalErr(self, line: int, contex: str):
        template = "[×] An error of type UnboundLocalError occurred at line: {0}."
        message = template.format(line)
        module_name = re.findall("'([^']*)'", contex)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] You need to assign a value for '{}' before using it.".format(*module_name) + Style.RESET_ALL)

    def ValueErr(self, line: int):
        template = "[×] An error of type ValueError occurred at line: {0}."
        message = template.format(line)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] This is because you are trying to pass argument to function but argument type is wrong." + Style.RESET_ALL)

    def FileNotFoundErr(self, line: int):
        template = "[×] An error of type FileNotFoundError occurred at line: {0}."
        message = template.format(line)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] This file is not found, check your path and try again." + Style.RESET_ALL)

    def NameErr(self, line: int, contex: str):
        template = "[×] An error of type NameError occurred at line: {0}."
        message = template.format(line)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] There is no variable called '{}' in your current scope.".format(*re.findall("'([^']*)'", contex)) + Style.RESET_ALL)

    def OSErr(self, line: int):
        template = "[×] An error of type OSError occurred at line {}."
        print(
            Fore.RED + template.format(line) + Style.RESET_ALL)

        print(
            Fore.CYAN + "[*] This error is caused by 'os' module functions, check your os-specific function." + Style.RESET_ALL)

    def OverflowErr(self, line: int):
        template = "[×] An error of type OverflowError occurred at line {0}."
        print(
            Fore.RED + template.format(line) + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] This operation exceeds the limits of the variable type." + Style.RESET_ALL)

    def IndentationErr(self, line: int):
        template = "[×] An error of type IndentationError occurred at line {0}."
        print(
            Fore.RED + template.format(line) + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] Fix your indentation and try again." + Style.RESET_ALL)

    def NotImplementedErr(self, line: int, contex: str):
        template = "[×] An error of type NotImplementedError occurred at line: {0}."
        message = template.format(line)
        print(
            Fore.RED + message + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] Check the code associated with this syntax '{}', this may indicate that a method or behavior needs to be defined by a subclass.".format(contex) + Style.RESET_ALL)

    def ReferenceErr(self, line: int):
        template = "[×] An error of type ReferenceError occurred at line {0}."
        print(
            Fore.RED + template.format(line) + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] Weakref proxy is used to access an object that has already been garbage collected." + Style.RESET_ALL)
        print(
            Fore.CYAN + "[*] This exception is raised when a weak reference proxy, created by the weakref.proxy() function, is used to access an attribute of the referent after it has been garbage collected. For more information on weak references, for more info google [weakref] module." + Style.RESET_ALL)
