
class ContactList(list):

    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    # Bellow is a class variable, common to all objects
    all_contacts = ContactList()

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __str__(self) -> str:
        return f"Contact name: {self.name}\t contact email: {self.email}"


class Supplier(Contact):

    def order(self, order) -> None:
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )


class Friend(Contact):

    def __init__(self, name, email, phone) -> None:
        super().__init__(name, email)
        self.phone = phone


class LongNameDict(dict):

    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


def main():
    print("### First Example ###")
    Contact("Someone1", "someone1@example.com")
    Contact("Someone2", "someone2@example.com")
    Contact("Someone3", "someone3@example.com")
    Friend("Friend1", "friend1@example.com", "1199999-9999")
    supplier = Supplier("Supplier", "supplier@example.com")

    for c in Contact.all_contacts:
        print(c)

    supplier.order("Some order item here")

    print([c.name for c in Contact.all_contacts.search("Sup")])

    print("\n### Second Example ###")
    long_keys = LongNameDict()
    long_keys["hello"] = 1
    long_keys["longest"] = 5
    long_keys["longest yet to date"] = 'world'
    print(long_keys.longest_key())


if __name__ == "__main__":
    main()
