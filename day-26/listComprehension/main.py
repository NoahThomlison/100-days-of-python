with open("file1.txt") as file1:
  file1Data = file1.readlines()
with open("file2.txt") as file2:
  file2Data = file2.readlines()

  commonNumbers = [int(num) for num in file1Data if num in file2Data]
  print(commonNumbers)
