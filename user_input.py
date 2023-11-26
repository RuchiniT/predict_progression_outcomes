credit_range = [0, 20, 40, 60, 80, 100, 120]


def credit_input(print_text):
    """
    Validate user input(Check for integer and out of range).

    Parameters:
    - print_text (string): The print text for new input.

    Returns:
    int: Validated user input.
    """

    while True:
        # Reference: https://stackoverflow.com/a/23294659
        try:
            credit = int(input(print_text))
        except ValueError:
            print("Integer required.\n")
        else:
            if not credit in credit_range:
                print("Out of range.\n")
            else:
                break
    return credit
