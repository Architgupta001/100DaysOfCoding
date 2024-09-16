import os
path = os.chdir('C:/Users/gupta/Desktop/100DaysOfCoding/Python/Day-16/Automatic File Cleaner')

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f'{folder} created successfully...')

createIfNotExist("Images")
createIfNotExist("Word Docs")
createIfNotExist("Excel Docs")
createIfNotExist("PPT Docs")

files = os.listdir()

# All the extensions of the file 

imgExt = ['.jpg','.png','.jpeg','.webp','.bmp']
wordDocExt = ['.docx','.txt']
excelExt = ['.xlsx']
pptExt = ['.pptx']

images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]

for image in images:
    os.replace(image,f'Images/{image}')

wordDocs = [file for file in files if os.path.splitext(file)[1].lower() in wordDocExt]

for doc in wordDocs:
    os.replace(doc,f'Word Docs/{doc}')

pptDocs = [file for file in files if os.path.splitext(file)[1].lower() in pptExt]

for ppt in pptDocs:
    os.replace(ppt,f'PPT Docs/{ppt}')

excelDocs = [file for file in files if os.path.splitext(file)[1].lower() in excelExt]

for excel in excelDocs:
    os.replace(excel,f'Excel Docs/{excel}')
