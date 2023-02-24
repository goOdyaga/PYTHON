from part1 import File
from part2 import Directory
from part3 import Dataset, final_test

###########################################
########### TESTS FOR PART 1 ##############
###########################################
def test_part1_1():
  correct = False
  try:
    file1 = File("image1.png", 60)
    pred = file1.get_name()
    target = "image1.png"
    correct = pred == target
    
  except:
    print('There is a problem with your code. Have you implemented File.get_name()?')

  assert correct, f"Your method File.get_name() should return {target} but it returns {pred} instead"

  

def test_part1_2():
  correct = False
  try:
    file1 = File("image1.png", 60)
    pred = file1.get_size()
    target = 60
    correct = pred == target
    
  except:
    print('There is a problem with your code. Have you implemented File.get_size()?')

  assert correct, f"Your method File.get_size() should return {target} but it returns {pred} instead"

  

def test_part1_3():
  correct = False
  try:
    file1 = File("image1.png", 60)
    file1.set_name("img1.png")
    pred = file1.get_name()
    target = "img1.png"
    correct = pred == target
    
  except:
    print('There is a problem with your code. Have you implemented File.set_name()?')

  assert correct, "Your method File.set_name() may be problematic"

  

def test_part1_4():
  correct = False
  try:
    file1 = File("image1.png", 60)
    file1.set_size(20)
    pred = file1.get_size()
    target = 20
    correct = pred == target
    
  except:
    print('There is a problem with your code. Have you implemented File.set_size()?')

  assert correct, "Your method File.set_size() may be problematic"

  

def test_part1_5():
  correct = False
  try:
    file1 = File("image1.png", 60)
    file2 = File("image1.png", 60)
    pred = file1 == file2
    target = True
    correct = pred == target
    
  except:
    print('There is a problem with your code. Have you implemented File.__eq__()?')

  assert correct, "Your method File.__eq__() may be problematic"

  

def test_part1_6():
  correct = False
  try:
    file1 = File("image1.png", 60)
    file2 = File("image1.png", 70)
    pred = file1 == file2
    target = False
    correct = pred == target
    
  except:
    print('There is a problem with your code. Have you implemented File.__eq__()?')

  assert correct, "Your method File.__eq__() may be problematic"

  

def test_part1_7():
  correct = False
  try:
    file1 = File("image1.png", 60)
    file2 = File("image1.png", 70)
    pred = file1 < file2
    target = True
    correct = pred == target
    
  except:
    print('There is a problem with your code. Have you implemented File.__lt__()?')

  assert correct, "Your method File.__lt__() may be problematic"

  

def test_part1_8():
  correct = False
  try:
    file1 = File("image1.png", 60)
    file2 = File("image1.png", 60)
    pred = file1 < file2
    target = False
    correct = pred == target
    
  except:
    print('There is a problem with your code. Have you implemented File.__lt__()?')

  assert correct, "Your method File.__lt__() may be problematic"

###########################################
########### TESTS FOR PART 2 ##############
###########################################
def test_part2_1():
  # tests if they understood size vs max_size
  correct = False
  try:
    my_directory = Directory("Documents", 20)
    target = 0
    pred = my_directory.get_size()
    correct = pred == target
    
  except:
    print('There was a problem. Have you implemented Directory.get_size()?')

  assert correct, f'Directory.get_size() should return {target}, yours returns {pred}'

def test_part2_2():
  # tests set_size()
  correct = False
  try:
    my_directory = Directory("Documents", 20)
    my_directory.set_size(10)
    target = 10
    pred = my_directory.get_size()
    correct = pred == target
    
  except:
    print('There was a problem. Have you implemented Directory.set_size()?')

  assert correct, f'Directory.get_size() should return {target}, yours returns {pred}. Check Directory.set_size()'
  
def test_part2_3():
  # tests if add_file() updates size
  correct = False
  try:
    file1 = File('img1.png', 25)
    file2 = File('img2.png', 25)
    file3 = File('img3.png', 25)
    my_directory = Directory("Documents", 100)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3)
    pred = my_directory.get_size()
    target = 75
    correct = pred == target
    
  except:
    print('There is something wrong with Directory.add_file()')
  
  assert correct, f'After adding files, Directory.get_size() shoudl return {target}. Yours returns {pred}'

