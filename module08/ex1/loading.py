from importlib.metadata import PackageNotFoundError, version


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")

    PACKAGES = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("matplotlib", "Visualization ready"),
    ]

    missing = []

    for name, message in PACKAGES:
        try:
            v = version(name)
        except PackageNotFoundError:
            missing.append(name)
            print(f"[NOT FOUND] {name} - not installed")
        else:
            print(f"[OK] {name} ({v}) - {message}")

    if missing:
        print(
            f"[ERROR]: {len(missing)} package(s) missing: "
            f"{', '.join(missing)}\n"
        )
        print("Make sure you are in the Virtual Environment")
        print("Prefix (matrix_env) should be in the terminal.\n")
        print("To load the programs, run:")
        print("pip install -r requirements.txt      # with pip")
        print("poetry install                       # with poetry\n")
        print("Then run this program again.")
        return


if __name__ == "__main__":
    main()
