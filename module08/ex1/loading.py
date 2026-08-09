from importlib.metadata import PackageNotFoundError, version


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

    run_analysis()


if __name__ == "__main__":
    main()
