"""Validate space missions built from nested crew member models.

A SpaceMission holds a list of CrewMember, so Pydantic validates
every member before the mission's own safety rules run.
"""

import datetime as dt
from enum import StrEnum

from pydantic import BaseModel, Field, ValidationError, model_validator

SEPARATOR = "=" * 40


class Rank(StrEnum):
    """Crew ranks, lowest to highest.

    StrEnum so members print as "captain" rather than
    "Rank.CAPTAIN" in the crew listing.
    """

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """One crew member, validated on creation."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """A mission and its crew, checked against safety requirements."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: dt.datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def custom_rules(self) -> "SpaceMission":
        """Apply the launch requirements once the crew is valid.

        mode="after" means self.crew already holds real CrewMember
        objects, so member.rank is a Rank and member.is_active a
        bool. A crew member failing its own fields stops validation
        before this runs.
        """
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        if not any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
                )

        if self.duration_days > 365:
            experienced = sum(
                1 for member in self.crew if member.years_experience >= 5
                )
            # Doubling instead of dividing keeps this integer maths,
            # so an odd crew size cannot round the wrong way.
            if experienced * 2 < len(self.crew):
                raise ValueError(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Show one approved mission, then one rejected by a rule."""
    print("Space Mission Crew Validation")
    print(SEPARATOR)

    crew1 = CrewMember(
        member_id="001",
        name="Vanessa",
        rank=Rank.LIEUTENANT,
        age=21,
        specialization="Navigation",
        years_experience=5,
    )

    crew2 = CrewMember(
        member_id="002",
        name="Jason",
        rank=Rank.CAPTAIN,
        age=21,
        specialization="Mission Command",
        years_experience=7,
    )

    crew3 = CrewMember(
        member_id="003",
        name="Benji",
        rank=Rank.OFFICER,
        age=21,
        specialization="Engineering",
        years_experience=8,
    )

    valid = SpaceMission(
        mission_name="Jupiter Colony Establishment",
        mission_id="M2026_JUPITER",
        destination="Jupiter",
        launch_date=dt.datetime(2056, 12, 1, 15, 37),
        duration_days=3000,
        budget_millions=9000.0,
        crew=[crew1, crew2, crew3],
    )

    print("Valid mission created:")
    print(f"Mission: {valid.mission_name}")
    print(f"ID: {valid.mission_id}")
    print(f"Destination: {valid.destination}")
    print(f"Launch: {valid.launch_date}")
    print(f"Duration: {valid.duration_days} days")
    print(f"Budget: ${valid.budget_millions}M")
    print(f"Crew size: {len(valid.crew)}")
    print("Crew members:")
    # Read the mission's own list, so the printout stays true if
    # the crew passed above ever changes.
    for member in valid.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")

    print("\n" + SEPARATOR)
    print("Expected validation error:")

    # A crew of a lieutenant and an officer: every member is valid
    # on its own, so only the mission-level rule can reject this.
    try:
        SpaceMission(
            mission_name="Jupiter Colony Establishment",
            mission_id="M2026_JUPITER",
            destination="Jupiter",
            launch_date=dt.datetime(2056, 12, 1, 15, 37),
            duration_days=3000,
            budget_millions=9000.0,
            crew=[crew1, crew3],
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
