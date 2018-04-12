#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Misc module

import people
import verbs
import names 

from random import *
from util import *
		
class Events(WordList):
	def __init__(self):
		super().__init__(['Ash Wednesday',
		'Christmas Eve',
		'Easter Sunday',
		'Friday',
		'Halloween',
		'Highschool Graduation',
		'Homecoming',
		'Hump Day',
		'Independence Day',
		'International Women\'s Day',
		'Junior Prom',
		'Mardis Gras',
		'Mother\'s Day',
		'my anniversary',
		'my birthday',
		'my wedding day',
		'New Year\'s Eve',
		'Spring Break',
		'St. Patrick\'s Day',
		'Superbowl Sunday',
		'teacher planning day',
		'Valentine\'s Day'])
		
	def RemoveMy(self, sWord):
		return sWord.replace('my ','')
		
	def GetWord(self, bRemoveMy = False):
		sEvent = ""
		
		sEvent = super().GetWord()
			
		if bRemoveMy:
			sEvent = self.RemoveMy(sEvent)
			
		return sEvent
		
class MaleSO(WordList):
	def __init__(self):
		super().__init__(['boyfriend',
			'fiancé',
			'hubby',
			'husband'])
			
class FemaleSO(WordList):
	def __init__(self):
		super().__init__(['bride',
			'girlfriend',
			'fiancé',
			'wife'])
		
class Hashtags(WordList):
	def __init__(self):
		super().__init__(['50shades',
			'amwriting',
			'BDSM',
			#'bitcoin',
			#'blockchain',
			'bot',
			'botally'
			'botlife',
			'botlove',
			'eartg',
			'eartg',
			'erotica',
			'erotica',
			'fantasy',
			'fiftyshades',
			'filthy',
			#'litecoin',
			'lovestory',
			'lprtg',
			'lprtg',
			'mrbrtg',
			'naughty',
			'nsfw',
			'PleaseRT',
			'scifi',
			'romance',
			'smut',
			'sorrynotsorry',
			'ssrtg',
			'ssrtg',
			'taboo',
			'truelove',
			'twitterbot',
			'twitterbot',
			'wprtg'])
		
class BadGirlNames(NounAdjList):
	DefaultNoun = 'slut'
	DefaultAdj = 'little'
	
	NounList = ['hussy',
		'minx',
		'nympho',
		'skank',
		'slut',
		'slut',
		'slut',
		'tart',
		'tramp',
		'trollop',
		'whore',
		'whore']
		
	AdjList = ['brazen',
		'cheeky',
		'filthy',
		'little',
		'nasty',
		'outrageous',
		'saucy',
		'shameless',
		'wanton']
		
class SexyAdjs(WordList):
	def __init__(self):
		super().__init__(['dirty',
		'erotic',
		'filthy',
		'hot',
		'kinky',
		'naughty',
		'sexy',
		'sensual',
		'steamy',
		'taboo'])

class BookSellers(WordList):
	def __init__(self):
		super().__init__(['Apple Books',
			'Amazon',
			'B&N',
			'Kindle Unlimited',
			'Kobo',
			'Radish Fiction',
			'Smashwords',
			'WattPad'])
			
class BookGirlsBasic(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Blonde',
			'Bride',
			'Bride',
			'Bridesmaid',
			'Brunette',
			'Co-ed',
			'Girlfriend',
			'Housewife',
			'Lady',
			'Latina',
			'Lesbian',
			'Maid',
			'Maiden',
			'Momma',
			'Redhead',
			'Sisters',
			'Step-Daughter',
			'Submissive',
			'Teacher',
			'Wallflower',
			'Waitress',
			'Wife',
			'Woman'])
			
class BookGirls(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Airline Stewardess',
			'Amateur Porn Star',
			'Amish Maiden',
			'Anal Virgin',
			'Babysitter',
			'Bad Girl',
			'Bikini Model',
			'Bimbo',
			'Brat',
			'BBW',
			'Call-Girl',
			'College Girl',
			'Concubine',
			'Dancer',
			'Dominatrix',
			'Escort',
			'Fashion Model',
			'Farmer\'s Daughter',
			'Flight Attendant',
			'Futa',
			'Governess',
			'Handmaiden',
			'Harem Girl',
			'Hotwife',
			'House Maid',
			'Flight Attendant',
			'French Maid',
			'Librarian',
			'Lingerie Model',
			'Masseuse',
			'Mature Woman',
			'MILF',
			'Milk Maid',
			'Nanny',
			'Nurse',
			'Older Woman',
			'Pastor\'s Wife',
			'Porn Star',
			'Princess',
			'Princess',
			'Secretary',
			'Secretary',
			'Sex Slave',
			'Sex Surrogate',
			'Sex Witch',
			'Schoolgirl',
			'Single Mom',
			'Small-Town Girl',
			'Slut',
			'Starlet',
			'Submissive',
			'Supermodel',
			'Twin Sisters',
			'Virgin',
			'Wet Nurse',
			'Whore'])
			
