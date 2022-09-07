import pandas as pd
from sklearn.metrics import roc_curve, auc


class data_type:
    def __init__(self, min_age, blood_presure_lower_bound, family_history, low_WHR, is_male, is_diabetic, is_smoker,
                 ten_year_cardi_risk):
        self.min_age = min_age
        self.blood_presure_lower_bound = blood_presure_lower_bound
        self.family_history, low_WHR = family_history, low_WHR
        self.is_male = is_male
        self.is_diabetic = is_diabetic
        self.is_smoker = is_smoker
        self.ten_year_cardi_risk = ten_year_cardi_risk

    def set_goal_val(self, goal_val):
        self.goal_val = goal_val


class data_sample:
    def __init__(self, age, blood_presure, family_history, low_WHR, is_male, is_diabetic, is_smoker,
                 ten_year_cardi_risk):
        if age >= 75:
            self.min_age = 75
        else:
            self.min_age = 10 * int((age - 5) / 10) + 5
        # self.age = age
        if blood_presure >= 160:
            self.blood_presure_lower_bound = 160
        elif blood_presure < 120:
            self.blood_presure_lower_bound = 0
        else:
            self.blood_presure_lower_bound = 10 * int(blood_presure / 10)
        # self.blood_presure = blood_presure
        self.family_history = family_history
        self.low_WHR = low_WHR
        self.is_male = is_male
        self.is_diabetic = is_diabetic
        self.is_smoker = is_smoker
        self.ten_year_cardi_risk = ten_year_cardi_risk


def find_ninth_value_by_attributes(all_data_type, attributes_vals):
    age, blood_presure, family_history, low_WHR, is_male, is_diabetic, is_smoker, ten_year_cardi_risk = attributes_vals
    smpl = data_sample(age, blood_presure, family_history, low_WHR, is_male, is_diabetic, is_smoker,
                       ten_year_cardi_risk)
    all_attrubutes = list(all_data_type[0].__dict__.keys())
    all_attrubutes.remove('goal_val')
    for dt_tp in all_data_type:
        if not False in [smpl.__getattribute__(attrubute) == dt_tp.__getattribute__(attrubute) for attrubute in
                         all_attrubutes]:
            return dt_tp.goal_val


def get_excel_row_attributes(excel_row):
    blood_presure_cats = [100, 120, 140, 160]
    blood_presure = blood_presure_cats[int(excel_row['sbp_cat']) - 1]
    ten_year_cardi_risk = excel_row['tchcat']
    age = excel_row['age']
    family_history = excel_row['family_history'] == 1
    low_WHR = excel_row['whr'] == 0
    is_male = excel_row['sex'] == 1
    is_diabetic = excel_row['diabetes'] == 1
    is_smoker = excel_row['smoker'] == 1
    return (age, blood_presure, family_history, low_WHR, is_male, is_diabetic, is_smoker, ten_year_cardi_risk)


def find_ninth_value_of_excel_row(all_data_types, excel_row):
    return find_ninth_value_by_attributes(all_data_types, get_excel_row_attributes(excel_row))




