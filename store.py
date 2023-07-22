import numpy as np
import pandas as pd

class Store:
    def __init__(self) -> None:
        self.sheet = self.loadData()

    def loadData(self):
        df = pd.read_excel('store.xlsx')
        return df
    
    def getHeaderFirstColumn(self):
        columns = self.sheet.columns.ravel()
        return columns[0]