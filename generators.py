# Utilities module

import sys, threading, traceback
from random import *
from util import *
from misc import *
from names import *
from people import *
from texttoimg import *

PromoHistoryQ = HistoryQ(2)

def GetTweet(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None):
	Generator = None
	GenType = None 
	
	if not Type is None:
		GenType = Type 
	else:
		GenType = None 
	#print("GetTweet() Generator Type is " + str(GenType))
	
	iSwitch = 999
	
	GenSel = GeneratorSelector()
	if bTest:
		gen = GenSel.GetGenerator(iGeneratorNo)
		if not gen == None:
			Generator = gen
	else:
		gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)

		if not gen == None:
			Generator = gen
		
	return Generator

def AddHashtag(Tweets):
	# if the last tweet has left over space, append a random hashtag to it: eartg, lprtg, wprtg, ssrtg, imabot, smut, erotica, etc
	if not Tweets is None and type(Tweets) in [list,tuple] and len(Tweets) > 0:
		sHashtag = "\n#" + misc.Hashtags().GetWord()
		if len(Tweets[len(Tweets) - 1]) + len(sHashtag) < MAX_TWITTER_CHARS:
			Tweets[len(Tweets) - 1] += sHashtag

	return Tweets

class Generator():
	ID = -1
	# each generator should have a unique ID
	Priority = 1
	# increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
	Type = GeneratorType.Normal
	# most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
	
	def GetMaster(self, NotList = None):
		sMaster = ""
		
		iRand = randint(1,12)
		
		if iRand == 1:
		# non-basic master, no adjs
			sMaster = self.Masters.GetWord()
		elif iRand == 2:
		# non-basic master, 1 reg adj
			sNoun = self.Masters.GetWord()
			sAdj = self.MasterAdjs.GetWord(NotList = [sNoun])
			sMaster = sAdj + " " + sNoun
		elif iRand == 3:
		#non-basic master, 1 comp adj
			sNoun = self.Masters.GetWord()
			sAdj = self.MasterCompAdjs.GetWord(NotList = [sNoun])
			sMaster = sAdj + " " + sNoun
		elif iRand == 4:
		#non-basic master, 1 reg adj & 1 comp adj
			sNoun = self.Masters.GetWord()
			sAdj1 = self.MasterAdjs.GetWord(NotList = [sNoun])
			sAdj2 = self.MasterCompAdjs.GetWord(NotList = [sNoun, sAdj1])
			sMaster = sAdj1 + " " + sAdj2 + " " + sNoun
		elif iRand == 5:
		#non-basic master, 2 comp adjs 
			sNoun = self.Masters.GetWord()
			sAdj1 = self.MasterAdjs.GetWord(NotList = [sNoun])
			sAdj2 = self.MasterCompAdjs.GetWord(NotList = [sNoun, sAdj1])
			sMaster = sAdj1 + " " + sAdj2 + " " + sNoun
		elif iRand == 6:
		#basic master, 1 reg adj
			sNoun = self.MastersBasic.GetWord()
			sAdj = self.MasterAdjs.GetWord(NotList = [sNoun])
			sMaster = sAdj + " " + sNoun
		elif iRand == 7:
		#basic master, 1 comp adj
			sNoun = self.MastersBasic.GetWord()
			sAdj = self.MasterCompAdjs.GetWord(NotList = [sNoun])
			sMaster = sAdj + " " + sNoun
		elif iRand == 7:
		#basic master, 1 reg adj & 1 comp adj 
			sNoun = self.MastersBasic.GetWord()
			sAdj1 = self.MasterAdjs.GetWord(NotList = [sNoun])
			sAdj2 = self.MasterCompAdjs.GetWord(NotList = [sNoun, sAdj1])
			sMaster = sAdj1 + " " + sAdj2 + " " + sNoun
		elif iRand == 8:
		#basic master, 2 comp adjs 
			sNoun = self.MastersBasic.GetWord()
			sAdj1 = self.MasterCompAdjs.GetWord(NotList = [sNoun])
			sAdj2 = self.MasterCompAdjs.GetWord(NotList = [sNoun, sAdj1])
			sMaster = sAdj1 + " " + sAdj2 + " " + sNoun
		elif iRand == 9:
		#gang, no adjs
			sMaster = self.MasterGangs.GetWord()
		elif iRand == 10:
		#gang, 1 reg adj 
			sNoun = self.MasterGangs.GetWord()
			sAdj = self.MasterAdjs.GetWord(NotList = [sNoun])
			sMaster = sAdj + " " + sNoun
		elif iRand == 11:
		#gang, 1 comp adj
			sNoun = self.MasterGangs.GetWord()
			sAdj = self.MasterCompAdjs.GetWord(NotList = [sNoun])
			sMaster = sAdj + " " + sNoun
		elif iRand == 12:
		#gang, 1 reg adj & 1 comp adj 
			sNoun = self.MasterGangs.GetWord()
			sAdj1 = self.MasterAdjs.GetWord(NotList = [sNoun])
			sAdj2 = self.MasterCompAdjs.GetWord(NotList = [sNoun, sAdj1])
			sMaster = sAdj1 + " " + sAdj2 + " " + sNoun
	
		return sMaster
		
	def GetGirl(self, NotList = None):
		sGirl = ""
		
		iRand = randint(1,8)
		
		if iRand == 1:
		# non-basic girl, no adjs
			sGirl = self.Girls.GetWord()
		elif iRand == 2:
		# non-basic girl, 1 reg adj
			sNoun = self.Girls.GetWord()
			sGirl = self.GirlAdjs.GetWord(NotList = [sNoun]) + " " + sNoun
		elif iRand == 3:
		# non-basic girl, 1 reg and 1 comp adj 
			sNoun = self.Girls.GetWord()
			sAdj1 = self.GirlAdjs.GetWord(NotList = [sNoun])
			sAdj2 = self.GirlCompAdjs.GetWord(NotList = [sNoun, sAdj1])
			sGirl = sAdj1 + " " + sAdj2 + " " + sNoun
		elif iRand == 4:
		# non-basic girl, 2 comp adjs
			sNoun = self.Girls.GetWord()
			sAdj1 = self.GirlCompAdjs.GetWord(NotList = [sNoun])
			sAdj2 = self.GirlCompAdjs.GetWord(NotList = [sNoun, sAdj1])
			sGirl = sAdj1 + " " + sAdj2 + " " + sNoun
		elif iRand == 5:
		# basic girl, 1 reg adj 
			sNoun = self.GirlsBasic.GetWord()
			sAdj = self.GirlAdjs.GetWord(NotList = [sNoun])
			sGirl = sAdj + " " + sNoun
		elif iRand == 6:
		# basic girl, 1 comp adj 
			sNoun = self.GirlsBasic.GetWord()
			sAdj = self.GirlCompAdjs.GetWord(NotList = [sNoun])
			sGirl = sAdj + " " + sNoun
		elif iRand == 7:
		# basic girl, 1 reg adj and 1 comp adj 
			sNoun = self.GirlsBasic.GetWord()
			sAdj1 = self.GirlAdjs.GetWord(NotList = [sNoun])
			sAdj2 = self.GirlCompAdjs.GetWord(NotList = [sNoun, sAdj1])
			sGirl = sAdj1 + " " + sAdj2 + " " + sNoun
		elif iRand == 8:
		# basic girl, 2 comp adjs
			sNoun = self.GirlsBasic.GetWord()
			sAdj1 = self.GirlCompAdjs.GetWord(NotList = [sNoun])
			sAdj2 = self.GirlCompAdjs.GetWord(NotList = [sNoun, sAdj1])
			sGirl = sAdj1 + " " + sAdj2 + " " + sNoun
			
		return sGirl
		
	def _getFMs_(self):
		FMs = ""
		
		iRandLen = randint(4,10)
		for x in range(1, iRandLen):
			iRandChoice = randint(1,3)
			if iRandChoice == 1:
				FMs += "F"
			else:
				FMs += "M"
				
		if "M" not in FMs:
			FMs += "M"
		elif "F" not in FMs:
			FMs += "F"
		
		return FMs
	
	def GenerateTweet(self):
		self.Girls = BookGirls()
		self.GirlsBasic = BookGirlsBasic()
		self.GirlAdjs = BookGirlAdjs()
		self.GirlCompAdjs = BookGirlCompAdjs()
		self.Masters = BookMasters()
		self.MastersBasic = BookMastersBasic()
		self.MasterGangs = BookMasterGangs()
		self.MasterAdjs = BookMasterAdjs()
		self.MasterCompAdjs = BookMasterCompAdjs()
		self.VerbsBy = BookVerbsBy()
		self.VerbsTo = BookVerbsTo()
		self.HerName = NamesFemale().FirstName()
		self.HisName = NamesMale().FirstName()
		
		return ""
		
