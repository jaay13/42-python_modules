import math


def get_player_pos() -> tuple[float, float, float]:
    """Prompt the user for 3D coordinates until valid input is given.

    Repeatedly asks for coordinates in the format 'x,y,z', validating
    that exactly three comma-separated values are provided and that
    each one can be converted to a float. Re-prompts on any invalid
    input instead of raising an error.

    Returns:
        tuple: The (x, y, z) coordinates as floats.
    """

    # Loop until a valid triplet is entered, re-prompting on every error
    while True:
        coords_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        coords = coords_input.split(",")

        # Unpacking raises ValueError itself when the count isn't exactly 3
        try:
            x_str, y_str, z_str = coords
        except ValueError:
            print("Invalid syntax")
            continue

        # Convert each axis separately so the faulty one can be named
        try:
            x = float(x_str)
        except ValueError as e:
            print(f"Error on parameter '{x_str}': {e}")
            continue
        try:
            y = float(y_str)
        except ValueError as e:
            print(f"Error on parameter '{y_str}': {e}")
            continue
        try:
            z = float(z_str)
        except ValueError as e:
            print(f"Error on parameter '{z_str}': {e}")
            continue
        break
    return x, y, z


def main() -> None:
    print("=== Game Coordinate System ===")

    # A tuple prints as a whole, and is also indexable element by element
    print("\nGet a first set of coordinates")
    coords_1 = get_player_pos()
    print(f"Got a first tuple: {coords_1}")
    print(f"It includes: X={coords_1[0]}, Y={coords_1[1]}, Z={coords_1[2]}")

    # 3D extension of pythagorean theorem: distance to the origin (0, 0, 0)
    distance_center = math.sqrt(
        coords_1[0] ** 2
        + coords_1[1] ** 2
        + coords_1[2] ** 2
    )
    print(f"Distance to center: {round(distance_center, 4)}")

    print("\nGet a second set of coordinates")
    coords_2 = get_player_pos()

    # distance between the two points
    distance_coords = math.sqrt(
        (coords_1[0] - coords_2[0]) ** 2
        + (coords_1[1] - coords_2[1]) ** 2
        + (coords_1[2] - coords_2[2]) ** 2
    )
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(distance_coords, 4)}"
    )


if __name__ == "__main__":
    main()
