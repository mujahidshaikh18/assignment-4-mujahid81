import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20


def erase_objects(canvas, eraser, cells):
    """Erase objects in contact with the eraser."""
    # Get the coordinates of the eraser
    left_x, top_y, right_x, bottom_y = canvas.coords(eraser)

    # Check for overlaps
    for cell in cells:
        cell_coords = canvas.coords(cell)
        if (
            left_x < cell_coords[2]
            and right_x > cell_coords[0]
            and top_y < cell_coords[3]
            and bottom_y > cell_coords[1]
        ):
            canvas.itemconfig(cell, fill="white")


def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Eraser Canvas")

    # Create the canvas widget
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    # Create grid of blue cells
    cells = []
    for row in range(CANVAS_HEIGHT // CELL_SIZE):
        for col in range(CANVAS_WIDTH // CELL_SIZE):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue")
            cells.append(cell)

    # Create the eraser
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

    # Function to move the eraser with the mouse
    def on_mouse_move(event):
        canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        erase_objects(canvas, eraser, cells)

    # Bind mouse motion to eraser movement
    canvas.bind("<Motion>", on_mouse_move)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
