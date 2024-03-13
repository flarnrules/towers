# calculates the panel size overlay for ASTEROID_TOWERS

new_canvas_grid_x = 5
current_canvas_x = 768

new_canvas_grid_y = new_canvas_grid_x
current_canvas_y = current_canvas_x

panel_x = current_canvas_x / new_canvas_grid_x
panel_y = panel_x
panel_size = f"{panel_y}x{panel_x}"

print(f"The panel size you want is: {panel_size}")