import pgzrun
from pgzero import clock
from pgzhelper import *
import random 
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
nightfilter = Actor("night_filter")
bg = Actor("bg")
bg_over = Actor("gover", (250,100))
grass_corner_l = Actor("tile_0017") #2
grass = Actor("tile_0018") #1
grass_corner_r = Actor("tile_0019") # 5
grass_dirt_l = Actor("tile_0021") #6
grass_dirt = Actor("tile_0022")#7
grass_dirt_r = Actor("tile_0023")#8
dirt = Actor("tile_0122") #-1
dirt_corner_l = Actor("tile_0121") #3
dirt_corner_r = Actor("tile_0123") #4
right_sign = Actor("tile_0085")#9
plat_l = Actor("tile_0048")#10
plat = Actor("tile_0049")#11
plat_r = Actor("tile_0050")#12
grass_plat = Actor("tile_0078")#13
grass_plat_l = Actor("tile_0077")#14
grass_plat_r = Actor("tile_0079")#15
plant1 = Actor("tile_0127")#16
tree = Actor("tile_0126")#17
plant2 = Actor("tile_0125")#18
plant3 = Actor("tile_0124")#19
mushplat = Actor("tile_0013")#20
mushplat_l = Actor("tile_0014")#21
mushplat_r = Actor("tile_0015")#22
mush_plat2 = Actor("tile_0012")#23
mush_base = Actor("tile_0052")#24
grass_2 = Actor("tile_0038")#25
grass_2r = Actor("tile_0039")#26
grass_2l = Actor("tile_0037")#27
door_cl = Actor("door_cl", (70, 120))
door1 = Actor("door_op", (90, 155))
door2 = Actor("door_op", (470, 155))
door3 = Actor("door_op", (230, 45))
char = Actor("char_st", (200, 265))
npc = Actor("city-npc_st2", (500, 260))
npc_txt = Actor("npc_text", (400, 90))
ex_sign = Actor("ex_sign", (498, 215 ))
diamond = Actor("tile_0067", (66, 27))
diamond_txt = Actor("tile_0067")
wrench = Actor("wrench", (82, 305))
wrench2 = Actor("wrench", (20, 25))
wrench3 = Actor("wrench", (30, 215))
wrench_txt = Actor("wrench")
char.hp = 10
char.atk = 20
heart1 = Actor("tile_0044", (10, 10))
heart2 = Actor("tile_0044", (30, 10))
heart3 = Actor("tile_0044", (50, 10))
heart4 = Actor("tile_0044", (70, 10))
heart5 = Actor("tile_0044", (90, 10))
char_txt = Actor("char_txt", (400, 100))
my_house1 = Actor("door_animation1", (75, 230))
my_house2 = Actor("window_animation1", (74, 230))
house1 = Actor("house1", (64, 153))
house1.hp = 0
house2 = Actor("house2", (234, 195))
house2.hp = 0
house3 = Actor("house3", (410, 168))
house3.hp = 0
jumper = Actor("tile_0108")
key1 = Actor("tile_0027", (235, 35))
sign = Actor("tile_0086", (480, 228))
sign_txt = Actor("tile_00862", (400,100))
#rope sprite = "tile_0089"
#box sprite = "tile_0029"
lever = Actor("tile_0066", (25, 138))
text_box = Actor("text_box", (280, 250))
text_box2 = Actor("text_box2", (400,100))
enter_b = Actor("enter", (430, 270))
s_button = Actor("s_button", (500, 300))
yes_b = Actor("yes_b_50", (200, 300))
no_b = Actor("no_b", (300, 300))
lock = Actor("tile_0028", (280, 243))
b_press = Actor("tile_0148", (530, 45))
plane = Actor("plane", (600, 30))
boulder = Actor("boulder", (680, 175))
bird = Actor("bird2", (700, -100))
start = Actor("start", (270, 230))
tree1 = Actor("tree1", (100, 122))
tree2 = Actor("tree2", (400, 139))
#pressed = "tile_0149"
size_w = 30
size_h = 20
WIDTH = grass.width * size_w
HEIGHT = grass.height * size_h
TITLE = "City's Rebuild"
FPS = 60
jump_speed = 0
gravity = 1
jump = 0
right = 0
img = 0
house_showagain = "yes"
key_repeat = "yes"
mode = -2 #-1 GO #1 #2 #3 #4 #5 #6 #7 #8 #9 #10 #11 #12 #13 = text
level = 0
anim = 0
old_x = 0
old_y = 0
touch = 0
key = 0
bg_img = 0
k1follow = 0
d1follow = 0
w1follow = 0
open_d1 = 0
read_txt = 0
lever_on1 = 0
wrench3_draw = 0
move_rope = 0
move_rope2 = 0
night_filter = 0
platform_draw = 0
ladder1 = 0
repair = 0
move_box2 = 0
move_chain2 = 0
raindrop_list = []
sparkle_list = []
rope_list1 = []
rope_list2= []
box_list1= []
smoke_list1 = []
smoke_list2 = []
smoke_list3 = []
clouds_list = []
platform_list1 = []
ladder_list = []
box_list2 = []
chain_list1 = []
grenade_list = []
arrow_list = []
sign_show1 = 1
gren1 = 0
gren2 = 0
gren3 = 0
gren4 = 0
col1 = 0
txt_repeat = 0



x = 520
y = 10

x1 = 30
y1 = 45
x2 = 35
y2 = 27
x3 = 35
y3 = 9
x4 = 48
y4 = 48
x5 = 118
y5 = 224
x6 = 513
y6 = 10
x7 = 48
y7 = -80
space_playing = 0
music.set_volume(0.2)
music.play("uptown dancing")

for i in range(8):
    ladder = Actor("tile_0071", (x4, y4))
    if i == 0:
        ladder.image = "tile_0051"
    if i == 7:
        ladder.image = "tile_00512"
    y4 +=18
    ladder_list.append(ladder)

for i in range(3):
  
    platform = Actor("tile_0009", (x1, y1))
    platform_list1.append(platform)
    x1 += 18
for i in range(2):
   
    chain = Actor("tile_0131", (x2, y2))
    x2 += 36
    platform_list1.append(chain)

for i in range(2):

    chain = Actor("tile_0131", (x3, y3))

    x3 += 36
    platform_list1.append(chain)


for i in range(40):
    raindrop = Actor("raindrop", (random.randint(0, 540), random.randint(-700, 0)))
    raindrop_list.append(raindrop)

    
for i in range(12):
    cloud_x = random.randint(600, 1200)
    cloud_y = random.randint(10, 200)
    
    cloud_img = random.randint(1, 5)
    
    cloud = Actor("cloud1", (cloud_x, cloud_y))
    
    if cloud_img == 2:
        cloud.image = "cloud2"
    elif cloud_img == 3:
        cloud.image = "cloud3"
    elif cloud_img == 4:
        cloud.image = "cloud4"
    elif cloud_img == 5:
        cloud.image = "cloud5"
    clouds_list.append(cloud)
    
    
    
    
for i in range(10):
    
    rope = Actor("tile_0089", (x, y))
    rope_list1.append(rope)
    y += 18
    
for i in range(3):
    
    box = Actor("tile_0029", (x, y))
    box_list1.append(box)
    y +=18
    
    
for i in range(10):
    smoke = Actor("smoke", (random.randint(20,130), random.randint(50, 265)))   
    smoke_list1.append(smoke)
    
    
for i in range(10):
    
    smoke = Actor("smoke", (random.randint(170,270), random.randint(50, 265)))
    smoke_list2.append(smoke)
    
for i in range(10):
    
    smoke = Actor("smoke", (random.randint(350,440), random.randint(50, 265)))
    smoke_list3.append(smoke)

    
for i in range(3):
    box = Actor("tile_0029", (x5, y5))
    rope_list2.append(box)
    y5 += 18
for i in range(10):
    rope = Actor("tile_0089", (x5, y5))
    rope_list2.append(rope)
    y5 += 18
for i in range(3):
    box = Actor("tile_0029", (x6, y6))
    box_list2.append(box)
    y6 += 18

for i in range(8):
    chain = Actor("tile_0131", (x7, y7))
    chain_list1.append(chain)
    y7 += 18
for i in range(4):
    grenade = Actor("grenade", (random.randint(20, 530), 0))
    grenade_list.append(grenade)
for i in range(2):
    arrow = Actor("arrow", (-40, random.randint(20, 530)))
    arrow_list.append(arrow)

    
    
    
world1_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,19 ,18 ,19 ,16 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ,7 ,7 ,7 ,7 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 ,-1 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 17, 18, 0 ,18 ,0 ,19 ,0 ,17 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 ,-1 ],
              [6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7 ,7 ,7 ,7 ,7 ,7 ,8 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 ,-1 ],
              [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ,-1 ,-1 ,-1 ,-1 ,-1 ,4 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 , -1 ],
              [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ,-1 ,-1 ,-1 ,-1 ,-1 ,4 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 , -1 ],
              [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ,-1 ,-1 ,-1 ,-1 ,-1 ,4 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 , -1 ]]
              

world2_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 18, 0 ,0 ,19 ,0 ,16 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 13, 13, 13 ,13 ,13 ,13 ,15 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [11, 11, 11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [11, 11, 11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 16, 9, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,16 ,0 ,18 ,0 ,19 ],
              [7, 7, 7, 7, 7, 8, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ,7 ,7 ,7 ,7 ],
              [-1, -1, -1, -1, -1, 4, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 ,-1 ],
              [-1, -1, -1, -1, -1, 4, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 ,-1 ],
              [-1, -1, -1, -1, -1, 4, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 ,-1 ],
              [-1, -1, -1, -1, -1, 4, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 , -1 ],
              [-1, -1, -1, -1, -1, 4, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 , -1 ],
              [-1, -1, -1, -1, -1, 4, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,-1 ,-1 ,-1 , -1 ]]
              
world3_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 17, 18, 0 ,18 ,0 ,19 ,0 ,17 ,0 ,0 ,17 ,0 ,0 ,19 ,0 ,17 ,0 ,18 ,18 ,0 ],
              [6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ],
              [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 , -1 ],
              [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 , -1 ],
              [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 , -1 ]]


world4_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 20, 20 ,20 ,20 ,22 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 10, 11, 11, 11, 11, 12, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,14 ,13 ,13 ,13 ,13 ,15 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 ],
              [0, 19, 17, 0, 18, 19, 0, 0, 19, 0, 17, 18, 0 ,18 ,0 ,19 ,0 ,17 ,0 ,0 ,17 ,0 ,0 ,19 ,0 ,17 ,0 ,18 ,18 ,0 ],
              [6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ],
              [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 , -1 ],
              [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 , -1 ],
              [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 , -1 ]]
              
              
world5_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,21 ,20 ,20 ,20 ,23 ,20 ,20 ,20 ,20 ,22 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [21, 20, 20, 23, 20, 20, 22, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 21 ,20 ,23 ,20 ,22 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 24, 23, 22, 0, 0, 0, 0, 0, 0, 0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 24, 24, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,24 ,0 ,0 ,0 ,0 ,0 ]]


world6_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [11, 11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,10 ,11 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 10, 11, 12, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,10 ,11 ,12 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,10 ,12 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 10, 11, 11, 12, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,10 ,11 ,11 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,10 ,11 ,12 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,10 ,12 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]]


world7_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,5 ,0 ,0 ,2 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ],
              [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25 ,25 ,26 ,0 ,0 ,27 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ],
              [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25 ,25 ,26 ,0 ,0 ,27 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ],
              [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25 ,25 ,26 ,0 ,0 ,27 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ],
              [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25 ,25 ,25 ,1 ,1 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ],
              [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ],
              [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ,25 ]]




