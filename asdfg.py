import random

def approximate_cargo_location():
    return random.sample(range(1, 8), 3)
# we took range from 1 to 8, because the city was 7 kilometers away, so the Martians could hide cargos only in that distance


def check_cargo_locations (locations, kilometers):
    if len(locations)!= len(kilometers):
        return False
    for i in range(3):
         if locations[i]!= kilometers[i]:
             return False
    return True

def check_total_weight(total_weight,weights):
    return total_weight == sum(weights)
# the total weight should be equal to 713 kg
def main():
     total_weight=713
     weights=[]
     while True:
        cargo_location=approximate_cargo_location()
        print(cargo_location)
        kilometers=[]
        for i in range(3):
            kilometer_of_cargo = int(input(f"Enter the kilometer mark (number from 1 to 7) for box {i + 1}: "))
            kilometers.append(kilometer_of_cargo)
        cargo_found=check_cargo_locations(cargo_location,kilometers)
        if cargo_found:
            print("Congratulations! You found all the cargo.Now let's find their weights.")
            for i in range(3):
                weight = int(input(f'Enter the weight for box {i + 1}: '))
                weights.append(weight)
            cargo_weight = check_total_weight(total_weight, weights)
            if cargo_weight:
                print("Congratulations! You found all the cargo!")
                break
            else:
                 print("Fail, you entered wrong weight. Try again.")
        else:
             cargo_location=approximate_cargo_location()
             print(  'Fail, the cargoes were not found. Cargoes have changed their location,enter new kilometer marks.')
main()
