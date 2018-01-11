from sys import exit
from random import randint
class Engine(object):
	def __init__(self,scene):
		self.scene=scene
	def play(self):
		current_scene=self.scene.opening_scene()
		while True:
			print "\n-------------"
			next_scene_name=current_scene.enter()
			current_scene=self.scene.next_scene(next_scene_name)

class MainRoad(object):
	def enter(self):
		print "You are standing on a fully crowded road on such a busy day."
		print "You start walking towards a shop with the aim of stealing some food product"
		print "The shopkeeper catches you shoplifting and gives you off to his pet monster"
		print "Now you are present in a dark room with a hungry monster regurgitating fire at you."
		print "1) You fly off up in the air faster than the dragon could move its neck, and cut it off into 2 pieces with your big nails."
		print "2) You don't want to kill the poor creature and try negotiating with it"
		print "3) You sit there and await your death like an idiot that you are."
		choice=int( raw_input(">"))
		while not(choice>=1 and choice<=3):
			print "Man! enter a number from 1 to 3 only :("
			choice = int(raw_input(">"))
		if choice==1:
			print 'You safely get out of the place,only to find teachers standing outside the shop who take you back to your class :|'
			return 'class'
		elif choice == 2:
			print "Seriously! you try negotiaiting with a hungry dragon ! You're dead"
			return 'death'
		else:
			print "Great! just give up like you always do"
			return 'death'

class Death(object):
	list=['You seriously are  big loooser, gear up for the next time bro!',
	'You died.... Not that you were ever alive  ',
	'You couldn\'t even win in your dream! Great man']
	def enter(self):
		print Death.list[randint(0,len(self.list)-1)]
		exit(1)

class Class(object):
	def enter(self):
		print "You are sitting in your maths class and your monstrous professor is firing formulae with his gun"
		print "He humiliates you like always."
		print "You get furious and answer him back."
		#for i in (1,10000)
		print "He takes out his butcher knife. Damn! you always knew he had a part time job"
		print "Bell rings and everyone rushes out (including you)"
		print "Coward!"
		print "1)You decide to teach the teacher a lesson and go to the proff's house."
		print "2)You forgive the teacher and forget the incident"
		print "3)You go and apologise to the teacher and ask him out for drinks"
		choice= int(raw_input(">"))
		while not(choice>=1 and choice<=3):
			print "Man! enter a number from 1 to 3 only :("
			choice =int( raw_input(">"))
		if choice==1:
			return 'faculty_house'
		elif choice == 2:
			print "Seriously! the teacher complains against you, and the Diretor orders your execution."
			print "You're dead"
			return 'death'
		else:
			print "You and the teacher become good friends and he tells you to call him Tom."
			print "You go to get drinks together at a local bar:)"
			return 'bar'

class FacultyHouse(object):
	def enter(self):
		print "You use your special skills and sneak into the house of the teacher without him knowing"
		print "The teacher is drinking wine lying on the couch"
		print "1) Sneak quietly and kill him without him knowing"
		print "2) Reveal yourself and have a proper fight"
		choice = int(raw_input(">"))
		while not(choice>=1 and choice<=3):
			print "Man! enter a number from 1 to 2 only :("
			choice =int(raw_input(">"))

		if choice == 1:
			print "You get in reveal yourself and shout that you are gonna have your revenge."
			print "The teacher gets up and starts growing in size, laughing"
			print "You take out your gun and war begins"
			print "The teacher uses his magnet to take you gun away and starts firing it at you"
			print "You use your shield to defend and there's a small gap after a specific number of fires."
			print "1st after 1 blow, then 2 then 3 then 5, then 8 and then after 13 fires there's a small gap"
			print "Now, after how many fires do you take the shield down?"
			c=int(raw_input(">"))
			if c != 21:
				print "No! you lose to your maths teacher"
				return 'death'
			else:
				print "You safely defend and attack later after 21 fires."
				print "The teacher is injured, on the ground and asking for mercy"
				print "You go to him look him in the eye"
				print "And..... shoot him dead"
				return 'win'

		else:
			print "The teacher goes to sleep and you silently follow him"
			print "You see the evil teacher sleeping peacefully with such a pacifist face"
			print "He looks like a small baby"
			print "You recall all the insults he did"
			print "And stab him directly in the heart"
			print "You do a million holes in his body and leave the house with a biiig smile (:"
			return 'police'

class Bar(object):
	def enter(self):
		print "You and Tom together come to a bar where both of you drink till you become tighhhhhhht"
		print "Tom goes out of control and you try your best to control him from getting into trouble"
		print "Thats when the college bully enters the bar and starts to order everyone "
		print "\'Not this time\' You think"
		print "The bully comes to you and tells you to vacate the seat for him"
		print "You look him in the eye and tell him to fuck off giving him the hardest blow you could have ever given"
		print "The bully turns around and starts shouting to the top of his voice"
		print "Within seconds, the room is filled with hundreds of his clones, who are about 100 times stronger than him"
		print "\'You take the ones on the left\' Tom says"
		print "You and Tom start fighting the bullies"
		print "Remembering the previous humiliations, you start hitting each bully with full force, killing most"
		print "You had nearly killed all when you see the bully has captured Tom"
		print "The bully is about to kill him when Tom says:"
		print "\'ivefiay\'\n What number is this in pig latin?"
		ch=int(raw_input(">"))
		if ch !=5:
			print "Tom is killed and and then the bully turns towards you :("
			return 'death'
		else:
			print "You press 5 on Tom's watch, and boom! a bullet comes out of his sleeve straight into the bully's head"
			return 'win'

class win(object):
	def enter(self):
		print "Bravo! you win,(only in your dream) \n You are a failure in your exam :( SHAME"
		exit(1)

class Begin(object):
	def enter(self):
		print "You are sitting in your chemistry exam and don't know what to write."
		print "You close your eyes for a few seconds"
		print "Next, you are standing outside your hostel and you feel a different power in you"
		print "You jump and realise that you can fly"
		print "You understand you are in your sleep and you can do anything"
		print "You want to go out of the college gate and enjoy outside"
		print "1) Yeah, go on outside"
		print "2) No, you just wake up to give the test"
		choice = int(raw_input(">"))
		print choice
		if choice == 1 :
			return 'main_road'
		elif choice == 2:
			return 'death'
		#print "Man! enter a number from 1 to 2 only :("
		#	choice = raw_input(">")


class Map(object):
	scenes= {'death':Death(),'main_road':MainRoad(),'class':Class(),'faculty_house':FacultyHouse(),'bar':Bar(),'win':win(),'begin':Begin()}
	def __init__(self,start_scene):
		self.start_scene=start_scene
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map=Map('begin')
a_game=Engine(a_map)
a_game.play()