def draw_level():
    if level == 0:
        for i in range(len(world1_map)):
            for j in range(len(world1_map[0])):
                if world1_map[i][j] == 1:
                    grass.left = grass.width * j
                    grass.top = grass.height * i
                    grass.draw()
                if world1_map[i][j] == -1:
                    dirt.left = dirt.width * j
                    dirt.top = dirt.height * i
                    dirt.draw()
                if world1_map[i][j] == 2:
                    grass_corner_l.left = grass_corner_l.width * j
                    grass_corner_l.top = grass_corner_l.height * i
                    grass_corner_l.draw()
                if world1_map[i][j] == 3:
                    dirt_corner_l.left = dirt_corner_l.width * j
                    dirt_corner_l.top = dirt_corner_l.height * i
                    dirt_corner_l.draw()
                if world1_map[i][j] == 4:
                    dirt_corner_r.left = dirt_corner_r.width * j
                    dirt_corner_r.top = dirt_corner_r.height * i
                    dirt_corner_r.draw()
                if world1_map[i][j] == 5:
                    grass_corner_r.left = grass_corner_r.width * j
                    grass_corner_r.top = grass_corner_r.height * i
                    grass_corner_r.draw()
                if world1_map[i][j] == 6:
                    grass_dirt_l.left = grass_dirt_l.width * j
                    grass_dirt_l.top = grass_dirt_l.height * i
                    grass_dirt_l.draw()
                if world1_map[i][j] == 7:
                    grass_dirt.left = grass_dirt.width * j
                    grass_dirt.top = grass_dirt.height * i
                    grass_dirt.draw()
                if world1_map[i][j] == 8:
                    grass_dirt_r.left = grass_dirt_r.width * j
                    grass_dirt_r.top = grass_dirt_r.height * i
                    grass_dirt_r.draw()
                if world1_map[i][j] == 9:
                    right_sign.left = grass_dirt_r.width * j
                    right_sign.top = grass_dirt_r.height * i
                    right_sign.draw()
                if world1_map[i][j] == 10:
                    plat_l.left = grass_dirt_r.width * j
                    plat_l.top = grass_dirt_r.height * i
                    plat_l.draw()
                if world1_map[i][j] == 11:
                    plat.left = grass_dirt_r.width * j
                    plat.top = grass_dirt_r.height * i
                    plat.draw()
                if world1_map[i][j] == 12:
                    plat_r.left = grass_dirt_r.width * j
                    plat_r.top = grass_dirt_r.height * i
                    plat_r.draw()
                if world1_map[i][j] == 13:
                    grass_plat.left = grass_dirt_r.width * j
                    grass_plat.top = grass_dirt_r.height * i
                    grass_plat.draw()
                if world1_map[i][j] == 14:
                    grass_plat_l.left = grass_dirt_r.width * j
                    grass_plat_l.top = grass_dirt_r.height * i
                    grass_plat_l.draw()
                if world1_map[i][j] == 15:
                    grass_plat_r.left = grass_dirt_r.width * j
                    grass_plat_r.top = grass_dirt_r.height * i
                    grass_plat_r.draw()
                if world1_map[i][j] == 16:
                    plant1.left = grass_dirt_r.width * j
                    plant1.top = grass_dirt_r.height * i
                    plant1.draw()
                if world1_map[i][j] == 17:
                    tree.left = grass_dirt_r.width * j
                    tree.top = grass_dirt_r.height * i
                    tree.draw()
                if world1_map[i][j] == 18:
                    plant2.left = grass_dirt_r.width * j
                    plant2.top = grass_dirt_r.height * i
                    plant2.draw()
                if world1_map[i][j] == 19:
                    plant3.left = grass_dirt_r.width * j
                    plant3.top = grass_dirt_r.height * i
                    plant3.draw()
                if world1_map[i][j] == 20:
                    mushplat.left = grass_dirt_r.width * j
                    mushplat.top = grass_dirt_r.height * i
                    mushplat.draw()
                if world1_map[i][j] == 21:
                    mushplat_l.left = grass_dirt_r.width * j
                    mushplat_l.top = grass_dirt_r.height * i
                    mushplat_l.draw()
                if world1_map[i][j] == 22:
                    mushplat_r.left = grass_dirt_r.width * j
                    mushplat_r.top = grass_dirt_r.height * i
                    mushplat_r.draw()
                if world1_map[i][j] == 23:
                    mush_plat2.left = grass_dirt_r.width * j
                    mush_plat2.top = grass_dirt_r.height * i
                    mush_plat2.draw()
                if world1_map[i][j] == 24:
                    mush_base.left = grass_dirt_r.width * j
                    mush_base.top = grass_dirt_r.height * i
                    mush_base.draw()
                if world1_map[i][j] == 25:
                    grass_2.left = grass_dirt_r.width * j
                    grass_2.top = grass_dirt_r.height * i
                    grass_2.draw()
                if world1_map[i][j] == 26:
                    grass_2r.left = grass_dirt_r.width * j
                    grass_2r.top = grass_dirt_r.height * i
                    grass_2r.draw()
                if world1_map[i][j] == 27:
                    grass_2l.left = grass_dirt_r.width * j
                    grass_2l.top = grass_dirt_r.height * i
                    grass_2l.draw()
    
    elif level == 1:
        for i in range(len(world2_map)):
            for j in range(len(world2_map[0])):
                if world2_map[i][j] == 1:
                    grass.left = grass.width * j
                    grass.top = grass.height * i
                    grass.draw()
                if world2_map[i][j] == -1:
                    dirt.left = dirt.width * j
                    dirt.top = dirt.height * i
                    dirt.draw()
                if world2_map[i][j] == 2:
                    grass_corner_l.left = grass_corner_l.width * j
                    grass_corner_l.top = grass_corner_l.height * i
                    grass_corner_l.draw()
                if world2_map[i][j] == 3:
                    dirt_corner_l.left = dirt_corner_l.width * j
                    dirt_corner_l.top = dirt_corner_l.height * i
                    dirt_corner_l.draw()
                if world2_map[i][j] == 4:
                    dirt_corner_r.left = dirt_corner_r.width * j
                    dirt_corner_r.top = dirt_corner_r.height * i
                    dirt_corner_r.draw()
                if world2_map[i][j] == 5:
                    grass_corner_r.left = grass_corner_r.width * j
                    grass_corner_r.top = grass_corner_r.height * i
                    grass_corner_r.draw()
                if world2_map[i][j] == 6:
                    grass_dirt_l.left = grass_dirt_l.width * j
                    grass_dirt_l.top = grass_dirt_l.height * i
                    grass_dirt_l.draw()
                if world2_map[i][j] == 7:
                    grass_dirt.left = grass_dirt.width * j
                    grass_dirt.top = grass_dirt.height * i
                    grass_dirt.draw()
                if world2_map[i][j] == 8:
                    grass_dirt_r.left = grass_dirt_r.width * j
                    grass_dirt_r.top = grass_dirt_r.height * i
                    grass_dirt_r.draw()
                if world2_map[i][j] == 9:
                    right_sign.left = grass_dirt_r.width * j
                    right_sign.top = grass_dirt_r.height * i
                    right_sign.draw()
                if world2_map[i][j] == 10:
                    plat_l.left = grass_dirt_r.width * j
                    plat_l.top = grass_dirt_r.height * i
                    plat_l.draw()
                if world2_map[i][j] == 11:
                    plat.left = grass_dirt_r.width * j
                    plat.top = grass_dirt_r.height * i
                    plat.draw()
                if world2_map[i][j] == 12:
                    plat_r.left = grass_dirt_r.width * j
                    plat_r.top = grass_dirt_r.height * i
                    plat_r.draw()
                if world2_map[i][j] == 13:
                    grass_plat.left = grass_dirt_r.width * j
                    grass_plat.top = grass_dirt_r.height * i
                    grass_plat.draw()
                if world2_map[i][j] == 14:
                    grass_plat_l.left = grass_dirt_r.width * j
                    grass_plat_l.top = grass_dirt_r.height * i
                    grass_plat_l.draw()
                if world2_map[i][j] == 15:
                    grass_plat_r.left = grass_dirt_r.width * j
                    grass_plat_r.top = grass_dirt_r.height * i
                    grass_plat_r.draw()
                if world2_map[i][j] == 16:
                    plant1.left = grass_dirt_r.width * j
                    plant1.top = grass_dirt_r.height * i
                    plant1.draw()
                if world2_map[i][j] == 17:
                    tree.left = grass_dirt_r.width * j
                    tree.top = grass_dirt_r.height * i
                    tree.draw()
                if world2_map[i][j] == 18:
                    plant2.left = grass_dirt_r.width * j
                    plant2.top = grass_dirt_r.height * i
                    plant2.draw()
                if world2_map[i][j] == 19:
                    plant3.left = grass_dirt_r.width * j
                    plant3.top = grass_dirt_r.height * i
                    plant3.draw()
                if world2_map[i][j] == 20:
                    mushplat.left = grass_dirt_r.width * j
                    mushplat.top = grass_dirt_r.height * i
                    mushplat.draw()
                if world2_map[i][j] == 21:
                    mushplat_l.left = grass_dirt_r.width * j
                    mushplat_l.top = grass_dirt_r.height * i
                    mushplat_l.draw()
                if world2_map[i][j] == 22:
                    mushplat_r.left = grass_dirt_r.width * j
                    mushplat_r.top = grass_dirt_r.height * i
                    mushplat_r.draw()
                if world2_map[i][j] == 23:
                    mush_plat2.left = grass_dirt_r.width * j
                    mush_plat2.top = grass_dirt_r.height * i
                    mush_plat2.draw()
                if world2_map[i][j] == 24:
                    mush_base.left = grass_dirt_r.width * j
                    mush_base.top = grass_dirt_r.height * i
                    mush_base.draw()
                if world2_map[i][j] == 25:
                    grass_2.left = grass_dirt_r.width * j
                    grass_2.top = grass_dirt_r.height * i
                    grass_2.draw()
                if world2_map[i][j] == 26:
                    grass_2r.left = grass_dirt_r.width * j
                    grass_2r.top = grass_dirt_r.height * i
                    grass_2r.draw()
                if world2_map[i][j] == 27:
                    grass_2l.left = grass_dirt_r.width * j
                    grass_2l.top = grass_dirt_r.height * i
                    grass_2l.draw()
                
    elif level == 2:
        for i in range(len(world3_map)):
            for j in range(len(world3_map[0])):
                if world3_map[i][j] == 1:
                    grass.left = grass.width * j
                    grass.top = grass.height * i
                    grass.draw()
                if world3_map[i][j] == -1:
                    dirt.left = dirt.width * j
                    dirt.top = dirt.height * i
                    dirt.draw()
                if world3_map[i][j] == 2:
                    grass_corner_l.left = grass_corner_l.width * j
                    grass_corner_l.top = grass_corner_l.height * i
                    grass_corner_l.draw()
                if world3_map[i][j] == 3:
                    dirt_corner_l.left = dirt_corner_l.width * j
                    dirt_corner_l.top = dirt_corner_l.height * i
                    dirt_corner_l.draw()
                if world3_map[i][j] == 4:
                    dirt_corner_r.left = dirt_corner_r.width * j
                    dirt_corner_r.top = dirt_corner_r.height * i
                    dirt_corner_r.draw()
                if world3_map[i][j] == 5:
                    grass_corner_r.left = grass_corner_r.width * j
                    grass_corner_r.top = grass_corner_r.height * i
                    grass_corner_r.draw()
                if world3_map[i][j] == 6:
                    grass_dirt_l.left = grass_dirt_l.width * j
                    grass_dirt_l.top = grass_dirt_l.height * i
                    grass_dirt_l.draw()
                if world3_map[i][j] == 7:
                    grass_dirt.left = grass_dirt.width * j
                    grass_dirt.top = grass_dirt.height * i
                    grass_dirt.draw()
                if world3_map[i][j] == 8:
                    grass_dirt_r.left = grass_dirt_r.width * j
                    grass_dirt_r.top = grass_dirt_r.height * i
                    grass_dirt_r.draw()
                if world3_map[i][j] == 9:
                    right_sign.left = grass_dirt_r.width * j
                    right_sign.top = grass_dirt_r.height * i
                    right_sign.draw()
                if world3_map[i][j] == 10:
                    plat_l.left = grass_dirt_r.width * j
                    plat_l.top = grass_dirt_r.height * i
                    plat_l.draw()
                if world3_map[i][j] == 11:
                    plat.left = grass_dirt_r.width * j
                    plat.top = grass_dirt_r.height * i
                    plat.draw()
                if world3_map[i][j] == 12:
                    plat_r.left = grass_dirt_r.width * j
                    plat_r.top = grass_dirt_r.height * i
                    plat_r.draw()
                if world3_map[i][j] == 13:
                    grass_plat.left = grass_dirt_r.width * j
                    grass_plat.top = grass_dirt_r.height * i
                    grass_plat.draw()
                if world3_map[i][j] == 14:
                    grass_plat_l.left = grass_dirt_r.width * j
                    grass_plat_l.top = grass_dirt_r.height * i
                    grass_plat_l.draw()
                if world3_map[i][j] == 15:
                    grass_plat_r.left = grass_dirt_r.width * j
                    grass_plat_r.top = grass_dirt_r.height * i
                    grass_plat_r.draw()
                if world3_map[i][j] == 16:
                    plant1.left = grass_dirt_r.width * j
                    plant1.top = grass_dirt_r.height * i
                    plant1.draw()
                if world3_map[i][j] == 17:
                    tree.left = grass_dirt_r.width * j
                    tree.top = grass_dirt_r.height * i
                    tree.draw()
                if world3_map[i][j] == 18:
                    plant2.left = grass_dirt_r.width * j
                    plant2.top = grass_dirt_r.height * i
                    plant2.draw()
                if world3_map[i][j] == 19:
                    plant3.left = grass_dirt_r.width * j
                    plant3.top = grass_dirt_r.height * i
                    plant3.draw()
                if world3_map[i][j] == 20:
                    mushplat.left = grass_dirt_r.width * j
                    mushplat.top = grass_dirt_r.height * i
                    mushplat.draw()
                if world3_map[i][j] == 21:
                    mushplat_l.left = grass_dirt_r.width * j
                    mushplat_l.top = grass_dirt_r.height * i
                    mushplat_l.draw()
                if world3_map[i][j] == 22:
                    mushplat_r.left = grass_dirt_r.width * j
                    mushplat_r.top = grass_dirt_r.height * i
                    mushplat_r.draw()
                if world3_map[i][j] == 23:
                    mush_plat2.left = grass_dirt_r.width * j
                    mush_plat2.top = grass_dirt_r.height * i
                    mush_plat2.draw()
                if world3_map[i][j] == 24:
                    mush_base.left = grass_dirt_r.width * j
                    mush_base.top = grass_dirt_r.height * i
                    mush_base.draw()
                if world3_map[i][j] == 25:
                    grass_2.left = grass_dirt_r.width * j
                    grass_2.top = grass_dirt_r.height * i
                    grass_2.draw()
                if world3_map[i][j] == 26:
                    grass_2r.left = grass_dirt_r.width * j
                    grass_2r.top = grass_dirt_r.height * i
                    grass_2r.draw()
                if world3_map[i][j] == 27:
                    grass_2l.left = grass_dirt_r.width * j
                    grass_2l.top = grass_dirt_r.height * i
                    grass_2l.draw()
    elif level == 3:
        for i in range(len(world4_map)):
            for j in range(len(world4_map[0])):
                if world4_map[i][j] == 1:
                    grass.left = grass.width * j
                    grass.top = grass.height * i
                    grass.draw()
                if world4_map[i][j] == -1:
                    dirt.left = dirt.width * j
                    dirt.top = dirt.height * i
                    dirt.draw()
                if world4_map[i][j] == 2:
                    grass_corner_l.left = grass_corner_l.width * j
                    grass_corner_l.top = grass_corner_l.height * i
                    grass_corner_l.draw()
                if world4_map[i][j] == 3:
                    dirt_corner_l.left = dirt_corner_l.width * j
                    dirt_corner_l.top = dirt_corner_l.height * i
                    dirt_corner_l.draw()
                if world4_map[i][j] == 4:
                    dirt_corner_r.left = dirt_corner_r.width * j
                    dirt_corner_r.top = dirt_corner_r.height * i
                    dirt_corner_r.draw()
                if world4_map[i][j] == 5:
                    grass_corner_r.left = grass_corner_r.width * j
                    grass_corner_r.top = grass_corner_r.height * i
                    grass_corner_r.draw()
                if world4_map[i][j] == 6:
                    grass_dirt_l.left = grass_dirt_l.width * j
                    grass_dirt_l.top = grass_dirt_l.height * i
                    grass_dirt_l.draw()
                if world4_map[i][j] == 7:
                    grass_dirt.left = grass_dirt.width * j
                    grass_dirt.top = grass_dirt.height * i
                    grass_dirt.draw()
                if world4_map[i][j] == 8:
                    grass_dirt_r.left = grass_dirt_r.width * j
                    grass_dirt_r.top = grass_dirt_r.height * i
                    grass_dirt_r.draw()
                if world4_map[i][j] == 9:
                    right_sign.left = grass_dirt_r.width * j
                    right_sign.top = grass_dirt_r.height * i
                    right_sign.draw()
                if world4_map[i][j] == 10:
                    plat_l.left = grass_dirt_r.width * j
                    plat_l.top = grass_dirt_r.height * i
                    plat_l.draw()
                if world4_map[i][j] == 11:
                    plat.left = grass_dirt_r.width * j
                    plat.top = grass_dirt_r.height * i
                    plat.draw()
                if world4_map[i][j] == 12:
                    plat_r.left = grass_dirt_r.width * j
                    plat_r.top = grass_dirt_r.height * i
                    plat_r.draw()
                if world4_map[i][j] == 13:
                    grass_plat.left = grass_dirt_r.width * j
                    grass_plat.top = grass_dirt_r.height * i
                    grass_plat.draw()
                if world4_map[i][j] == 14:
                    grass_plat_l.left = grass_dirt_r.width * j
                    grass_plat_l.top = grass_dirt_r.height * i
                    grass_plat_l.draw()
                if world4_map[i][j] == 15:
                    grass_plat_r.left = grass_dirt_r.width * j
                    grass_plat_r.top = grass_dirt_r.height * i
                    grass_plat_r.draw()
                if world4_map[i][j] == 16:
                    plant1.left = grass_dirt_r.width * j
                    plant1.top = grass_dirt_r.height * i
                    plant1.draw()
                if world4_map[i][j] == 17:
                    tree.left = grass_dirt_r.width * j
                    tree.top = grass_dirt_r.height * i
                    tree.draw()
                if world4_map[i][j] == 18:
                    plant2.left = grass_dirt_r.width * j
                    plant2.top = grass_dirt_r.height * i
                    plant2.draw()
                if world4_map[i][j] == 19:
                    plant3.left = grass_dirt_r.width * j
                    plant3.top = grass_dirt_r.height * i
                    plant3.draw()
                if world4_map[i][j] == 20:
                    mushplat.left = grass_dirt_r.width * j
                    mushplat.top = grass_dirt_r.height * i
                    mushplat.draw()
                if world4_map[i][j] == 21:
                    mushplat_l.left = grass_dirt_r.width * j
                    mushplat_l.top = grass_dirt_r.height * i
                    mushplat_l.draw()
                if world4_map[i][j] == 22:
                    mushplat_r.left = grass_dirt_r.width * j
                    mushplat_r.top = grass_dirt_r.height * i
                    mushplat_r.draw()
                if world4_map[i][j] == 23:
                    mush_plat2.left = grass_dirt_r.width * j
                    mush_plat2.top = grass_dirt_r.height * i
                    mush_plat2.draw()
                if world4_map[i][j] == 24:
                    mush_base.left = grass_dirt_r.width * j
                    mush_base.top = grass_dirt_r.height * i
                    mush_base.draw()
                if world4_map[i][j] == 25:
                    grass_2.left = grass_dirt_r.width * j
                    grass_2.top = grass_dirt_r.height * i
                    grass_2.draw()
                if world4_map[i][j] == 26:
                    grass_2r.left = grass_dirt_r.width * j
                    grass_2r.top = grass_dirt_r.height * i
                    grass_2r.draw()
                if world4_map[i][j] == 27:
                    grass_2l.left = grass_dirt_r.width * j
                    grass_2l.top = grass_dirt_r.height * i
                    grass_2l.draw()

    elif level == 4:
        for i in range(len(world5_map)):
            for j in range(len(world5_map[0])):
                if world5_map[i][j] == 1:
                    grass.left = grass.width * j
                    grass.top = grass.height * i
                    grass.draw()
                if world5_map[i][j] == -1:
                    dirt.left = dirt.width * j
                    dirt.top = dirt.height * i
                    dirt.draw()
                if world5_map[i][j] == 2:
                    grass_corner_l.left = grass_corner_l.width * j
                    grass_corner_l.top = grass_corner_l.height * i
                    grass_corner_l.draw()
                if world5_map[i][j] == 3:
                    dirt_corner_l.left = dirt_corner_l.width * j
                    dirt_corner_l.top = dirt_corner_l.height * i
                    dirt_corner_l.draw()
                if world5_map[i][j] == 4:
                    dirt_corner_r.left = dirt_corner_r.width * j
                    dirt_corner_r.top = dirt_corner_r.height * i
                    dirt_corner_r.draw()
                if world5_map[i][j] == 5:
                    grass_corner_r.left = grass_corner_r.width * j
                    grass_corner_r.top = grass_corner_r.height * i
                    grass_corner_r.draw()
                if world5_map[i][j] == 6:
                    grass_dirt_l.left = grass_dirt_l.width * j
                    grass_dirt_l.top = grass_dirt_l.height * i
                    grass_dirt_l.draw()
                if world5_map[i][j] == 7:
                    grass_dirt.left = grass_dirt.width * j
                    grass_dirt.top = grass_dirt.height * i
                    grass_dirt.draw()
                if world5_map[i][j] == 8:
                    grass_dirt_r.left = grass_dirt_r.width * j
                    grass_dirt_r.top = grass_dirt_r.height * i
                    grass_dirt_r.draw()
                if world5_map[i][j] == 9:
                    right_sign.left = grass_dirt_r.width * j
                    right_sign.top = grass_dirt_r.height * i
                    right_sign.draw()
                if world5_map[i][j] == 10:
                    plat_l.left = grass_dirt_r.width * j
                    plat_l.top = grass_dirt_r.height * i
                    plat_l.draw()
                if world5_map[i][j] == 11:
                    plat.left = grass_dirt_r.width * j
                    plat.top = grass_dirt_r.height * i
                    plat.draw()
                if world5_map[i][j] == 12:
                    plat_r.left = grass_dirt_r.width * j
                    plat_r.top = grass_dirt_r.height * i
                    plat_r.draw()
                if world5_map[i][j] == 13:
                    grass_plat.left = grass_dirt_r.width * j
                    grass_plat.top = grass_dirt_r.height * i
                    grass_plat.draw()
                if world5_map[i][j] == 14:
                    grass_plat_l.left = grass_dirt_r.width * j
                    grass_plat_l.top = grass_dirt_r.height * i
                    grass_plat_l.draw()
                if world5_map[i][j] == 15:
                    grass_plat_r.left = grass_dirt_r.width * j
                    grass_plat_r.top = grass_dirt_r.height * i
                    grass_plat_r.draw()
                if world5_map[i][j] == 16:
                    plant1.left = grass_dirt_r.width * j
                    plant1.top = grass_dirt_r.height * i
                    plant1.draw()
                if world5_map[i][j] == 17:
                    tree.left = grass_dirt_r.width * j
                    tree.top = grass_dirt_r.height * i
                    tree.draw()
                if world5_map[i][j] == 18:
                    plant2.left = grass_dirt_r.width * j
                    plant2.top = grass_dirt_r.height * i
                    plant2.draw()
                if world5_map[i][j] == 19:
                    plant3.left = grass_dirt_r.width * j
                    plant3.top = grass_dirt_r.height * i
                    plant3.draw()
                if world5_map[i][j] == 20:
                    mushplat.left = grass_dirt_r.width * j
                    mushplat.top = grass_dirt_r.height * i
                    mushplat.draw()
                if world5_map[i][j] == 21:
                    mushplat_l.left = grass_dirt_r.width * j
                    mushplat_l.top = grass_dirt_r.height * i
                    mushplat_l.draw()
                if world5_map[i][j] == 22:
                    mushplat_r.left = grass_dirt_r.width * j
                    mushplat_r.top = grass_dirt_r.height * i
                    mushplat_r.draw()
                if world5_map[i][j] == 23:
                    mush_plat2.left = grass_dirt_r.width * j
                    mush_plat2.top = grass_dirt_r.height * i
                    mush_plat2.draw()
                if world5_map[i][j] == 24:
                    mush_base.left = grass_dirt_r.width * j
                    mush_base.top = grass_dirt_r.height * i
                    mush_base.draw()
                if world5_map[i][j] == 25:
                    grass_2.left = grass_dirt_r.width * j
                    grass_2.top = grass_dirt_r.height * i
                    grass_2.draw()
                if world5_map[i][j] == 26:
                    grass_2r.left = grass_dirt_r.width * j
                    grass_2r.top = grass_dirt_r.height * i
                    grass_2r.draw()
                if world5_map[i][j] == 27:
                    grass_2l.left = grass_dirt_r.width * j
                    grass_2l.top = grass_dirt_r.height * i
                    grass_2l.draw()
    elif level == 5:
        for i in range(len(world6_map)):
            for j in range(len(world6_map[0])):
                if world6_map[i][j] == 1:
                    grass.left = grass.width * j
                    grass.top = grass.height * i
                    grass.draw()
                if world6_map[i][j] == -1:
                    dirt.left = dirt.width * j
                    dirt.top = dirt.height * i
                    dirt.draw()
                if world6_map[i][j] == 2:
                    grass_corner_l.left = grass_corner_l.width * j
                    grass_corner_l.top = grass_corner_l.height * i
                    grass_corner_l.draw()
                if world6_map[i][j] == 3:
                    dirt_corner_l.left = dirt_corner_l.width * j
                    dirt_corner_l.top = dirt_corner_l.height * i
                    dirt_corner_l.draw()
                if world6_map[i][j] == 4:
                    dirt_corner_r.left = dirt_corner_r.width * j
                    dirt_corner_r.top = dirt_corner_r.height * i
                    dirt_corner_r.draw()
                if world6_map[i][j] == 5:
                    grass_corner_r.left = grass_corner_r.width * j
                    grass_corner_r.top = grass_corner_r.height * i
                    grass_corner_r.draw()
                if world6_map[i][j] == 6:
                    grass_dirt_l.left = grass_dirt_l.width * j
                    grass_dirt_l.top = grass_dirt_l.height * i
                    grass_dirt_l.draw()
                if world6_map[i][j] == 7:
                    grass_dirt.left = grass_dirt.width * j
                    grass_dirt.top = grass_dirt.height * i
                    grass_dirt.draw()
                if world6_map[i][j] == 8:
                    grass_dirt_r.left = grass_dirt_r.width * j
                    grass_dirt_r.top = grass_dirt_r.height * i
                    grass_dirt_r.draw()
                if world6_map[i][j] == 9:
                    right_sign.left = grass_dirt_r.width * j
                    right_sign.top = grass_dirt_r.height * i
                    right_sign.draw()
                if world6_map[i][j] == 10:
                    plat_l.left = grass_dirt_r.width * j
                    plat_l.top = grass_dirt_r.height * i
                    plat_l.draw()
                if world6_map[i][j] == 11:
                    plat.left = grass_dirt_r.width * j
                    plat.top = grass_dirt_r.height * i
                    plat.draw()
                if world6_map[i][j] == 12:
                    plat_r.left = grass_dirt_r.width * j
                    plat_r.top = grass_dirt_r.height * i
                    plat_r.draw()
                if world6_map[i][j] == 13:
                    grass_plat.left = grass_dirt_r.width * j
                    grass_plat.top = grass_dirt_r.height * i
                    grass_plat.draw()
                if world6_map[i][j] == 14:
                    grass_plat_l.left = grass_dirt_r.width * j
                    grass_plat_l.top = grass_dirt_r.height * i
                    grass_plat_l.draw()
                if world6_map[i][j] == 15:
                    grass_plat_r.left = grass_dirt_r.width * j
                    grass_plat_r.top = grass_dirt_r.height * i
                    grass_plat_r.draw()
                if world6_map[i][j] == 16:
                    plant1.left = grass_dirt_r.width * j
                    plant1.top = grass_dirt_r.height * i
                    plant1.draw()
                if world6_map[i][j] == 17:
                    tree.left = grass_dirt_r.width * j
                    tree.top = grass_dirt_r.height * i
                    tree.draw()
                if world6_map[i][j] == 18:
                    plant2.left = grass_dirt_r.width * j
                    plant2.top = grass_dirt_r.height * i
                    plant2.draw()
                if world6_map[i][j] == 19:
                    plant3.left = grass_dirt_r.width * j
                    plant3.top = grass_dirt_r.height * i
                    plant3.draw()
                if world6_map[i][j] == 20:
                    mushplat.left = grass_dirt_r.width * j
                    mushplat.top = grass_dirt_r.height * i
                    mushplat.draw()
                if world6_map[i][j] == 21:
                    mushplat_l.left = grass_dirt_r.width * j
                    mushplat_l.top = grass_dirt_r.height * i
                    mushplat_l.draw()
                if world6_map[i][j] == 22:
                    mushplat_r.left = grass_dirt_r.width * j
                    mushplat_r.top = grass_dirt_r.height * i
                    mushplat_r.draw()
                if world6_map[i][j] == 23:
                    mush_plat2.left = grass_dirt_r.width * j
                    mush_plat2.top = grass_dirt_r.height * i
                    mush_plat2.draw()
                if world6_map[i][j] == 24:
                    mush_base.left = grass_dirt_r.width * j
                    mush_base.top = grass_dirt_r.height * i
                    mush_base.draw()
                if world6_map[i][j] == 25:
                    grass_2.left = grass_dirt_r.width * j
                    grass_2.top = grass_dirt_r.height * i
                    grass_2.draw()
                if world6_map[i][j] == 26:
                    grass_2r.left = grass_dirt_r.width * j
                    grass_2r.top = grass_dirt_r.height * i
                    grass_2r.draw()
                if world6_map[i][j] == 27:
                    grass_2l.left = grass_dirt_r.width * j
                    grass_2l.top = grass_dirt_r.height * i
                    grass_2l.draw()
    elif level == 6:
        for i in range(len(world6_map)):
            for j in range(len(world6_map[0])):
                if world7_map[i][j] == 1:
                    grass.left = grass.width * j
                    grass.top = grass.height * i
                    grass.draw()
                if world7_map[i][j] == -1:
                    dirt.left = dirt.width * j
                    dirt.top = dirt.height * i
                    dirt.draw()
                if world7_map[i][j] == 2:
                    grass_corner_l.left = grass_corner_l.width * j
                    grass_corner_l.top = grass_corner_l.height * i
                    grass_corner_l.draw()
                if world7_map[i][j] == 3:
                    dirt_corner_l.left = dirt_corner_l.width * j
                    dirt_corner_l.top = dirt_corner_l.height * i
                    dirt_corner_l.draw()
                if world7_map[i][j] == 4:
                    dirt_corner_r.left = dirt_corner_r.width * j
                    dirt_corner_r.top = dirt_corner_r.height * i
                    dirt_corner_r.draw()
                if world7_map[i][j] == 5:
                    grass_corner_r.left = grass_corner_r.width * j
                    grass_corner_r.top = grass_corner_r.height * i
                    grass_corner_r.draw()
                if world7_map[i][j] == 6:
                    grass_dirt_l.left = grass_dirt_l.width * j
                    grass_dirt_l.top = grass_dirt_l.height * i
                    grass_dirt_l.draw()
                if world7_map[i][j] == 7:
                    grass_dirt.left = grass_dirt.width * j
                    grass_dirt.top = grass_dirt.height * i
                    grass_dirt.draw()
                if world7_map[i][j] == 8:
                    grass_dirt_r.left = grass_dirt_r.width * j
                    grass_dirt_r.top = grass_dirt_r.height * i
                    grass_dirt_r.draw()
                if world7_map[i][j] == 9:
                    right_sign.left = grass_dirt_r.width * j
                    right_sign.top = grass_dirt_r.height * i
                    right_sign.draw()
                if world7_map[i][j] == 10:
                    plat_l.left = grass_dirt_r.width * j
                    plat_l.top = grass_dirt_r.height * i
                    plat_l.draw()
                if world7_map[i][j] == 11:
                    plat.left = grass_dirt_r.width * j
                    plat.top = grass_dirt_r.height * i
                    plat.draw()
                if world7_map[i][j] == 12:
                    plat_r.left = grass_dirt_r.width * j
                    plat_r.top = grass_dirt_r.height * i
                    plat_r.draw()
                if world7_map[i][j] == 13:
                    grass_plat.left = grass_dirt_r.width * j
                    grass_plat.top = grass_dirt_r.height * i
                    grass_plat.draw()
                if world7_map[i][j] == 14:
                    grass_plat_l.left = grass_dirt_r.width * j
                    grass_plat_l.top = grass_dirt_r.height * i
                    grass_plat_l.draw()
                if world7_map[i][j] == 15:
                    grass_plat_r.left = grass_dirt_r.width * j
                    grass_plat_r.top = grass_dirt_r.height * i
                    grass_plat_r.draw()
                if world7_map[i][j] == 16:
                    plant1.left = grass_dirt_r.width * j
                    plant1.top = grass_dirt_r.height * i
                    plant1.draw()
                if world7_map[i][j] == 17:
                    tree.left = grass_dirt_r.width * j
                    tree.top = grass_dirt_r.height * i
                    tree.draw()
                if world7_map[i][j] == 18:
                    plant2.left = grass_dirt_r.width * j
                    plant2.top = grass_dirt_r.height * i
                    plant2.draw()
                if world7_map[i][j] == 19:
                    plant3.left = grass_dirt_r.width * j
                    plant3.top = grass_dirt_r.height * i
                    plant3.draw()
                if world7_map[i][j] == 20:
                    mushplat.left = grass_dirt_r.width * j
                    mushplat.top = grass_dirt_r.height * i
                    mushplat.draw()
                if world7_map[i][j] == 21:
                    mushplat_l.left = grass_dirt_r.width * j
                    mushplat_l.top = grass_dirt_r.height * i
                    mushplat_l.draw()
                if world7_map[i][j] == 22:
                    mushplat_r.left = grass_dirt_r.width * j
                    mushplat_r.top = grass_dirt_r.height * i
                    mushplat_r.draw()
                if world7_map[i][j] == 23:
                    mush_plat2.left = grass_dirt_r.width * j
                    mush_plat2.top = grass_dirt_r.height * i
                    mush_plat2.draw()
                if world7_map[i][j] == 24:
                    mush_base.left = grass_dirt_r.width * j
                    mush_base.top = grass_dirt_r.height * i
                    mush_base.draw()
                if world7_map[i][j] == 25:
                    grass_2.left = grass_dirt_r.width * j
                    grass_2.top = grass_dirt_r.height * i
                    grass_2.draw()
                if world7_map[i][j] == 26:
                    grass_2r.left = grass_dirt_r.width * j
                    grass_2r.top = grass_dirt_r.height * i
                    grass_2r.draw()
                if world7_map[i][j] == 27:
                    grass_2l.left = grass_dirt_r.width * j
                    grass_2l.top = grass_dirt_r.height * i
                    grass_2l.draw()
