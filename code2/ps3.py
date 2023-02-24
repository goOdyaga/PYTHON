"""
Write your solutions in place of pass statements.
Do not modify the function headers unless instructed.
Remove any additional lines outside the function definitions before commit&push.
"""


def part1(current_loc, current_path, maze) :
  current_path.append(current_loc)
  if (maze[current_loc]+current_loc>=len(maze)):
    return []
  elif (maze[current_loc]+current_loc==len(maze)-1):
    current_path.append(len(maze)-1)
    return current_path
  else:
    # current_path.append(current_loc)
    return part1(current_loc+maze[current_loc],current_path,maze)
  


def part2(current_loc, current_path, maze, all_trajectories):

  if(maze[current_loc]+current_loc<=len(maze) -1):
    current_path.append(current_loc)
    lise1=[]

    for i in current_path:
        lise1.append(i)

    part2(current_loc+maze[current_loc],current_path,maze,all_trajectories)

    lise1.pop()
    current_path=lise1

  if(maze[current_loc]+current_loc<=len(maze) -1 and current_loc-maze[current_loc]>0):

    if(current_loc-maze[current_loc]+maze[current_loc-maze[current_loc]]!=current_loc):
      current_path.append(current_loc)
      lise1=[]

      for i in current_path:
        lise1.append(i)

      part2(current_loc-maze[current_loc],current_path,maze,all_trajectories)
      lise1.pop()
      current_path=lise1
  

  elif(current_loc==len(maze) -1 ):
    current_path.append(current_loc)
    all_trajectories.append(current_path)
  

def part3(current_loc, current_path, maze, all_trajectories):
  if(current_loc[1]+maze[current_loc[0]][current_loc[1]]<len(maze[0])):
    current_path.append(current_loc)
    lise1=[]

    for i in current_path:
        lise1.append(i)
    part3(((current_loc[0],current_loc[1]+maze[current_loc[0]][current_loc[1]])),current_path,maze,all_trajectories)
    lise1.pop()
    current_path=lise1
  if(current_loc[0]+maze[current_loc[0]][current_loc[0]]<len(maze)):
    current_path.append(current_loc)
    lise1=[]

    for i in current_path:
        lise1.append(i)
    part3(((current_loc[0]+maze[current_loc[0]][current_loc[1]],current_loc[1])),current_path,maze,all_trajectories)
    lise1.pop()
    current_path=lise1
  elif(current_loc[0]==len(maze) -1 and current_loc[1]==len(maze[0]) -1 ):
    current_path.append(current_loc)
    all_trajectories.append(current_path)



def part4(current_loc, current_path, maze, all_trajectories):
  if(current_loc[1]+maze[current_loc[0]][current_loc[1]]<len(maze[0]) and (current_loc[0],current_loc[1]+maze[current_loc[0]][current_loc[1]])not in current_path):
    # if(current_loc[1]+maze[current_loc[0]][current_loc[1]]-maze[current_loc[0]][current_loc[1]+maze[current_loc[0]][current_loc[1]]]!=current_loc[1]):
    
      current_path.append(current_loc)
      lise1=[]

      for i in current_path:
          lise1.append(i)

      part4((current_loc[0],current_loc[1]+maze[current_loc[0]][current_loc[1]]),current_path,maze,all_trajectories)
      
      lise1.pop()
      current_path=lise1

  if(current_loc[1]-maze[current_loc[0]][current_loc[1]]>=0 and ((current_loc[0],current_loc[1]-maze[current_loc[0]][current_loc[1]]) not in current_path) ):
    # print((current_loc[0],current_loc[1]-maze[current_loc[0]][current_loc[1]]))
    if(current_loc[1]-maze[current_loc[0]][current_loc[1]]+maze[current_loc[0]][current_loc[1]-maze[current_loc[0]][current_loc[1]]]!=current_loc[1]):
      current_path.append(current_loc)
      lise1=[]

      for i in current_path:
          lise1.append(i)
      part4((current_loc[0],current_loc[1]-maze[current_loc[0]][current_loc[1]]),current_path,maze,all_trajectories)
      lise1.pop()
      current_path=lise1

  if(current_loc[0]-maze[current_loc[0]][current_loc[1]]>=0 and (current_loc[0]-maze[current_loc[0]][current_loc[1]],current_loc[1]) not in current_path):
    if(current_loc[0]-maze[current_loc[0]][current_loc[1]]+maze[current_loc[0]-maze[current_loc[0]][current_loc[1]]][current_loc[1]]!=current_loc[0]):
      current_path.append(current_loc)
      lise1=[]

      for i in current_path:
          lise1.append(i)
      part4(((current_loc[0]-maze[current_loc[0]][current_loc[1]],current_loc[1])),current_path,maze,all_trajectories)
      lise1.pop()
      current_path=lise1
  if(current_loc[0]+maze[current_loc[0]][current_loc[1]]<len(maze) and (current_loc[0]+maze[current_loc[0]][current_loc[1]],current_loc[1]) not in current_path):
    # print((current_loc[0]+maze[current_loc[0]][current_loc[1]],current_loc[1]))
    # if(current_loc[0]+maze[current_loc[0]][current_loc[1]]-maze[current_loc[0]+maze[current_loc[0]][current_loc[1]]][current_loc[1]]!=current_loc[0]):
      current_path.append(current_loc)
      lise1=[]

      for i in current_path:
          lise1.append(i)
      part4(((current_loc[0]+maze[current_loc[0]][current_loc[1]],current_loc[1])),current_path,maze,all_trajectories)
      lise1.pop()
      current_path=lise1
  elif(current_loc[0]==(len(maze) -1) and current_loc[1]==(len(maze[0]) -1 )):
    current_path.append(current_loc)
    all_trajectories.append(current_path)
# a=part1(0, [], maze = [1, 2, 2, 2, 3])
maze = [[2, 2, 1], [1, 2, 2], [1, 1, 2]]
all_trajectories = []
part4((0, 0), [], maze, all_trajectories)
print(all_trajectories)