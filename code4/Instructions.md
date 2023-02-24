# COMP100 - Fall 2022 - PS5
## OOP and Inheritance
### Deadline: 20.01.2023 

In this assignment, we will simulate a file system that allows us to store files inside directories. We will further create a dataset class that allows for more structured storage and organisation.

### Part 1: File Class
Your task is to design a `File` class in this part. Intializing an object instance of the `File` class would mean you have initialized a file such as an image or a txt file which have certain attributes. The `File` class should have the `__init__` and proper getter and setter methods for all the attributes described below. 


* `__init__(self, name, size)`: This method should initialize a `File` object with a string `name` and an int `size` (in bytes).
* `get_size(self)`: This method should return an integer representing the current size of the file (in bytes).
* `get_name(self)`: This method should return a string representing the name of the file.
* `set_size(self, new_size)`: This method should change the size of the file to the `new_size` given as an argument. The type of `new_size` is expected to be an integer. 
* `set_name(self, new_name)`: This method should change the name of the file to the `new_name` given as an argument. The type of `new_name` is expected to be a string. 
* `__eq__(self, other)`: This method takes another `File` object as an argument for comparison and returns `True` if *this* file and the *other* file have the same name and the same size, otherwise `False`. Implementing this method will allow us to use `==` operator to compare two `File` object instances.
* `__str__(self)` should return a string representation of the file object in the following format: `File name: <name>, File size: <size>`.
* `__lt__(self, other)` should take another `File` object as an argument and return `True` if the size attribute of *this* file is smaller than the *other*'s. Return `False` otherwise. Implementing this method will allow us to use `<` operator to compare the two `File` object instances.

Example use case:
```
  file1 = File('hello.txt', 10)
  file2 = File('hello.txt', 10)
  print(file1) # Should print 'File name: hello.txt, File size: 10'

  file3 = File('bybye.md', 20)
  print(file3) # Should print 'File name: bybye.md, File size: 20'

  print(file1 == file3) # Should print False
  print(file1 == file2) # Should print True
```

### Part 2: Directory Class
In this part your task is to design a `Directory` class. The `Directory` class should have the following methods:

* `__init__(self, name, max_size)` This method should initialize a `Directory` object with a string `name` and an int `max_size` (in bytes). It should also keep track of how much of the memory is currently used, e.g. with a `size` attribute which is initialized to 0. Your `Directory` class should also have a `files` attribute that is a list of `File` objects contained in this directory. 
* `get_size(self)` This method should return an integer representing the current size of the directory (in bytes).
* `set_size(self, new_size)` This method should take an integer argument and change the current size of the directory.
* `add_file(self, file)`: This method takes a `File` object as an argument and should add the file to the directory if there is sufficient memory for it. If there is not enough memory, the method should return a string message saying `"Not enough memory."`.
* `rm_file(self, file)`: This method should find and remove the `File` object passed as argument from the list of files in the directory. To compare file objects, you can use `==` operator, thanks to implementation of `__eq__` in the `File` object. If the file is not in the directory, it should return a string message saying `"File not in the directory."`. If the file was in the directory and it was successfully removed, this function should return `None`.
* `sort_dir(self, in_place=True)` should modify `self.files` such that the files are sorted in ascending order in terms of size. This method will change the order of files in the directory if `in_place` is `True`. If `in_place` is `False`, **you should return a new list of file objects**, sorted in ascending order according to their size without modifying the order of files in the directory. **Hint:** Use the `<` operator to compare `File` objects.
* `get_largest_file(self)`: This method should return the largest file in the directory. 
* `get_smallest_file(self)`: This method should return the smallest file in the directory. 
* `get_files_larger_than(self, ref_file)`: This method should return a new list of file objects that are larger than the `ref_file`.
* `__str__(self)`: This method should return a list of names of the files (casted as a string) in the directory i.e. "[<name_of_file>, <name_of_file>, <name_of_file>, . . .]".
* `__lt__(self, other)`: This method should take another `Directory` object as an argument and return a boolean that represents whether *this* directory is *smaller than* the *other* directory in terms of the actual size they use. 

**Hint:** Do not forget to update the current size and list of files of the directory after adding or removing a file.

**Note:** Example use cases are available in `part2.py`.


### Part 3: Dataset Class
In this part, we will design a `Dataset` class that inherits from the `Directory` class. The `Dataset` class should have the following methods:

* `__init__(self, name, max_size, category)`: This method should initialize a `Dataset` object with a string `name`, int `max_size`, and a str `category`. The `category` is a brief description of the dataset, e.g. "Autonomous Driving", "Object Detection", "Image Classification", etc.

* `get_category(self)` This method should return the `category` of the dataset.

Here is how you can create a COCO, NuScenes, and MOT17 dataset objects:
```
coco = Dataset('COCO', 1000000000, 'Object Detection')
nu_scenes = Dataset('NuScenes', 500000000, 'Autonomous Driving')
mot17 = Dataset('MOT17', 500000000, 'Tracking')
```
If you implemented inheritance correctly, you can add files to a dataset like this:
```
file1 = File('image1.jpg', 1000000)
file2 = File('image2.jpg', 2000000)
coco.add_file(file1)
coco.add_file(file2)
```
You can get the size of a dataset like this:
```
size = coco.get_size()
```

Now, let's do a few interesting things by writing some code into the function `final_test()` in `part3.py`. First create a few files, directories, and datasets to play with.
```
file1 = File('img001.png', 10)
file2 = File('img002.png', 20)
file3 = File('img003.png', 30)
file4 = File('img004.png', 40)
file5 = File('img005.png', 50)
file6 = File('img006.png', 60)
file7 = File('img007.png', 70)
file8 = File('img008.png', 80)
file9 = File('img009.png', 90)
file10 = File('img010.png', 100)
file11 = File('img011.png', 110)
file12 = File('img012.png', 120)

dataset1 = Dataset('d1', 1000, 'first dataset')
dataset2 = Dataset('d2', 1000, 'second dataset')
directory3 = Directory('d3', 1000)

dataset1.add_file(file1)
dataset1.add_file(file2)
dataset1.add_file(file3)
dataset1.add_file(file4)

dataset2.add_file(file5)
dataset2.add_file(file6)
dataset2.add_file(file7)
dataset2.add_file(file8)

directory3.add_file(file9)
directory3.add_file(file10)
directory3.add_file(file11)
directory3.add_file(file12)
```

Afterwards, your `final_test()` function should do the following:

* For any file in any directory/dataset that's larger than the largest file in dataset2, move it to dataset1. To do so, you need to find the largest file in dataset2, and then find all files from dataset1 and directory 3 that are larger than it. Then, add those files to dataset1 and remove them from directory3.
* Then, for any file in any directory/dataset that's smaller than the smallest file in dataset2, move it to directory3. To do so, you need to find the smallest file in dataset2, and then find all files from dataset1 and directory 3 that are smaller than it. Then, add those files to directory3 and remove them from dataset1
* return the tuple (dataset1, dataset2, directory3)

---------------