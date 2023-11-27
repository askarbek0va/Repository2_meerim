import random

def initialize_cargo():
    # Initialize three boxes with random weights and random initial locations
    boxes = [{"weight": random.randint(100, 300), "location": random.randint(1, 7)} for _ in range(3)]
    return boxes

def move_boxes(boxes):
    # Simulate the movement of boxes with legs
    for box in boxes:
        box["location"] = (box["location"] + 1) % 7  # Assuming a circular path of 7 kilometers

def check_cargo(boxes, marks):
    total_weight = 0
    correct_locations = 0

    for i, box in enumerate(boxes):
        if marks[i] == box["location"]:
            total_weight += box["weight"]
            correct_locations += 1

    return total_weight, correct_locations == len(boxes)

def main():
    print("Welcome to the Martian Cargo Finder Program!")

    cargo_boxes = initialize_cargo()

    while True:
        marks = []
        for i in range(3):
            mark = int(input(f"Enter the kilometer mark for box {i + 1}: "))
            marks.append(mark)

        move_boxes(cargo_boxes)
        total_weight, cargo_found = check_cargo(cargo_boxes, marks)

        if cargo_found and total_weight == 713:
            print("Congratulations! You found all the cargo.")
            break
        else:
            print("Cargo not found or incorrect. Boxes moved. Try again.")

if __name__ == "__main__":
    main()
