def is_non_neg_float(s):
    return s > 0
def get_non_neg_float(message):
    number = -1
    times = 0
    check_number = is_non_neg_float(number)

    while not check_number:
        if times > 0: print("\nPlease enter a positive number!\n")
        try:
            print(message)
            number = float(input(": "))
        except ValueError:
            number = -1
        times += 1
        check_number = is_non_neg_float(number)

    return number

def calculate_area():
    print("This program asks for width and height and gives back the area.")
    height = round(get_non_neg_float("Please enter the height."))
    width = round(get_non_neg_float("Please enter the width."))
    area = round(height * width)

    print(f"\n\nThe height is {height}.\nThe width is {width}.\nThe area is {area}")

calculate_area()