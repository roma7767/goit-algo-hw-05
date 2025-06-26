
contacts = {}

# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such contact found."
        except IndexError:
            return "Please enter a command and arguments."
    return inner

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_phone(args):
    name = args[0]
    return contacts[name]

@input_error
def show_all_contacts(args):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

# Головний цикл
def main():
    while True:
        command_input = input("Enter a command: ").strip()
        if not command_input:
            continue

        parts = command_input.split()
        command = parts[0].lower()
        args = parts[1:]

        if command == "add":
            print(add_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all_contacts(args))
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()