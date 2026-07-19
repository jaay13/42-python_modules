
def ft_count_harvest_iterative():
    until_harvest = int(input("Days until harvest: "))
    for x in range(1, until_harvest+1):
        print(f"Day {x}")
    print("Harvest time!")
