import json
import sys
import os
import csv
import ast
from datetime import datetime

from PySide2.QtCore import QObject, Signal, Slot


class AscConverter(QObject):
    progress_update = Signal(str)  # Define a custom signal for progress updates

    def __init__(self):
        super().__init__()
        print('asc_to_xyz converter')

    def ListAscToXyz(self, files_list):
        self.progress_update.emit("Rozpoczęcie konwersji asc na xyz")
        print("Rozpoczęcie konwersji asc na xyz")

        idx_file = 1
        files_count = len(files_list)
        for asc_file in files_list:
            # Get the directory and base name of the input file
            directory, base_name = os.path.split(asc_file)
            self.progress_update.emit(f"Konwertowanie pliku {idx_file} z {files_count}")
            print(f"Konwertowanie pliku {idx_file} z {files_count} ({base_name})")
            self.AscToXyz(asc_file)
            idx_file += 1

        self.progress_update.emit("Konwertowanie plików zakończone")
        print("Konwertowanie plików zakończone")

    def AscToXyz(self, input_file):
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

        x_param = 'xllcorner' if 'xllcorner' in lines[2].lower() else 'xllcenter'
        x_value = float(lines[2].split()[1])

        y_param = 'yllcorner' if 'yllcorner' in lines[3].lower() else 'yllcenter'
        y_value = float(lines[3].split()[1])

        cellsize = float(lines[4].split()[1])
        nodata_value = float(lines[5].split()[1])

        data = [list(map(float, line.split())) for line in lines[6:]]

        # Get the directory and base name of the input file
        directory, base_name = os.path.split(input_file)
        # Remove the original extension from the base name
        base_name = os.path.splitext(base_name)[0]
        # Create the output file path with the same directory and a new extension
        output_file = os.path.join(directory, f"{base_name}.xyz")

        with open(output_file, 'w') as f:
            for i in range(nrows):
                for j in range(ncols):
                    if data[i][j] != nodata_value:
                        x = x_value + (j + 0.5) * cellsize if x_param == 'xllcorner' else x_value + j * cellsize
                        y = y_value + (nrows - 1 - i + 0.5) * cellsize if y_param == 'yllcorner' else y_value + (
                                    nrows - 1 - i) * cellsize  # Flip the rows and add half of the cell size
                        z = data[i][j]
                        f.write(f"{x} {y} {z}\n")


def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]  # Get the ini_path from the command line
        converter = AscConverter()
        converter.AscToXyz(file_path)
    else:
        print("Uzycie:\n"
              "script.py <sciezka_pliku_asc>")
        sys.exit(1)

if __name__ == "__main__":
    main()