def draw_cinematic():
    global txt_repeat
    if mode == 1 and house_showagain == "yes":
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("This is my house", pos = (100, 200), color = "white", fontsize = 34)
        char_txt.draw()
        
    if mode == 2 and house_showagain == "yes":
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("It's very beautiful.", pos = (100, 200), color = "white", fontsize = 34)
        char_txt.draw()
        
    if mode == 3:
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("Our city is in problems, we need help.", pos = (100, 200), color = "white", fontsize = 28)
        sign_txt.draw()
        
    if mode == 4:
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("Whoever reads this, please come", pos = (100, 200), color = "white", fontsize = 28)
        screen.draw.text("and see.", pos = (100, 222), color = "white", fontsize = 28)
        sign_txt.draw()
        
    if mode == 5 :
        
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("I can see there's a door over there", pos = (100, 200), color = "white", fontsize = 32)
        char_txt.draw()
        
    if mode == 6 :
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("I think I shoud open it before", pos = (100, 200), color = "white", fontsize = 32)
        screen.draw.text("jumping.", pos = (100, 222), color = "white", fontsize = 32)
        char_txt.draw()
    if mode == 7 :
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("Hi cute girl, you don't seem to", pos = (100, 200), color = "white", fontsize = 28)
        screen.draw.text("live here. Are you an outlander?", pos = (100, 222), color = "white", fontsize = 28)
        npc_txt.draw()
    if mode == 8 :
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("Our city was destroyed by a criminal.", pos = (100, 200), color = "white", fontsize = 28)
        screen.draw.text("You need to help us fix it!", pos = (100, 222), color = "white", fontsize = 28)
        npc_txt.draw()
    if mode == 9 :
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("If you keep following your path", pos = (100, 200), color = "white", fontsize = 28)
        screen.draw.text("you'll run into some challenges we", pos = (100, 222), color = "white", fontsize = 28)
        screen.draw.text("haven't solved yet.", pos = (100, 244), color = "white", fontsize = 28)
        npc_txt.draw()
    if mode == 10 :
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("You need to solve them in order to", pos = (100, 200), color = "white", fontsize = 28)
        screen.draw.text("fix the city.", pos = (100, 222), color = "white", fontsize = 28)
        screen.draw.text("That's all, may god bless you!", pos = (100, 244), color = "white", fontsize = 28)
        npc_txt.draw()

    if mode == 11:
        txt_repeat = 1
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("Congratulations!!!", pos = (100, 200), color = "white", fontsize = 28)
        screen.draw.text("You managed to fix our houses", pos = (100, 222), color = "white", fontsize = 28)
        screen.draw.text("and didn't ask for a pay!", pos = (100, 244), color = "white", fontsize = 28)
        npc_txt.draw()
    if mode == 12:
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("You're the most adventurous", pos = (100, 200), color = "white", fontsize = 28)
        screen.draw.text("girl we've ever met.", pos = (100, 222), color = "white", fontsize = 28)
        screen.draw.text("Thank you for your hard work!", pos = (100, 244), color = "white", fontsize = 28)
        npc_txt.draw()


    if mode == 13:
        text_box.draw()
        enter_b.draw()
        text_box2.draw()
        screen.draw.text("Now we can continue to live", pos = (100, 200), color = "white", fontsize = 28)
        screen.draw.text("happily again!", pos = (100, 222), color = "white", fontsize = 28)
        screen.draw.text("See you around girl!", pos = (100, 244), color = "white", fontsize = 28)
        npc_txt.draw()