def test_part2_4():
  # tests if add_file updates size with max_size check
  correct = False
  try:
    file1 = File('img1.png', 25)
    file2 = File('img2.png', 25)
    file3 = File('img3.png', 25)
    my_directory = Directory("Documents", 50)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3) # should fail and return message
    pred = my_directory.get_size()
    target = 50
    correct = pred == target
  except:
    print('There is something wrong with Directory.add_file()')
  assert correct, f'After adding more files than the capacity, Directory.get_size() should return {target}. Yours returns {pred}. Also make sure you are using max_size'

def test_part2_5():
  # tests if add_file updates files
  correct = False
  try:
    file1 = File('img1.png', 25)
    file2 = File('img2.png', 25)
    file3 = File('img3.png', 25)
    my_directory = Directory("Documents", 100)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3)
    pred = my_directory.files
    target = [file1, file2, file3]
    correct = pred == target
    
  except:
    print('There is a problem with your implementation. Check add_files() and .files attribute')

  assert correct, f'Do you have a Directory.files attribute with the added files?'

def test_part2_6():
  # tests if add_file updates files with max_size check
  correct = False
  try:
    file1 = File('img1.png', 25)
    file2 = File('img2.png', 25)
    file3 = File('img3.png', 25)
    my_directory = Directory("Documents", 50)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3) # should fail because of max_size
    pred = my_directory.files
    target = [file1, file2]
    correct = pred == target
    
  except:
    print('There is a problem with your implementation. Check add_files() and .files attribute')

  assert correct, f'Do you have a Directory.files attribute with the added files? Make sure you check with max_size before adding files'

def test_part2_7():
  # tests if rm_file updates files
  correct = False
  try:
    file1 = File('img1.png', 25)
    file2 = File('img2.png', 25)
    file3 = File('img3.png', 25)
    my_directory = Directory("Documents", 100)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3)
    my_directory.rm_file(file1) # this part should remove the file (and update size)
    pred = my_directory.files
    target = [file2, file3]
    correct = pred == target
    
  except:
    print('There is a problem with your implementation. Check rm_files() and .files attribute')

  assert correct, f'Do you update the Directory.files attribute with rm files?'

def test_part2_8():
  # tests if rm_file updates size
  correct = False
  try:
    file1 = File('img1.png', 25)
    file2 = File('img2.png', 25)
    file3 = File('img3.png', 25)
    my_directory = Directory("Documents", 100)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3)
    my_directory.rm_file(file1) # this part should remove the file and update size
    pred = my_directory.get_size()
    target = 50
    correct = pred == target
    
  except:
    print('There is a problem with your implementation. Check rm_files() and .files attribute')

  assert correct, f'Do you update the Directory.size attribute with rm files?'

def test_part2_9():
  # tests sort_dir(in_place=True)
  correct = False
  try:
    file1 = File('img1.png', 30)
    file2 = File('img2.png', 20)
    file3 = File('img3.png', 10)
    my_directory = Directory("Documents", 100)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3)
    my_directory.sort_dir(True) # this part should sort files attribute directly
    pred = my_directory.files
    target = [file3, file2, file1]
    correct = pred == target
    
  except:
    print('There is a problem with your implementation. Check sort_dir(in_place)')

  assert correct, f'Do you update the Directory.files attribute with sort_dir() when in_place is True?'

def test_part2_10():
  # tests sort_dir(in_place=False)
  correct = False
  try:
    file1 = File('img1.png', 30)
    file2 = File('img2.png', 20)
    file3 = File('img3.png', 10)
    my_directory = Directory("Documents", 100)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3)
    sorted_files = my_directory.sort_dir(False) # this part should NOT sort files attribute directly, and return the sorted files list instead
    pred_1, pred_2 = sorted_files, my_directory.files
    target_1, target_2 = [file3, file2, file1], [file1, file2, file3]
    correct = pred_1 == target_1 and pred_2 == target_2
    
  except:
    print('There is a problem with your implementation. Check sort_dir(in_place)')

  assert correct, f"Do you return a sorted list of files sort_dir() when in_place is False? Also make sure that you aren't changing the order of the files attribute itself when in_place is False"

