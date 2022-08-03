from fetchTerm import fetchTerm


def main():
    while True:
        query = input("Enter term : ")

        if query == "quit":
            break

        print(fetchTerm(query))

    print("Bye!")


if __name__ == "__main__":
    main()
