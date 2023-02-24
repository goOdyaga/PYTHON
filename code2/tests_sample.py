"""
Do not modify this file unless instructed.
"""

from ps3 import part1, part2, part3, part4


def test_part1_1():
  maze = [1, 2, 2, 1, 3]
  assert part1(0, [], maze) == [0, 1, 3, 4]


def test_part1_2():
  maze = [1, 2, 2, 2, 3]
  assert part1(0, [], maze) == []


def test_part2_1():
  maze = [1, 2, 2, 1, 3]
  all_trajectories = []
  part2(0, [], maze, all_trajectories)
  assert all_trajectories == [[0, 1, 3, 4], [0, 1, 3, 2, 4]]


def test_part2_2():
  maze = [1, 2, 4, 1, 2, 1, 2, 1, 3]
  all_trajectories = []
  part2(0, [], maze, all_trajectories)
  assert all_trajectories == [[0, 1, 3, 4, 6, 8], [0, 1, 3, 4, 2, 6, 8],
                              [0, 1, 3, 2, 6, 8]]


def test_part3_1():
  maze = [[1, 1, 1], [2, 4, 3]]
  all_trajectories = []
  part3((0, 0), [], maze, all_trajectories)
  assert all_trajectories == [[(0, 0), (0, 1), (0, 2), (1, 2)],
                              [(0, 0), (1, 0), (1, 2)]]


def test_part3_2():
  maze = [[2, 2, 1], [1, 2, 2], [1, 1, 2]]
  all_trajectories = []
  part3((0, 0), [], maze, all_trajectories)
  assert all_trajectories == [[(0, 0), (2, 0), (2, 1), (2, 2)]]


def test_part4_1():
  maze = [[1, 1, 1], [2, 4, 3]]
  all_trajectories = []
  part4((0, 0), [], maze, all_trajectories)
  assert all_trajectories == [[(0, 0), (0, 1), (0, 2), (1, 2)],
                              [(0, 0), (1, 0), (1, 2)]]


def test_part4_2():
  maze = [[2, 2, 1], [1, 2, 2], [1, 1, 2]]
  all_trajectories = []
  part4((0, 0), [], maze, all_trajectories)
  assert all_trajectories == [[(0, 0), (0, 2), (0, 1), (2, 1), (2, 2)],
                              [(0, 0), (0, 2), (1, 2), (1, 0), (2, 0), (2, 1),
                               (2, 2)], [(0, 0), (2, 0), (2, 1), (2, 2)]]


if __name__ == '__main__':

  tests = [
    test_part1_1, test_part1_2, test_part2_1, test_part2_2, test_part3_1,
    test_part3_2, test_part4_1, test_part4_2
  ]

  print('Points:')
  for t in tests:
    try:
      t()
      print(str(t).split()[1], 1)
    except AssertionError:
      print(str(t).split()[1], 0)