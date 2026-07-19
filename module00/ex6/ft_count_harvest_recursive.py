
def ft_count_harvest_recursive(default=None):
    if default == 0:
        return

    if (default is None):
        days = int(input("Days until harvest: "))
        ft_count_harvest_recursive(days)
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(default - 1)
        print(f"Day {default}")
