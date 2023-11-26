from chart import draw_column_chart
from data import levels, outcomes
from user_input import credit_input

progressions = []
progress = 0
trailer = 0
retriever = 0
excluded = 0

while True:
    # run the program until user exit
    while True:
        # run the program until user input data meet the correct total.
        pass_credits = credit_input("Enter your total PASS credits: ")
        defer_credits = credit_input("Enter your total DEFER credits: ")
        fail_credits = credit_input("Enter your total FAIL credits: ")

        user_credits = [pass_credits, defer_credits, fail_credits]
        total = sum(user_credits)

        if total == 120:
            for level in levels:
                if user_credits == level:
                    position = levels.index(level)
                    progressions.append(position)
                    outcome = outcomes[position]
                    if outcome == "Progress":
                        progress += 1
                    elif outcome == "Progress(module trailer)":
                        trailer += 1
                    elif outcome == "Do not Progress-module retriever":
                        retriever += 1
                    elif outcome == "Exclude":
                        excluded += 1
                    print(outcome)
                    break    # break the for loop after finding correct level.
            break    # break the while true loop - correct total.
        elif total < 120 or total > 120:
            print("Total incorrect.\n")

    while True:
        # prompt user input until user input correct option(q/y).
        option = input(
            "\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        print()
        if option != "q" and option != "y":
            print("Input must be 'q' or 'y'.\n")
        else:
            break
    if option == "q":
        break

total_inputs = progress + trailer + retriever + excluded

print("\nPart 2:")
for progression in progressions:
    level = levels[progression]
    outcome = outcomes[progression]
    final_output = outcome + " - " + str(level[0]) + ", " + str(level[1]) + " , " + str(level[2])
    print(final_output)

chart_title = "Histogram Results"
column_names = ["Progress", "Trailer", "Retriever", "Excluded"]
column_counts = [progress, trailer, retriever, excluded]
chart_footer = str(total_inputs) + " outcomes in total."

draw_column_chart(chart_title, column_names, column_counts, chart_footer)

