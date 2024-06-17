class Grid:
    def __init__(self, canvas, rows=6, cols=10, cell_size=50):
        # Draw vertical lines
        for i in range(cols + 1):
            x = i * cell_size
            canvas.create_line(x, 0, x, rows * cell_size, fill="black", width=5)

        # Draw horizontal lines
        for i in range(rows + 1):
            y = i * cell_size
            canvas.create_line(0, y, cols * cell_size, y, fill="black", width=5)

if __name__ == "__main__":
    print("Cannot run directly this file. Execute gui.py")
    # Additional code that runs when the script is executed directly