def draw_UI():
    global mode
    
    heart1.draw()
    heart2.draw()
    heart3.draw()
    heart4.draw()
    heart5.draw()
      
    
    
    if char.hp >= 10:  
        
        heart5.image = "tile_0044"
        heart4.image = "tile_0044"
        heart3.image = "tile_0044"
        heart2.image = "tile_0044"
        heart1.image = "tile_0044"
      
        
    elif char.hp >= 9:
        
        heart5.image = "tile_0045"
            
    elif char.hp >= 8:
        
        heart5.image = "tile_0046"
        
    elif char.hp >= 7:
        
        
        heart4.image = "tile_0045"
        
        
    elif char.hp >= 6:
        
        heart4.image = "tile_0046"
        
    elif char.hp >= 5:
        
        heart3.image = "tile_0045"
        
    elif char.hp >= 4:
        
        heart3.image = "tile_0046"
        
        
    elif char.hp >= 3:
        
        heart2.image = "tile_0045"
        
    elif char.hp >= 2:
        
        heart2.image = "tile_0046"
        
    elif char.hp >= 1:
        
        heart1.image = "tile_0045"
        
    elif char.hp >= 0:
        mode = -1
        music.stop()
    
    
    
    
    
def draw_structures():
    global sign_show1
    global w1follow
    
    
        
    #level 0 strctures:
    
    if level == 0:
        my_house1.draw()
        my_house2.draw()
        
    if level == 1:
        door_cl.draw()
        jumper.x = 95
        jumper.y = 228
        jumper.draw()
        key1.draw()
        sign.draw()
        lever.draw()
        for i in range(len(rope_list1)):
            rope_list1[i].draw()
        for i in range(len(box_list1)):
            box_list1[i].draw()
            
    if level == 2:
        house1.draw()
        house2.draw()
        house3.draw()
        npc.draw()
        if sign_show1 == 1:
            ex_sign.draw()
        if txt_repeat == 0 and npc.image == "city-npc_st":
            ex_sign.draw()
            
        for i in range(len(smoke_list1)):
            smoke_list1[i].draw()
        for i in range(len(smoke_list2)):
            smoke_list2[i].draw()
            
        for i in range(len(smoke_list3)):
            smoke_list3[i].draw()
        if repair == 1:
            if char.colliderect(house1) and w1follow == 0 and level == 2 and house1.hp == 0:
                
                screen.draw.text("Repair?", pos = (30, 155), color = (173, 216, 230), fontsize = 34)
                screen.draw.text("x1", pos = (60, 185), color = (255, 0, 0), fontsize = 28)
                wrench_txt.x = 95
                wrench_txt.y = 195
                wrench_txt.draw()
            elif char.colliderect(house1) and w1follow >= 1 and level == 2 and house1.hp == 0:
                s_button.draw()
                screen.draw.text("Repair?", pos = (30, 155), color = (173, 216, 230), fontsize = 34)
                screen.draw.text("x1", pos = (60, 185), color = (0, 255, 0), fontsize = 28)
                wrench_txt.x = 95
                wrench_txt.y = 195
                wrench_txt.draw()
            elif char.colliderect(house2) and w1follow == 0 and level == 2  and house2.hp == 0:
               
                screen.draw.text("Repair?", pos = (190, 105), color = (173, 216, 230), fontsize = 34)
                screen.draw.text("x1", pos = (210, 135), color = (255, 0, 0), fontsize = 28)
                wrench_txt.x = 245
                wrench_txt.y = 145
                wrench_txt.draw()
            elif char.colliderect(house2) and w1follow >= 1 and level == 2 and house2.hp == 0:
                s_button.draw()
                screen.draw.text("Repair?", pos = (190, 105), color = (173, 216, 230), fontsize = 34)
                screen.draw.text("x1", pos = (210, 135), color = (0, 255, 0), fontsize = 28)
                wrench_txt.x = 245
                wrench_txt.y = 145
                wrench_txt.draw()


            elif char.colliderect(house3) and w1follow == 0 and level == 2 and house3.hp == 0:
                
                screen.draw.text("Repair?", pos = (370, 105), color = (173, 216, 230), fontsize = 34)
                screen.draw.text("x1", pos = (390, 135), color = (255, 0, 0), fontsize = 28)
                wrench_txt.x = 425
                wrench_txt.y = 145
                wrench_txt.draw()

            elif char.colliderect(house3) and w1follow >= 1 and level == 2 and house3.hp == 0:
                s_button.draw()
                screen.draw.text("Repair?", pos = (370, 105), color = (173, 216, 230), fontsize = 34)
                screen.draw.text("x1", pos = (390, 135), color = (0, 255, 0), fontsize = 28)
                wrench_txt.x = 425
                wrench_txt.y = 145
                wrench_txt.draw()


 

    if level == 3:
        door1.draw()
        door2.draw()
        door3.draw()
        if char.colliderect(door1) and level == 3 or char.colliderect(door2) and level == 3 or char.colliderect(door3) and level == 3:
            s_button.draw()
    
    for i in range(len(raindrop_list)):
        raindrop_list[i].draw()





    if level == 4:
        for i in range(len(rope_list2)):
            rope_list2[i].draw()
        lock.draw()
        wrench.draw()
        if char.colliderect(lock):
            if d1follow == 0:
                screen.draw.text("Open?", pos = (245, 145), color = (173, 216, 230), fontsize = 32)
                screen.draw.text("x1", pos = (255, 175), color = (255, 0, 0), fontsize = 28)
                diamond_txt.x = 295
                diamond_txt.y = 185
                diamond_txt.draw()
            elif d1follow == 1:
                screen.draw.text("Open?", pos = (245, 145), color = (173, 216, 230), fontsize = 32)
                screen.draw.text("x1", pos = (255, 175), color = (0, 255, 0), fontsize = 28)
                diamond_txt.x = 295
                diamond_txt.y = 185
                diamond_txt.draw()
                s_button.draw()
        if platform_draw == 1:
            
            for i in range(len(platform_list1)):
                platform_list1[i].draw()
            for i in range(len(ladder_list)):
                ladder_list[i].draw()
            diamond.draw()
            


        lever.x = 510
        lever.y = 100
        lever.draw()
        


        if char.colliderect(lever) and level == 4:
            s_button.draw()
    if w1follow == 1:
        wrench.draw()
    if w1follow == 2:
        wrench2.draw()
    if w1follow == 3:
        wrench3.draw()

    if level == 5:
        for i in range(len(box_list2)):
            box_list2[i].draw()
        for i in range(len(chain_list1)):
            chain_list1[i].draw()
        lever.x = 520
        lever.y = 298
        lever.draw()
        b_press.draw()
        wrench2.draw()
        if char.colliderect(lever):
            s_button.draw()
        for i in range(len(grenade_list)):
            if gren1 == 0:
                grenade_list[0].y = plane.y
            if gren2 == 0:
                grenade_list[1].y = plane.y
            if gren3 == 0:
                grenade_list[2].y = plane.y
            if gren4 == 0:
                grenade_list[3].y = plane.y
            if gren1 == 1:
                grenade_list[0].draw()
            if gren2 == 1:
                grenade_list[1].draw()
            if gren3 == 1:
                grenade_list[2].draw()
            if gren4 == 1:
                grenade_list[3].draw()
        for i in range(len(arrow_list)):
            arrow_list[i].draw()
            
        plane.draw()
    if level == 6:
        tree1.draw()
        tree2.draw()

        lever.x = 510
        lever.y = 228
        lever.draw()
        if lever.colliderect(char):
            s_button.draw()
        if wrench3_draw == 1:
            wrench3.draw()
        