class GeneratorPromo(Generator):
	ID = 0
	Priority = 0
	Type = GeneratorType.Promo
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		#sTweet = "Blue Diamond: \U0001F539 Eggplant: \U0001F346 Fire: \U0001F525 Laughing: \U0001F923 Robot: \U0001F916 Green Heart: \U0001F49A Blue Heart: \U0001F499 Purple Heart: \U0001F49C No one under 18: \U0001F51E Winking kiss face: \U0001F618 Star: \U00002B50"

		iRand = randint(1,7)
		while not PromoHistoryQ.PushToHistoryQ(iRand):
			iRand = randint(1,7)

		if iRand == 1:
			sTweet = "Reply to " + WordList(["one of my tweets", "an @bot_lust tweet", "a Flaming Lust Bot tweet"]).GetWord() + " for a fun surprise! " + GetEmoji()
			sTweet += "\n\n\U0001F539Reply \"#book\" and I'll respond with a made-up smutty book title."
			sTweet += "\n\U0001F539Reply \"#lovescene\" to get your own custom love scene!"
		elif iRand == 2:
			sTweet = "Tell your family, friends and lovers to follow " + WordList(["@bot_lust", "Flaming Lust Bot", "me", "this bot"]).GetWord() + " for all the steamy, sweaty, silly action!\n" + GetEmoji(randint(1,3))
		elif iRand == 3:
			sTweet = WordList(["@bot_lust", "Flaming Lust Bot", "this bot"]).GetWord() + " is very naughty, and NOT appropriate for anyone under 18! \U0001F51E\n\nThat includes you, " + WordList(["kid who is hiding their phone behind their math book while they check twitter", str(randint(6,11)) + "th grader who is supposed to be doing homework", str(randint(6,11)) + "th grader who is supposed to be reading"]).GetWord() + "!"
			if CoinFlip(): 
				sTweet += " \U0001F928"
		elif iRand == 4:
			sTweet = "I am a twitter bot\U0001F916 designed to automatically generate " + WordList(["hot", "sexy", "naughty", "steamy"]).GetWord() + "\U0001F525, " + WordList(["filthy", "dirty"]).GetWord() + "\U0001F346, and " + WordList(["funny", "hilarious", "ridiculous", "silly"]).GetWord() + "\U0001F923 scenes from the world's worst smutty romance novel!\n\nReply to one of my tweets " + WordList(["and get a surprise!", "if you want more.", "if you're impatient for my next terrible love scene!"]).GetWord()
		elif iRand == 5:
			if CoinFlip():
				sTweet = "Full disclosure: "
			sTweet += "I am a bot\U0001F916!\n\nBut not the Russian kind of bot, the " + WordList(["funny", "sexy", "naughty", "silly", "dirty"]).GetWord() + " kind of bot!" 
			if CoinFlip():
				sTweet += " " + GetEmoji()
			if CoinFlip():
				sTweet += "\n#botlife #twitterbot"
		elif iRand == 6:
			sTweet = "Look what " + WordList(["my followers are", "people are ", "other twitter users are", "the internet is"]).GetWord() + " saying:\n\n\U00002B50'I am hooked on this ridiculous account!'\n\U00002B50'The stuff this bot comes up with is hysterical. XD'\n\U00002B50'[S]imultaneously hilarious, nauseating, and inspiring'\n\n" + WordList(["Thank you!", "Thanks!", "Thank you all!", "Big bot love to everyone!"]).GetWord() 
			sTweet += " " + GetEmoji(randint(1,3))
		else:
			sTweet = WordList(["I love you", "You're the best", "Big Bot Love", "I \U00002764 you"]).GetWord() + ", followers!"
			if CoinFlip():
				sTweet = "*" + sTweet + "*"
			sTweet += "\n\n" + GetHeartEmoji(randint(1,5))
			
		return sTweet
		
