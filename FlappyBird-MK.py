import pygame, sys
import random

pygame.init()

# Defining some colors
BLACK = (0, 0, 0)

# Setting the width and height of the screen [width, height]
width = 900
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)
window = screen.get_rect()

# Defining some variables for game functionality
score_add = True # variable to indicate when to add a point
score = 0
highscore = 0
wallx = 840 # starting width of the walls (pipes)
birdy = 288 # starting height of the bird
gap = 60 # variable to manipulate the gap between walls(pipes). The actual gap is 2 times gap
offset_var = 50 # variable determining the range for the random generation of the offset
offset = random.randint(-offset_var, offset_var) # randomly generating the offset variable (the higher it is the bigger distance between consecutive gaps)
wallspeed = 0.5 # the speed at which the walls are moving to the left of the screen

# Defining the walls that the bird has to move through and the bird itself
wallup = pygame.image.load("top.png").convert_alpha() #Source: http://www.palmentieri.it/flappyjam/pipe.png
walldown = pygame.image.load("bottom.png").convert_alpha() #Source: http://www.palmentieri.it/flappyjam/pipe.png
bird = pygame.image.load("bird.png").convert_alpha() #Source: http://www.ellison.rocks/clumsy-bird/data/img/bg.png
birdRect = pygame.Rect(435, birdy, bird.get_width(), bird.get_height()) # getting rectangles of all images to make mathematics and collision correct
wallupRect = pygame.Rect(wallx, (-200 - gap + offset), wallup.get_width(), wallup.get_height())
walldownRect = pygame.Rect(wallx, (300 + gap + offset), walldown.get_width(), walldown.get_height())

# Setting the caption for the game
pygame.display.set_caption("FlappyBird the Game by Milosz Kadziela")

# Loading the image that will be used as the game background
background_image = pygame.image.load("bg.png").convert_alpha()

# Defining some fonts that will be used in the messages below
font = pygame.font.Font('freesansbold.ttf', 24) #d efining smallest font that will be used for controls description
font2 = pygame.font.Font('freesansbold.ttf', 32) # defining a bigger font that will be used for main directional messages
font3 = pygame.font.Font('freesansbold.ttf', 40) # defining even bigger font that will be used for the main_menu title of the game
font4 = pygame.font.Font('freesansbold.ttf', 50) # defining the biggest for that will be used for "top of the screen" messages

# Defining some messages that will be displayed on the screen throughout the gameplay (directional messages - key instuctions)
controls_msg = font2.render("'C' - Controls", True, BLACK)
quit_msg = font2.render("'Q' - Quit", True, BLACK)
menu_msg = font2.render("'M' - Menu", True, BLACK)
restart_msg = font2.render(" 'R' - Restart", True, BLACK)
game_msg = font2.render("'P' - Play", True, BLACK)
back_msg = font2.render("'B' - Back", True, BLACK)

# Defining some other messages that will be visible in the game
name_msg = font3.render("FlappyBird the Game by Milosz Kadziela", True, BLACK)
gameover_msg = font4.render("Game Over!", True, BLACK)
controls_heading_msg = font2.render("Controls:", True, BLACK)
controls_description_msg = font.render("To fly the bird use 'SPACEBAR'", True, BLACK)
score_msg = font.render("Score: ", True, BLACK)
highscore_msg = font.render("Highscore: ", True, BLACK)
diff_heading_msg = font4.render("Choose the diffuculty:", True, BLACK)
diff1_msg = font.render("'1' - Easy ", True, BLACK)
diff2_msg = font.render("'2' - Medium ", True, BLACK)
diff3_msg = font.render("'3' - Hard ", True, BLACK)


def update():
	'''Function responsible for conroling the movement of the walls, generating the gap, controlling the movement of the bird
	adding score and restating the position of walls when they reacg the left side of the screen'''
	global wallx, wallspeed, wallup, walldown, score, score_add, offset, x, wallupRect, walldownRect, birdy, birdRect, score_msg
	wallx -= wallspeed
	birdy += 0.2
	wallupRect = pygame.Rect(wallx, (-200 - gap + offset), wallup.get_width(), wallup.get_height())
	walldownRect = pygame.Rect(wallx, (300 + gap + offset), walldown.get_width(), walldown.get_height())
	birdRect = pygame.Rect(435, birdy, bird.get_width(), bird.get_height())
	if score_add == True:
		if wallx < 450:
			score += 1
			score_add = False
	if wallx < 0:
		score_add = True
		offset = random.randint(-offset_var, offset_var)
		wallx = 900

# Variable used to manage how fast the screen updates
clock = pygame.time.Clock()