def draw_boulder():
    if level == 6:
        boulder.draw()
        bird.draw()

def draw_bg():
    
    global bg_img
    
    bg.draw()
    
    
    for i in range(len(clouds_list)):
        clouds_list[i].draw()

    if bg_img == 0:
        bg.image = "bg"
    elif bg_img == 1:
        bg.image = "citybg_ruin"
    elif bg_img == 2:
        bg.image = "lvlselect_bg"
    elif bg_img == 3:
        bg.image = "night_bg"
    elif bg_img == 4:
        bg.image = "night_gif"
    elif bg_img ==5:
        bg.image = "fuji"
    elif bg_img == 6:
        bg.image = "jungle"
    for i in range(len(sparkle_list)):
        sparkle_list[i].draw()
    
def night_filter2():
    if night_filter == 1:

        nightfilter.draw() 

    
    
        
        
    
def draw():
    global mode
    global house_showagain
    
    
    
    if mode == 0:
        screen.fill("black")
        draw_bg()
        draw_level()
        draw_structures()
        char.draw()
        draw_boulder()
        night_filter2()
        draw_UI()

        
        
    if char.colliderect(lever) and level == 1 and lever_on1 == 0:
        s_button.draw()
    if read_txt == 1 and level == 1:
        s_button.draw()
        screen.draw.text("Read?", pos = (440, 150), color = (173, 216, 230), fontsize = 30)
    for i in range(len(ladder_list)):
        if ladder_list[i].colliderect(char) and platform_draw == 1 and level == 4:
            s_button.draw()
    
    
    draw_cinematic()
    
    
    
    if mode == -1:
        bg.draw()
        bg_over.draw()
        screen.draw.text("Respawn?", pos = (150, 200), color = (255, 192, 203) , fontsize = 58)
        yes_b.draw()
        no_b.draw()
    if mode == -2:
        bg.draw()
        start.draw()
        screen.draw.text("City's rebuild", pos = (110, 100), color = (255, 192, 203), fontsize = 68)
        for i in range(len(sparkle_list)):
            sparkle_list[i].draw()
        for i in range(len(raindrop_list)):
            raindrop_list[i].draw()
        for i in range(len(world1_map)):
            for j in range(len(world1_map[0])):
                if world1_map[i][j] == 1:
                    grass.left = grass.width * j
                    grass.top = grass.height * i
                    grass.draw()
                if world1_map[i][j] == -1:
                    dirt.left = dirt.width * j
                    dirt.top = dirt.height * i
                    dirt.draw()
                if world1_map[i][j] == 2:
                    grass_corner_l.left = grass_corner_l.width * j
                    grass_corner_l.top = grass_corner_l.height * i
                    grass_corner_l.draw()
                if world1_map[i][j] == 3:
                    dirt_corner_l.left = dirt_corner_l.width * j
                    dirt_corner_l.top = dirt_corner_l.height * i
                    dirt_corner_l.draw()
                if world1_map[i][j] == 4:
                    dirt_corner_r.left = dirt_corner_r.width * j
                    dirt_corner_r.top = dirt_corner_r.height * i
                    dirt_corner_r.draw()
                if world1_map[i][j] == 5:
                    grass_corner_r.left = grass_corner_r.width * j
                    grass_corner_r.top = grass_corner_r.height * i
                    grass_corner_r.draw()
                if world1_map[i][j] == 6:
                    grass_dirt_l.left = grass_dirt_l.width * j
                    grass_dirt_l.top = grass_dirt_l.height * i
                    grass_dirt_l.draw()
                if world1_map[i][j] == 7:
                    grass_dirt.left = grass_dirt.width * j
                    grass_dirt.top = grass_dirt.height * i
                    grass_dirt.draw()
                if world1_map[i][j] == 8:
                    grass_dirt_r.left = grass_dirt_r.width * j
                    grass_dirt_r.top = grass_dirt_r.height * i
                    grass_dirt_r.draw()
                if world1_map[i][j] == 9:
                    right_sign.left = grass_dirt_r.width * j
                    right_sign.top = grass_dirt_r.height * i
                    right_sign.draw()
                if world1_map[i][j] == 10:
                    plat_l.left = grass_dirt_r.width * j
                    plat_l.top = grass_dirt_r.height * i
                    plat_l.draw()
                if world1_map[i][j] == 11:
                    plat.left = grass_dirt_r.width * j
                    plat.top = grass_dirt_r.height * i
                    plat.draw()
                if world1_map[i][j] == 12:
                    plat_r.left = grass_dirt_r.width * j
                    plat_r.top = grass_dirt_r.height * i
                    plat_r.draw()
                if world1_map[i][j] == 13:
                    grass_plat.left = grass_dirt_r.width * j
                    grass_plat.top = grass_dirt_r.height * i
                    grass_plat.draw()
                if world1_map[i][j] == 14:
                    grass_plat_l.left = grass_dirt_r.width * j
                    grass_plat_l.top = grass_dirt_r.height * i
                    grass_plat_l.draw()
                if world1_map[i][j] == 15:
                    grass_plat_r.left = grass_dirt_r.width * j
                    grass_plat_r.top = grass_dirt_r.height * i
                    grass_plat_r.draw()
                if world1_map[i][j] == 16:
                    plant1.left = grass_dirt_r.width * j
                    plant1.top = grass_dirt_r.height * i
                    plant1.draw()
                if world1_map[i][j] == 17:
                    tree.left = grass_dirt_r.width * j
                    tree.top = grass_dirt_r.height * i
                    tree.draw()
                if world1_map[i][j] == 18:
                    plant2.left = grass_dirt_r.width * j
                    plant2.top = grass_dirt_r.height * i
                    plant2.draw()
                if world1_map[i][j] == 19:
                    plant3.left = grass_dirt_r.width * j
                    plant3.top = grass_dirt_r.height * i
                    plant3.draw()
                if world1_map[i][j] == 20:
                    mushplat.left = grass_dirt_r.width * j
                    mushplat.top = grass_dirt_r.height * i
                    mushplat.draw()
                if world1_map[i][j] == 21:
                    mushplat_l.left = grass_dirt_r.width * j
                    mushplat_l.top = grass_dirt_r.height * i
                    mushplat_l.draw()
                if world1_map[i][j] == 22:
                    mushplat_r.left = grass_dirt_r.width * j
                    mushplat_r.top = grass_dirt_r.height * i
                    mushplat_r.draw()
                if world1_map[i][j] == 23:
                    mush_plat2.left = grass_dirt_r.width * j
                    mush_plat2.top = grass_dirt_r.height * i
                    mush_plat2.draw()
                if world1_map[i][j] == 24:
                    mush_base.left = grass_dirt_r.width * j
                    mush_base.top = grass_dirt_r.height * i
                    mush_base.draw()
                if world1_map[i][j] == 25:
                    grass_2.left = grass_dirt_r.width * j
                    grass_2.top = grass_dirt_r.height * i
                    grass_2.draw()
                if world1_map[i][j] == 26:
                    grass_2r.left = grass_dirt_r.width * j
                    grass_2r.top = grass_dirt_r.height * i
                    grass_2r.draw()
                if world1_map[i][j] == 27:
                    grass_2l.left = grass_dirt_r.width * j
                    grass_2l.top = grass_dirt_r.height * i
                    grass_2l.draw()
                my_house1.draw()
                my_house2.draw()
    if mode == -3:
        bg.image = "lvlselect_bg"
        bg.draw()
        screen.draw.text("You win!", pos = (170, 100), color = (255, 192, 203), fontsize = 68)
        screen.draw.text("Play again?", pos = (180, 170), color = (0, 255, 255), fontsize = 48)


        for i in range(len(sparkle_list)):
            sparkle_list[i].draw()
        for i in range(len(raindrop_list)):
            raindrop_list[i].draw()
        yes_b.x = 260
        yes_b.y = 250
        yes_b.draw()

    
    


   
    
def sound():
    global jump_sound
    global jump_s1, jump_s2, jump_s3, jump_s4, jump_s5
    global jump_sounds_char
    global key_pickup
    global door_open
    global lever_switch
    global move_rope_sound
    global trampoline_sound
    jump_sound = sounds.jumpsound
    jump_sound.set_volume(0.2)
    jump_s1 = sounds.jump1
    jump_s2 = sounds.jump2
    jump_s3 = sounds.jump3
    jump_s4 = sounds.jump4
    jump_s5 = sounds.jump5
    jump_sounds_char = [jump_s1, jump_s2, jump_s3, jump_s4, jump_s5]
    key_pickup = sounds.key_pickup
    key_pickup.set_volume(0.85)
    door_open = sounds.door_open
    door_open.set_volume(0.85)
    lever_switch = sounds.lever_switch
    lever_switch.set_volume(0.85)
    move_rope_sound = sounds.move_rope
    move_rope_sound.set_volume(0.8)
    trampoline_sound = sounds.trampoline_jump


            
        