class Generator1(Generator):
	# Blackmailed by the Billionaire Mountain Man 
	ID = 1
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.VerbsBy.GetWord() + " by the " + self.GetMaster()
		
		return sTweet
		
class Generator2(Generator):
	# Veonica Gets Blackmailed by the Billionaire Mountain Man 
		
	ID = 2
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord() + " by the " + self.GetMaster()
		
		return sTweet

class Generator3(Generator):
	# Married to the Alpha Wolf
	ID = 3
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = self.VerbsTo.GetWord() + " to the " + self.GetMaster()
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nA " + self._getFMs_() + " Romance"
			else:
				sTweet += ":\nA BDSM Romance"
		
		return sTweet

class Generator4(Generator):
	# Veronica Gets Married to the Alpha Wolf	
	ID = 4
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.HerName + " Gets " + self.VerbsTo.GetWord() + " to the " + self.GetMaster()
		
		return sTweet
		
class Generator5(Generator):
	# The President's Amish Milkmaid
	ID = 5
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "The " + self.GetMaster() + "'s " + self.GetGirl()
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nA BDSM Romance"
			else:
				sTweet += ":\nA Hot Ménage"
		
		return sTweet
		
class Generator6(Generator):
	# Seduced in the Bed of the Billionaire	
	ID = 6
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		if CoinFlip():
			sTweet = self.VerbsTo.GetWord() + " in the Bed of the " + self.GetMaster()
		else:
			sTweet = self.VerbsBy.GetWord() + " in the Bed of the " + self.GetMaster()
		
		return sTweet
		
