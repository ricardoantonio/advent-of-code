def extract_game_sets(string):
    sets = []
    for set_str in string.split(":")[1].split(";"):
        cubes = {color: int(quantity) for quantity, color in (cube.strip().split() for cube in set_str.split(","))}
        sets.append(cubes)
    return sets

def calculate_set_power(sets): 
    minimum_required = {}
    for game_set in sets:
        for color, quantity in game_set.items():
            minimum_required[color] = max(quantity, minimum_required.get(color, 0))
    
    power = 1
    for color in minimum_required:
        power *= minimum_required[color]
    
    return power

sum_of_possible_game_ids = sum(
    calculate_set_power(extract_game_sets(line.strip()))
    for line in open("input.txt")
)

print(sum_of_possible_game_ids)