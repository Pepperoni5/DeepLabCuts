import csv
import math

###################################################################################################
# code

# adjust for more or less precision of intersecting circles
circle_length = 4.5

body_part_dictionary = [
    "nose",
    "right paw",
    "left paw",
    "left ear",
    "right ear",
    "tail",
]

paw_touches_paw_count = 0
paw_touches_nose_count = 0
paw_touches_ear_count = 0
tail_touches_nose_count = 0


# converts coordinate list from
# ['458.74460992711874', '282.1591979206494', '424.70199214801517', '307.4729393461366', '426.44776741873847', '300.48983826324366', 'None', '259.46411940124705', '428.1935426894617', '262.0827823073319', 'None', '317.9475909704762']
# to
# [458, 282, 424, 307, 426, 300, None, 259, 428, 262, None, 317]
def convert_coordinates_to_integer(lst):
    int_lst = []
    for item in lst:
        if item == '':
            int_lst.append(None)
        else:
            int_lst.append(int(float(item)))
    return int_lst

def distance(p1, p2):
    if p1[0] is None or p1[1] is None or p2[0] is None or p2[1] is None:
        return float('inf')
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def convert_coordinates_to_float(results):
    return [float(x) if x != '' else None for x in results]

# uncomment this when using convert_coordinates_to_float
#
# def distance(p1, p2):
#     if p1[0] is None or p1[1] is None or p2[0] is None or p2[1] is None:
#         return float('inf')
#     return math.sqrt((float(p2[0]) - float(p1[0]))**2 + (float(p2[1]) - float(p1[1]))**2)

def detect_identical_pairs(individual_name, row_number, coordinates):

    global paw_touches_paw_count
    global paw_touches_nose_count
    global paw_touches_ear_count
    global tail_touches_nose_count

    for i in range(len(coordinates)-1):
        if coordinates[i] is None:
            continue
        for j in range(i+1, len(coordinates)-1):
            if j+1 < len(coordinates) and i+1 < len(coordinates):
                if distance((coordinates[i], coordinates[i+1]), (coordinates[j], coordinates[j+1])) <= circle_length:

                    body_part_1 = body_part_dictionary[i//2]
                    body_part_2 = body_part_dictionary[j//2]

                    if((("paw" in body_part_1) and ("paw" in body_part_2)) or (("paw" in body_part_1) and ("paw" in body_part_2))):
                        paw_touches_paw_count += 1

                    if((("nose" in body_part_1) and ("paw" in body_part_2)) or (("paw" in body_part_1) and ("nose" in body_part_2))):
                        paw_touches_nose_count += 1

                    if((("ear" in body_part_1) and ("paw" in body_part_2)) or (("paw" in body_part_1) and ("ear" in body_part_2))):
                        paw_touches_ear_count += 1

                    if((("nose" in body_part_1) and ("tail" in body_part_2)) or (("tail" in body_part_1) and ("nose" in body_part_2))):
                        tail_touches_nose_count += 1

                    #print(f"Intersection at row number {row_number} for {individual_name}, at [{body_part_dictionary[i//2]}] and [{body_part_dictionary[j//2]}] at coordinates ({coordinates[i]},{coordinates[i+1]}) and ({coordinates[j]},{coordinates[j+1]})")
                    # print(f"Circles at index {i} and {j} intersect at coordinates ({coordinates[i]},{coordinates[i+1]}) and ({coordinates[j]},{coordinates[j+1]})")

###################################################################################################

results = []
# read csv file locally
with open("00258data.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

print(len(results))

# start at row '4' because 'scorer' is row 0, 'individuals' is row 1, 'bodyparts' is row 2 and 'coords' is row 3
count = 0


print("--------------INDIVIDUAL 1---------------")

paw_touches_nose_count = 0
paw_touches_ear_count = 0
tail_touches_nose_count = 0

for labeled_data_row_number in range(4, len(results)):
    labeled_data_row = results[labeled_data_row_number]

    # storing coordinates for each individuals
    individual1_coordinates = convert_coordinates_to_integer(labeled_data_row[3:15])
    # uncomment for more accuracy
    # individual1_coordinates = convert_coordinates_to_float(labeled_data_row[3:15])
    detect_identical_pairs("individual1", labeled_data_row_number, individual1_coordinates)

# print(f"paw_touches_paw_count={paw_touches_paw_count}")
print(f"paw_touches_nose_count={paw_touches_nose_count}")
print(f"paw_touches_ear_count={paw_touches_ear_count}")
print(f"tail_touches_nose_count={tail_touches_nose_count}")


print("--------------INDIVIDUAL 2---------------")

paw_touches_nose_count = 0
paw_touches_ear_count = 0
tail_touches_nose_count = 0

for labeled_data_row_number in range(4, len(results)):
    labeled_data_row = results[labeled_data_row_number]

    # storing coordinates for each individuals
    individual2_coordinates = convert_coordinates_to_integer(labeled_data_row[15:27])
    # uncomment for more accuracy
    # individual2_coordinates = convert_coordinates_to_float(labeled_data_row[15:27])
    detect_identical_pairs("individual2", labeled_data_row_number, individual2_coordinates)

print(f"paw_touches_nose_count={paw_touches_nose_count}")
print(f"paw_touches_ear_count={paw_touches_ear_count}")
print(f"tail_touches_nose_count={tail_touches_nose_count}")

print("--------------INDIVIDUAL 3---------------")

paw_touches_nose_count = 0
paw_touches_ear_count = 0
tail_touches_nose_count = 0

for labeled_data_row_number in range(4, len(results)):
    labeled_data_row = results[labeled_data_row_number]

    # storing coordinates for each individuals
    individual3_coordinates = convert_coordinates_to_integer(labeled_data_row[27:])
    # uncomment for more accuracy
    # individual3_coordinates = convert_coordinates_to_float(labeled_data_row[27:])
    detect_identical_pairs("individual3", labeled_data_row_number, individual3_coordinates)

print(f"paw_touches_nose_count={paw_touches_nose_count}")
print(f"paw_touches_ear_count={paw_touches_ear_count}")
print(f"tail_touches_nose_count={tail_touches_nose_count}")
