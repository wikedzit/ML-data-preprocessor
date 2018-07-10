# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Preprocessor:
    dataset = []
    targetIndex = -1;
    targetVariable = []
    independentVaraibles = []
    
    def __init__(self, dataSource, targetIndex = -1):
        self.dataset = pd.read_csv(dataSource)
        self.targetIndex = targetIndex
        self.setIndependentAndTargetValues()
        
    def getDataset(self):
        return self.dataset

    def setDataset(self, dataset):
        self.dataset = dataset
        
    def setIndependentAndTargetValues(self):
        self.targetVariable = self.dataset.iloc[:,-1].values
        self.independentVariables = self.dataset.iloc[:,:-1].values
        if self.targetIndex == 0:
            self.targetVariable = self.dataset.iloc[:,0].values
            self.independentVariables = self.dataset.iloc[:,1:-1].values
            
            
preprocessor = Preprocessor('Data.csv')

Y = preprocessor.targetVariable
X = preprocessor.independentVariables
