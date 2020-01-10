with open("gt.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

result = []
check = []

content = [data.split(",") for data in content]

path = "/home/anhdh/projects/tensorflow-yolov3/data/samsung/data"

for i in range(len(content)):
    if (content[i][0] in check): continue
    current = []
    # /home/yang/test/VOC/test/VOCdevkit/VOC2007/JPEGImages/000001.jpg 48,240,195,371,11 8,12,352,498,14
    current.append("{},{},{},{},{}".format(content[i][1], content[i][2], content[i][3], content[i][4], content[i][5]))

    for j in range(i+1, len(content)):
        if content[i][0] == content[j][0]:
            current.append("{},{},{},{},{}".format(content[j][1], content[j][2], content[j][3], content[j][4], content[j][5]))
    result.append("{}/{} {}".format(path, content[i][0], " ".join(current)))
    check.append(content[i][0])

print(len(result))

with open('../dataset/samsung_train.txt', 'w') as f:
    for item in result[:800]:
        f.write("%s\n" % item)

with open('../dataset/samsung_val.txt', 'w') as f:
    for item in result[800:]:
        f.write("%s\n" % item)