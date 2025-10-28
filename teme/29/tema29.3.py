# Task 3
# Implement a class Stadium. Class fields shout store the following:
# stadium's name, date of opening, country, city, seating capacity.
# Implement class methods for data input and output, provide access
#  to individual fields through class methods.
class Stadium:
    def __init__(self, name="", date_of_opening="", country="", city="", capacity=0):
        self.name = name
        self.date_of_opening = date_of_opening
        self.country = country
        self.city = city
        self.capacity = capacity

    # Method for data input
    def input_data(self):
        self.name = input("Enter stadium name: ")
        self.date_of_opening = input("Enter date of opening (e.g., YYYY-MM-DD): ")
        self.country = input("Enter country: ")
        self.city = input("Enter city: ")
        self.capacity = int(input("Enter seating capacity: "))

    # Method for data output
    def display_data(self):
        print("\nStadium Information:")
        print(f"Name: {self.name}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Seating Capacity: {self.capacity:,}")

    # Accessor methods (getters)
    def get_name(self):
        return self.name

    def get_date_of_opening(self):
        return self.date_of_opening

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    # Mutator methods (setters)
    def set_name(self, name):
        self.name = name

    def set_date_of_opening(self, date_of_opening):
        self.date_of_opening = date_of_opening

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity


# Example usage:
if __name__ == "__main__":
    stadium1 = Stadium()
    stadium1.input_data()
    stadium1.display_data()
