

def find_number_penaltyG_per_age(dict_of_dataset):
  ages=[]
  goals=[]
  res=[]
  list_values=[]
  peanllty_goals={}

  for i in dict_of_dataset:
    list_values.append(dict_of_dataset[i])
  for i in list_values:
    age=int(float(i[0][3]))
    goal=0
    goal1=0
    goal2=0
    np1=0
    np=0
    ages.clear()
    goals.clear()
    res.clear()
    for j in i:
      if int(float(j[3]))!=age:
        ages.append(age)
        goals.append(goal2)
        age=int(float(j[3]))
        goal2=0
      goal1=int(j[6])-goal
      np1=int(j[7])-np
      goal2+=goal1-np1
      goal=int(j[6])
      np=int(j[7])
    res.append(ages)
    res.append(goals)
    empty_list=[]
    for h in res:
      empty_list2=[]
      for k in h:
        empty_list2.append(k)
      empty_list.append(empty_list2)
    peanllty_goals[i[0][1]]=empty_list[:]
  return peanllty_goals