def controls():
    global img
    global mode
    global house_showagain
    if level == 0:
        if keyboard.a and char.x > 0 and char.y <= 265 and mode == 0 :
            char.x -= 5
            img = 1
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_l1"
            elif char.image == "char_l1" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6": 
                char.image = "char_l2"
            elif char.image == "char_l2" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l3"
            elif char.image == "char_l3" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l4"
            elif char.image == "char_l4" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l5"
            elif char.image == "char_l5" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l6"
            elif char.image == "char_l6" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_stl"
            
        elif keyboard.a and char.y >=265 and char.x > 342 and char.x < 450 and mode == 0:
            char.x -= 5
        
                
        elif keyboard.d and char.y <= 265 and char.x < 540 and mode == 0 :
            img = 0
            char.x += 5
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_r1"
            elif char.image == "char_r1" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r2"
            elif char.image == "char_r2" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r3"
            elif char.image == "char_r3" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r4"
            elif char.image == "char_r4" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r5"
            elif char.image == "char_r5" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r6"
            elif char.image == "char_r6" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_st"
                
        elif keyboard.d and char.y >=265 and char.x > 342 and char.x < 450 and mode == 0:
            char.x += 5
        
        elif keyboard.w and mode == 0:
            
            if  img == 0:
                char.image = "char_r1"
            else:
                char.image = "char_l1"
        elif jump_speed == 0 and jump == 0:
            if img == 0:
                char.image = "char_st"
            else:
                char.image = "char_stl"
    if level == 1:
        if keyboard.a and char.x > 0 and char.y <= 211 and mode == 0 or keyboard.left and char.x > 0 and char.y <= 120 and mode == 0 :
            char.x -= 5
            img = 1
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_l1"
            elif char.image == "char_l1" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6": 
                char.image = "char_l2"
            elif char.image == "char_l2" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l3"
            elif char.image == "char_l3" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l4"
            elif char.image == "char_l4" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l5"
            elif char.image == "char_l5" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l6"
            elif char.image == "char_l6" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_stl"
            
        elif keyboard.a and char.y >=211 and char.x > 110 and char.x < 460 and mode == 0:
            char.x -= 5
        
                
        elif keyboard.d and char.y <= 211 and char.x < 540 and mode == 0 or keyboard.right and char.y == 120 and mode == 0:
            img = 0
            char.x += 5
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_r1"
            elif char.image == "char_r1" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r2"
            elif char.image == "char_r2" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r3"
            elif char.image == "char_r3" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r4"
            elif char.image == "char_r4" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r5"
            elif char.image == "char_r5" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r6"
            elif char.image == "char_r6" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_st"
                
        elif keyboard.d and char.y >=211 and char.x > 110 and char.x <= 440 and mode == 0:
            char.x +=5
        
        elif keyboard.w and mode == 0:
            
            if  img == 0:
                char.image = "char_r1"
            else:
                char.image = "char_l1"
        elif jump == 0 or char.y == 120:
            if img == 0:
                char.image = "char_st"
            else:
                char.image = "char_stl"
                
    if level == 2:
        if keyboard.a and char.x >= 0 and char.x <= 540 and mode == 0:
            char.x -= 5
            img = 1
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_l1"
            elif char.image == "char_l1" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6": 
                char.image = "char_l2"
            elif char.image == "char_l2" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l3"
            elif char.image == "char_l3" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l4"
            elif char.image == "char_l4" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l5"
            elif char.image == "char_l5" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l6"
            elif char.image == "char_l6" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_stl"
        
                
        elif keyboard.d and char.x >= 0 and char.x <= 540:
            img = 0
            char.x += 5
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_r1"
            elif char.image == "char_r1" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r2"
            elif char.image == "char_r2" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r3"
            elif char.image == "char_r3" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r4"
            elif char.image == "char_r4" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r5"
            elif char.image == "char_r5" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r6"
            elif char.image == "char_r6" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_st"
                
       
        
        elif keyboard.w and mode == 0:
            
            if  img == 0:
                char.image = "char_r1"
            else:
                char.image = "char_l1"
        elif jump == 0 or char.y == 120:
            if img == 0:
                char.image = "char_st"
            else:
                char.image = "char_stl"  
        
    if level == 3:
        if keyboard.a and char.x >= 0 and char.x <= 540 and mode == 0:
            char.x -= 5
            img = 1
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_l1"
            elif char.image == "char_l1" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6": 
                char.image = "char_l2"
            elif char.image == "char_l2" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l3"
            elif char.image == "char_l3" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l4"
            elif char.image == "char_l4" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l5"
            elif char.image == "char_l5" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l6"
            elif char.image == "char_l6" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_stl"
        
                
        elif keyboard.d and char.x >= 0 and char.x <= 540:
            img = 0
            char.x += 5
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_r1"
            elif char.image == "char_r1" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r2"
            elif char.image == "char_r2" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r3"
            elif char.image == "char_r3" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r4"
            elif char.image == "char_r4" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r5"
            elif char.image == "char_r5" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r6"
            elif char.image == "char_r6" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_st"
                
       
        
        elif keyboard.w and mode == 0:
            
            if  img == 0:
                char.image = "char_r1"
            else:
                char.image = "char_l1"
        elif jump == 0 or char.y == 120:
            if img == 0:
                char.image = "char_st"
            else:
                char.image = "char_stl" 




    if level == 4:
        if keyboard.a and char.x >= 0 and char.x <= 540 and mode == 0:
            char.x -= 5
            img = 1
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_l1"
            elif char.image == "char_l1" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6": 
                char.image = "char_l2"
            elif char.image == "char_l2" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l3"
            elif char.image == "char_l3" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l4"
            elif char.image == "char_l4" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l5"
            elif char.image == "char_l5" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l6"
            elif char.image == "char_l6" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_stl"
        
                
        elif keyboard.d and char.x >= 0 and char.x <= 540:
            img = 0
            char.x += 5
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_r1"
            elif char.image == "char_r1" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r2"
            elif char.image == "char_r2" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r3"
            elif char.image == "char_r3" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r4"
            elif char.image == "char_r4" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r5"
            elif char.image == "char_r5" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r6"
            elif char.image == "char_r6" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_st"
                
       
        
        elif keyboard.w and mode == 0:
            
            if  img == 0:
                char.image = "char_r1"
            else:
                char.image = "char_l1"
        elif jump == 0 or char.y == 120:
            if img == 0:
                char.image = "char_st"
            else:
                char.image = "char_stl" 
    if level == 5:
        if keyboard.a and char.x >= 0 and char.x <= 540 and mode == 0:
            char.x -= 5
            img = 1
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_l1"
            elif char.image == "char_l1" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6": 
                char.image = "char_l2"
            elif char.image == "char_l2" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l3"
            elif char.image == "char_l3" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l4"
            elif char.image == "char_l4" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l5"
            elif char.image == "char_l5" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l6"
            elif char.image == "char_l6" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_stl"
        
                
        elif keyboard.d and char.x >= 0 and char.x <= 540:
            img = 0
            char.x += 5
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_r1"
            elif char.image == "char_r1" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r2"
            elif char.image == "char_r2" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r3"
            elif char.image == "char_r3" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r4"
            elif char.image == "char_r4" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r5"
            elif char.image == "char_r5" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r6"
            elif char.image == "char_r6" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_st"
                
       
        
        elif keyboard.w and mode == 0:
            
            if  img == 0:
                char.image = "char_r1"
            else:
                char.image = "char_l1"
        elif jump == 0 or char.y == 120:
            if img == 0:
                char.image = "char_st"
            else:
                char.image = "char_stl" 




    if level == 6:
        if keyboard.a and char.x >= 0 and char.x <= 540 and mode == 0 and wrench3_draw == 0:
            char.x -= 5
            img = 1
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_l1"
            elif char.image == "char_l1" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6": 
                char.image = "char_l2"
            elif char.image == "char_l2" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l3"
            elif char.image == "char_l3" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l4"
            elif char.image == "char_l4" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l5"
            elif char.image == "char_l5" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_l6"
            elif char.image == "char_l6" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                char.image = "char_stl"
        
                
        elif keyboard.d and char.x >= 0 and char.x <= 540 and wrench3_draw == 0:
            img = 0
            char.x += 5
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_r1"
            elif char.image == "char_r1" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r2"
            elif char.image == "char_r2" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r3"
            elif char.image == "char_r3" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r4"
            elif char.image == "char_r4" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r5"
            elif char.image == "char_r5" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r6"
            elif char.image == "char_r6" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                
                char.image = "char_st"
        elif keyboard.a and char.x >= 0 and char.x <= 540 and mode == 0 and wrench3_draw == 1:
            char.x -= 1.5
            img = 1
            if char.image == "char_st" or char.image == "char_stl":
                    char.image = "char_l1"
            elif char.image == "char_l1" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6": 
                    char.image = "char_l2"
            elif char.image == "char_l2" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                    char.image = "char_l3"
            elif char.image == "char_l3" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                    char.image = "char_l4"
            elif char.image == "char_l4" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                    char.image = "char_l5"
            elif char.image == "char_l5" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                    char.image = "char_l6"
            elif char.image == "char_l6" or char.image == "char_r1" or char.image == "char_r2" or char.image == "char_r3" or char.image == "char_r4" or char.image == "char_r5" or char.image == "char_r6":
                    char.image = "char_stl"



        elif keyboard.d and char.x >= 0 and char.x <= 540 and wrench3_draw == 1:
            img = 0
            char.x += 1.5
            if char.image == "char_st" or char.image == "char_stl":
                char.image = "char_r1"
            elif char.image == "char_r1" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r2"
            elif char.image == "char_r2" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r3"
            elif char.image == "char_r3" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r4"
            elif char.image == "char_r4" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r5"
            elif char.image == "char_r5" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                char.image = "char_r6"
            elif char.image == "char_r6" or char.image == "char_l1" or char.image == "char_l2" or char.image == "char_l3" or char.image == "char_l4" or char.image == "char_l5" or char.image == "char_l6":
                
                char.image = "char_st"
       
        
        elif keyboard.w and mode == 0 :
            
            if  img == 0:
                char.image = "char_r1"
            else:
                char.image = "char_l1"
        elif jump == 0 or char.y == 120:
            if img == 0:
                char.image = "char_st"
            else:
                char.image = "char_stl" 

    
                
    
    
            

        

    
    
        
        
            
def jump2():
    global jump_speed
    global jump
    char.y += jump_speed
    jump_speed += gravity
    jump = 1
    if jump_speed >= 10 and jump == 1:
        jump_speed = 10

    if level == 0:
        
        if char.y > 540:
            char.y = 265
            char.x = 200
            char.hp -= 1
        
            
        if char.y >= 265 and char.x < 342:
            jump_speed = 0
            char.y = 265
            jump = 0
            
        elif char.y >= 211 and char.x > 450:
            jump_speed = 0
            char.y = 211
            jump = 0
        
        elif img == 0:
            jump = 1
            char.image = "char_r1"
        
        else:
            jump = 1
            char.image = "char_l1"
    if level == 1:
        
        if char.y > 540:
            char.y = 210
            char.x = 100
            char.hp -= 1
            
       
            
            
        
        if char.y <= 187 and char.y >= 172 and char.x < 80:
            jump_speed = 0
            jump_speed += gravity
            jump = 0
            
        if char.y <= 120 and char.y >= 80 and char.x <= 75:
            jump_speed = 0
            jump_speed += gravity
            jump = 0
            
            
            
        if char.y >= 210 and char.x < 110:
            jump_speed = 0
            char.y = 210
            jump = 0
            
        elif char.y >= 120 and char.y < 157 and char.x < 80:
            jump_speed = 0
            char.y = 120
            jump = 0
            
        elif char.y >= 211 and char.x > 450:
            jump_speed = 0
            char.y = 211
            jump = 0
            
        elif char.y >= 45  and char.y <= 75 and char.x <= 75:
            jump_speed = 0
            char.y = 55
            jump = 0
            
        elif char.y >= 21  and char.y <= 30 and char.x >= 160 and char.x <= 300:
            jump_speed = 0
            char.y = 30
            jump = 0
            
        elif char.y >= 58  and char.y <= 108 and char.x >= 160 and char.x <= 300:
            jump_speed = 0
            jump_speed += gravity
            jump = 0
        
        
        elif img == 0:
            jump = 1
            char.image = "char_r1"
        
        else:
            jump = 1
            char.image = "char_l1"
            
            
    if level == 2:
        if char.y >= 265:
            jump_speed = 0
            char.y = 265
            jump = 0
    
    
    if level == 3:
        if char.y >= 265:
            jump_speed = 0
            char.y = 265
            jump = 0
        
        if char.y <= 205 and char.y >= 190 and char.x >= 30 and char.x <= 140:
            jump_speed = 0
            jump_speed += gravity
            jump = 1
            
        if char.y <= 160 and char.y >= 140 and char.x >= 30 and char.x <= 140:
            jump_speed = 0
            char.y = 155
            jump = 0
            
        if char.y <= 205 and char.y >= 190 and char.x >= 420 and char.x <= 520:
            jump_speed = 0
            jump_speed += gravity
            jump = 1
            
        if char.y <= 160 and char.y >= 140 and char.x >= 420 and char.x <= 520:
            jump_speed = 0
            char.y = 155
            jump = 0
            
            
        if char.y <= 52 and char.y >= 40 and char.x >= 190 and char.x <= 280:
            jump_speed = 0
            char.y = 45
            jump = 0
            
        if char.y <= 64 and char.y >= 57 and char.x >= 190 and char.x <= 280:
            jump_speed = 0
            jump_speed += gravity
            jump = 1
    if level == 4:



        if char.x <=120 and char.y >=165 and char.y <= 175:
            jump_speed = 0
            char.y = 175
            jump = 0

        if char.x >= 80 and char.x <= 118 and char.y >= 285 and char.y <= 305:
            jump_speed = 0
            char.y = 300
            jump = 0
        if char.x >= 220 and char.x <= 300 and char.y >= 215 and char.y <= 235:
            jump_speed = 0
            char.y = 225
            jump = 0
        if char.x >= 360 and char.x <= 540 and char.y >= 75 and char.y <= 90:
            jump_speed = 0
            char.y = 85
            jump = 0
        if char.y >= 600 and level == 4:
            char.x = 5
            char.y = 150
            jump_speed = 0
            char.hp -= 1
    if level == 5:
       

        if char.x <= 30 and char.y >= 275 and char.y <= 303:
            jump_speed = 0 
            char.y = 285 
            jump = 0
        if char.x >= 110 and char.x <= 190 and char.y >= 220 and char.y <= 248:
            jump_speed = 0
            char.y = 230
            jump = 0
        if char.x >= 250 and char.x <= 320 and char.y >= 290 and char.y <= 318:
            jump_speed = 0
            char.y = 300
            jump = 0
        if char.x >= 380 and char.x <= 420 and char.y >= 305 and char.y <= 333:
            jump_speed = 0
            char.y = 315
            jump = 0
        if char.x >= 480 and char.y >= 275 and char.y <= 303:
            jump_speed = 0
            char.y = 285
            jump = 0
        if char.x >= 230 and char.x <= 270 and char.y >= 125 and char.y <= 153:
            jump_speed = 0
            char.y = 135
            jump = 0
        if char.x >= 360 and char.x <= 420 and char.y >= 75 and char.y <= 103:
            jump_speed = 0
            char.y = 83
            jump = 0
        if char.x >= 500 and char.y >= 20 and char.y <= 48:
            jump_speed = 0
            char.y = 30
            jump = 0
        if char.x >= 120 and char.x <= 190 and char.y >= 55 and char.y <= 83:
            jump_speed = 0
            char.y = 65
            jump = 0
        if char.x <= 60 and char.y >= 20 and char.y <= 38:
            jump_speed = 0
            char.y = 30
            jump = 0
    if level == 6:
        if char.x <= 270 and char.y >= 205 and char.y <= 215 or char.x >= 300 and char.y >= 205 and char.y <= 215:
            jump_speed = 0
            char.y = 215
            jump = 0
        if char.x >= 270 and char.x <= 310 and char.y >= 275 and char.y <= 285:
            jump_speed = 0
            char.y = 285
            jump = 0

        if char.y >= 230 and char.y <= 285 and char.x >= 300:
            char.x = 295


        if char.y >= 230 and char.y <= 285 and char.x <= 275:
            char.x = 280
        

            
        
    