class Generator7(Generator):
	# The Virgin, The Werewolf, and The Billionaire Manticore: A Hot Menage	
	
	ID = 7
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "The " + self.GetGirl() + ", The " + self.GetMaster() + ", & The " + self.GetMaster() + ":\n"
		if CoinFlip():
			sTweet += "A Hot Ménage"
		else:
			sTweet += "A " + self._getFMs_() + " Romance"
		
		return sTweet

class Generator8(Generator):
	# The Virgin's Secret Daddy Dom 
	ID = 8
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "The " + self.GetGirl() + "'s " + self.GetMaster()
		
		return sTweet
		
class Generator9(Generator):
	# The Secretary and the Space Werewolf 
	ID = 9
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "The " + self.GetGirl() + " & the " + self.GetMaster()
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nA BDSM Romance"
			else:
				sTweet += ":\nA " + self._getFMs_() + " Romance"
		
		return sTweet
		
class Generator10(Generator):
	# Baby for the Stay-at-Home Manticore
	ID = 10
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = "Baby for the " + self.GetMaster() 
		if CoinFlip():
			sTweet += ":\nA " + self._getFMs_() + " Romance"
		
		return sTweet
		
class Generator11(Generator):
	# The Millionaire Sherrif's Virgin
	ID = 11
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "The " + self.GetMaster() + "'s " + self.GetGirl()

		return sTweet
		
