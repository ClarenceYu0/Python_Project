#Clarence Yu R00213439

id_counter = 0
booking_space = 30

def read_file(filename):
    accommodation = []
    season_cost = []
    booking_no = []
    with open(filename) as file_handler:
        while True:
            line = file_handler.readline()
            if line == "":
                break
            line_data = line.split(",")
            accommodation.append(str(line_data[0]))
            season_cost.append(int(line_data[1]))
            booking_no.append(int(line_data[2]))

    return accommodation, season_cost, booking_no

def write_to_file(filename, accommodation, season_cost, booking_no):
    with open(filename, "w") as file_handler:
        for i, item in enumerate(accommodation):
            print(item + "," + str(season_cost[i]) + "," + str(booking_no[i]), file=file_handler)

def booking():
    accommodation, season_cost, booking_no = read_file('Booking_2022.txt')
    extras_value = read_extra_file('Extra.txt')
    total_cost = 0
    allowed_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '\'']

    kids_camp_price = 100
    pool_pass_price = 150

    while True:
        surname = input("Enter your surname : ")
        if any(x not in allowed_char for x in surname):
            print("You did not enter a valid name\n")
        elif 1 > len(surname) > 14:
            print("You did not enter a valid name\n")
        else:
            break

    contact_num = input("Enter your contact number : ")
    while True:
        if 0 == len(contact_num) or len(contact_num) >= 12 or contact_num.isnumeric() == False:
            contact_num = input("Enter your contact number : ")
        else:
            break

    print("Choose the type of accommodation : ")
    for i, type in enumerate(accommodation):
        print(f"{i+1}. {type} (€{season_cost[i]}) {booking_no[i]} booked ")

    print("4. No Booking")
    accommodation_type = int(input("=> "))
    while True:
        if 4 < accommodation_type or accommodation_type < 1:
            accommodation_type = int(input("=> "))
        else:
            break

    while True:
        if accommodation_type == 1:
            total_cost += season_cost[accommodation_type-1]
            break
        elif accommodation_type == 2:
            total_cost += season_cost[accommodation_type-1]
            break
        elif accommodation_type == 3:
            total_cost += season_cost[accommodation_type-1]
            break
        else:
            accommodation_type = int(input("=> "))

    while True:
        people_num = input("Enter the number of people : ")
        try:
            people_num = int(people_num)
            if people_num <= 0:
                print("Number must be greater than 0")
            else:
                break
        except ValueError:
            print("You must enter a number")

    family_pool = str(input("Do you wish to buy a family pool Y/N : "))
    while True:
        if family_pool.upper() != "Y" and family_pool.upper() != "N":
            family_pool = str(input("Do you wish to buy a family pool Y/N : "))
        elif family_pool.upper() == 'Y':
            total_cost += pool_pass_price
            extras_value[1] += 1
            break
        else:
            break

    while True:
        children_num = input("Enter the number of children : ")
        try:
            children_num = int(children_num)
            if children_num < 0 or children_num > people_num:
                print("Children must not exceed the number of people")
            else:
                total_cost += (children_num*kids_camp_price)
                extras_value[0] += children_num
                break
        except ValueError:
            print("You must enter a number")

    global id_counter
    id_counter += 1

    # open a file using surname and print details into that file
    filename = f"{surname}_{id_counter:02d}.txt"
    with open(filename, "w") as output:
        print(f"ID:{id_counter:02d}", file=output)
        print(f"Surname:{surname}", file=output)
        print(f"Contact Number:{contact_num}", file=output)
        print(f"Accommodation Type:{accommodation_type}", file=output)
        print(f"No. of people:{people_num}", file=output)
        print(f"No. of children:{children_num}", file=output)
        print(f"Cost:€{total_cost}", file=output)

    type = accommodation[accommodation_type - 1]

    write_extra_file("Extra.txt", extras_value)

    return surname, contact_num, type, people_num, children_num, family_pool, total_cost

def read_extra_file(filename):
    extras_values = []
    with open(filename, "r") as location:
        for line in location:
            stripped_line = line.strip('\n')
            line_data = stripped_line.split(',')
            extras_values.append(int(line_data[1]))

    return extras_values

def write_extra_file(filename, extra_values):
    extra_names = ['Kids Camp', 'Pool Pass']
    with open(filename, "w") as file_handler:
        for i, item in enumerate(extra_names):
            print(f"{item},{extra_values[i]}", file=file_handler)

def get_menu_choice():
    print("LONG ISLAND HOLIDAYS")
    print("=" * 20)
    print("1. Make a Booking")
    print("2. Review Booking")
    print("3. Exit")

    while True:
        try:
            choice = int(input("=>"))
            if 1 <= choice <= 3:
                break
            else:
                print('Please Enter a valid choice')
        except ValueError:
            print("Please Enter a valid choice")
    return choice

def booking_detail():
    accommodation, season_cost, booking_no = read_file("Booking_2022.txt")
    global id_counter

    surname, contact_num, type, people_num, children_num, family_pool, total_cost = booking()
    print("Booking Details")
    print("=" * 15)
    print(f"Booking id :{id_counter}")
    print(f"Accommodation Type : {type}")
    print(f"No of people : {people_num}")
    print(f"Pool Pass : {family_pool}")
    print(f"No. for kids club : {children_num}")
    print(f"Cost €{total_cost}")
    print("=" * 20)

    for i, item in enumerate(accommodation):
        if type == item:
            booking_no[i] = booking_no[i] + 1

    write_to_file("Booking_2022.txt", accommodation, season_cost, booking_no)

    return total_cost

def booking_reviews(total_cost):
    global id_counter
    accommodation, season_cost, booking_no = read_file("Booking_2022.txt")
    kids_camp, pool_pass = read_extra_file("Extra.txt")
    print("=" * 20)
    print(f"{accommodation[0]} booked: {booking_no[0]}")
    print(f"{accommodation[1]} booked: {booking_no[1]}")
    print(f"{accommodation[2]} booked: {booking_no[2]}")
    print(f"Kids Camp:{kids_camp}")
    print(f"Pool Pass:{pool_pass}")
    print(f"Total income:{total_cost}")
    print(f"Average income:{total_cost/id_counter}")
    print(f"Booking space:{booking_space}")
    print("=" * 20)

def main():
    global booking_space
    counter = 0
    while True:
        choice = get_menu_choice()
        if choice == 1:
            counter += 1
            booking_space -= 1
            total_cost = booking_detail()
        elif choice == 2:
            if counter == 0:
                print("No bookings have been made")
            else:
                booking_reviews(total_cost)
        elif counter:
            break

        if booking_space == 0:
            print("There is no more booking space ")
            break

main()