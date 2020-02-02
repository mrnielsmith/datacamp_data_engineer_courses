from .data_shell import DataShell
import numpy as np

class StDevShell(DataShell):

    def __init__(self, filename):
        DataShell.filename = filename
        self.array = self._create_datashell()

    def get_stdev(self, col_pos):
        column = self.array[1:, col_pos].astype(np.float)
        stdev = np.ndarray.std(column, axis=0)
        return f"Standard Deviation of column {col_pos}: {stdev}"
