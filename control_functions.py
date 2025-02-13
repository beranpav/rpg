def check_for_mosters(map,map_matrix):
    nm = 0
    map_size_x = map.shape[0]
    map_size_y = map.shape[1]
    for i in range(0, map_size_x):
        for j in range(0, map_size_y):
            if map[i,j]["monster"] == 9: #or map[i,j]["monster"] == 2:
                nm += 1
                for ii in range(i-3,i+4):
                    for jj in range(j-3,j+4):
                        if ii >= 0 and ii < map_size_x and jj >=0 and jj < map_size_y:
                            if (i-ii)**2 == (j-jj)**2:
                                map_matrix[ii,jj,0] = 0
                                map_matrix[ii,jj,1] = 255
                                map_matrix[ii,jj,2] = 0
            """
            if map[i,j]["monster"] == 3 or map[i,j]["monster"] == 4 or map[i,j]["monster"] == 5:
                nm += 1
                for ii in range(i-3,i+4):
                    for jj in range(j-3,j+4):
                        if ii >= 0 and ii < map_size_x and jj >=0 and jj < map_size_y:
                            if (i-ii)**2 == (j-jj)**2:
                                map_matrix[ii,jj,0] = 0
                                map_matrix[ii,jj,1] = 0
                                map_matrix[ii,jj,2] = 255
            if map[i,j]["monster"] == 6 or map[i,j]["monster"] == 7 or map[i,j]["monster"] == 8:
                nm += 1
                for ii in range(i-3,i+4):
                    for jj in range(j-3,j+4):
                        if ii >= 0 and ii < map_size_x and jj >=0 and jj < map_size_y:
                            if (i-ii)**2 == (j-jj)**2:
                                map_matrix[ii,jj,0] = 255
                                map_matrix[ii,jj,1] = 0
                                map_matrix[ii,jj,2] = 0
            """
def check_for_loot(map,map_matrix):
    nm = 0
    map_size_x = map.shape[0]
    map_size_y = map.shape[1]
    for i in range(0, map_size_x - 1):
        for j in range(0, map_size_y - 1):
            if map[i,j]["inventory"] == 1 or map[i,j]["inventory"] == 2 or map[i,j]["inventory"] == 3:
                nm += 1
                for ii in range(i-3,i+3):
                    for jj in range(j-3,j+3):
                        if ii >= 0 and ii < map_size_x and jj >=0 and jj < map_size_y:
                            map_matrix[ii,jj,0] = 255
                            map_matrix[ii,jj,1] = 0
                            map_matrix[ii,jj,2] = 0
            if map[i,j]["inventory"] == 4:
                nm += 1
                for ii in range(i-3,i+3):
                    for jj in range(j-3,j+3):
                        if ii >= 0 and ii < map_size_x and jj >=0 and jj < map_size_y:
                            map_matrix[ii,jj,0] = 0
                            map_matrix[ii,jj,1] = 255
                            map_matrix[ii,jj,2] = 0
            if map[i,j]["inventory"] == 5 or map[i,j]["inventory"] == 6:
                nm += 1
                for ii in range(i-3,i+3):
                    for jj in range(j-3,j+3):
                        if ii >= 0 and ii < map_size_x and jj >=0 and jj < map_size_y:
                            map_matrix[ii,jj,0] = 0
                            map_matrix[ii,jj,1] = 0
                            map_matrix[ii,jj,2] = 255