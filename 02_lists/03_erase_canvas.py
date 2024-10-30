from graphlib import Canvas
import time

CANVAS_WIDTH : int = 400
CANVAS_HEIGHT : int = 400

CELL_SIZE : int = 40
ERASER_SIZE : int = 20

def erase_object(canvas, eraser):
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
# Calculate where our eraser is
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find things that overlap with our eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # For everything that overlaps with our eraser (that isn't our eraser), change
    # its color to white
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')

# There is no need to edit code beyond this point

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE  # Figure out how many rows of cells we need
    num_cols = CANVAS_WIDTH // CELL_SIZE   # Figure out how many columns of cells we need
    
    # Make a grid of squares based on the number of rows and columns.
    # The rows and columns along with our cell size help determine where
    # each individual cell belongs in our grid!
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE   # The right coordinate of the cell is CELL_SIZE pixels away from the left
            bottom_y = top_y + CELL_SIZE   # The bottom coordinate of the cell is CELL_SIZE pixels away from the top
            
            # Create a single cell in the grid
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
            
            
    canvas.wait_for_click()  # Wait for the user to click before creating the eraser
    
    last_click_x, last_click_y = canvas.get_last_click()  # Get the starting location for the eraser
    
    # Create our eraser
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )
    
    # Move the eraser, and erase what it's touching
    while True:
        # Get where our mouse is and move the eraser to there
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        # Erase anything touching the eraser
        erase_object(canvas, eraser) 
        
        time.sleep(0.05)


if __name__ == '__main__':
    main()