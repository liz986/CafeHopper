from tabulate import tabulate


cafes = {"Sunrise Cafe": [10, "Art Cafe", "Savoury"],
         "The Cozy Cup": [20, "Book Cafe", "Bakery"],
         "The Rustic Bean": [30, "Book Cafe", "Coffee"],
         "The Daily Grind": [40, "Productivity Cafe", "Savoury"],
         "Coffee Canvas": [50, "Art Cafe", "Coffee"],
         "Byte & Bean": [60, "Productivity Cafe", "Bakery"],
         "Meow & Mocha": [15, "Cat Cafe", "Dessert"],
         "Tabby's Teahouse": [25, "Cat Cafe", "Savoury"],
         "Matcha Break": [35, "Japanese Cafe", "Bakery"],
         "The Timeless Teapot": [45, "Japanese Cafe", "Dessert"]}
names = list(cafes.keys())


def main():
    print("\n Welcome to CafeHopper!")
    print()
    print(tabulate([["Choice", "Duration"], ["A", "15 minutes or less"], ["B", "30 minutes or less"], ["C", "45 minutes or less"],
                    ["D", "1 hour or less"], ["E", "No preference"]], headers = "firstrow", tablefmt = "grid"))
    ch1 = input("Select a choice to get started: ").upper()
    itinerary_time = filter_time(ch1)

    print()
    print(tabulate([["Choice", "Theme"], ["A", "Book Cafe"], ["B", "Art Cafe"], ["C", "Productivity Cafe"],
                    ["D", "Cat Cafe"], ["E", "Japanese Cafe"], ["F", "No preference"]], headers = "firstrow", tablefmt = "grid"))
    ch2 = input("Choose your theme: ").upper()
    itinerary_theme = filter_theme(ch2)

    print()
    print(tabulate([["Choice", "Specialty"], ["A", "Savoury"], ["B", "Dessert"], ["C", "Coffee"], ["D", "Bakery"],
                    ["E", "No preference"]], headers = "firstrow", tablefmt = "grid"))
    ch3 = input("Are you looking for a specialty? ").upper()
    itinerary_specialty = filter_specialty(ch3)

    itinerary = list(set(itinerary_time) & set(itinerary_theme) & set(itinerary_specialty))
    print()
    if len(itinerary) == 0:
        print("Sorry, we can't find cafes that suit your requirements")
    else:
        print("Here is your recommended itinerary: ")
        final = {"Name": ["Minutes away", "Theme", "Specialty"]}
        for cafe in itinerary:
            final[cafe] = cafes[cafe]
        print(tabulate(final, headers="keys"))
        print()


def filter_time(ch):
    options = []
    for name in names:
        data = cafes[name]
        match ch:
            case "A":
                if data[0] <= 15:
                    options.append(name)
            case "B":
                if data[0]  <= 30:
                    options.append(name)
            case "C":
                if data[0]  <= 45:
                    options.append(name)
            case "D" | "E":
                options = names
            case _:
                print("Invalid choice")
                break
    return options

def filter_theme(ch):
    options = []
    for name in names:
        match ch:
            case "A":
                if "Book Cafe" in cafes[name]:
                    options.append(name)
            case "B":
                if "Art Cafe" in cafes[name]:
                    options.append(name)
            case "C":
                if "Productivity Cafe" in cafes[name]:
                    options.append(name)
            case "D":
                if "Cat Cafe" in cafes[name]:
                    options.append(name)
            case "E":
                if "Japanese Cafe" in cafes[name]:
                    options.append(name)
            case "F":
                options = names
            case _:
                print("Invalid choice")
                break
    return options


def filter_specialty(ch):
    options = []
    for name in names:
        match ch:
            case "A":
                if "Savoury" in cafes[name]:
                    options.append(name)
            case "B":
                if "Dessert" in cafes[name]:
                    options.append(name)
            case "C":
                if "Coffee" in cafes[name]:
                    options.append(name)
            case "D":
                if "Bakery" in cafes[name]:
                    options.append(name)
            case "E":
                options = names
            case _:
                print("Invalid choice")
                break
    return options


if __name__ == "__main__":
    main()