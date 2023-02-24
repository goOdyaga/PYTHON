def read_dataset(dataset_path):
  file=open(dataset_path, 'r', encoding="utf-8")
  dictioanry={}
  list_names=[]
  list_values=[]
  for i in file:
    m = i.strip()
    a=list(m.split(","))

    # print(a)
    if a[1] not in list_names:
      list_names.append(a[1])
    list_values.append(a)
  list_values.remove(list_values[0])
  list_names.remove(list_names[0])
  counter=0
  list_total=[]
  # print(len(list_values))
  for i in list_values:
    # print(list_names[counter])
    # print(list_names[counter])
    if list_names[counter] == i[1]:
      list_total.append(i)
    else:
      # print("a")
      # print(list_total)
      dictioanry[str(list_names[counter])]=tuple(list_total)
      list_total.clear()
      list_total.append(i)
      counter+=1
    # dictioanry.clear()
  dictioanry[str(list_names[counter])]=tuple(list_total)
  # print(dictioanry["Kevin Phillips"][12])
  return dictioanry
  # print(dictioanry)


  # print(dictioanry)


    # else:
    #     list_values.append(a)
    # for i in range(0,len(list_names)):
    #   dictioanry[list_names[i]]=list_values[i]
  # print(list_names)
  ##########################
  ### START OF YOUR CODE ###
  ##########################


  ##########################
  ###  END OF YOUR CODE  ###
  ##########################
read_dataset("dataset.txt")