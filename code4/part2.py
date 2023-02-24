from part1 import File

class Directory:
    def __init__(self, name, max_size):
        self.name = name
        self.max_size = max_size
        self.size = 0
        self.files = []
    
    def get_size(self):
        return self.size
    
    def set_size(self, new_size):
        self.size = new_size
    
    def add_file(self, file):
        if self.size + file.get_size() > self.max_size:
            return "Not enough memory."
        self.files.append(file)
        self.size += file.get_size()
    
    def rm_file(self, file):
        if file not in self.files:
            return "File not in the directory."
        self.files.remove(file)
        self.size -= file.get_size()
    
    def sort_dir(self, in_place=True):
        if in_place:
            self.files.sort(key = lambda x: x.get_size())
        else:
            return sorted(self.files, key = lambda x: x.get_size())
        
    def get_largest_file(self):
        self.files.sort(key = lambda x: x.get_size(), reverse=True)
        return self.files[0]
    
    def get_smallest_file(self):
        self.files.sort(key = lambda x: x.get_size())
        return self.files[0]
    
    def get_files_larger_than(self, ref_file):
        return [f for f in self.files if f.get_size() > ref_file.get_size()]
    
    def __str__(self):
        return str([f.get_name() for f in self.files])
    
    def __lt__(self, other):
        return self.size < other.size

  
if __name__ == '__main__':
  
  print('------------------------------------------------------------')
  my_directory = Directory("Documents", 20) # create a directory with max size of 20 bytes
  file1 = File("image_001.jpg", 10) # create a file of 10 bytes
  file2 = File("image_002.jpg", 10) # create a file of 10 bytes
  file3 = File("image_003.jpg", 10) # create a file of 10 bytes

  print(my_directory.get_size()) # should print 0
  my_directory.add_file(file1) # add file1 to the directory. the directory size should update
  print(my_directory.get_size()) # should print 10
  my_directory.add_file(file2) # add file2 to the directory. the directory size should update
  print(my_directory.get_size()) # should print 20
  print(my_directory.add_file(file3)) # adding file3 to the directory should fail and print "Not enough memory."

  my_directory.rm_file(file1) # remove file1 from the directory should succeed
  print(my_directory.rm_file(file1)) # # remove file1 from the directory should fail and should print "File not in the directory."
  print(my_directory.get_size()) # should print 10
  
  print('------------------------------------------------------------')
  my_directory_2 = Directory("Desktop", 200) # create a new directory
  file4 = File("image_004.jpg", 5)
  file5 = File("image_005.jpg", 20)
  file6  = File("image_006.jpg", 10)
  my_directory_2.add_file(file4)
  my_directory_2.add_file(file5)
  my_directory_2.add_file(file6)
  print(my_directory_2) # shoud print "['image_004.jpg', 'image_005.jpg', 'image_006.jpg']"
  sorted_files = my_directory_2.sort_dir(False) # should return a list of sorted File objects
  print([file.get_name() for file in sorted_files]) # shoud print "['image_004.jpg', 'image_006.jpg', 'image_005.jpg']"
  print(my_directory_2) # shoud print "['image_004.jpg', 'image_005.jpg', 'image_006.jpg']"
  my_directory_2.sort_dir(True) # should sort the files in place
  print(my_directory_2) # shoud print "['image_004.jpg', 'image_006.jpg', 'image_005.jpg']"
  print(my_directory_2.get_size()) # should print 35

  print('------------------------------------------------------------')
  my_directory_3 = Directory("Documents", 200) # create a new directory
  file7 = File("image_007.jpg", 5)
  file8 = File("image_008.jpg", 20)
  file9  = File("image_009.jpg", 10)
  file10 = File("image_010.jpg", 2)
  my_directory_3.add_file(file7)
  my_directory_3.add_file(file8)
  my_directory_3.add_file(file9)
  my_directory_3.add_file(file10)

  files_larger_than_file7 = my_directory_3.get_files_larger_than(file7) # should return a list of file objects
  print([file.get_name() for file in files_larger_than_file7]) # should print ['image_008.jpg', 'image_009.jpg']

  print('------------------------------------------------------------')
  print(my_directory_3.get_size()) # should print 37
  print(my_directory_2.get_size()) # should print 35
  print(my_directory_2 < my_directory_3) # should print True
  
  