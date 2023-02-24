# PS4
## Deadline: 08 January 2023 23:59

In this assignment, your will design a Football Player Analyzer using "worldfootball.net" data provided as a .txt file.

Step by step, we will develop the following functionalities :
1. Reading the football data,
2. Finding the number of goals by minutes played,
3. Finding the number of penalty goals by age,
4. Finding the Ratio Between Goal and Played Minutes by Specific Date

### Part I: Reading the football data (20 pts)

The data for the PS4 is provided in the "dataset.txt" file. It includes the following information in each line:

* **ID:** ID of the football player
* **Name:** Name of the football player
* **Date:** Date
* **Age** Detailed age of the football player
* **Mins** Minutes played by a football player on that date
* **G** Goals scored by a football player on that date
* **NPG** Non-penalty goals scored by a football player on that date

Our goal is to read, extract, and store this data in a data structure for further processing. We will be using this data to report some statistics for football players.

You need to create a dictionary to store these rows for every football player:
1. Key should be the name of the football player,
2. Value should be tuples that contains list for every rows from the dataset

Expected Output :
> {Lionel Messi : (['1', 'Lionel Messi', '2004-10-16', '17.314', '7', '1', '0', '0', '691', '609', '0.92', '0.81\n'], ['1', 'Lionel Messi', '2004-12-11', '17.467', '196', '6', '0', '0', '691', '609', '0.92', '0.81\n'], ...)
...}

**Warning**
When you read the txt file don't forget to add encoding="utf-8" property. Because some football players' names cannot be read due to the unique characters on their names

For example:
Luis Suárez becomes Luis SuÃ¡rez
Zlatan Ibrahimović becomes Zlatan IbrahimoviÄ‡

You can provide the `encoding` as an argument as follows:
```
with open(dataset_path, 'r', encoding="utf-8") as file:
```

**Warning 2**
You should not read the file after this part. You should use the dictionary you obtained from part 1.


### Part II: Finding the number of goals by minutes played (20 pts)

In this part, you are going to compute the goals scored against the minutes played by every football player. Note that the goals and minutes columns are cumulative values (increasing by successive additions). 


| Date         |  Mins       |
| -----------  | ----------- |
| 16.10.2004   | 7           |
| 27.10.2004   | 98          |
| 11.12.2004   | 196         |

For example this football player 
1. played 7 minutes till 16.10.2004 
2. played 98-7 = 91 minutes till 27.10.2004
3. plated 196-98 = 98 minutes till 11.12.2004

That means you need to extract the goals scored for a specific age. 

You need to create an interval for the minutes played. For example:
```
minutes_played = [7, 91, 98, ...]
```

This `minutes_played` interval should be indexed with goals scored by football players. For example:
```
0 Minutes Played -> 0 Goals Scored
7 Minutes Played -> 3 Goals Scored
91 Minutes Played -> 10 Goals Scored
98 Minutes Played -> 12 Goals Scored
...
```


You need to create a dictionary to store these lists for every football player:
1. Key should be the name of the football player
2. Value should contain two list 
    * First list should be the `minutes_played` list
    * Second list should be the goals scored 

Remember first and second lists must be in sync.

Expected Output :
* {Lionel Messi : ([7, 189, 158, 323, ...], 
                 [0, 0, 1, 1, ...])
...}


### Part III: Finding the Number of Penalty Goals by Age (30 pts)

In this part, you will calculate the penalty goals scored by each football player at his age. Note that the goals column are cumulative values. That means you need to extract the goals scored for a specific age. As you can observe, penalty goals are not directly provided in the dataset. You have goals scored and non-penalty goals scored by football players. First, you need to find the penalty goals scored by every football player individually. 

You need to create an interval for the age. For example:
```
age = [17, 18, 19, 20, 21, 22, ...]
```
You can create this age interval by using the `min()` and `max()` functions.

Be careful about this interval. The age data in the dataset is not integer values. You should create an interval with integer values (ages). For example:

```
In Age 17.314 -> 0 Penalty Goals Scored
In Age 17.344 -> 1 Penalty Goals Scored
In Age 17.467 -> 0 Penalty Goals Scored
In Age 17.854 -> 0 Penalty Goals Scored

should be converted to:

In Age 17 -> 1 Penalty Goals Scored
...
```

This `minutes_played` interval should be indexed with penalty goals scored by a football player. For example:

```
In Age 17 -> 0 Penalty Goals Scored
In Age 18 -> 0 Penalty Goals Scored
In Age 19 -> 0 Penalty Goals Scored
In Age 20 -> 4 Penalty Goals Scored
In Age 20 -> 4 Penalty Goals Scored
In Age 21 -> 1 Penalty Goals Scored
...
```

You need to create a dictionary to store these lists for every football player:
1. Key should be the name of the football player,
2. Value should contain two list 
    * First list should be the age interval
    * Second list should be penalty goals scored at every age in the age interval

Remember first and second lists must be in sync.
Expected Output :
* {Lionel Messi : (['17', '18', '19', '20', '21','22', ...], 
                   [0, 0, 0, 4, 4, 1, ...]
...}


### Part IV: Finding the Ratio Between Goal and Played Minutes by Specific Date (30 pts)

In this part, you are going to find the ratio between goals scored and played minutes in **2018** months. You need to create an interval for the months. For example:

```
months = [1, 2, 3, 4, 5, 9, 10, 12]
```

The ratio of goals scored and played minutes should be calculated with respect to played minute played in that month. For example, in the first month, Messi played 482 minutes, and 5 goals were scored by Messi in those matches. Then the ratio would be 5/485.

You need to create a dictionary to store these ratio lists for every football player:
1. Key should be the name of the football player,
2. Value should contain two list 
    * First list should be the months
    * Second list should be ratio

Remember first and second lists must be in sync in terms of the month.


Expected Output :
* {Lionel Messi : (['01','02','03','04', ...], 
                   [0.0098, 0.0090, 0.0091, 0.0104, ...]
...}

