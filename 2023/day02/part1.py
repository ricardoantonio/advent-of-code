available_cubes = {
  "red": 12,
  "green": 13,
  "blue": 14,
}

def extract_game_id(string):
    return int(string.split(":")[0][5:])

def extract_game_sets(string):
    sets = []
    for set_str in string.split(":")[1].split(";"):
        cubes = {color: int(quantity) for quantity, color in (cube.strip().split() for cube in set_str.split(","))}
        sets.append(cubes)
    return sets

def is_game_possible(sets, available_cubes): 
    for game_set in sets:
        for color, quantity in game_set.items():
            if quantity > available_cubes.get(color, 0):
                return False
    return True

sum_of_possible_game_ids = sum(
    extract_game_id(line.strip())
    for line in open("input.txt")
    if is_game_possible(extract_game_sets(line), available_cubes)
)

print(sum_of_possible_game_ids)