import json
import math

# READING FROM JSON
with open('20200319_dhldemo_0000.json') as json_file:
    data_read = json.load(json_file)

for i in range(len(data_read)):
    print('item: {} - score: {:.2f} % - coordinates: {}'.format(i+1, (data_read[i]['score'])*100, (data_read[i]['segmentation'])))



# vypocet vektora, velkost prepravky 100x100x10, rozdelene na 4 sektory, x,y = 0, 0 je v strede prepravky
center_object_x, center_object_y, center_object_z = 45, 45, 8
center_box_x, center_box_y, center_box_z = 0, 0, 0
zone = 0 # 1 top_right, 2 down_right, 3 down_left, 4 top_left
vector_x_start, vector_y_start, vector_z_start = 0, 0, 0
vector_x_end, vector_y_end, vector_z_end = 0, 0, 0
length_vector = 10 # length of vector = 10cm

def compute_vector(center_object_x, center_object_y, center_object_z):
    # objekt je napravo od stredu
    if center_box_x >= 0:
        if center_box_y >= 0:
            zone = 1
            vector_x_start, vector_y_start, vector_z_start = center_object_x, center_object_y, center_object_z
            a = center_object_y - center_box_y
            b = center_object_x - center_box_x
            c = math.sqrt((a*a)+(b*b))
            alpha = 1 / math.sin(a/c)

        if center_box_y < 0:
            zone = 2
            vector_x_start, vector_y_start, vector_z_start = center_object_x, center_object_y, center_object_z



    if center_box_x < 0:
        if center_box_y < 0:
            zone = 3
            vector_x_start, vector_y_start, vector_z_start = center_object_x, center_object_y, center_object_z

        if center_box_y >= 0:
            zone = 4
            vector_x_start, vector_y_start, vector_z_start = center_object_x, center_object_y, center_object_z


    return (vector_x_start, vector_y_start, vector_z_start, vector_x_end, vector_y_end, vector_z_end)