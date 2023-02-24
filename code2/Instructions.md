# PS3: Recursive Maze Solver

## Deadline: 18 December 2022 (11:59 PM)

In this assignment, we will implement a maze solving game. We will start simple in Part 1, and at each part the game gets a little more complicated. Therefore, it is suggested to implement the parts in order. 

**Note:** You must solve all parts using `recursion`. Non-recursive solutions will not be accepted. Avoid nested functions that break the recursive logic. 

---

### Part 1: Moving Forward in a 1D Maze (25 pts)

Consider a 1-dimensional grid of length N, represented as a list. Each player starts at the left-most position of this grid, and wants to reach the right-most position in the grid.  

At each grid cell, a number is given that represents the player's next step size. You can assume that the step size is always a **non-negative number**. In this part, the player **can only move right** according to the given step size.

Implement the `part1` function that takes the maze as input, and returns the trajectory of the player (as indices) if the target location can be reached successfully. If not, you should return an empty list. 

For example, consider this grid:

| 1 | 2 | 2 | 1 | 3 |
|---|---|---|---|---|

- The player always starts at the 1st position (leftmost position), the next step size is 1.
- The player moves to the 2nd position, next step size becomes 2.
- The player moves to the 4th position, next step size becomes 1.
- The player moves to the 5th position, which is the target location (rightmost position).

The return value of your `part1` function should be: `[0, 1, 3, 4]` corresponding to the indices that were visited. 

Note that the target location must be visited to count the trajectory as successful. So, if the 4th position above had 2 in it, then the player would pass over the target location, and it would be unsuccessful. In that case, the return value of your `part1` function should be an empty list. 


---

### Part 2: Moving Forward & Backward in a 1D Maze (25 pts)

Consider the same setup as Part 1, but now the player **can move to the right or left** as long as it is between the boundaries of the maze. 
Notice that this introduces some stochasticity to the game. Since there might be multiple successful trajectories, we will keep a list of all possible trajectories (i.e. list of lists). In your `part2` function, when you find a valid trajectory, append it to the `all_trajectories` parameter. Do not return anything. 

**Note:** To avoid circular loops, do not visit a grid cell you've already visited. 

For example, consider the same grid:

| 1 | 2 | 2 | 1 | 3 |
|---|---|---|---|---|

- Starting at the 1st position, the next step size is 1, since there is no cells to the left, the player can only go to the right by 1.
- The player moves to the 2nd position, next step size becomes 2, can only go right because 2 to the left is beyond the boundaries.
- The player moves to the 4th position, next step size becomes 1, the player can move to the left or right by 1.
  - If right is chosen, the player moves to the 5th position, which is the target location. Trajectory is completed and successful.
  - If left is chosen, the player moves to the 3rd position, next step size becomes 2.
    - The player can not move to the left by 2, because it is already visited.
    - The player moves to the right by 2, arriving at the target location. Trajectory is completed and successful.

In this case, `all_trajectories` should become
`[[0, 1, 3, 4], [0, 1, 3, 2, 4]]`.

--- 

### Part 3: Moving Forward & Downward in a 2D Maze (25 pts)

For the remaining parts, consider a 2-dimensional `M x N` grid as your maze. The maze will be given to you as a list of lists, where each sublist corresponds to one row of the maze. A player always starts at the top-left cell, and wants to reach the bottom-right cell.

For example, here is a sample maze:
|  1  |  1  |  1  |
|:---:|:---:|:---:|
|**2**|**4**|**3**|

Here is how this maze will be given as input to your function:  
```
[[1, 1, 1],
 [2, 4, 3]]
```

In this part, the player **can only move right or down.** Notice that this is also stochastic due to multiple valid actions, so there may be multiple successful trajectories. As before, in your `part3` function, when you find a valid trajectory, append it to the `all_trajectories` parameter. Do not return anything. 

In your trajectory lists, you should represent maze indices as tuples `(row,column)`. For example, the top left corner is `(0,0)`. In the sample maze given above, the index that contains integer 4 is `(1,1)`.

Sample execution for the maze given above is as follows:

- Starting at top-left cell, the player can move to the right or down by 1.
  - If right is chosen, next step size becomes 1. The player can move right or down by 1.
    - If right is chosen, next step size becomes 1. The player can only move down by 1, since right is out of boundaries. The player moves down by 1 and reaches the bottom-right cell. Trajectory is completed and successful. 
    - If down is chosen, next step size becomes 4. The player can not move to anywhere because all actions would result in a location out of boundaries. Trajectory is completed and unsuccessful.
  - If down is chosen, next step size becomes 2. The player can only move to the right by 2, since down is out of boundaries. The player moves right by 2 and reaches the bottom-right cell. Trajectory is completed and successful.

At the end, `all_trajectories` should become
`[[(0,0), (0,1), (0,2), (1,2)],  [(0,0), (1,0), (1,2)]]`.

--- 

### Part 4: Moving Forward, Backward, Downward & Upward in a 2D Maze (25 pts)

Consider the same setup as Part 3, but now the player **can move right, left, up or down** as long as it is within the boundaries of the maze. Since there might be multiple successful trajectories, in your `part4` function, when you find a valid trajectory append it to the `all_trajectories` parameter. Do not return anything. 

**Note:** As in Part 2, to avoid circular loops, do not visit a grid cell you've already visited. 