#!/usr/bin/env python
# coding: utf-8

import sys
from cat import catFoodInfo
from post import post

cat_type = sys.argv[1]
cat_weight = sys.argv[2]
weight_unit = sys.argv[3]

cat_weight = float(cat_weight)

cat = catFoodInfo()
calorie = cat.getCalorie(cat_type, cat_weight, weight_unit)
table = cat.displayTable()

wp = post()
wp.post(calorie, "Calorie")
wp.post(table, "Calorie Table")
