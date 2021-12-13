import os

directory = os.fsencode('pdf/')

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"):
        print(os.path.join('pdf/',filename))
        continue
    else:
        continue