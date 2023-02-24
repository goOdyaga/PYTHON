
def find_number_of_goals_per_min(dict_of_dataset):
  minute=0
  goal=0
  minutes_played={}
  list_values=[]
  minutes=[]
  goals=[]
  res=[]
  for i in dict_of_dataset:
    list_values.append(dict_of_dataset[i])
  for i in list_values:
    minute=0
    goal=0
    minutes.clear()
    goals.clear()
    res.clear()
    for j in i:
      minutes.append(int(j[4])-minute)
      goals.append(int(j[6])-goal)
      minute=int(j[4])
      goal=int(j[6])
    res.append(minutes)
    res.append(goals)
    empty_list=[]
    for h in res:
      empty_list2=[]
      for k in h:
        empty_list2.append(k)
      empty_list.append(empty_list2)
    minutes_played[i[0][1]]=empty_list[:]
  return minutes_played