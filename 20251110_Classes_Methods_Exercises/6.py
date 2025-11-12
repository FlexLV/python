
class AddressBook:
    def __init__(self):
        self.addresses = []

    def add_address(self, name, address):
        entry = {"name": name, "address": address}
        self.addresses.append(entry)
        print(f"Added address for {name}.")

    def find_address(self, name):
        for entry in self.addresses:
            if entry["name"].lower() == name.lower():
                return entry["address"]
        return "Address not found."

book = AddressBook()
book.add_address("Alice", "123 Main Street, Berlin")
book.add_address("Bob", "42 Park Avenue, Munich")

print(book.find_address("Alice"))
print(book.find_address("Charlie"))
