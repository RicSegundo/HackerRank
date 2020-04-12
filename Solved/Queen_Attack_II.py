n = 5
k = 3
r_q = 4
c_q = 3

obstacles = [[5, 5], [4, 2], [2, 3]]


# Create natural obstacles, e.g the boarders of the chess table
obst_w = [r_q, 0]
obst_e = [r_q, n+ 1]
obst_n = [n + 1, c_q]
obst_s = [0, c_q]

if r_q + c_q <= n + 1:
    obst_nw = [r_q + c_q, 0]
    obst_se = [0, c_q + r_q]
else:
    obst_nw = [n + 1, c_q - (n + 1 - r_q)]
    obst_se = [r_q - (n + 1 - c_q), n + 1]

if r_q - c_q >= 0:
    obst_sw = [r_q - c_q, 0]
    obst_ne = [n + 1, c_q + (n + 1 - r_q)]
else:
    obst_sw = [0, c_q - r_q]
    obst_ne = [r_q + (n + 1 - c_q), n + 1]

# Evaluate each obstacle, determining if they cross the paths of the queen
# If they do and they are the closest to the queen position for each of the 8 directions, store them
for obstacle in obstacles:
    # W condition
    if obstacle[0] == r_q and c_q > obstacle[1] > obst_w[1]:
        obst_w = obstacle
    # E condition
    elif obstacle[0] == r_q and c_q < obstacle[1] < obst_e[1]:
        obst_e = obstacle
    # N condition
    elif obstacle[1] == c_q and r_q < obstacle[0] < obst_n[0]:
        obst_n = obstacle
    # S condition
    elif obstacle[1] == c_q and r_q > obstacle[0] > obst_s[0]:
        obst_s = obstacle
    # NW condition
    elif obstacle[1] < c_q and obstacle[0] > r_q and (abs(c_q - obstacle[1]) == abs(r_q - obstacle[0])) and \
            obstacle[0] < obst_nw[0]:
        obst_nw = obstacle
    # SW condition
    elif obstacle[1] < c_q and obstacle[0] < r_q and (abs(c_q - obstacle[1]) == abs(r_q - obstacle[0])) and \
            obstacle[0] > obst_sw[0]:
        obst_sw = obstacle
    # SE condition
    elif obstacle[1] > c_q and obstacle[0] < r_q and (abs(c_q - obstacle[1]) == abs(r_q - obstacle[0])) and \
            obstacle[0] > obst_se[0]:
        obst_se = obstacle
    # NE condition
    elif obstacle[1] > c_q and obstacle[0] > r_q and (abs(c_q - obstacle[1]) == abs(r_q - obstacle[0])) and \
            obstacle[0] < obst_ne[0]:
        obst_ne = obstacle

print(obst_n)
print(obst_nw)
print(obst_w)
print(obst_sw)
print(obst_s)
print(obst_se)
print(obst_e)
print(obst_ne)

# Calculate the distances for each direction:
# spaces = N+NW+W+SW+S+SE+E+NE
spaces = (obst_n[0] - r_q) + (obst_nw[0] - r_q) + (c_q - obst_w[1]) + (r_q - obst_sw[0]) + (r_q - obst_s[0]) + (
            r_q - obst_se[0]) + (obst_e[1] - c_q) + (obst_ne[0] - r_q) - 8

print(spaces)

