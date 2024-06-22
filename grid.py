class Grid:
    def __init__(self, canvas, rows=6, cols=6, cell_size=50):
        initial_offset = 20
        line_horizontal = initial_offset + cols * cell_size
        line_vertical = initial_offset + rows * cell_size
        # Draw vertical lines
        for i in range(cols + 1):
            x = initial_offset + i * cell_size
            canvas.create_line(x, initial_offset, x, line_vertical, fill="black", width=5)

        # Draw horizontal lines
        for i in range(rows + 1):
            y = initial_offset + i * cell_size
            canvas.create_line(initial_offset, y, line_horizontal, y, fill="black", width=5)

if __name__ == "__main__":
    print("Cannot run directly this file. Execute gui.py")
    # Additional code that runs when the script is executed directly
