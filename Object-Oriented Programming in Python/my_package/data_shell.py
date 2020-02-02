import numpy as np
from scipy import stats

class DataShell:
    # class variable
    family = 'DataShell'

    # constructor
    def __init__(self, filename):
        # instance variables/attributes
        self.filename = filename
        self.array = self._create_datashell()

    # method to create shell from fileobject
    def _create_datashell(self):
        self.array = np.genfromtxt(self.filename, delimiter=',', dtype='unicode')
        return self.array

    # method to rename column
    def rename_column(self, old_colname, new_colname):
        for index, value in enumerate(self.array[0]):
            if value == old_colname:
                self.array[0][index] = new_colname
        return self.array

    def show_shell(self):
        print(self.array)

    def five_figure_summary(self, col_pos):
        statistics = stats.describe(self.array[1:][col_pos].astype(np.float))
        return f"Five-figure stats of column {col_pos}: {statistics}"