def collisions():
    
    global mode
    global house_showagain
    global level
    global jump_speed
    global jump
    global touch
    global key
    global k1follow
    global open_d1
    global read_txt
    global old_x
    global lever_on1
    global move_rope
    global key_repeat
    global bg_img
    global sign_show1
    global night_filter
    global platform_draw
    global gravity
    global ladder1
    global d1follow
    global move_rope2
    global w1follow
    global repair 
    global move_box2
    global move_chain2
    global gren1, gren2, gren3, gren4
    global wrench3_draw
    global col1
    global txt_repeat
    global house
    global old_y
    global space_playing



    for i in range(len(clouds_list)):
        if clouds_list[i].x < -20:
            clouds_list[i].y = random.randint(10, 200)
            clouds_list[i].x = random.randint(600, 1200)
            
    if char.colliderect(my_house1) and house_showagain == "yes" and mode == 0 and level == 0:
        house = 1
        mode = 1
    else:
        house = 0
        
    if char.x >= 540 and level == 0:
        level = 1
        char.x = 5
        char.y = 210
        old_x = 5
        old_y = 210
    if char.x <= 0 and char.y >= 180 and level == 1:
        level = 0
        char.x = 540
        char.y = 210
    if char.x >= 539 and level == 1:


        if house1.hp == 0 or house2.hp == 0 or house3.hp == 0:


            music.stop()
            music.set_volume(0.2)
            music.play("tanks go to battle")
            space_playing = 0


        level = 2
        char.x = 5
        char.y = 265
        bg_img = 1
    if char.x <= 2 and level == 2:
        if space_playing == 0:
            music.stop()
            music.set_volume(1.5)
            music.play("space date")
        lever.x = 25
        lever.y = 138
        level = 1
        char.x = 535
        char.y = 210
        bg_img = 0
    if char.x >= 540 and level == 2:
        if space_playing == 0:
            music.stop()
            music.set_volume(1.5)
            music.play("space date")
        level = 3
        char.x = 5
        char.y = 265
        bg_img = 2
    if char.x <= 0 and level == 3:
        if house1.hp == 0 or house2.hp == 0 or house3.hp == 0:


            music.stop()
            music.set_volume(0.2)
            music.play("tanks go to battle")
            space_playing = 0

        
        level = 2
        char.x = 530
        char.y = 265
        bg_img = 1
        
    if char.colliderect(door_cl) and level == 1 and key == 1 or char.colliderect(door_cl) and level == 1 and open_d1 == 1:
        if door_cl.image == "door_cl":
            door_open.play()

        door_cl.x =  63
        door_cl.image = "door_op"
        open_d1 = 1
        key -= 1
        k1follow = 0
        key1.x = 900
        key1.y = 1000
        
    elif char.colliderect(door_cl) and level == 1 and open_d1 != 1:
        char.x = 90
        
        
    if char.colliderect(jumper) and level == 1:
        
        jumper.image = "tile_0107"
        char.y = char.y - 3
        touch = 1
        jump_speed = 0
    else:
        jumper.image = "tile_0108"
        touch = 0
        
    if touch == 1  and keyboard.w:
        trampoline_sound.play()
        jump_speed = -20 
        jump = 1
        touch = 0
        
    if char.colliderect(key1) and mode == 0 and level == 1:
        
        key = 1
        k1follow = 1
    if char.colliderect(key1) and mode == 0 and level == 1 and key_repeat == "yes":
        mode = 5
        
    if k1follow == 1:
        
        key1.y = char.y - 8
        key1.x = char.x + 25
        
    if sign.colliderect(char) and level == 1:
        read_txt = 1
    else:
        read_txt = 0
    if read_txt == 1 and keyboard.s:
        mode = 3
    if char.colliderect(lever) and keyboard.s and level == 1:
        lever_on1 = 1

    if char.colliderect(door3) and keyboard.s and level == 3:
        jump_speed = 0
        lever.image = "tile_0066"
        bg_img = 3
        level = 4
        char.x = 5
        char.y = 175
        night_filter = 1

    if char.x <= 0 and char.y <= 175 and char.y >= 150 and level == 4:
        level = 3
        char.x = 230
        char.y = 45
        bg_img = 2
        night_filter = 0
    if char.colliderect(door1) and keyboard.s and level == 3:
        lever.image = "tile_0066"
        level = 5
        bg_img = 5
        char.x = 5
        char.y = 285

    if char.y >= 600:
        char.hp -= 1
        char.x = 5
        char.y = 285
    if char.x >= 540:
        char.x = 530
    if char.x <= 0 and char.y != 285:
        char.x = 10
    if level == 5 and char.x <=0 and char.y == 285:
        level = 3
        bg_img = 2
        char.x = 100
        char.y = 155
        jump_speed = 0

        
        
    for i in range(len(rope_list1)):
        if rope_list1[i].colliderect(char) and level == 1:
            char.x = 495
    for i in range(len(box_list1)):
        if box_list1[i].colliderect(char) and level == 1:
            char.x = 495
    if char.colliderect(npc) and sign_show1 == 1 and level == 2 and house1.hp == 0 and house2.hp == 0 and house3.hp == 0:
        char.y = 265
        char.x = 450
        sign_show1 = 0
        mode = 7
        repair = 1
    if char.colliderect(lever) and keyboard.s and level == 4:
        lever_on1 = 1
        platform_draw = 1

    for i in range(len(ladder_list)):   
        if ladder_list[i].colliderect(char) and platform_draw == 1 and level == 4:
            ladder1 = 1

        elif keyboard.s and ladder1 == 1 and platform_draw == 1 and level == 4:
            jump_speed = 0
            char.y = 15
        

        else:
            ladder1 = 0
        
    for i in range(len(platform_list1)):
        if platform_list1[i].colliderect(char) and platform_draw == 1 and level == 4:
            jump_speed = 0
            char.y = 15
            jump = 0



    if diamond.colliderect(char) and level == 4 and platform_draw == 1:
        d1follow = 1

    if d1follow == 1:
        
        diamond.y = char.y - 8
        diamond.x = char.x + 25
    if char.colliderect(lock) and d1follow == 1 and keyboard.s and level == 4:
        d1follow = 0
        diamond.x = 800
        diamond.y = 800
        move_rope2 = 1

    for i in range(len(rope_list2)):
        if rope_list2[i].colliderect(char) and level == 4:
            char.x = 135
    if char.colliderect(wrench) and level == 4 and w1follow == 0:
        w1follow = 1

    if w1follow == 1:
        wrench.x = char.x + 25
        wrench.y = char.y - 8
    if w1follow == 2:
        wrench2.x = char.x + 25
        wrench2.y = char.y - 8

    if w1follow == 3:
        wrench3.x = char.x + 25
        wrench3.y = char.y - 8


    if char.colliderect(house1) and w1follow == 1 and house1.hp == 0 and keyboard.s and level == 2:
        house1.hp = 1
        w1follow = 0
        wrench.x = 800
        wrench.y = 800
    if char.colliderect(house1) and w1follow == 2 and house1.hp == 0 and keyboard.s and level == 2:
        house1.hp = 1
        w1follow = 0
        wrench2.x = 800
        wrench2.y = 800

    if char.colliderect(house1) and w1follow == 3 and house1.hp == 0 and keyboard.s and level == 2:
        house1.hp = 1
        w1follow = 0
        wrench3.x = 800
        wrench3.y = 800

    if char.colliderect(house2) and w1follow == 1 and house2.hp == 0 and keyboard.s and level == 2:
        house2.hp = 1
        w1follow = 0
        wrench.x = 800
        wrench.y = 800
    if char.colliderect(house2) and w1follow == 2 and house2.hp == 0 and keyboard.s and level == 2:
        house2.hp = 1
        w1follow = 0
        wrench2.x = 800
        wrench2.y = 800
    if char.colliderect(house2) and w1follow == 3 and house2.hp == 0 and keyboard.s and level == 2:
        house2.hp = 1
        w1follow = 0
        wrench3.x = 800
        wrench3.y = 800

    if char.colliderect(house3) and w1follow == 1 and house3.hp == 0 and keyboard.s and level == 2:
        house3.hp = 1
        w1follow = 0
        wrench.x = 800
        wrench.y = 800

    if char.colliderect(house3) and w1follow == 2 and house3.hp == 0 and keyboard.s and level == 2:
        house3.hp = 1
        w1follow = 0
        wrench2.x = 800
        wrench2.y = 800

    if char.colliderect(house3) and w1follow == 3 and house3.hp == 0 and keyboard.s and level == 2:
        house3.hp = 1
        w1follow = 0
        wrench3.x = 800
        wrench3.y = 800
    
    for i in range(len(box_list2)):
        if box_list2[i].colliderect(char) and level == 5:
            char.x = 490
    for i in range(len(chain_list1)):
        if chain_list1[i].colliderect(char) and level == 5:
            char.x = 70
    if char.colliderect(lever) and level == 5 and keyboard.s:
        lever_on1 = 1
        move_box2 = 1
        gren1 = random.randint(20, 530)
    if move_box2 == 1 and level == 5:
        plane.x -= 3
    if plane.x <= -50:
        plane.x = 600
    for i in range(len(box_list2)):
        if move_box2 == 1 and level == 5:
            box_list2[i].y -= 2
        if box_list2[i].y <= -50:
            box_list2.pop(i)
            break
    if char.colliderect(b_press):
        b_press.image = "tile_0149"
        move_chain2 = 1
    for i in range(len(chain_list1)):

        if move_chain2 == 1 and level == 5:
            chain_list1[i].y -= 2
        if chain_list1[i].y <= -130:
            chain_list1.pop(i)
            break
    if char.colliderect(wrench2) and level == 5 and w1follow == 0:
        w1follow = 2
    if level == 5:

        for i in range(len(grenade_list)):
            if grenade_list[0].colliderect(plane):
                gren1 = 1
            if gren1 == 1 and grenade_list[0].image == "grenade":
                grenade_list[0].y += 1

            if grenade_list[1].colliderect(plane):
                gren2 = 1

            if gren2 == 1 and grenade_list[1].image == "grenade":
                grenade_list[1].y += 1

            if grenade_list[2].colliderect(plane):
                gren3 = 1
            if gren3 == 1 and grenade_list[2].image == "grenade":
                grenade_list[2].y += 1

            if grenade_list[3].colliderect(plane):
                gren4 = 1
            if gren4 == 1 and grenade_list[3].image == "grenade":
                grenade_list[3].y += 1



            if grenade_list[i].y >= 600:
                grenade_list[i].y = plane.y
                grenade_list[i].x = random.randint(20 , 530)
            if grenade_list[0].y >= 600:
                gren1 = 0
            if grenade_list[1].y >= 600:
                gren2 = 0
            if grenade_list[2].y >= 600:
                gren3 = 0
            if grenade_list[3].y >= 600:
                gren4 = 0
            if grenade_list[i].colliderect(char) and grenade_list[i].image == "grenade" and grenade_list[i].y >= 50:
                grenade_list[i].image = "grenade2"
                char.hp -= 1
        for i in range(len(arrow_list)):

            if move_chain2 == 1:
                arrow_list[i].x += 3
            if arrow_list[i].x >= 600:
                arrow_list[i].x = -40
                arrow_list[i].y = random.randint(20, 530)
                
            if arrow_list[i].colliderect(char):
                char.hp -= 1
                arrow_list[i].x = -40
                arrow_list[i].y = random.randint(20, 530)
    if level == 3 and char.colliderect(door2) and keyboard.s:
        bg_img = 6
        level = 6
        char.x = 10
        char.y = 205
        lever.image = "tile_0066"


    if level == 6 and char.x <= 5:
        level = 3
        bg_img = 2
        char.x = 460
        char.y = 155
    if level == 6:
        if char.colliderect(lever) and keyboard.s:
            wrench3_draw = 1
            lever_on1 = 1 


        if char.colliderect(wrench3) and wrench3_draw == 1 and w1follow == 0:
            w1follow = 3
        if wrench3_draw == 1:
            boulder.x -= 2
        if char.colliderect(boulder) and wrench3_draw == 1 and level == 6:
            boulder.x = -700
            char.hp = 0
            wrench3_draw = 0
            lever.image = "tile_0066"

        if boulder.x <= -200 and level == 3:
            wrench3_draw = 0
            lever.image = "tile_0066"

        if bird.y <= 200 and bird.image == "bird2":
            bird.y += 5
            bird.x -= 5

        if bird.y >= 200:
            bird.y = 200
            bird.image = "bird"

        if bird.y == 200:
            bird.x -= 5
        if bird.x <= 400:




            bird.image = "bird3"
            bird.y -= 5
            bird.x -= 5

        if bird.y <= - 10 and bird.image == "bird3":
            bird.x = 700
            bird.y = -100
            bird.image = "bird2"
            col1 = 0

        if bird.colliderect(char) and col1 == 0:
            char.hp -= 1
            col1 = 1
    if house1.hp != 0 and house2.hp != 0 and house3.hp != 0 and level == 2:
        npc.image = "city-npc_st"
        


    if char.colliderect(npc) and level == 2 and npc.image == "city-npc_st" and txt_repeat == 0 and mode == 0:
        sign_show1 = 0
        txt_repeat = 0
        mode = 11
        if space_playing == 0:
            space_playing = 1
            music.set_volume(1.5)
            music.play("space date")
        
        


    

