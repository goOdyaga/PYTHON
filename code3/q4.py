

def find_ratio_goal_and_min_by_date(dict_of_dataset):
  minute=0
  minute1=0
  res=[]
  new_list=[]
  list_values=[]
  list_ratio=[0]*12
  peanllty_goals={}
  list_months=[]
  goal=0
  goal1=0
  control =False
  for i in dict_of_dataset:
    list_values.append(dict_of_dataset[i])
  for i in list_values:
    control=False
    for j in i:
      minute1=int(j[4])-minute
      minute=int(j[4])
      goal1=int(j[6])-goal
      goal=int(j[6])
      year=int(list(j[2].split("-"))[0])
      if year==2018:
        control=True
        month=int(list(j[2].split("-"))[1])
        ratio=str(goal1/minute1)
        result=ratio
        if(goal1/minute1!=0):
          n = len(str(ratio).split(".")[1])
          x=[m for m in ratio]
          if(goal1/minute1)!=0:
            if 19!=n:
              for z in range(0,19-n):
                x.append(".")
            for s in range(0,15):
              x.pop()
          x.append("1")
          result="".join(str(xs) for xs in x)
        result=round(float(result), 4)
        list_ratio[month-1]=result
        list_months.append(month)
        new_list.append(result)
    a=len(list_ratio)
    res.append(list_months)
    res.append(new_list)
    empty_list=[]
    for h in res:
      empty_list2=[]
      for k in h:
        empty_list2.append(k)
      empty_list.append(empty_list2)
    if control:
      peanllty_goals[i[0][1]]=empty_list[:]
    list_months.clear()
    new_list.clear()
    res.clear()
  return peanllty_goals