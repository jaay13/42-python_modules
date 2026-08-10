"""Validate space station data with a Pydantic model."""

import datetime as dt

from pydantic import BaseModel, Field, ValidationError

SEPARATOR = "=" * 40


class SpaceStation(BaseModel):
    """A space station, validated on creation.

    Strings and numbers use different constraints: min_length and
    max_length count characters, while ge and le compare values.
    Using min_length on an int would not restrict its range.
    """

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: dt.datetime
    is_operational: bool = Field(default=True)
    # "str | None" only allows the value None - it does not make the
    # field optional. Omitting it is allowed because of default=None.
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    """Create one valid station, then show an invalid one failing."""
    print("Space Station Data Validation")
    print(SEPARATOR)

    valid_space_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        # An ISO string such as "2026-08-10 11:53" is accepted here
        # too - Pydantic parses it into a datetime.
        last_maintenance=dt.datetime(2026, 8, 10, 11, 53),
    )

    print("Valid station created:")
    print(f"ID: {valid_space_station.station_id}")
    print(f"Name: {valid_space_station.name}")
    print(f"Crew: {valid_space_station.crew_size} people")
    print(f"Power: {valid_space_station.power_level}%")
    print(f"Oxygen: {valid_space_station.oxygen_level}%")
    print(f"Last Maintenance: {valid_space_station.last_maintenance}")
    if valid_space_station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Not operational")

    print(f"\n{SEPARATOR}")

    # crew_size=25 breaks the le=20 constraint, so the constructor
    # raises instead of returning a station. Catching it here keeps
    # the program running so the failure can be reported.
    try:
        SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=dt.datetime.now().astimezone(),
        )
    except ValidationError as e:
        print("Expected validation error:")
        # e.errors() gives one dict per failed field. Printing only
        # "msg" keeps the output clean; print(e) would add the field
        # name, the input value and a documentation URL.
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
