# our dunn program will show us core OOP concepts:
# encapsulation data which is menu and prices they will be bundled in the class
# Abstraction: complies delivery logic is hidden behind simple method calls

class DunnDelivery:
    def __init__(self):
        # class attriubes that show encapsulation which keeps related data together
        self.menu = {
            "Energy Drinks": ["Red bull", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuchino", "Oreo cafe Cooler", "Rasberry Cooler", "Hot Choclate"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Burger", "Falafel Wrap", "Chicken Wrap"]
        }

        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuchino": 4.99,"Oreo cafe Cooler": 5.99, "Rasberry Cooler": 5.99, "Hot Choclate": 5.99,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Burger": 8.99, "Falafel Wrap": 8.99, "Chicken Wrap": 8.99
        }

        self.delivery_locations = {
            "Libary": 10,
            "Academic Success Centre": 8,
            "ITEC computer lab": 5
        }
        # our next step will show the items avalible for delivery

    def show_menu(self, category=None):
        if category:
            print(f"\n=== {category} ===")
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}")
        else:
            for category in self.menu:
                print(f"\n=== {category} ===")
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}")


    def calculate_total(self, items, has_student_id=False):
        total = sum(self.prices[items] for item in items)

        if has_student_id:
         total *= 0.9
        return total
        

        

    def estimate_delivery(self, location, current_hour):
        base_time = self.delivery_locations[location]
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            return base_time + 5
        return base_time

    # this method will print the order for the delivery orders
    def print_order(self, location, items, current_hours, has_student_id=False):
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems Ordered")
        for items in items:


            print(f"- {items}: ${self.prices[items]}:.2f")
        total = self.calculate_total(items, has_student_id);
        delivery_time = self.estimate_delivery(location, current_hours)
        print(f"\nSubtotal: ${sum(self.prices[items] for item in items):.2f}")
        if has_student_id and total < sum(self.prices[items] for item in items):
            print("student discount applied!")
        print(f"total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

    def rating_delivery(self, rating):
        if 1 <= rating <= 5:
         print(f"thank you for choosing our store. hope to see you soon ")
        else:
            print("you entered a invalid rating, please enter a number 1-5")


def main():
    delivery = DunnDelivery() 

    delivery.show_menu("Coffee Drinks")

    order = ["Latte", "Bagel"]

    delivery.print_order("ITEC computer lab", order, 9, has_student_id=True)
    
    user_input = input("please enter a rating from 1 - 5 = ")
    rating = int(user_input)
    delivery.rating_delivery(rating)

    
       
if __name__ == "__main__":
    main()
4