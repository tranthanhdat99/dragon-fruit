import os
import glob
des = 'D:\DAT\computer_vision\yolov5\dataset\labels_new'
if __name__ == '__main__':
    labels = 'D:\DAT\computer_vision\yolov5\dataset\labels'
    for label in glob.glob(os.path.join(labels, '*.txt')):
        with open(label, 'r') as f:
            lines = f.readlines()
            name_label = os.path.basename(label)
            with open(os.path.join(des, name_label ), 'w') as file:
                for line in lines:
                    line = line.split(" ")
                    if line[0] == '1':
                        line[0] = '0'
                    elif line[0] == '2':
                        line[0] = '1'
                    elif line[0] == '3':
                        line[0] = '2'
                    for _ in range(len(line) - 1):
                        file.write(line[_] + ' ')
                        if line[_] == '2':
                            print(name_label)
                    file.write(line[-1])
                    # file.write("\n")