class Generator12(Generator):
	# Babysitter to the Billionaire Uniporn
	ID = 12
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.GetGirl() + " to the " + self.GetMaster()
		
		return sTweet
		
class Generator13(Generator):	
	# Babysitter for the Billionaire Uniporn
	ID = 13
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.GetGirl() + " for the " + self.GetMaster()
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nAn " + self._getFMs_() + " Adventure"
			else:
				sTweet += ":\nA BDSM Romance"
		
		return sTweet
	
class Generator14(Generator):
	# The Virgin Call-Girl's Gang Bang
	ID = 14
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = "The " + self.GetGirl() + "'s Gang Bang:\nA " + self._getFMs_() + " Romance"
		
		return sTweet
		
class Generator15(Generator):
	# The Small-Town Virgin's First Porno
	ID = 15
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "The " + self.GetGirl() + "'s First Porno"
		if CoinFlip():
			sTweet += ":\nAn " + self._getFMs_() + " Adventure"

		return sTweet
		
class Generator16(Generator):
	# The Small-Town Virgin's First Time
		
	ID = 16
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = "The " + self.GetGirl() + "'s First Time"
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nA " + self._getFMs_() + " Romance"
			else:
				sTweet += ":\nA BDSM Romance"

		return sTweet
		
class Generator17(Generator):
	# Enslaved: The Ebony Older Woman & The Duke 
	ID = 17
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.VerbsBy.GetWord() + ":\n"
		if CoinFlip():
			sTweet += "The " + self.GetGirl() + " & The " + self.GetMaster()
		else:
			sTweet += AddArticles(self.GetGirl()) + " Romance"
		
		return sTweet
		
class Generator18(Generator):
	# Oh No! My Step-Daughter is a Porn Star
	ID = 18
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet += "\"" + WordList(["Oh No!", "Uh Oh!", "Whoops!", "WTF?!?"]).GetWord() + " My " + self.GetGirl() + " Is A " + WordList(["Porn Star", "Lesbian", "Call-Girl", "Stripper"]).GetWord() + "!\""
		
		return sTweet
		
class Generator19(Generator):
	# Full Frontal for the Shy Amish Virgin: A BDSM Romance
	ID = 19
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		if CoinFlip():
			sTweet = "Full Frontal Nudity for the "
			if CoinFlip():
				sTweet += self.GetMaster()
			else:
				sTweet += self.GetGirl()
		else:
			sTweet = "Naked for the " + self.GetMaster()
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nAn " + self._getFMs_() + " Adventure"
			else:
				sTweet += ":\nA BDSM Romance"
		
		return sTweet
		
class Generator20(Generator):
	# I Was Stripped In Public, And I Liked It
	ID = 20
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = "\"I Was " + self.VerbsBy.GetWord()
		if not "in public" in self.VerbsBy.GetWord().lower():
			sTweet += " By " + AddArticles(self.GetMaster())
		sTweet += ", And I Liked It\""

		return sTweet
		
class Generator21(Generator):
	# Pleasured by the Shape-Shifting Single Dad: A Nudist Secretary Story
	ID = 21
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.VerbsBy.GetWord()  + " by "
		sTweet += "the " + self.GetMaster() + ":\nA " + self.GetGirl() + " Story"
		
		return sTweet
		
class Generator22(Generator):
	# The Amish Virgin and the Taboo MILF: A Lesbian Love Story 
	ID = 22
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = "The " + self.GetGirl() + " and the " + self.GetGirl()
		if CoinFlip():
			sTweet += ":\nA Lesbian Love Story"
		else:
			sTweet += ":\nA Secret Lesbian Affair"
		
		return sTweet
		
class Generator23(Generator):
	# Deflowered Live on the Internet: An Amish Futa Princess Experience 
	ID = 23
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "Deflowered Live"
		if CoinFlip():
			sTweet += "! "
		else:
			if CoinFlip():
				sTweet += " on the Interet:\n"
			else:
				sTweet += " on Television:\n"
		sTweet += AddArticles(self.GetGirl()) + " Experience"

		return sTweet
		
