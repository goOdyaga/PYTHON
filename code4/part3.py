from part1 import File
from part2 import Directory
class Dataset(Directory):
    def __init__(self, name: str, max_size: int, category: str):
        super().__init__(name, max_size)
        self.category = category
        
    def get_category(self):
        return self.category


def final_test():
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
    
    largest_file_ds2 = max(dataset2.files, key=lambda file: file.size)
    for file in directory3.files[:]:
        if file.size > largest_file_ds2.size:
            dataset1.add_file(file)
            directory3.rm_file(file)
    
    smallest_file_ds2 = min(dataset2.files, key=lambda file: file.size)
    for file in dataset1.files[:]:
        if file.size < smallest_file_ds2.size:
            directory3.add_file(file)
            dataset1.rm_file(file)
    return dataset1, dataset2, directory3
if __name__ == '__main__':
  # You can then use these classes like this:
  coco = Dataset('COCO', 1000000000, 'Object Detection')
  nu_scenes = Dataset('NuScenes', 500000000, 'Autonomous Driving')

  file1 = File('image1.jpg', 1000000)
  file2 = File('image2.jpg', 2000000)
  coco.add_file(file1)
  coco.add_file(file2)

  size = coco.get_size()
  category = coco.get_category()

  dataset1, dataset2, directory3 = final_test()
  print(dataset1)
  print(dataset2)
  print(directory3)

