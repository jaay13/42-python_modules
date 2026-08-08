from os.path import basename
from site import getsitepackages
from sys import base_prefix, executable, prefix


def in_venv() -> bool:
    return prefix != base_prefix


def main() -> None:
    if in_venv():
        print("\nMATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {executable}")
        print(f"Virtual Environment: {basename(prefix)}")
        print(f"Environment Path: {prefix}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        print("Package installation path:")
        print(getsitepackages()[0])

    else:
        print("\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")

        print("Then run this program again.")


if __name__ == "__main__":
    main()
