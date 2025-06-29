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
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all_contacts(args, contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

@input_error
def say_hello(args, contacts=None):
    return "How can I help you?"

@input_error
def parse_command(command_input):
    parts = command_input.strip().split()
    if not parts:
        raise IndexError
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    contacts = {}
    while True:
        command_input = input("Enter a command: ")

        result = parse_command(command_input)
        if not isinstance(result, tuple):
            print(result)  # Показує повідомлення про помилку, якщо воно є
            continue

        command, args = result

        if command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(args, contacts))
        elif command == "hello":
            print(say_hello(args))
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()