def animations():
    global anim
    global lever_on1
    global move_rope
    global sign_show1
    
    for i in range(len(clouds_list)):
        clouds_list[i].x -= 2
        
        
    if char.hp == 9 and anim == 0:
        heart5.y = 8
        anim = 1
        
    if heart5.y == 8:
        animate(heart5, tween = "bounce_end", duration = 0.5, y = 10)
        
    if char.hp == 8 and anim == 1:
        heart5.y = 8
        anim = 2
        
    if heart5.y == 8:
        
        animate(heart5, tween = "bounce_end", duration = 0.5, y = 10)
    
    if char.hp == 7 and anim == 2:
        heart5.y = 8
        heart4.y = 8
        anim = 3
        
    if heart4.y == 8:
        
        animate(heart5, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart4, tween = "bounce_end", duration = 0.5, y = 10)
        
    if char.hp == 6 and anim == 3:
        heart5.y = 8
        heart4.y = 8
        anim = 4
        
    if heart4.y == 8:
        
        animate(heart5, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart4, tween = "bounce_end", duration = 0.5, y = 10)
    
    if char.hp == 5 and anim == 4:
        heart5.y = 8
        heart4.y = 8
        heart3.y = 8
        anim = 5
        
        
    if heart3.y == 8:
        
        animate(heart5, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart4, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart3, tween = "bounce_end", duration = 0.5, y = 10)
        
    if char.hp == 4 and anim == 5:
        heart5.y = 8
        heart4.y = 8
        heart3.y = 8
        anim = 6
        
        
    if heart3.y == 8:
        
        animate(heart5, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart4, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart3, tween = "bounce_end", duration = 0.5, y = 10)
    
    if char.hp == 3 and anim == 6:
        heart5.y = 8
        heart4.y = 8
        heart3.y = 8
        heart2.y = 8
        anim = 7
        
        
    if heart3.y == 8:
        
        animate(heart5, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart4, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart3, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart2, tween = "bounce_end", duration = 0.5, y = 10)
    
    if char.hp == 2 and anim == 7:
        heart5.y = 8
        heart4.y = 8
        heart3.y = 8
        heart2.y = 8
        anim = 8
        
        
    if heart3.y == 8:
        
        animate(heart5, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart4, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart3, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart2, tween = "bounce_end", duration = 0.5, y = 10)
    
    if char.hp == 1 and anim == 8:
        heart5.y = 8
        heart4.y = 8
        heart3.y = 8
        heart2.y = 8
        heart1.y = 8
        anim = 9
        
        
    if heart3.y == 8:
        
        animate(heart5, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart4, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart3, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart2, tween = "bounce_end", duration = 0.5, y = 10)
        animate(heart1, tween = "bounce_end", duration = 0.5, y = 10)
    
    
    if my_house2.image == "window_animation1":
        my_house2.image = "window_animation2"
    elif my_house2.image == "window_animation2":
        my_house2.image = "window_animation3"
    elif my_house2.image == "window_animation3":
        my_house2.image = "window_animation4"
    elif my_house2.image == "window_animation4":
        my_house2.image = "window_animation5"
    elif my_house2.image == "window_animation5":
        my_house2.image = "window_animation6"
    elif my_house2.image == "window_animation6":
        my_house2.image = "window_animation7"
    elif my_house2.image == "window_animation7":
        my_house2.image = "window_animation8"
    elif my_house2.image == "window_animation8":
        my_house2.image = "window_animation9"
    elif my_house2.image == "window_animation9":
        my_house2.image = "window_animation10"
    elif my_house2.image == "window_animation10":
        my_house2.image = "window_animation11"
    elif my_house2.image == "window_animation11":
        my_house2.image = "window_animation12"
    elif my_house2.image == "window_animation12":
        my_house2.image = "window_animation13"
    elif my_house2.image == "window_animation13":
        my_house2.image = "window_animation14"
    elif my_house2.image == "window_animation14":
        my_house2.image = "window_animation15"
    elif my_house2.image == "window_animation15":
        my_house2.image = "window_animation16"
    elif my_house2.image == "window_animation16":
        my_house2.image = "window_animation17"
    elif my_house2.image == "window_animation17":
        my_house2.image = "window_animation1"
    
    if lever_on1 == 1: 
        
        lever_on1 = 0
        if lever.image == "tile_0066":
            lever.image = "tile_0065"
        elif lever.image == "tile_0065":
            lever.image = "tile_0064"
            move_rope = 1
            

            
            
    if move_rope == 1:
         
        for i in range(len(rope_list1)):
            if rope_list1[i].y >= 0:
                rope_list1[i].y -= 5
            else:
                rope_list1.pop(i)
                break
        for i in range(len(box_list1)):
            if box_list1[i].y >= 0:
                box_list1[i].y -= 5
            else:
                box_list1.pop(i)
                break
        

    for i in range(len(smoke_list1)):
        if level == 2 and house1.hp == 0:
            smoke_list1[i].y -= 5
            if smoke_list1[i].y <= -50:
                smoke_list1[i].y = random.randint(50, 265)
                smoke_list1[i].x = random.randint(20, 130)
        elif level == 2 and house1.hp == 1:
            smoke_list1.pop(i)
            break
           

    for i in range(len(smoke_list2)):
        if level == 2 and house2.hp == 0:    
            smoke_list2[i].y -= 5
            if smoke_list2[i].y <= -50:
                smoke_list2[i].y = random.randint(50, 265)
                smoke_list2[i].x = random.randint(170, 270)
        elif level == 2 and house2.hp == 1:
            smoke_list2.pop(i)
            break
                

    for i in range(len(smoke_list3)):
        if level == 2 and house3.hp == 0:
            smoke_list3[i].y -= 5
            if smoke_list3[i].y <= -50:
                smoke_list3[i].y = random.randint(50, 265)
                smoke_list3[i].x = random.randint(350, 440)
        elif level == 2 and house3.hp == 1:
            smoke_list3.pop(i)
            break
    for i in range(len(grenade_list)):
        if grenade_list[i].image == "grenade2":
            grenade_list[i].image = "boom1"
        elif grenade_list[i].image == "boom1":
            grenade_list[i].image = "boom2"
        elif grenade_list[i].image == "boom2":
            grenade_list[i].image = "boom3"
        elif grenade_list[i].image == "boom3":
            grenade_list[i].image = "boom4"
        elif grenade_list[i].image == "boom4":
            grenade_list[i].image = "boom5"
        elif grenade_list[i].image == "boom5":
            grenade_list[i].image = "boom6"
        elif grenade_list[i].image == "boom6":
            grenade_list[i].y = 600
            grenade_list[i].image = "grenade"
    if level == 6 and wrench3_draw == 1:
        if boulder.image == "boulder":
            boulder.image = "boulder2"
        elif boulder.image == "boulder2":
            boulder.image = "boulder3"
        elif boulder.image == "boulder3":
            boulder.image = "boulder4"
        elif boulder.image == "boulder4":
            boulder.image = "boulder5"
        elif boulder.image == "boulder5":
            boulder.image = "boulder6"
        elif boulder.image == "boulder6":
            boulder.image = "boulder"

        
        
        
        
        





    if level == 2 and sign_show1 == 1 and ex_sign.y == 215:
        ex_sign.y = 212
    elif ex_sign.y == 212:
        ex_sign.y = 215
    
            
    for i in range(len(raindrop_list)):
        raindrop_list[i].y += 8
        if raindrop_list[i].y >= 550:
            raindrop_list[i].x = random.randint(0, 540)
            raindrop_list[i].y = random.randint(-300, 0)

    if move_rope2 == 1:
        for i in range(len(rope_list2)):
            if rope_list2[i].y <= 550:
                rope_list2[i].y += 2
            else:
                rope_list2.pop(i)
                break        
def update(dt):
    jump2()
    controls()
    collisions()
    animations()
    sound()

    



def on_key_down(key):
    global jump_speed
    global jump
    global mode
    global house_showagain
    global old_x
    global old_y
    global key_repeat
    global sign_show1
    global jump_sound
    global jump_sounds_char
    

    if char.colliderect(lock) and d1follow == 1:
        move_rope_sound.play()
    if keyboard.s and char.colliderect(lever) and lever.image == "tile_0066":
        lever_switch.play()
        if level == 1 or level == 5:
            move_rope_sound.play()
    if keyboard.w and jump == 0:
        current_jump = random.choice(jump_sounds_char)
        current_jump.set_volume(0.9)
        jump_speed -= 16
        jump = 1
        current_jump.play()
        jump_sound.play()
        
    if keyboard.f and mode == 1 and level == 0:
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 2
        
        
    elif keyboard.f and mode == 2 and level == 0:
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 0
        house_showagain = "no"
        
    elif keyboard.f and mode == 3 and level == 1:
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 4
    elif keyboard.f and mode == 4 and level == 1:
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 0
        
        
    elif keyboard.f and mode == 5 and level == 1 and key_repeat == "yes":
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 6
        
    elif keyboard.f and mode == 6 and level == 1 and key_repeat == "yes":
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 0
        key_pickup.play()
        key_repeat = "no"
    elif keyboard.f and mode == 6 and level == 1 and key_repeat == "yes":
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 0
        key_repeat = "no"
        
        
    elif keyboard.f and mode == 7 and level == 2:
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 8
        
        
    elif keyboard.f and mode == 8 and level == 2:
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 9
        
    elif keyboard.f and mode ==9  and level == 2:
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 10
    elif keyboard.f and mode ==10  and level == 2:
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 0


    elif keyboard.f and mode == 11:

        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 12



    elif keyboard.f and mode == 12:
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        mode = 13
    elif keyboard.f and mode == 13:
        enter_b.y = 268
        animate(enter_b, tween = "bounce_end", duration = 0.5, y =270)
        
        mode = -3
        
        

        

def on_mouse_down(button, pos):
    global mode
    global key
    global k1follow
    global w1follow
    global d1follow
    global house_showagain
    global level
    global jump_speed
    global jump
    global touch
    global k1follow
    global open_d1
    global read_txt
    global old_x
    global lever_on1
    global move_rope
    global key_repeat
    global bg_img
    global sign_show1
    global night_filter
    global platform_draw
    global gravity
    global ladder1
    global move_rope2
    global repair 
    global move_box2
    global move_chain2
    global gren1, gren2, gren3, gren4
    global wrench3_draw
    global col1
    global right, img, anim, old_y, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7
    global txt_repeat
    global space_playing
    if mode == -2 and start.collidepoint(pos):
        mode = 0
        music.set_volume(1.5)
        music.play("space date")

    if mode == -1 and yes_b.collidepoint(pos):
        music.set_volume(1.5)
        music.play("space date")
        bg_img = 0
        char.x = 200
        char.y = 265
        char.hp = 10
        lever.x = 25
        lever.y = 138
        plane.x = 600
        plane.y = 30
        boulder.x = 680
        boulder.y = 175
        bird.x = 700
        bird.y = -100
        mode = 0
        level = 0
        key = 0
    if k1follow == 1:
        k1follow = 0
        key1.x = 235
        key1.y = 35
    if w1follow == 1:
        w1follow = 0
        wrench.x = 82
        wrench.y = 305
    if w1follow == 2:
        w1follow = 0
        wrench2.x = 20
        wrench2.y = 25
    if w1follow == 3:
        w1follow = 0
        wrench3.x = 30
        wrench3.y = 215
    if d1follow == 1:
        d1follow = 0
        diamond.x = 66
        diamond.y = 27
        


    elif mode == -1 and no_b.collidepoint(pos) or mode == -3 and yes_b.collidepoint(pos):
        space_playing = 0
        char.x = 200
        char.y = 265
        txt_repeat = 0
        char.hp = 10
        lever.x = 25
        lever.y = 138
        wrench.x = 82
        wrench.y = 305
        wrench2.x = 20
        wrench2.y = 25
        wrench3.x = 30
        wrench3.y = 215
        diamond.x = 66
        diamond.y = 27
        plane.x = 600
        plane.y = 30
        boulder.x = 680
        boulder.y = 175
        bird.x = 700
        bird.y = -100
        b_press.image = "tile_0148"

        mode = -2
        key = 0
        jump = 0
        right = 0
        img = 0
        house_showagain = "yes"
        key_repeat = "yes"
        level = 0
        anim = 0
        old_x = 0
        old_y = 0
        touch = 0
        key = 0
        bg_img = 0
        k1follow = 0
        d1follow = 0
        w1follow = 0
        open_d1 = 0
        read_txt = 0
        lever_on1 = 0
        wrench3_draw = 0
        night_filter = 0
        platform_draw = 0
        ladder1 = 0
        repair = 0
        sign_show1 = 1
        gren1 = 0
        gren2 = 0
        gren3 = 0
        gren4 = 0
        col1 = 0
        lever.image = "tile_0066"
        door_cl.image = "door_cl"
        npc.image = "city-npc_st2"
        key1.x = 235
        key1.y = 35
        music.set_volume(0.2)
        music.play("uptown dancing")




        x = 520
        y = 10

        x1 = 30
        y1 = 45
        x2 = 35
        y2 = 27
        x3 = 35
        y3 = 9
        x4 = 48
        y4 = 48
        x5 = 118
        y5 = 224
        x6 = 513
        y6 = 10
        x7 = 48
        y7 = -80


            
        for i in range(10):
            if move_rope == 1:
                rope = Actor("tile_0089", (x, y))
                rope_list1.append(rope)
                y += 18
                
            
        for i in range(3):
            if move_rope == 1:
                box = Actor("tile_0029", (x, y))
                box_list1.append(box)
                y +=18
                if i == 2:
                    move_rope = 0
            
            
        for i in range(10):
            if house1.hp != 0:

                smoke = Actor("smoke", (random.randint(20,130), random.randint(50, 265)))
                smoke_list1.append(smoke)
                if i == 9:
                    house1.hp = 0
            
            
        for i in range(10):
            if house2.hp != 0:
                smoke = Actor("smoke", (random.randint(170,270), random.randint(50, 265)))
                smoke_list2.append(smoke)
            if i == 9:
                    house2.hp = 0
            
        for i in range(10):
            if house3.hp != 0:

                smoke = Actor("smoke", (random.randint(350,440), random.randint(50, 265)))
                smoke_list3.append(smoke)
            if i == 9:
                    house3.hp = 0

            
        for i in range(3):
            if move_rope2 != 0:

                box = Actor("tile_0029", (x5, y5))
                rope_list2.append(box)
                y5 += 18
        for i in range(10):
            if move_rope2 != 0:
                rope = Actor("tile_0089", (x5, y5))
                rope_list2.append(rope)
                y5 += 18
                if i == 9:
                    move_rope2 = 0


        for i in range(3):
            if move_box2 != 0:

                box = Actor("tile_0029", (x6, y6))
                box_list2.append(box)
                y6 += 18
                if i == 2:
                    move_box2 = 0

        for i in range(8):
            if move_chain2 != 0:

                chain = Actor("tile_0131", (x7, y7))
                chain_list1.append(chain)
                y7 += 18
                if i == 7:
                    move_chain2 = 0
        for i in range(len(arrow_list)):
            arrow_list[i].x = -40
            arrow_list[i].y = random.randint(20, 530)
        yes_b.x = 200
        yes_b.y = 300
        
        
        

        

    
    
    




pgzrun.go()






