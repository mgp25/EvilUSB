from termcolor import colored
import sys

class Log():
    @staticmethod
    def _print(word):
        sys.stdout.write(word)
        sys.stdout.flush()

    @staticmethod
    def info(word):
        Log._print(colored("[+] ", "cyan", attrs=["bold"]) + "%s\n" % word)

    @staticmethod
    def warning(word):
        Log._print("[!] %s\n" % word)

    @staticmethod
    def error(word):
        Log._print(colored("[-] ", "red", attrs=["bold"]) + "%s\n" % word)

    @staticmethod
    def success(word):
        Log._print(colored("\n[+] ", "green", attrs=["bold"]) + "%s\n" % word)

    @staticmethod
    def data(word):
        Log._print(colored("> ", "blue", attrs=["bold"]) + "%s\n" % word)

    @staticmethod
    def query(word):
        Log._print("[?] %s\n" % word)

    @staticmethod
    def context(context):
        Log._print(colored("%s" % context, "magenta", attrs=["bold"]))

    @staticmethod
    def phrases(context):
        Log._print(colored("%s\n\n" % context, "magenta", attrs=["bold"]))

    @staticmethod
    def ascii(ascii):
        Log._print(colored("%s" % ascii, "green", attrs=["bold"]))
