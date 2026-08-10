"""Validate alien contact reports with cross-field business rules.

Field constraints (length, range) can only judge one value at a
time. Rules like "telepathic contact needs 3 witnesses" depend on
two fields at once, so they live in a @model_validator instead.
"""

import datetime as dt
from enum import StrEnum

from pydantic import BaseModel, Field, ValidationError, model_validator

SEPARATOR = "=" * 40


class ContactType(StrEnum):
    """How the contact was made.

    StrEnum rather than Enum so members print as "radio" instead
    of "ContactType.RADIO", which is what the report expects.
    With a plain Enum every print site would need .value instead,
    and a forgotten one would quietly print the member name.
    """

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """A single contact report, validated on creation."""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: dt.datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    # default=None is what makes the field omissible; "str | None"
    # alone would still require the key to be present.
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def custom_rules(self) -> "AlienContact":
        """Apply the Observatory's rules once every field is valid.

        mode="after" means the fields have already been parsed, so
        witness_count is a real int and contact_type a real enum
        member. Failures are raised as ValueError - Pydantic wraps
        them into the ValidationError the caller finally sees.
        """
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        # "not message_received" also catches an empty string, which
        # is as useless as no message at all.
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        # An "after" validator must hand the model back, or the
        # instance is lost.
        return self


def main() -> None:
    """Show one accepted report, then one rejected by a rule."""
    print("Alien Contact Log Validation")
    print(SEPARATOR)

    valid_contact = AlienContact(
        contact_id="AC_2026_001",
        timestamp=dt.datetime.now().astimezone(),
        contact_type=ContactType.RADIO,    # works aswell: "radio"
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )

    print("Valid contact report:")
    print(f"ID: {valid_contact.contact_id}")
    print(f"Time: {valid_contact.timestamp}")
    print(f"Type: {valid_contact.contact_type}")
    print(f"Location: {valid_contact.location}")
    print(f"Signal: {valid_contact.signal_strength}/10")
    print(f"Duration: {valid_contact.duration_minutes} minutes")
    print(f"Witnesses: {valid_contact.witness_count}")
    print(f"Message: '{valid_contact.message_received}'\n")

    print(SEPARATOR)
    print("Expected validation error:")

    # Telepathic with a single witness: every field is individually
    # valid, so only the cross-field rule can reject this.
    try:
        AlienContact(
            contact_id="AC_2026_002",
            timestamp=dt.datetime(2026, 8, 17, 11, 47),
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
        )
    except ValidationError as e:
        # Pydantic labels anything we raised as "Value error, ...".
        # Dropping that prefix leaves our own message, and leaves a
        # built-in one (out of range, too short) untouched.
        for error in e.errors():
            print(error["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
