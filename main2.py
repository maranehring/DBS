import re

original = []
noCapitals = []
alphanumerical = []
alphaNumNoCaps = []
bigList = []
lenNoCap = len(noCapitals)
lenAlpNum = len(alphanumerical)
lenAlpNumNoCap = (len(alphaNumNoCaps))
with open("tweets.txt") as fh:
    for i in fh.readlines():
        original.append(i.strip())

for i in original:
    noCapitals.append(i.lower())

for j in original:
    alphanumerical.append(re.sub(r'[^A-Za-z0-9#]+', '', j).lstrip())

for j in alphanumerical:
    alphaNumNoCaps.append(j.lower())
for i in original:
    bigList.append(i)
for j in noCapitals:
    bigList.append(j)
for k in alphanumerical:
    bigList.append(k)
for l in alphaNumNoCaps:
    bigList.append(l)

"""
for i in range(0,len(bigList)):
    for j in range(i,len(bigList)):
        if i % n != j % n and bigList[i]==bigList[j]:
            print (findDistance(i,j))

for i in range(0,len(bigList)):
    for j in range(i,len(bigList)):
        if i % n != j % n and (bigList[i] in bigList[j] or bigList[j] in bigList[i]):
            print (findDistance(i,j)+1)
"""


def makeitmin(m, n):
    return min(
        [dist(m, n), dist(m + len(original), n), dist(2 * len(original) + m, n), dist(3 * len(original) + m, n),
         dist(m, n + len(original)), dist(m + len(original), n + len(original)),
         dist(2 * len(original) + m, n + len(original)), dist(3 * len(original) + m, n + len(original)),
         dist(m, 2 * len(original) + n), dist(m + len(original), 2 * len(original) + n),
         dist(2 * len(original) + m, 2 * len(original) + n),
         dist(3 * len(original) + m, 2 * len(original) + n), dist(m, 3 * len(original) + n),
         dist(m + len(original), 3 * len(original) + n), dist(2 * len(original) + m, 3 * len(original) + n),
         dist(3 * len(original) + m, 3 * len(original) + n)])


def dist(i, j):
    if (i % len(original) != j % len(original)) and (bigList[i] == bigList[j]):

        #print(int(finddistance(i, j)))
        return int(finddistance(i, j))

    elif i % len(original) != j % len(original) and bigList[j] in bigList[i]:
        #print(((int(finddistance(i, j))) + 1))
        return (int(finddistance(i, j)) + 1)

    elif i % len(original) != j % len(original) and bigList[i] in bigList[j]:
        #print(((int(finddistance(i, j))) + 1))
        return (int(finddistance(i, j)) + 1)

    else:

        return 100


def finddistance(x, y):
    if x < len(original) and y < len(original):
        return 0
    elif ((x < len(original) and y >= len(original) and y <= (2 * len(original) - 1)) or (
                    y < len(original) and (x >= len(original) and x <= (2 * len(original) - 1))) or (
                (x < len(original) and y >= 2 * len(original) and y <= (3 * len(original) - 1)) or (
                            y < len(original) and (x >= 2 * len(original) and x <= (3 * len(original) - 1))))):
        return 1
    elif (
                (x > len(original) and x <= (2 * len(original) - 1) and y > len(original) and y <= (
                                2 * len(original) - 1)) or (
                                    x >= (2 * len(original) - 1) and x <= (3 * len(original) - 1) and y >= (
                                        2 * len(original) - 1) and y <= (3 * len(original) - 1))):
        return 1
    elif (((x > len(original) and x <= (2 * len(original) - 1)) and (
                    y >= (2 * len(original) - 1) and y <= (3 * len(original) - 1))) or (
                (y > len(original) and y <= (2 * len(original) - 1)) and (
                            x >= (2 * len(original) - 1) and x <= (3 * len(original) - 1)))):
        return 2
    elif ((((x < len(original)) and (y >= 3 * len(original))) or (y < len(original) and x >= 3 * len(original)))):
        return 2
    elif (((y >= 3 * len(original)) and (x >= (2 * len(original) - 1) and x <= (3 * len(original) - 1)) or (
                        y >= 3 * len(original) and x > len(original) and x <= (2 * len(original) - 1))) or (
                    (x >= 3 * len(original)) and (y >= (2 * len(original) - 1) and y <= (3 * len(original) - 1)) or (
                                x >= 3 * len(original) and y > len(original) and y <= (2 * len(original) - 1)))):
        return 1
    elif (y >= 3 * len(original)) and (x >= 3 * len(original)):
        return 2
    else:
        return 4


"""
print("Hashtag1\t |\t Hashtag2\t|\t Dist")
print("bigList", len(bigList))
print("n", len(original))
"""
lili = []
def main():


    for i in range(0, len(original)):
        for j in range(0, len(original)):
            if bigList[i] == '#' or bigList[j] == '#':
                continue
            if makeitmin(i, j) == 100:
                continue
            #print(original[i], original[j], makeitmin(i, j))
            #print(makeitmin(i,j))
            lili.append(makeitmin(i,j))
    return





            # print(alphaNumNoCaps)
            # print(noCapitals)
            # print(original)
main()

with open("aa.txt","w") as b:
    for i in lili:
        b.write("%s\n" % i)
