import sys
import os
import traceback
from core.handler import Handler
from colorama import Fore, Style
from argparse import ArgumentParser, RawDescriptionHelpFormatter

HANDLER = Handler()


def py_errors(PATH):
    if not os.path.isfile(PATH):
        print(
            Fore.RED + '[×] ERROR: No such file was found, check your path and try again.' + Style.RESET_ALL)
    else:
        print(
            Fore.GREEN + '[✓] File Located: Script is busy' + Style.RESET_ALL)

        try:
            print(Fore.GREEN + "[*] Running ..." + Style.RESET_ALL)
            exec(open(PATH).read())
            print(Fore.GREEN + "[✓] Your script is ok!" + Style.RESET_ALL)
            sys.exit()
        except KeyboardInterrupt as err:
            print(Fore.RED + '[×] KEYBOARD INTERRUPT ERROR' + Style.RESET_ALL)

        except Exception as err:
            error_class = err.__class__.__name__
            cl, exc, tb = sys.exc_info()

            if error_class == "AssertionError":
                HANDLER.AssertionErr(traceback.extract_tb(tb)[-1][1])

            elif error_class == "AttributeError":
                HANDLER.AttributeErr(traceback.extract_tb(
                    tb)[-1][1], sys.exc_info()[1])

            elif error_class == "EOFError":
                HANDLER.EOFErr(traceback.extract_tb(tb)[-1][1])

            elif error_class == "FileNotFoundError":
                HANDLER.FileNotFoundErr(traceback.extract_tb(tb)[-1][1])

            elif error_class == "IndexError":
                HANDLER.IndexErr(traceback.extract_tb(tb)[-1][1])

            elif error_class == "ImportError":
                HANDLER.ImportErr(traceback.extract_tb(
                    tb)[-1][1], str(sys.exc_info()[1]))

            elif error_class == "KeyError":
                HANDLER.KeyErr(traceback.extract_tb(
                    tb)[-1][1], sys.exc_info()[1])

            elif error_class == "ModuleNotFoundError":
                HANDLER.ModuleNotFoundErr(
                    traceback.extract_tb(tb)[-1][1], str(sys.exc_info()[1]))

            elif error_class == "MemoryError":
                print(
                    Fore.RED + "[×] An error of type MemoryError occurred." + Style.RESET_ALL)
                print(
                    Fore.CYAN + "[*] Your program memory is full, try to delete some objects or check your loops and the program will recover." + Style.RESET_ALL)

            elif error_class == "NameError":
                HANDLER.NameErr(traceback.extract_tb(
                    tb)[-1][1], str(sys.exc_info()[1]))

            elif error_class == "NotImplementedError":
                HANDLER.NotImplementedErr(traceback.extract_tb(
                    tb)[-1][1], str(sys.exc_info()[1]))

            elif error_class == "OSError":
                HANDLER.OSErr((traceback.extract_tb(tb)[-1][1]))

            elif error_class == "OverflowError":
                HANDLER.OverflowErr(traceback.extract_tb(tb)[-1][1])

            elif error_class == "ReferenceError":
                HANDLER.ReferenceErr(traceback.extract_tb(tb)[-1][1])

            elif error_class == "TabError":
                HANDLER.TabErr(traceback.extract_tb(tb)[-1][1])

            elif error_class == "TypeError":
                HANDLER.TypeErr(traceback.extract_tb(
                    tb)[-1][1], sys.exc_info()[1])

            elif error_class == "StopIteration":
                HANDLER.StopIterationErr(traceback.extract_tb(tb)[-1][1])

            elif error_class == "SyntaxError":
                contex = err.text.replace("\n", "")
                HANDLER.SyntaxErr(err.lineno, contex)

            elif error_class == "SystemError":
                print(
                    Fore.RED + "[×] The interpreter detects a bug or fatal failure, [ERROR SystemError: internal error]" + Style.RESET_ALL)

            elif error_class == "IndentationError":
                HANDLER.IndentationErr(traceback.extract_tb(tb)[-1][1])

            elif error_class == "UnboundLocalError":
                HANDLER.UnboundLocalErr(traceback.extract_tb(
                    tb)[-1][1], str(sys.exc_info()[1]))

            elif error_class == "ValueError":
                HANDLER.ValueErr(traceback.extract_tb(tb)[-1][1])

            elif error_class == "ZeroDivisionError":
                HANDLER.ZeroDivisionErr(traceback.extract_tb(tb)[-1][1])

            else:
                Warnings = ["DeprecationWarning", "PendingDeprecationWarning", "RuntimeWarning", "SyntaxWarning",
                            "UserWarning", "FutureWarning", "ImportWarning", "UnicodeWarning", "BytesWarning", "ResourceWarning"]
                if error_class in Warnings:
                    print(
                        Fore.YELLOW + '[*] Your script contains warnings, Please run " python pyerrors.py PATH " for more informations about the warning."' + Style.RESET_ALL)
                else:
                    print(
                        Fore.RED + '[×] UNKOWN ERROR OCCURED "{} {}" : Check your script and try again!'.format(error_class, err) + Style.RESET_ALL)
        else:
            print(
                Fore.GREEN + '[✓] NO ERRORS FOUND: Your script is OK!' + Style.RESET_ALL)


def py_warnings(PATH):
    print(Fore.YELLOW +
          "IMPORTANT: You need to include: [ import warnings warnings.filterwarnings('error') ] at the start of your script in order to catch warnings." + Style.RESET_ALL)
    if not os.path.isfile(PATH):
        print(
            Fore.RED + '[×] ERROR: No such file was found, check your path and try again.' + Style.RESET_ALL)
    else:
        print(
            Fore.GREEN + '[✓] File Located: Searching for warnings ... ' + Style.RESET_ALL)

        warnings = {}
        try:
            exec(open(PATH).read())
            print(Fore.GREEN +
                  "[✓] No warnings was detected!" + Style.RESET_ALL)
            sys.exit()
        except Exception as x:
            cl, exc, tb = sys.exc_info()
            warnings["Type: "+x.__class__.__name__] = 1
            for x in warnings:
                print(
                    Fore.YELLOW +
                    "[*] Warning Found: \n[-] " + x +
                    " at line {}.".format(traceback.extract_tb(
                        tb)[-1][1]) + Style.RESET_ALL
                )


def main():

    # Just fancy text
    print('''
     ____ __  __ ______ ____   ____   ____   ____  _____
   / __ \\ \/ // ____// __ \ / __ \ / __ \ / __ \/ ___/
  / /_/ / \  // __/  / /_/ // /_/ // / / // /_/ /\__ \ 
 / ____/  / // /___ / _, _// _, _// /_/ // _, _/___/ / 
/_/      /_//_____//_/ |_|/_/ |_| \____//_/ |_|/____/  
                                                       
    ''')
    module_name = "PyError: Know More From Errors"
    version = 1.0

    parser = ArgumentParser(
        description=f"{module_name} (Version {version})"
    )

    parser.add_argument("--errors", "-e", type=str, default=False,
                        help="show errors for python script")

    parser.add_argument("--warnings", "-w", type=str, default=False,
                        help="look for warnings in python script")

    py_args = parser.parse_args()

    if py_args.errors:
        py_errors(py_args.errors)

    elif py_args.warnings:
        py_warnings(py_args.warnings)


exec(open("__main__.py").read())
