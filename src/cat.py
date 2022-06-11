#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

class catFoodInfo:
    table = {"weight_in_kg" : [2.3, 3.4, 4.5, 5.7, 6.8, 7.9, 9.1],
        "weight_in_lbs" : [5, 7.5, 10, 12.5, 15, 17.5, 20],
        "neutered_or_spayed" : [157, 210, 260, 298, 354, 296, 440],
        "intact" : [183, 245, 303, 262, 413, 462, 513],
        "prone_to_gaining_weight": [131, 175, 216, 258, 295, 330, 367],
        "Pet_in_need_of_weight_loss": [105, 140, 173, 207, 236, 264, 293]}
    df = pd.DataFrame.from_dict(table)
        
    def getCalorie(self, type: str, weight: int, unit: str):
        z=np.polyfit(self.df[unit], self.df[type], 1) # 기울기와 절편 확인
        f=np.poly1d(z) 
        kcal = f(weight)
        u = unit[9:]
        h1 = "<h1> Diagnosis </h1>"
        p1 = "<p>Your cat needs " + str(round(kcal, 1)) + " kcal a day<p>"
        p2 = "<p>your cat's weight: "+str(weight)+u+" </p>"
        p3 = "<p>your cat's type: "+type+" </p>"
        html = "<html><body>" + h1 + p1 + p2 + p3 + "</body></html>"
        return html

    def displayTable(self):
        return self.df.to_html()

