import os
import re

#  "random telephone number is 408-555-1234"

comp_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

for folder , sub_folders , files in os.walk("."):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for fn in files:
        print("\t File: "+fn)
        with open(folder+'/'+fn,'r') as f:
            i = 1
            for line in f:
                if phonelist := re.findall(comp_regex,line):
                    for match in phonelist:
                        print()
                        print("in file:",fn)
                        print("match found:", match)
                        print()
                        print(f"line[{i}]...")
                        # print(f"line[{i}]:{line}")
                        print()
                i += 1
        # phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
    print('\n')
    
    # Now look at subfolders