####################################################################################
######################### copied from given voroudi.txt ############################
pre_gen_a = [
    [6, 8, 9, 10, 11, 8, 10, 11, 13, 14, 11, 14, 16, 17, 19, 15, 18, 20, 23, 24, 8, 10, 11, 13, 14, 11, 13, 15, 17, 18,
     15, 18, 20, 23, 24, 19, 23, 26, 29, 31, 8, 10, 11, 12, 14, 11, 13, 15, 16, 18, 15, 18, 20, 22, 24, 19, 23, 26, 28,
     31, 11, 13, 15, 16, 18, 14, 17, 19, 21, 23, 19, 23, 26, 28, 31, 25, 30, 33, 36, 39, 9, 11, 13, 14, 15, 12, 15, 17,
     18, 20, 17, 20, 23, 25, 27, 22, 26, 29, 32, 34, 12, 15, 17, 18, 20, 16, 19, 22, 24, 26, 22, 26, 29, 32, 34, 28, 33,
     37, 40, 43, 12, 14, 16, 18, 20, 16, 19, 21, 23, 25, 21, 25, 28, 31, 34, 27, 32, 36, 39, 42, 16, 19, 21, 23, 25, 20,
     24, 27, 30, 32, 27, 32, 36, 39, 42, 35, 41, 45, 49, 52],
    [5, 6, 6, 7, 8, 6, 7, 9, 9, 10, 9, 10, 12, 13, 14, 11, 14, 15, 17, 19, 6, 8, 9, 9, 10, 8, 10, 11, 12, 14, 11, 14,
     15, 17, 19, 15, 18, 20, 22, 24, 6, 7, 8, 9, 10, 8, 10, 11, 12, 13, 11, 13, 15, 17, 18, 14, 17, 20, 22, 24, 8, 10,
     11, 12, 13, 10, 13, 14, 16, 17, 14, 17, 20, 22, 24, 19, 23, 25, 28, 30, 7, 8, 9, 11, 12, 9, 11, 12, 14, 15, 12, 15,
     17, 19, 21, 16, 20, 22, 24, 27, 9, 11, 12, 14, 15, 12, 14, 16, 18, 20, 16, 20, 22, 24, 27, 21, 25, 28, 31, 34, 9,
     11, 12, 14, 15, 12, 14, 16, 18, 19, 16, 19, 22, 24, 26, 21, 25, 28, 31, 33, 12, 14, 16, 18, 19, 15, 18, 21, 23, 25,
     21, 25, 28, 31, 33, 27, 32, 36, 39, 42],
    [4, 4, 5, 5, 6, 5, 6, 7, 7, 8, 7, 8, 9, 10, 11, 9, 10, 12, 13, 14, 5, 6, 7, 7, 8, 6, 8, 9, 10, 10, 9, 10, 12, 13,
     14, 11, 14, 16, 17, 19, 5, 6, 6, 7, 8, 6, 7, 8, 9, 10, 8, 10, 12, 13, 14, 11, 13, 15, 17, 18, 6, 7, 8, 9, 10, 8,
     10, 11, 12, 13, 11, 13, 15, 17, 18, 15, 18, 20, 22, 24, 5, 6, 7, 8, 9, 7, 8, 10, 11, 12, 10, 12, 13, 15, 16, 13,
     15, 17, 19, 21, 7, 8, 10, 11, 12, 9, 11, 13, 14, 15, 13, 15, 17, 19, 21, 16, 20, 22, 25, 27, 7, 8, 9, 10, 11, 9,
     11, 12, 14, 15, 12, 15, 17, 19, 20, 16, 19, 22, 24, 26, 9, 11, 12, 14, 15, 12, 14, 16, 18, 19, 16, 19, 22, 24, 26,
     21, 25, 28, 31, 33],
    [2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 6, 7, 8, 9, 9, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 6, 7, 8, 9, 9, 7, 9, 10,
     11, 12, 3, 4, 4, 5, 5, 4, 5, 5, 6, 7, 5, 7, 8, 8, 9, 7, 9, 10, 11, 12, 4, 5, 5, 6, 7, 5, 6, 7, 8, 9, 7, 9, 10, 11,
     12, 9, 12, 13, 15, 16, 3, 4, 5, 5, 6, 4, 5, 6, 7, 8, 6, 8, 9, 10, 10, 8, 10, 11, 13, 14, 4, 5, 6, 7, 8, 6, 7, 8, 9,
     10, 8, 10, 11, 13, 14, 11, 13, 15, 16, 18, 4, 5, 6, 7, 7, 6, 7, 8, 9, 10, 8, 10, 11, 12, 13, 11, 13, 15, 16, 18, 6,
     7, 8, 9, 10, 8, 9, 11, 12, 13, 11, 13, 15, 16, 18, 14, 17, 19, 21, 23],
    [5, 6, 7, 7, 8, 6, 8, 9, 10, 10, 9, 10, 12, 13, 14, 11, 14, 16, 17, 19, 6, 8, 9, 10, 10, 8, 10, 11, 13, 14, 11, 14,
     16, 17, 19, 15, 18, 20, 22, 24, 6, 7, 8, 9, 10, 8, 10, 11, 12, 13, 11, 13, 15, 17, 18, 15, 18, 20, 22, 24, 8, 10,
     11, 12, 13, 11, 13, 15, 16, 18, 15, 18, 20, 22, 24, 19, 23, 26, 28, 31, 7, 8, 10, 11, 12, 9, 11, 13, 14, 15, 13,
     15, 17, 19, 21, 16, 20, 22, 25, 27, 9, 11, 13, 14, 15, 12, 15, 16, 18, 20, 16, 20, 22, 25, 27, 21, 26, 29, 31, 34,
     9, 11, 12, 14, 15, 12, 14, 16, 18, 19, 16, 19, 22, 24, 26, 21, 25, 28, 31, 33, 12, 14, 16, 18, 19, 15, 19, 21, 23,
     25, 21, 25, 28, 31, 33, 27, 32, 36, 39, 42],
    [3, 4, 5, 5, 6, 5, 6, 6, 7, 8, 6, 8, 9, 10, 11, 8, 10, 12, 13, 14, 5, 6, 6, 7, 8, 6, 7, 8, 9, 10, 8, 10, 12, 13, 14,
     11, 14, 15, 17, 18, 4, 5, 6, 7, 8, 6, 7, 8, 9, 10, 8, 10, 11, 13, 14, 11, 13, 15, 17, 18, 6, 7, 8, 9, 10, 8, 10,
     11, 12, 13, 11, 13, 15, 17, 18, 14, 17, 20, 22, 23, 5, 6, 7, 8, 9, 7, 8, 9, 10, 11, 9, 11, 13, 14, 16, 12, 15, 17,
     19, 20, 7, 8, 9, 10, 11, 9, 11, 12, 14, 15, 12, 15, 17, 19, 20, 16, 19, 22, 24, 26, 7, 8, 9, 10, 11, 9, 11, 12, 13,
     15, 12, 15, 17, 18, 20, 16, 19, 22, 24, 26, 9, 11, 12, 13, 15, 12, 14, 16, 18, 19, 16, 19, 22, 24, 26, 21, 25, 28,
     30, 33],
    [3, 3, 4, 4, 4, 3, 4, 5, 5, 6, 5, 6, 7, 8, 8, 6, 8, 9, 10, 11, 3, 4, 5, 5, 6, 5, 6, 6, 7, 8, 6, 8, 9, 10, 11, 9, 10,
     12, 13, 14, 3, 4, 5, 5, 6, 5, 6, 6, 7, 8, 6, 8, 9, 10, 11, 8, 10, 12, 13, 14, 5, 6, 6, 7, 8, 6, 7, 8, 9, 10, 8, 10,
     12, 13, 14, 11, 13, 15, 17, 18, 4, 5, 5, 6, 7, 5, 6, 7, 8, 9, 7, 9, 10, 11, 12, 9, 12, 13, 14, 16, 5, 6, 7, 8, 9,
     7, 8, 9, 11, 12, 9, 12, 13, 14, 16, 12, 15, 17, 19, 21, 5, 6, 7, 8, 9, 7, 8, 9, 10, 11, 9, 11, 13, 14, 16, 12, 15,
     17, 19, 20, 7, 8, 9, 10, 11, 9, 11, 12, 14, 15, 12, 15, 17, 19, 20, 16, 19, 22, 24, 26],
    [2, 2, 2, 3, 3, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 5, 7, 8,
     8, 9, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 5, 7, 7, 8, 9, 3, 4, 4, 5, 5, 4, 5, 5, 6, 7, 5, 7, 7, 8, 9, 7,
     9, 10, 11, 12, 2, 3, 3, 4, 4, 3, 4, 5, 5, 6, 5, 6, 6, 7, 8, 6, 7, 8, 9, 10, 3, 4, 5, 5, 6, 4, 5, 6, 7, 7, 6, 7, 8,
     9, 10, 8, 10, 11, 12, 14, 3, 4, 5, 5, 6, 4, 5, 6, 7, 7, 6, 7, 8, 9, 10, 8, 10, 11, 12, 13, 4, 5, 6, 7, 7, 6, 7, 8,
     9, 10, 8, 10, 11, 12, 13, 10, 13, 14, 16, 17],
    [3, 4, 5, 5, 6, 4, 5, 6, 7, 7, 6, 7, 8, 9, 10, 8, 10, 11, 12, 13, 4, 5, 6, 7, 7, 6, 7, 8, 9, 10, 8, 10, 11, 12, 13,
     10, 13, 14, 16, 17, 4, 5, 6, 7, 7, 6, 7, 8, 9, 9, 8, 9, 11, 12, 13, 10, 12, 14, 16, 17, 6, 7, 8, 9, 9, 7, 9, 10,
     11, 12, 10, 12, 14, 16, 17, 13, 16, 18, 20, 22, 5, 6, 7, 7, 8, 6, 8, 9, 10, 11, 9, 11, 12, 14, 15, 12, 14, 16, 18,
     19, 6, 8, 9, 10, 11, 8, 10, 12, 13, 14, 12, 14, 16, 18, 19, 15, 18, 21, 23, 25, 6, 8, 9, 10, 11, 8, 10, 11, 13, 14,
     11, 14, 16, 17, 19, 15, 18, 20, 22, 24, 8, 10, 11, 13, 14, 11, 13, 15, 17, 18, 15, 18, 20, 22, 24, 19, 23, 26, 29,
     31],
    [2, 3, 3, 4, 4, 3, 4, 4, 5, 5, 4, 5, 6, 7, 8, 6, 7, 8, 9, 10, 3, 4, 4, 5, 5, 4, 5, 6, 7, 7, 6, 7, 8, 9, 10, 8, 9,
     11, 12, 13, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 6, 7, 8, 9, 10, 8, 9, 11, 12, 13, 4, 5, 6, 6, 7, 5, 7, 8, 8, 9, 8, 9, 11,
     12, 13, 10, 12, 14, 15, 17, 4, 4, 5, 6, 6, 5, 6, 7, 7, 8, 7, 8, 9, 10, 11, 9, 11, 12, 13, 14, 5, 6, 7, 7, 8, 6, 8,
     9, 10, 11, 9, 11, 12, 13, 15, 11, 14, 16, 17, 19, 5, 6, 6, 7, 8, 6, 7, 8, 9, 10, 8, 10, 12, 13, 14, 11, 14, 15, 17,
     19, 6, 7, 8, 9, 10, 8, 10, 11, 12, 14, 11, 14, 15, 17, 19, 15, 18, 20, 22, 24],
    [2, 2, 3, 3, 3, 2, 3, 3, 4, 4, 3, 4, 5, 5, 6, 4, 5, 6, 7, 8, 2, 3, 3, 4, 4, 3, 4, 4, 5, 5, 4, 5, 6, 7, 8, 6, 7, 8,
     9, 10, 2, 3, 3, 4, 4, 3, 4, 4, 5, 5, 4, 5, 6, 7, 7, 6, 7, 8, 9, 10, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 6, 7, 8, 9, 10,
     8, 9, 11, 12, 13, 3, 3, 4, 4, 5, 4, 4, 5, 6, 6, 5, 6, 7, 8, 8, 7, 8, 9, 10, 11, 4, 4, 5, 6, 6, 5, 6, 7, 7, 8, 7, 8,
     9, 10, 11, 9, 11, 12, 13, 15, 3, 4, 5, 5, 6, 5, 6, 6, 7, 8, 6, 8, 9, 10, 11, 9, 10, 12, 13, 14, 5, 6, 6, 7, 8, 6,
     8, 9, 10, 10, 9, 10, 12, 13, 14, 11, 14, 15, 17, 19],
    [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 4, 3, 3, 4, 4, 5, 2, 2, 2, 2, 3, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 4, 5, 5,
     6, 6, 1, 2, 2, 2, 3, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 4, 5, 5, 6, 6, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 4, 5, 5, 6, 6, 5,
     6, 7, 8, 8, 2, 2, 2, 3, 3, 2, 3, 3, 4, 4, 3, 4, 4, 5, 5, 4, 5, 6, 7, 7, 2, 3, 3, 4, 4, 3, 4, 4, 5, 5, 4, 5, 6, 7,
     7, 6, 7, 8, 9, 10, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 6, 7, 8, 9, 9, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 6, 7,
     8, 9, 9, 7, 9, 10, 11, 12],
    [2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 5, 7, 8, 9, 9, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 6, 7, 8, 9, 9, 7, 9, 10,
     11, 12, 3, 4, 4, 5, 5, 4, 5, 5, 6, 7, 5, 7, 8, 8, 9, 7, 9, 10, 11, 12, 4, 5, 5, 6, 7, 5, 6, 7, 8, 9, 7, 9, 10, 11,
     12, 9, 11, 13, 14, 16, 3, 4, 5, 5, 6, 4, 5, 6, 7, 7, 6, 8, 9, 9, 10, 8, 10, 11, 12, 14, 4, 5, 6, 7, 7, 6, 7, 8, 9,
     10, 8, 10, 11, 12, 14, 11, 13, 15, 16, 18, 4, 5, 6, 7, 7, 6, 7, 8, 9, 10, 8, 10, 11, 12, 13, 10, 13, 14, 16, 17, 6,
     7, 8, 9, 10, 8, 9, 10, 12, 13, 10, 13, 14, 16, 17, 14, 17, 19, 21, 23],
    [2, 2, 2, 3, 3, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 5, 7, 8,
     8, 9, 2, 3, 3, 3, 4, 3, 3, 4, 4, 5, 4, 5, 6, 6, 7, 5, 6, 7, 8, 9, 3, 3, 4, 4, 5, 4, 5, 5, 6, 6, 5, 6, 7, 8, 9, 7,
     9, 10, 11, 12, 2, 3, 3, 4, 4, 3, 4, 5, 5, 6, 5, 6, 6, 7, 8, 6, 7, 8, 9, 10, 3, 4, 5, 5, 6, 4, 5, 6, 7, 7, 6, 7, 8,
     9, 10, 8, 10, 11, 12, 13, 3, 4, 4, 5, 5, 4, 5, 6, 7, 7, 6, 7, 8, 9, 10, 8, 10, 11, 12, 13, 4, 5, 6, 7, 7, 6, 7, 8,
     9, 10, 8, 10, 11, 12, 13, 10, 13, 14, 16, 17],
    [1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 3, 3, 4, 4, 3, 4, 4, 5, 5, 2, 2, 2, 3, 3, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6,
     6, 7, 2, 2, 2, 3, 3, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 2, 3, 3, 3, 4, 3, 4, 4, 4, 5, 4, 5, 6, 6, 7, 5,
     7, 7, 8, 9, 2, 2, 3, 3, 3, 2, 3, 3, 4, 4, 3, 4, 5, 5, 6, 5, 6, 6, 7, 8, 2, 3, 3, 4, 4, 3, 4, 5, 5, 6, 5, 6, 6, 7,
     8, 6, 7, 8, 9, 10, 2, 3, 3, 4, 4, 3, 4, 4, 5, 5, 4, 5, 6, 7, 8, 6, 7, 8, 9, 10, 3, 4, 4, 5, 5, 4, 5, 6, 7, 7, 6, 7,
     8, 9, 10, 8, 10, 11, 12, 13],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 3, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4,
     4, 4, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 3,
     4, 5, 5, 6, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 2, 2, 2, 2, 3, 2, 3, 3, 3, 4, 3, 4, 4, 5,
     5, 4, 5, 5, 6, 7, 2, 2, 2, 2, 3, 2, 3, 3, 3, 4, 3, 4, 4, 4, 5, 4, 5, 5, 6, 7, 2, 3, 3, 3, 4, 3, 3, 4, 4, 5, 4, 5,
     5, 6, 7, 5, 6, 7, 8, 9],
    [2, 2, 2, 2, 3, 2, 3, 3, 3, 4, 3, 4, 4, 4, 5, 4, 5, 5, 6, 7, 2, 3, 3, 3, 4, 3, 3, 4, 4, 5, 4, 5, 5, 6, 7, 5, 6, 7,
     8, 9, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 4, 5, 5, 6, 6, 5, 6, 7, 8, 8, 3, 3, 4, 4, 5, 4, 4, 5, 6, 6, 5, 6, 7, 8, 8, 7,
     8, 9, 10, 11, 2, 3, 3, 4, 4, 3, 4, 4, 5, 5, 4, 5, 6, 7, 7, 6, 7, 8, 9, 10, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 6, 7, 8,
     9, 10, 7, 9, 10, 11, 13, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 6, 7, 8, 9, 9, 7, 9, 10, 11, 12, 4, 5, 6, 6, 7, 5, 6, 7, 8,
     9, 7, 9, 10, 11, 12, 10, 12, 13, 15, 16],
    [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 4, 3, 3, 4, 4, 5, 2, 2, 2, 2, 3, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 4, 5, 5,
     6, 6, 1, 2, 2, 2, 3, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 4, 4, 5, 6, 6, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 6, 5,
     6, 7, 8, 8, 2, 2, 2, 3, 3, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 2, 3, 3, 4, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6,
     7, 6, 7, 8, 9, 9, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 5, 7, 8, 8, 9, 3, 4, 4, 5, 5, 4, 5, 5, 6, 7, 5, 7,
     8, 8, 9, 7, 9, 10, 11, 12],
    [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 4, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 4, 3, 3, 4,
     4, 5, 1, 1, 2, 2, 2, 1, 2, 2, 2, 3, 2, 3, 3, 3, 4, 3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 4,
     5, 5, 6, 6, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 3, 3, 4, 4, 3, 4, 4, 5, 5, 2, 2, 2, 3, 3, 2, 3, 3, 4, 4, 3, 4, 4, 5,
     5, 4, 5, 6, 7, 7, 2, 2, 2, 3, 3, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5, 6, 6, 7, 2, 3, 3, 3, 4, 3, 4, 4, 5, 5, 4, 5,
     6, 6, 7, 5, 7, 8, 8, 9],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 3,
     3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2,
     3, 3, 4, 4, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 3, 3, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3,
     3, 3, 3, 4, 4, 5, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
     4, 4, 5, 4, 4, 5, 5, 6]]