class BookGirlAdjs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Amish',
		'Anal',
		'Asian',
		'Asian',
		'Attractive',
		'Bashful',
		'BBW',
		'Beautiful',
		'Bi-Curious',
		'Black',
		'Black',
		'Blonde',
		'Buxom',
		'Chaste',
		'Christian',
		'Christian',
		'Conservative',
		'Country',
		'Curvy',
		'Desperate',
		'Divorced',
		'Ebony',
		'Erotic',
		'Fairy',
		'Fertile',
		'Gorgeous',
		'Harem',
		'High-Heeled',
		'Hot',
		'Hot',
		'Innocent',
		'Innocent',
		'Kept',
		'Kinky',
		'Lactating',
		'Latex-Clad',
		'Leather-Clad',
		'Leggy',
		'Lesbian',
		'Married',
		'Naked',
		'Naked',
		'Naughty',
		'Nubile',
		'Nude',
		'Nudist',
		'Nursing',
		'Petite',
		'Pregnant',
		'Promiscuous',
		'Sassy',
		'Servant',
		'Sex',
		'Sexy',
		'Sexy',
		'Shy',
		'Single',
		'Skinny',
		'Slutty',
		'Small-Town',
		'Submissive',
		'Taboo',
		'Teen',
		'Teenage',
		'Virgin',
		'Virgin',
		'Virgin',
		'Virginal',
		'Voluptuous',
		'Willing',
		'Young'])
		
class BookGirlCompAdjs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Bad Girl',
		'Ballerina',
		'BBW',
		'Big Titty',
		'Bimbo',
		'Call-Girl',
		'Co-ed',
		'Concubine',
		'Dancer',
		'Dominatrix',
		'Futa',
		'Hotwife',
		'Lesbian',
		'MILF',
		'Redhead',
		'Servant',
		'Single Mom',
		'Submissive',
		'Supermodel',
		'Teen'])
		
class BookMastersBasic(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Alpha',
			'Artist',
			'Athlete',
			'Boyfriend',
			'Dad',
			'Daddy',
			'Family Man',
			'Father-in-Law',
			'Freshman',
			'Gentleman',
			'Hipster',
			'Husband',
			'Preacher',
			'President',
			'Prince',
			'Roommate',
			'Step-Dad',
			'Widower'])

class BookMasters(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Alpha Male',
			'Alpha Wolf',
			'Astronaut',
			'Assassin',
			'Bachelor',
			'Barbarian',
			'BBC',
			'Biker',
			'Billionaire',
			'Bitcoin Billionaire',
			'Bodyguard',
			'Boss',
			'Boxer',
			'Breeding Stud',
			'Bull Rider',
			'CEO',
			'Centaur',
			'Centaur',
			'Count',
			'Cop',
			'Cowboy',
			'Dad',
			'Daddy',
			'Daddy Dom',
			'Defensive Lineman',
			'Dildo Designer',
			'Dinosaur',
			'Doctor',
			'Dom',
			'Dominatrix',
			'Duke',
			'Duke',
			'Fire Fighter',
			'Futanari',
			'Gangsta',
			'Gay-for-Pay Porn Star',
			'Gazillionaire',
			'Gentleman',
			'Gladiator',
			'Goat Man',
			'Guitar Player',
			'Hitman',
			'Incubus',
			'Jet Fighter Pilot',
			'Jock',
			'Killer-for-Hire',
			'King',
			'King',
			'King',
			'Kingpin',
			'Knight',
			'Lawyer',
			'Lesbian Cheerleader',
			'Lesbian Dominatrix',
			'Lesbian MILF',
			'Lipstick Lesbian',
			'Lumberjack',
			'Older Man',
			'Olympic Gold Medalist',
			'Outlaw',
			'Male Escort',
			'Male Stripper',
			'Man-o-taur',
			'Manor Lord',
			'Man-telope',
			'Man-ticore',
			'Marquis',
			'Mer-man',
			'MMA Fighter',
			'Millionaire',
			'Mob Boss',
			'Mountain Man',
			'Multi-Millionaire',
			'Navy Seal',
			'Pirate Captain',
			'Playboy Billionaire',
			'Pope',
			'Porn Star',
			'President',
			'Prime Minister',
			'Prince',
			'Prince',
			'Prince',
			'Professor',
			'Quarterback',
			'Rock Star',
			'Shah',
			'Secret Agent',
			'Sex Addict',
			'Sex Warlock',
			'Sheikh',
			'Sheriff',
			'Single Dad',
			'Sorcerer',
			'Spy',
			'Stallion',
			'Sugar Daddy',
			'Sultan',
			'Surfer',
			'Heart Surgeon',
			'Tentacle Monster',
			'Trillionaire',
			'Viking',
			'Uniporn',
			'Vampire',
			'Violinist',
			'Voyeur',
			'Warrior',
			'Werewolf'])
			
