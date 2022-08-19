import os

def getContent(path, indentation, decorator):
  contents = (os.listdir(path))
  for content in contents :
    if(os.path.isfile(f'{path}\{content}')):
      print(f'{indentation} {decorator} F {content}')
    else:
      print(f'{indentation} {decorator} D {content}')
      getContent(f'{path}\{content}', indentation + " ", "-")
      

# please change the path to the root of your folder
path= r"C:\Users\User\Documents\Jobs\Software\Topleft\input_directory"
getContent(path, "", "")