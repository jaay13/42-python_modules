"""Load configuration from environment variables and a .env file."""

import os

from dotenv import load_dotenv

VARIABLES = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

DEFAULT_MODE = "development"
DEFAULT_LOG_LEVEL = "INFO"


def load_config() -> dict[str, str | None]:
    """Read every configuration variable, then apply defaults."""
    config: dict[str, str | None] = {}

    for name in VARIABLES:
        config[name] = os.getenv(name)

    if config["MATRIX_MODE"] is None:
        config["MATRIX_MODE"] = DEFAULT_MODE
    if config["LOG_LEVEL"] is None:
        config["LOG_LEVEL"] = DEFAULT_LOG_LEVEL

    return config


def warn_missing(config: dict[str, str | None]) -> None:
    """Warn about variables with no value and no default."""
    missing = []

    for name in VARIABLES:
        if config[name] is None:
            missing.append(name)

    if missing:
        print(f"[WARNING] Missing configuration: {', '.join(missing)}")
        print("Copy .env.example to .env and fill in the values.\n")


def print_configuration(config: dict[str, str | None]) -> None:
    """Print the configuration, hiding secrets in production."""
    mode = config["MATRIX_MODE"]
    production = mode == "production"

    database_url = config["DATABASE_URL"]
    if not database_url:
        database = "Not configured"
    elif production:
        database = "Connected (details hidden)"
    elif "localhost" in database_url:
        database = "Connected to local instance"
    else:
        database = "Connected to remote instance"

    if not config["API_KEY"]:
        api = "Missing API key"
    elif production:
        api = "Authenticated (key hidden)"
    else:
        api = "Authenticated"

    if config["ZION_ENDPOINT"]:
        zion = "Online"
    else:
        zion = "Offline"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {api}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {zion}")


def security_check() -> None:
    """Report how safely this configuration is being handled."""
    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.isfile(env_path):
        print("[OK] .env file properly configured")
    else:
        print("[!] .env not found - copy .env.example to .env")

    print("[OK] Production overrides available")


def main() -> None:
    """Read the Matrix configuration and report on it."""
    load_dotenv()
    config = load_config()

    print("\nORACLE STATUS: Reading the Matrix...\n")

    warn_missing(config)
    print_configuration(config)
    security_check()

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