class BookMasterGangs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Baby Daddies',
			'Bandits',
			'Barbarians',
			'Basketball Team',
			'Biker Gang',
			'Billionaires Club',
			'Boy\'s School',
			'Brothers',
			'Cops',
			'Cowboys',
			'Football Team',
			'Gangstas',
			'Goat Men',
			'Herd of Centaurs',
			'Hockey Team',
			'Identical Twin Brothers',
			'Lesbian Harem',
			'Mer-men',
			'Mongol Horde',
			'Mountain Men',
			'Navy Seals',
			'Pirates',
			'Rock Band',
			'Seal Team Six',
			'S.W.A.T. Team',
			'Scottsmen',
			'Viking Hoard',
			'Vampire Coven',
			'Werewolf Pack'])
			
class BookMasterAdjs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Alpha',
			'Athletic',
			'Australian',
			'Bad Boy',
			'Bald',
			'Bearded',
			'Beefcake',
			'Black',
			'BDSM',
			'Brooding',
			'Charming',
			'Cocky',
			'Cuckolded',
			'Dominant',
			'Ebony',
			'Eligible',
			'Famous',
			'French',
			'Gang-Bang',
			'Geeky',
			'Ghost',
			'Hairy',
			'Handsome',
			'Handsome',
			'Highlander',
			'Horny',
			'Hung',
			'Irish',
			'Italian',
			'Kinky',
			'Leather',
			'Mustachioed',
			'Naked',
			'Norwegian',
			'Nudist',
			'Older',
			'Pantsless',
			'Playboy',
			'Rebel',
			'Reckless',
			'Renegade',
			'Rock-Hard',
			'Royal',
			'Savage',
			'Scottish',
			'Secret',
			'Sexy',
			'Shape-Shifting',
			'Shameless',
			'Silver Fox',
			'Space',
			'Spanish',
			'Stay-at-Home',
			'Strapping',
			'Strong',
			'Tall',
			'Tattooed',
			'Visibly Erect',
			'Wealthy',
			'Well-Hung',
			'Well-Endowed',
			'Wicked',
			'Widowed'])
			
class BookMasterCompAdjs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Astronaut',
			'Bitcoin Billionaire',
			'Biker',
			'Billionaire',
			'Boxer',
			'Centaur',
			'Cowboy',
			'Defensive Lineman',
			'Dinosaur',
			'Fire Fighter',
			'Futanari',
			'Gazillionaire',
			'Goat Man',
			'Guitar Player',
			'Hitman',
			'Lawyer',
			'Mer-man',
			'Millionaire',
			'MMA Fighter',
			'Mountain Man',
			'Multi-Millionaire',
			'Navy Seal',
			'Older Man',
			'Olympic Gold Medalist',
			'Outlaw',
			'Pirate',
			'Porn Star',
			'Rock Star',
			'Sex Addict',
			'Single Dad',
			'Stripper',
			'Surfer',
			'Heart Surgeon',
			'S.W.A.T. Team',
			'Trillionaire',
			'Viking',
			'Violinist',
			'Voyeur',
			'Werewolf'])
			
class BookVerbsBy(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Anally Deflowered',
			'Annally Deflowered in Public',
			'Beaten',
			'Blackmailed',
			'Bound',
			'Bred',
			'Broken',
			'Captured',
			'Caught on Video',
			'Claimed',
			'Claimed',
			'Claimed Hard',
			'Claimed in Public',
			'Collared',
			'Conquered',
			'Chained',
			'Charmed',
			'Cuckolded',
			'Cuddled',
			'Cuddled Hard',
			'Deflowered',
			'Deflowered',
			'Deflowered in Public',
			'Dominated',
			'Enslaved',
			'Exposed in Public',
			'Forced',
			'Hotwifed',
			'Humiliated',
			'Hunted For Food',
			'Hypnotized',
			'Impregnated',
			'Knocked Up',
			'Leashed',
			'Mastered',
			'Mind-Controlled',
			'Owned',
			'Paddled',
			'Pleasured',
			'Pleasured in Public',
			'Punished',
			'Punished in Public',
			'Ravished',
			'Ruled',
			'Seduced',
			'Sexually Harrassed At My Workplace',
			'Sold',
			'Sold',
			'Spanked',
			'Spanked in Public',
			'Shaved',
			'Stripped',
			'Stripped in Public',
			'Taken',
			'Taken',
			'Taken Hard',
			'Taken Hard in Public',
			'Taken in Public',
			'Tamed',
			'Tempted',
			'Trained',
			'Secretly Watched',
			'Violated',
			'Whipped'])
			
class BookVerbsTo(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Bred',
				'Bound',
				'Chained',
				'Engaged',
				'Enslaved',
				'Gifted',
				'Hotwifed',
				'Married',
				'Mated',
				'Pledged',
				'Sold',
				'Surrendered'])
			