# Setting the starting value for the variable which is used to navigate through modules in MainLoop
gamestate = "Menu"

# HERE STARTS THE PROGRAM MAIN LOOP CONTAINING 5 SUB-LOOPS FOR MENU PURPOSES AND THE LIVE GAME
while True:
	# --- MainLoop ---
	while gamestate == "Menu":
		# Event loop displaying Menu window
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				if event.key == pygame.K_c:
					gamestate = "Controls"
				if event.key == pygame.K_p:
					gamestate = "Settings"
			if event.type == pygame.QUIT:
				sys.exit()

		screen.blit(background_image, [0,0]) #sets the image as the background
		screen.blit(name_msg, [60, 100]) #blicts the message in the middle of the screen
		screen.blit(game_msg, [380, 200]) #blits the message in the middle of the screen
		screen.blit(controls_msg, [50,530]) #blits the message to bottom left corner
		screen.blit(quit_msg, [705, 530]) #blits the message to bottom right corner

		# Updating the screen
		pygame.display.flip()

		# Limiting to 60 frames per second
		clock.tick(60)

	while gamestate == "Settings":
		# Event loop displaying Difficulty_settings window
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				if event.key == pygame.K_1:
					offset_var = 50
					wallspeed = 0.5
					gamestate = "Game"
				if event.key == pygame.K_2:
					offset_var = 100
					wallspeed = 0.7
					gamestate = "Game"
				if event.key == pygame.K_3:
					offset_var = 200
					wallspeed = 0.9
					gamestate = "Game"
				if event.key == pygame.K_b:
					gamestate = "Menu"
			if event.type == pygame.QUIT:
				sys.exit()

		screen.blit(background_image, [0, 0])
		screen.blit(diff_heading_msg, [175, 50])
		screen.blit(diff1_msg, [380, 160])
		screen.blit(diff2_msg, [365, 200])
		screen.blit(diff3_msg, [380, 240])
		screen.blit(back_msg, [705, 530])

		pygame.display.flip()
		clock.tick(60)

	while gamestate == "Controls":
		# Event loop displaying Controls window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_m:
					gamestate = "Menu"

		screen.blit(background_image, [0, 0])
		screen.blit(menu_msg, [50, 530])
		screen.blit(controls_heading_msg, [400,50])
		screen.blit(controls_description_msg, [270,300])

		pygame.display.flip()

		clock.tick(60)

	while gamestate == "Game":
		# --- Live game loop ---
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				if event.key == pygame.K_SPACE:
					birdy -= 60

		# Declaring the collision statement check. To see if the bird has collided with any of the walls
		if birdRect.colliderect(wallupRect) or birdRect.colliderect(walldownRect):
			gamestate = "Gameover"
		# Declaring the collision statement check. To see if the bird has collided with the top or bottom of the screen
		# +20 and -20 to make it eaier to go through gaps that generate just at the top or bottom of the screen on the highest difficulty
		if birdRect.top < window.top - 20 or birdRect.bottom > window.bottom + 20:
			gamestate = "Gameover"
		update()

		score_msg = font2.render("Score: " + str(score), True, BLACK)

		screen.blit(background_image, [0, 0])
		screen.blit(wallup, (wallx, (-200 - gap + offset))) # blitting the screen with the upper wall
		screen.blit(walldown, (wallx, (300 + gap + offset))) # blitting the screen with the bottom wall
		screen.blit(bird, (435, birdy)) # blitting the screen with the bird
		screen.blit(score_msg, [400, 20]) # blitting the screen with the "live-updated" score msg at the top of the screen

		pygame.display.flip()

	while gamestate == "Gameover":
		# Event loop displaying Gameover window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_m:
					wallx = 900
					birdy = 288
					score = 0
					update()
					gamestate = "Menu"
				if event.key == pygame.K_r:
					wallx = 900 # setting the position of bird and walls to the original, so that user gets a fresh start when they hit restart
					birdy = 288
					score = 0
					update()
					gamestate = "Game"

		# condition for potential change of the highscore if the player surpasses the previous best
		if score > highscore:
			highscore = score
		score_msg = font.render("Score: " + str(score), True, BLACK)
		highscore_msg = font.render("Highscore: " + str(highscore), True, BLACK)

		screen.blit(background_image, [0, 0])
		screen.blit(menu_msg, [685, 530])
		screen.blit(restart_msg, [50,530])
		screen.blit(gameover_msg, [300, 120])
		screen.blit(score_msg, [400, 200])
		screen.blit(highscore_msg, [375, 240])

		pygame.display.flip()

		clock.tick(60)
# Close the window and quit
pygame.quit()