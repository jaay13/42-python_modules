from importlib.metadata import PackageNotFoundError, version

PACKAGES = [
    ("pandas", "Data manipulation ready"),
    ("numpy", "Numerical computation ready"),
    ("matplotlib", "Visualization ready"),
]


def compare_managers() -> None:
    """Print how pip and Poetry differ at managing this project's deps."""
    print("\nDEPENDENCY MANAGEMENT: pip vs Poetry\n")

    header = (
        f"{'Package':<12} {'Installed':<10} "
        f"{'requirements.txt':<20} pyproject.toml"
    )
    print(header)
    for name, _ in PACKAGES:
        v = version(name)
        pip_pin = f"{name}=={v}"
        poetry_pin = f'{name} = "^{v}"'
        print(f"{name:<12} {v:<10} {pip_pin:<20} {poetry_pin}")
    print()

    print("pip  -> requirements.txt")
    print("  Lists 12 packages: 3 you asked for, 9 pulled in as")
    print("  dependencies of those. Both look identical in the file.")
    print("  Versions are pinned exactly (==), so installs reproduce")
    print("  but never update.")
    print("  Install: pip install -r requirements.txt\n")

    print("poetry -> pyproject.toml")
    print("  Lists only the 3 packages you actually asked for, with")
    print("  flexible constraints (^2.5.1 = any 2.x from 2.5.1 up).")
    print("  Poetry resolves the other 9 itself and records the exact")
    print("  result in poetry.lock, keeping intent and outcome separate.")
    print("  Install: poetry install")


def run_analysis() -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("\nAnalyzing Matrix data...")

    seed = 42
    rng = np.random.default_rng(seed)
    data = rng.normal(loc=100, scale=15, size=1000)

    print(f"Processing {data.size} data points...")

    df = pd.DataFrame({"activity": data})
    average = df["activity"].mean()

    print("Generating visualization...")

    plt.hist(df["activity"], bins=30)
    plt.axvline(average, color="red", label="Average")
    plt.title("Matrix Analysis")
    plt.xlabel("Activity level")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")

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

    run_analysis()
    compare_managers()


if __name__ == "__main__":
    main()
