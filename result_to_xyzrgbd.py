import os
import os.path
import glob
import argparse
import numpy as np
#1008 * 768

original_files = [f for f in os.listdir(os.path.dirname(os.path.realpath(__file__)))]

new_file_names = []

for f in original_files:
    # check if it is an image files
    print(f)
    path, ext = os.path.splitext(f)
    if(ext != ".txt"):
        print("not an txt file : " + f)
        original_files.remove(f)
    else:
    # if it is an image file change the filename to be used as "graycode_nn" format
        tempNameList = path.split("_")
        newFileName = "xyzrgb_" + tempNameList[1]
        print("changed name is : " + newFileName)
        new_file_names.append(newFileName)

new_text_to_write = open( os.path.join(os.path.dirname(os.path.realpath(__file__)), new_file_names[0]+ ".txt") , 'w')

with open( os.path.join(os.path.dirname(os.path.realpath(__file__)),original_files[0])) as fp:
    for count, line in enumerate(fp):
        # if count < 10:
        #     print(parsed_line_list[3])
        #     print(parsed_line_list[3].strip() == "0.000000000000000000e+00")
        parsed_line_list = line.split(" ")
        if parsed_line_list[3].strip() == "0.000000000000000000e+00":
            # print(count)
            pass

        else :
            # if count < 100000 :
                # print("////////////")
                # print(count // 1002)
                # print("------------")
                # print(count %  1002)
                # print("////////////")
                # x , y , depth, r , g, b
            x = count % 1002
            y = count // 1002
            f= 500
            d = float(parsed_line_list[3].strip())
            z = d*f / np.sqrt(x*x + y*y + f*f) 

            tempLine = [str ( x * z / f), str(y * z / f * 2), str ( z ), parsed_line_list[0].strip(), parsed_line_list[1].strip(), parsed_line_list[2].strip(), '\n' ]
            # tempLine = [str ( x * d  /f), str(y * d  /f ), str ( d ), parsed_line_list[0].strip(), parsed_line_list[1].strip(), parsed_line_list[2].strip(), '\n' ]
            # tempLine = [str ( x ), str(y ), str ( d ), parsed_line_list[0].strip(), parsed_line_list[1].strip(), parsed_line_list[2].strip(), '\n' ]
            new_text_to_write.write(" ".join(tempLine))
            # else:
            #     pass

new_text_to_write.close()
print('Total Lines', count + 1)