def test_part2_11():
  # tests get_largest_file()
  correct = False
  try:
    file1 = File('img1.png', 10)
    file2 = File('img2.png', 30)
    file3 = File('img3.png', 20)
    my_directory = Directory("Documents", 100)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3)
    pred = my_directory.get_largest_file()
    target = file2
    correct = pred == target
    
  except:
    print('Have you implemented the get_largest_file() method?')

  assert correct, f'get_largest_file() should return the File object file2, yours returns {pred}'

def test_part2_12():
  # tests get_smallest_file()
  correct = False
  try:
    file1 = File('img1.png', 30)
    file2 = File('img2.png', 10)
    file3 = File('img3.png', 20)
    my_directory = Directory("Documents", 100)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3)
    pred = my_directory.get_smallest_file()
    target = file2
    correct = pred == target
    
  except:
    print('Have you implemented the get_smallest_file() method?')

  assert correct, f'get_smallest_file() should return the File object file2, yours returns {pred}'

def test_part2_13():
  # tests get_files_larger_than()
  correct = False
  try:
    file1 = File('img1.png', 10)
    file2 = File('img2.png', 20)
    file3 = File('img3.png', 30)
    file4 = File('img4.png', 40)
    my_directory = Directory("Documents", 100)
    my_directory.add_file(file1)
    my_directory.add_file(file2)
    my_directory.add_file(file3)
    my_directory.add_file(file4)

    pred = my_directory.get_files_larger_than(file2)
    target = [file3, file4]
    correct = pred == target
    
  except:
    pass
    
  assert correct, f"check get_files_larger_than(file2). It should return a list of file objects [file3, file4]. You don't need to sort anything"

def test_part2_14():
  correct = False
  try:
    file1 = File('img1.png', 10)
    file2 = File('img2.png', 10)
    file3 = File('img3.png', 20)
    file4 = File('img4.png', 20)
    
    my_directory_1 = Directory("Downloads", 100)
    my_directory_2 = Directory("Documents", 100)
    
    my_directory_1.add_file(file1)
    my_directory_1.add_file(file2)
    my_directory_2.add_file(file3)
    my_directory_2.add_file(file4)

    pred = my_directory_1 < my_directory_2
    target = True

    correct = pred == target
    
  except:
    print('Have you implemented Directory.__lt__()? Check if you implemented it right')
    
  assert correct, f'my_directory_1 < my_directory_2 should return True, yours returns {pred}'

###########################################
########### TESTS FOR PART 3 ##############
###########################################
def test_part3_1():
  correct = False
  try:
    dataset1, dataset2, directory3 = final_test()
    
    dataset_1_file_names = set([ file.get_name() for file in dataset1.files ])
    dataset_2_file_names = set([ file.get_name() for file in dataset2.files ])
    directory_3_file_names = set([ file.get_name() for file in directory3.files ])

    dataset_1_target = set(['img009.png', 'img010.png', 'img011.png', 'img012.png'])
    dataset_2_target = set(['img005.png', 'img006.png', 'img007.png', 'img008.png'])
    directory_3_target = set(['img001.png', 'img002.png', 'img003.png', 'img004.png'])

    cond_1 = dataset_1_file_names == dataset_1_target
    cond_2 = dataset_2_file_names == dataset_2_target
    cond_3 = directory_3_file_names == directory_3_target

    correct = cond_1 and cond_2 and cond_3
    
  except:
    print('Have you implemented final_test()?')

  assert correct, "dataset1 files should be ['img009.png', 'img010.png', 'img011.png', 'img012.png'],\
  dataset2 files should be ['img005.png', 'img006.png', 'img007.png', 'img008.png'], \
  directory3 files should be ['img001.png', 'img002.png', 'img003.png', 'img004.png']"
  
# def test_partX_X():
#   correct = False
#   try:
#     pass
    
#   except:
#     pass
    
#   assert correct, ''
test_part1_1()
test_part1_2()
test_part1_3()
test_part1_4()
test_part1_5()
test_part1_6()
test_part1_7()
test_part1_8()
test_part2_1()
test_part2_2()
test_part2_3()
test_part2_4()
test_part2_5()
test_part2_6()
test_part2_7()
test_part2_8()
test_part2_9()
test_part2_10()
test_part2_11()
test_part2_12()
test_part2_13()
test_part2_14()
test_part3_1()