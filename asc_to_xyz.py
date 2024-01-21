def ascii_grid_to_xyz(input_file, output_file):
    """
    Convert ASCII grid file to XYZ format.

    Parameters:
    - input_file: Input ASCII grid file path.
    - output_file: Output XYZ file path.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Assuming the first six lines are header information
    ncols = int(lines[0].split()[1])
    nrows = int(lines[1].split()[1])

    x_param = 'xllcorner' if 'xllcorner' in lines[2] else 'xllcenter'
    x_value = float(lines[2].split()[1])

    y_param = 'yllcorner' if 'yllcorner' in lines[3] else 'yllcenter'
    y_value = float(lines[3].split()[1])

    cellsize = float(lines[4].split()[1])
    nodata_value = float(lines[5].split()[1])

    data = [list(map(float, line.split())) for line in lines[6:]]

    with open(output_file, 'w') as f:
        for i in range(nrows):
            for j in range(ncols):
                if data[i][j] != nodata_value:
                    x = x_value + (j + 0.5) * cellsize if x_param == 'xllcorner' else x_value + j * cellsize
                    y = y_value + (nrows - 1 - i + 0.5) * cellsize if y_param == 'yllcorner' else y_value + (nrows - 1 - i) * cellsize  # Flip the rows and add half of the cell size
                    z = data[i][j]
                    f.write(f"{x} {y} {z}\n")


# Example usage:
#ascii_grid_file = r'test_data\77912_1385086_7.126.11.20.asc'
#xyz_output_file = r'test_data\77912_1385086_7.126.11.20.xyz'

#ascii_grid_to_xyz(ascii_grid_file, xyz_output_file)