class Generator24(Generator):
	# Here Cums The Bride: The Porn Star Pope & The Bi-Curious Christian Milk Maid 
	ID = 24
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "Here Cums The Bride:\nThe " + self.GetMaster() + " & The " + self.GetGirl()
		
		return sTweet
		
class Generator25(Generator):
	# Hotwife for Daddy: A BDSM Romance 
	ID = 25
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.GetGirl() + " for Daddy:\n"
		if CoinFlip():
			sTweet += "A BDSM Romance"
		else:
			sTweet += "An " + self._getFMs_() + " Adventure"
		
		return sTweet
		
# class Generator54(Generator):
	# ID = 51
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet

# class Generator55(Generator):
	# ID = 55
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator56(Generator):
	# ID = 56
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator57(Generator):
	# ID = 57
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator58(Generator):
	# ID = 58
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator59(Generator):
	# ID = 59
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
def GetImgTweetText(gen):
	#the bot's images are the random parts but we need to be careful that this isn't constantly generating static duplicate text. twitter won't like that.
	sText = ""
	
	TweetText = []
	BookSeller = BookSellers()
	Hashtag = Hashtags()
	SexyAdj = SexyAdjs()
	
	sText = "Coming soon on " + BookSeller.GetWord() 
	for _ in range(2):
		TweetText.append(sText)
	#=============================

	sText = "Available soon on " + BookSeller.GetWord() 
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "Look for this " + SexyAdj.GetWord() + " ebook on " + BookSeller.GetWord()  
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "Watch for this " + SexyAdj.GetWord() + " read on " + BookSeller.GetWord() 
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "Available soon to discerning readers on " + BookSeller.GetWord() 
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "My Patreon supporters get access to all my " + SexyAdj.GetWord() + " reads!"
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "Reply to this tweet and " 
	if CoinFlip():
		sText += "I'll tweet a randomly-generated erotica ebook title @ you!"
	else:
		sText += "get a custom erotic ebook title of your very own in response!"
	sText += " " + GetEmoji()
	for _ in range(2):
		TweetText.append(sText)
	#=============================

	# it seems that adding any kind of hashtag at all to a bot may lead to shadowbans. so for now I'm not using this.
	# if CoinFlip():
		# sText = TweetText[randint(0, len(TweetText) - 1)] + " #" + Hashtag.GetWord()
		# while IsTweetTooLong(sText):
			# sText = TweetText[randint(0, len(TweetText) - 1)] + " #" + Hashtag.GetWord()
	# else:
	sText = TweetText[randint(0, len(TweetText) - 1)] 
	while IsTweetTooLong(sText):
		sText = TweetText[randint(0, len(TweetText) - 1)] 
	
	return sText 
				
class GeneratorSelector():
	GeneratorList = []
	
	def __init__(self):
		for subclass in Generator.__subclasses__():
			item = subclass()
			for x in range(0, item.Priority):
				self.GeneratorList.append([item.ID, item])
			
	def RandomGenerator(self, bAllowPromo = True, Type = None):
		Generator = None
		AllowedTypes = []
		
		if not Type is None:
			AllowedTypes = [Type] 
		else:
			AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
		
		if bAllowPromo:
			AllowedTypes.append(GeneratorType.Promo)
			
		#print("RandomGenerator() Allowed types: " + str(AllowedTypes))
		if len(self.GeneratorList) > 0:

			Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
			while not Generator.Type in AllowedTypes:
				Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
				
		return Generator 
		
	def GetGenerator(self, iGen):
		Generator = None 
		
		if len(self.GeneratorList) > 0:
			for gen in self.GeneratorList :
				if gen[1].ID == iGen:
					Generator = gen[1]
					break
					
		return Generator
		