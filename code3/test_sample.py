from q1 import read_dataset
from q2 import find_number_of_goals_per_min
from q3 import find_number_penaltyG_per_age
from q4 import find_ratio_goal_and_min_by_date


######################
#### TESTS FOR Q1 ####
######################

def test_q1_1():
    correct = False
    first_row_of_messi = ['1', 'Lionel Messi', '2004-10-16', '17.314', '7', '1', '0', '0', '691', '609', '0.92', '0.81']
    if first_row_of_messi == read_dataset("dataset.txt")["Lionel Messi"][0]:
        correct = True

    assert correct, print('Your function returns something else')


def test_q1_2():
    correct = False
    tenth_row_of_ronaldo = ['2', 'Cristiano Ronaldo', '2004-11-23', '19.797', '3706', '60', '6', '6', '695', '566', '0.83', '0.67']
    if tenth_row_of_ronaldo == read_dataset("dataset.txt")["Cristiano Ronaldo"][10]:
        correct = True

    assert correct, print('Your function returns something else')


def test_q1_3():
    correct = False
    second_row_of_ibra = ['5', 'Zlatan Ibrahimović', '2002-11-27', '21.15', '773', '12', '6', '6', '400', '331', '0.68', '0.56']
    if second_row_of_ibra == read_dataset("dataset.txt")["Zlatan Ibrahimović"][2]:
        correct = True

    assert correct, print('Your function returns something else')

def test_q1_4():
    correct = False
    twelfth_row_of_ibra = ['20', 'Kylian Mbappé', '2017-11-04', '18.875', '4291', '72', '33', '33', '209', '192', '0.87', '0.8']

    if twelfth_row_of_ibra == read_dataset("dataset.txt")["Kylian Mbappé"][12]:
        correct = True

    assert correct, print('Your function returns something else')



######################
#### TESTS FOR Q2 ####
######################

def test_q2_1():
    correct = False
    dict_of_dataset = read_dataset("dataset.txt")
    played_minutes_by_messi = [7, 189, 158, 323]
    scored_goals_by_messi = [0, 0, 1, 1]
    if played_minutes_by_messi == find_number_of_goals_per_min(dict_of_dataset)["Lionel Messi"][0][:4] and scored_goals_by_messi == find_number_of_goals_per_min(dict_of_dataset)["Lionel Messi"][1][:4]:
        correct = True

    assert correct, print('Your function returns something else')

def test_q2_2():
    correct = False
    dict_of_dataset = read_dataset("dataset.txt")
    played_minutes_by_ronaldo = [80, 433, 516, 539]
    scored_goals_by_ronaldo = [3, 6, 5, 8]
    if played_minutes_by_ronaldo == find_number_of_goals_per_min(dict_of_dataset)["Ronaldo"][0][:4] and scored_goals_by_ronaldo == find_number_of_goals_per_min(dict_of_dataset)["Ronaldo"][1][:4] :
        correct = True

    assert correct, print('Your function returns something else')

def test_q2_3():
    correct = False
    dict_of_dataset = read_dataset("dataset.txt")
    played_minutes_by_salah = [16, 335, 339, 528]
    scored_goals_by_salah = [0, 0, 0, 3]
    if played_minutes_by_salah == find_number_of_goals_per_min(dict_of_dataset)["Mohamed Salah"][0][:4] and scored_goals_by_salah == find_number_of_goals_per_min(dict_of_dataset)["Mohamed Salah"][1][:4] :
        correct = True

    assert correct, print('Your function returns something else')

def test_q2_4():
    correct = False
    dict_of_dataset = read_dataset("dataset.txt")
    played_minutes_by_suarez = [17, 357, 510, 519]
    scored_goals_by_suarez = [1, 1, 4, 5]
    if played_minutes_by_suarez == find_number_of_goals_per_min(dict_of_dataset)["Luis Suárez"][0][:4] and scored_goals_by_suarez == find_number_of_goals_per_min(dict_of_dataset)["Luis Suárez"][1][:4] :
        correct = True

    assert correct, print('Your function returns something else')

######################
#### TESTS FOR Q3 ####
######################
def test_q3_1():
    correct = False
    dict_of_dataset = read_dataset("dataset.txt")
    age_of_baltazar = [26, 28, 29, 30]
    scored_penalty_goals_by_baltazar = [1, 1, 7, 4]
    if age_of_baltazar == find_number_penaltyG_per_age(dict_of_dataset)["Baltazar"][0][:4] and scored_penalty_goals_by_baltazar == find_number_penaltyG_per_age(dict_of_dataset)["Baltazar"][1][:4] :
        correct = True

    assert correct, print('Your function returns something else')

def test_q3_2():
    correct = False
    dict_of_dataset = read_dataset("dataset.txt")
    age_of_higuain = [19, 20, 21, 22]
    scored_penalty_goals_by_higuain = [0, 3, 1, 0]
    if age_of_higuain == find_number_penaltyG_per_age(dict_of_dataset)["Gonzalo Higuaín"][0][:4] and scored_penalty_goals_by_higuain == find_number_penaltyG_per_age(dict_of_dataset)["Gonzalo Higuaín"][1][:4] :
        correct = True

    assert correct, print('Your function returns something else')

def test_q3_3():
    correct = False
    dict_of_dataset = read_dataset("dataset.txt")
    age_of_cavani = [20, 21, 22, 23]
    scored_penalty_goals_by_cavani = [0, 0, 2, 3]
    if age_of_cavani == find_number_penaltyG_per_age(dict_of_dataset)["Edinson Cavani"][0][:4] and scored_penalty_goals_by_cavani == find_number_penaltyG_per_age(dict_of_dataset)["Edinson Cavani"][1][:4] :
        correct = True

    assert correct, print('Your function returns something else')

######################
#### TESTS FOR Q4 ####
######################

def test_q4_1():
    correct = False
    dict_of_dataset = read_dataset("dataset.txt")
    months_played_by_messi = [1, 2, 3, 4]
    ratio_by_messi = [0.0098, 0.0083, 0.0092, 0.0145]
    if months_played_by_messi == find_ratio_goal_and_min_by_date(dict_of_dataset)["Lionel Messi"][0][:4] and ratio_by_messi == find_ratio_goal_and_min_by_date(dict_of_dataset)["Lionel Messi"][1][:4] :
        correct = True

    assert correct, print('Your function returns something else')

def test_q4_2():
    correct = False
    dict_of_dataset = read_dataset("dataset.txt")
    months_played_by_mbappe = [1, 2, 3, 5]
    ratio_by_mbappe = [0.0086, 0.0025, 0.0086, 0.0044]
    if months_played_by_mbappe == find_ratio_goal_and_min_by_date(dict_of_dataset)["Kylian Mbappé"][0][:4] and ratio_by_mbappe == find_ratio_goal_and_min_by_date(dict_of_dataset)["Kylian Mbappé"][1][:4] :
        correct = True

    assert correct, print('Your function returns something else')

def test_q4_3():
    correct = False
    dict_of_dataset = read_dataset("dataset.txt")
    ratio_of_dataset = find_ratio_goal_and_min_by_date(dict_of_dataset)

    if len(ratio_of_dataset) == 8:
        correct = True

    assert correct, print('Your function returns something else')
test_q1_1()
test_q1_2()
test_q1_3()
test_q1_4()
test_q2_1()
test_q2_2()
test_q2_3()
test_q2_4()
test_q3_1()
test_q3_2()
test_q3_3()
test_q4_1()
test_q4_2()
test_q4_3()
# test_q3_4()