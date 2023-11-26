from graphics import *


def draw_column_chart(title, column_names, column_counts, chart_footer):
    """
    Draw Histogram using user inputted data.

    Parameters:
    - title (string): Histogram Title.
    - column_names (string): Histogram column names ["Progress", "Trailer", "Retriever", "Excluded"].
    - column_counts (int): Histogram column count(Default value 4).
    - chart_footer (string): Histogram footer (Display total outcomes).

    Returns:
    None.
    """

    while True:
        try:
            column_colours = ["cyan", "magenta", "orange", "light green"]
            histogram_window = GraphWin("Histogram", 640, 480)

            histogram_title = Text(Point(300, 30), title)
            histogram_title.setSize(18)
            histogram_title.draw(histogram_window)

            column_count = len(column_names)
            column_width = 100
            starting_x = 50
            starting_y = 80
            max_credit_count = max(column_counts)

            for i in range(column_count):
                x1 = starting_x + i * (column_width + 20)
                y1 = starting_y + ((max_credit_count - column_counts[i]) / max_credit_count) * 250
                x2 = x1 + column_width
                y2 = starting_y + 250

                column = Rectangle(Point(x1, y1), Point(x2, y2))
                column.setFill(column_colours[i])
                column.draw(histogram_window)

                column_name = Text(Point((x1 + x2) / 2, y2 + 15), column_names[i])
                column_name.draw(histogram_window)

                count_text = Text(Point((x1 + x2) / 2, y1 - 15), str(column_counts[i]))
                count_text.draw(histogram_window)

            histogram_footer = Text(Point(300, 380), chart_footer)
            histogram_footer.setSize(12)
            histogram_footer.draw(histogram_window)

            histogram_window.getMouse()
            histogram_window.close()
        except GraphicsError:
            # Reference: https://stackoverflow.com/a/61252777
            break
