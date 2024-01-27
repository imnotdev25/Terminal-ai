import argparse
import sys
import os
import time
from terminalai.chat import get_response


def cli():
    parser = argparse.ArgumentParser(description="AI Linux Terminal assistant")
    if len(sys.argv) == 1:
        os.system("echo Terminal AI dont allowed to run without arguments")
    elif any(
        i.lower()
        in [
            "delete",
            "rm",
            "remove",
            "del",
            "erase",
            "destroy",
            "uninstall",
            "purge",
            "clean",
            "clear",
            "wipe",
        ]
        for i in sys.argv[1:]
    ):
        os.system("echo Terminal AI dont allowed to delete files")
    else:
        response = get_response(sys.argv[1:])
        os.system(response)


if __name__ == "__main__":
    cli()