#################################
#################################
#################################
DATA = pd.read_excel('ParsDataSet7.xlsx', names=["IHHPCode", "sex", "whr", "smoker", "family_history", "diabetes",
                                                 "age",
                                                 "cholesterol", "blood_pressure", "dbp", "hdl", "ldl", "tg", "htn",
                                                 "sbp_cat", "sbp1", "sbp2", "sbp3", "sbp4", "tchcat", "tch1",
                                                 "tch2",
                                                 "tch3", "tch4",
                                                 "tch5", "FollowDu5th", "label"], header=0)


def aaa(pre_gen_a,datafram):
    DATA=datafram
    pre_gen_a=pre_gen_a
    all_data = []
    for row in pre_gen_a:
        all_data = all_data + row

    all_data_types = []
    ad_counter = 0
    for min_age in [75, 65, 55, 45, 35]:
        for blood_presure_lower_bound in [160, 140, 120, 0]:
            for family_history, low_WHR in [(True, False), (False, False), (True, True), (False, True)]:
                for is_male in [False, True]:
                    for is_diabetic in [False, True]:
                        for is_smoker in [False, True]:
                            for ten_year_cardi_risk in [1, 2, 3, 4, 5]:
                                new_data_type = data_type(min_age, blood_presure_lower_bound, family_history, low_WHR,
                                                          is_male, is_diabetic, is_smoker, ten_year_cardi_risk)
                                new_data_type.set_goal_val(all_data[ad_counter])
                                all_data_types.append(new_data_type)
                                ad_counter += 1

    DATA = pd.read_excel('ParsDataSet7.xlsx', names=["IHHPCode", "sex", "whr", "smoker", "family_history", "diabetes",
                                                     "age",
                                                     "cholesterol", "blood_pressure", "dbp", "hdl", "ldl", "tg", "htn",
                                                     "sbp_cat", "sbp1", "sbp2", "sbp3", "sbp4", "tchcat", "tch1",
                                                     "tch2",
                                                     "tch3", "tch4",
                                                     "tch5", "FollowDu5th", "label"], header=0)

    pars_res = []
    labels = []
    for k in range(len(DATA)):
        prediction_input = {
            key: DATA.iloc[k][key]
            for key in ["sex", "whr", "smoker", "family_history", "diabetes",
                        "age", "tchcat", "sbp_cat"]}
        val = find_ninth_value_of_excel_row(all_data_types, prediction_input)
        pars_res.append(val)

    fpr, tpr, _ = roc_curve(DATA['label'], pars_res)
    roc_auc = auc(fpr, tpr)
    print(f'pre gen roc auc: {roc_auc}')
