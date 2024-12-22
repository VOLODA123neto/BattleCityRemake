from wall import Wall
from map_data import map_data

def create_map(map_data, screen_width, screen_height, cell_size=50):
    walls = []
    
    max_col = (screen_width // cell_size) - 1
    max_row = (screen_height // cell_size) - 1
    
    for row in range(len(map_data)):
        for col in range(len(map_data[row])):
            x = col * cell_size
            y = row * cell_size
            
            if col <= max_col and row <= max_row:
                wall_type = map_data[row][col]
                if wall_type != 0:  
                    walls.append(Wall(x, y, cell_size, cell_size, wall_type))

    return walls