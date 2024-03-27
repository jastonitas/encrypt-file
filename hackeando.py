def read_file(file_path):
  my_file = open(file_path, "r+")
  file_content = my_file.read()
  my_file.close()
  return file_content