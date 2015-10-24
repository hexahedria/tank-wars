#
# A class to represent one Tank in our Tank Wars Game
#
# MuddHacks 2015
#

from tank_ais import AIManager
from bullet import Bullet

class Tank:

	def __init__(self, ID, AIpath, perma_board_copy, x_pos, y_pos, 
		               x_vel = 0,
					   y_vel = 0,
		 			   hp    = 30,
		               ammo  = 100000):
		self.AI = AIManager(AIpath, perma_board_copy)
		self.ID    = ID
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.x_vel = x_vel
		self.y_vel = y_vel

		self.hp = hp
		self.ammo = ammo

		self.recently_healed = false
		self.damage_IDs = []

	def take_turn(tank_coords):
		state = [tank_coords, self.hp, self.ammo, [self.x_pos, self.y_pos], self.damage_IDs]
		turn_info = AIManager.takeTurn(state)

		# set the tanks speed
		new_x_vel = turn_info[0][0]
		new_y_vel = turn_info[0][1]
		speed = math.sqrt(new_x_vel**2 + new_y_vel**2)
		if speed > MAX_TANK_SPEED:
			new_x_vel = new_x_vel*MAX_TANK_SPEED/speed
			new_y_vel = new_y_vel*MAX_TANK_SPEED/speed
		self.x_vel = new_x_vel
		self.y_vel = new_y_vel

		# make a bullet if necessary
		if len(turn_info) > 1 and self.ammo > 0:
			self.ammo -= 1
			b_x_vel = turn_info[1][0]
			b_y_vel = turn_info[1][1]
			b_x_pos = self.x_pos + b_x_vel*MAX_TANK_RADIUS
			b_y_pos = self.y_pos + b_y_vel*MAX_TANK_RADIUS
			return Bullet(b_x_pos,b_y_pos,b_x_vel,b_y_vel)

	def is_dead():
		""" tells you if the tank is dead """
		return self.hp <= 0

	def damage(dm):
		""" damages the tank """
		self.hp -= dm

	def heal(rate,dt):
		""" heals the tank if its standing on the hospital """
		self.hp 

	def move(dt):
		""" updates the position of the tank"""
		self.x_pos += x_vel*dt
		self.y_pos += y_vel*dt

	def get_pixel_pos():
		""" returns a list of points """
		top = int(self.y_pos)
		bottom = int(self.y_pos + 1)
		left = int(self.x_pos)
		right = int(self.x_pos + 1)

		upper_left  = [int(self.x_pos)  , int(self.y_pos)  ]
		upper_right = [int(self.x_pos+1), int(self.y_pos)  ]
		lower_left  = [int(self.x_pos)  , int(self.y_pos+1)]
		lower_right = [int(self.x_pos+1), int(self.y_pos+1)]

		return [upper_left,upper_right,lower_left,lower_right]

	
