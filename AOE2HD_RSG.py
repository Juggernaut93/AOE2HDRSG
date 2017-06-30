import locale
import os
from glob import glob
import sys
import pickle
import random

class Singleton(type):
	__instance = None
	def __call__(cls, *args, **kw):
		if not cls.__instance:
			cls.__instance = super(Singleton, cls).__call__(*args, **kw)
		return cls.__instance

class Map(dict):
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    if isinstance(v, dict):
                        v = Map(v)
                    if isinstance(v, list):
                        self.__convert(v)
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                if isinstance(v, dict):
                    v = Map(v)
                elif isinstance(v, list):
                    self.__convert(v)
                self[k] = v

    def __convert(self, v):
        for elem in xrange(0, len(v)):
            if isinstance(v[elem], dict):
                v[elem] = Map(v[elem])
            elif isinstance(v[elem], list):
                self.__convert(v[elem])

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]

class RSG(metaclass=Singleton):
	## GAME ##
	GAME = Map({
		'str': '13510',
		'values': Map({
			'RM': '9653',
			'RM_TURBO': '9764',
			'REGICIDE': '9228',
			'DEATHMATCH': '9751',
			#'SCENARIO': '9760',
			'KING_HILL': '9762',
			'BUILD_WONDER': '9761',
			'DEF_WONDER': '9763',
			'CTR': 'RELIC_MODE',
			'SUDDEN_DEATH': 'SUDDEN_DEATH_MODE'
		})
	})
	
	## MAP STYLE ##
	MAP_STYLE = Map({
		'str': '13560',
		'values': Map({
			'STANDARD': '13561',
			'REAL_WORLD': '13543',
			'SPECIAL': 'SPECIAL_MAPS_LABEL',
			'CUSTOM': '13562'
		})
	})
	
	## LOCATION ##
	LOCATION = Map({
		'str': '13511',
		'values': Map({
			'STANDARD': Map({
				'ARABIA': '10875',
				'ARCHIPELAGO': '10876',
				'BALTIC': '10877',
				'BLACK_FOREST': '10878',
				'COASTAL': '10879',
				'CONTINENTAL': '10880',
				'CRATER_LAKE': '10881',
				'FORTRESS': '10882',
				'GOLD_RUSH': '10883',
				'HIGHLAND': '10884',
				'ISLANDS': '10885',
				'MEDITERRANEAN': '10886',
				'MIGRATION': '10887',
				'RIVERS': '10888',
				'TEAM_ISLANDS': '10889',
				'FULL_RANDOM': '10890',
				'SCANDINAVIA': '10891',
				'MONGOLIA': '10892',
				'SALT_MARSH': '10893',
				'YUCATAN': '10894',
				'ARENA': '10895',
				'OASIS': '10897',
				'GHOST_LAKE': '10898',
				'RANDOM_LAND_MAP': '10899',
				'NOMAD': '10901',
				'BLIND_RANDOM': '10902',
				'ACROPOLIS': '10914',
				'BUDAPEST': '10915',
				'CENOTES': '10916',
				'CITY_OF_LAKES': '10917',
				'GOLDEN_PIT': '10918',
				'HIDEOUT': '10919',
				'HILL_FORT': '10920',
				'LOMBARDIA': '10921',
				'STEPPE': '10922',
				'VALLEY': '10923',
				'MEGARANDOM': '10924',
				'HAMBURGER': '10925',
				'CTR_RANDOM': '10926',
				'CTR_MONSOON': '10927',
				'CTR_PYRAMID_DESCENT': '10928',
				'CTR_SPIRAL': '10929',
				'KILIMANJARO': 'RMS_KILIMANJARO',
				'MOUNTAINPASS': 'RMS_MOUNTAINPASS',
				'NILEDELTA': 'RMS_NILEDELTA',
				'SERENGETI': 'RMS_SERENGETI',
				'SOCOTRA': 'RMS_SOCOTRA',
				'BOGISLANDS': 'RMS_BOGISLANDS',
				'MANGROVEJUNGLE': 'RMS_MANGROVEJUNGLE',
				'PACIFICISLANDS': 'RMS_PACIFICISLANDS',
				'SANDBANK': 'RMS_SANDBANK',
				'WATERNOMAD': 'RMS_WATERNOMAD'
			}),
			'REAL_WORLD': Map({
				'IBERIA': '13544',
				'BRITAIN': '13545',
				'MIDEAST': '13546',
				'TEXAS': '13547',
				'ITALY': '13548',
				'CENTRAL_AMERICA': '13549',
				'FRANCE': '13550',
				'NORSE_LANDS': '13551',
				'SEA_OF_JAPAN': '13552',
				'BYZANTIUM': '13553',
				'AMAZON': 'RWM_AMAZON',
				'CHINA': 'RWM_CHINA',
				'HORNOFAFRICA': 'RWM_HORNOFAFRICA',
				'INDIA': 'RWM_INDIA',
				'MADAGASCAR': 'RWM_MADAGASCAR',
				'WESTAFRICA': 'RWM_WESTAFRICA',
				'BOHEMIA': 'RWM_BOHEMIA',
				'EARTH': 'RWM_EARTH',
				'RANDOM': 'RWM_RANDOM',
				'AUSTRALIA': 'RWM_AUSTRALIA',
				'INDOCHINA': 'RWM_INDOCHINA',
				'INDONESIA': 'RWM_INDONESIA',
				'MALACCA': 'RWM_MALACCA',
				'PHILIPPINES': 'RWM_PHILIPPINES'
			}),
			'SPECIAL': Map({
				'CANYONS': 'SPECIALMAP_CANYONS',
				'ENEMYARCHIPELAGO': 'SPECIALMAP_ENEMYARCHIPELAGO',
				'ENEMYISLANDS': 'SPECIALMAP_ENEMYISLANDS',
				'FAROUT': 'SPECIALMAP_FAROUT',
				'FRONTLINE': 'SPECIALMAP_FRONTLINE',
				'INNERCIRCLE': 'SPECIALMAP_INNERCIRCLE',
				'MOTHERLAND': 'SPECIALMAP_MOTHERLAND',
				'OPENPLAINS': 'SPECIALMAP_OPENPLAINS',
				'RINGOFWATER': 'SPECIALMAP_RINGOFWATER',
				'SNAKEPIT': 'SPECIALMAP_SNAKEPIT',
				'THEEYE': 'SPECIALMAP_THEEYE',
				'RANDOM': 'SPECIALMAP_RANDOM',
				'JUNGLEISLANDS': 'SPECIALMAP_JUNGLEISLANDS',
				'HOLYLINE': 'SPECIALMAP_HOLYLINE',
				'BORDERSTONES': 'SPECIALMAP_BORDERSTONES',
				'YINYANG': 'SPECIALMAP_YINYANG',
				'JUNGLELANES': 'SPECIALMAP_JUNGLELANES'
			}),
			'CUSTOM': Map({
				'CANALS': 'es@canals_v2.rms',
				'CAPRICIOUS': 'es@capricious_v2.rms',
				'DINGOS': 'es@dingos_v2.rms',
				'GRAVEYARDS': 'es@graveyards_v2.rms',
				'METROPOLIS': 'es@metropolis_v2.rms',
				'MOATS': 'es@moats_v2.rms',
				'PARADISEISLAND': 'es@paradiseisland_v2.rms',
				'PILGRIMS': 'es@pilgrims_v2.rms',
				'PRAIRIE': 'es@prairie_v2.rms',
				'SEASONS': 'es@seasons_v2.rms',
				'SHERWOOD_FOREST': 'es@sherwood_forest_v2.rms',
				'SHERWOOD_HEROES': 'es@sherwood_heroes_v2.rms',
				'SHIPWRECK': 'es@shipwreck_v2.rms',
				'TEAM_GLACIERS': 'es@team_glaciers_v2.rms',
				'THE_UNKNOWN': 'es@the_unknown'
			})
		})
	})
	
	## MAP SIZE ##
	MAP_SIZE = Map({
		'str': '13512',
		'values': Map({
			'TINY': '10611',
			'SMALL': '10612',
			'MEDIUM': '10613',
			'NORMAL': '10614',
			'LARGE': '10615',
			'GIANT': '10616',
			'LUDIKRIS': '10617'
		})
	})
	
	## DIFFICULTY LEVEL ##
	DIFFICULTY = Map({
		'str': '10774',
		'values': Map({
			'EASIEST': '11220',
			'STANDARD': '11219',
			'MODERATE': '11218',
			'HARD': '11217',
			'HARDEST': '11216'
		})
	})
	
	## RESOURCES ##
	RESOURCES = Map({
		'str': '9735',
		'values': Map({
			'STANDARD': '10390',
			'LOW': '9736',
			'MEDIUM': '9737',
			'HIGH': '9738'
		})
	})
	
	## POPULATION ##
	POPULATION = Map({
		'str': '13516',
		'values': Map({
			'25': 25,
			'50': 50,
			'75': 75,
			'100': 100,
			'125': 125,
			'150': 150,
			'175': 175,
			'200': 200,
			'250': 250,
			'300': 300,
			'400': 400,
			'500': 500
		})
	})
	
	## GAME SPEED ##
	SPEED = Map({
		'str': '13517',
		'values': Map({
			'SLOW': '9432',
			'NORMAL': '9433',
			'FAST': '9434'
		})
	})
	
	## REVEAL MAP ##
	REVEAL_MAP = Map({
		'str': '9724',
		'values': Map({
			'NORMAL': '9755',
			'EXPLORED': '9756',
			'ALL_VISIBLE': '9757'
		})
	})
	
	## STARTING AGE ##
	STARTING_AGE = Map({
		'str': '13515',
		'values': Map({
			'STANDARD': '10390',
			'DARK': '4201',
			'FEUDAL': '4202',
			'CASTLE': '4203',
			'IMPERIAL': '4204',
			'POSTIMPERIAL': '4205'
		}),
		'numvalues': Map({
			'STANDARD': 0,
			'DARK': 0,
			'FEUDAL': 1,
			'CASTLE': 2,
			'IMPERIAL': 3,
			'POSTIMPERIAL': 3
		})
	})
	
	## ENDING AGE ##
	ENDING_AGE = Map({
		'str': '13563',
		'values': Map({
			'STANDARD': '10390',
			'DARK': '4201',
			'FEUDAL': '4202',
			'CASTLE': '4203',
			'IMPERIAL': '4204'
		}),
		'numvalues': Map({
			'STANDARD': 3,
			'DARK': 0,
			'FEUDAL': 1,
			'CASTLE': 2,
			'IMPERIAL': 3
		})
	})
	
	## TREATY LENGTH ##
	TREATY_LENGTH = Map({
		'str': 'TREATY_LENGTH',
		'MINUTES': 'MINUTES',
		'values': {
			'NONE': '10391',
			'5': 5,
			'10': 10,
			'15': 15,
			'20': 20,
			'25': 25,
			'30': 30,
			'35': 35,
			'40': 40,
			'45': 45,
			'50': 50,
			'55': 55,
			'60': 60,
			'90': 90
		}
	})
	
	## VICTORY ##
	VICTORY = Map({
		'str': '13518',
		'values': {
			'STANDARD': '10390',
			'CONQUEST': '4321',
			'TIME_LIMIT': '4329',
			'SCORE': '4330',
			'LAST_MAN': '4333'
		}
	})
	
	## TIME ##
	TIME = Map({
		'str': '13519',
		'values': {
			'1500y': '9780',
			'1300y': '9781',
			'1100y': '9782',
			'900y': '9783',
			'700y': '9784',
			'500y': '9785',
			'300y': '9786'
		}
	})
	
	## SCORE ##
	SCORE = Map({
		'str': '13520',
		'values': {
			'14000': 14000,
			'13000': 13000,
			'12000': 12000,
			'11000': 11000,
			'10000': 10000,
			'9000': 9000,
			'8000': 8000,
			'7000': 7000,
			'6000': 6000,
			'5000': 5000,
			'4000': 4000
		}
	})
	
	## OTHER ##
	__BOOLEAN = Map({
		'YES': '10754',
		'NO': '10755'
	})
	
	TEAM_TOGETHER = Map({
		'str': '13521',
		'values': __BOOLEAN
	})
	LOCK_TEAMS = Map({
		'str': '13523',
		'values': __BOOLEAN
	})
	ALL_TECHS = Map({
		'str': '13524',
		'values': __BOOLEAN
	})
	LOCK_SPEED = Map({
		'str': '13525',
		'values': __BOOLEAN
	})
	ALLOW_CHEATS = Map({
		'str': '13526',
		'values': __BOOLEAN
	})
	
	__ALLSTRMAPS = [GAME, MAP_STYLE, LOCATION, MAP_SIZE, DIFFICULTY, RESOURCES, POPULATION, SPEED, REVEAL_MAP, STARTING_AGE, ENDING_AGE, TREATY_LENGTH, VICTORY, TIME, SCORE, __BOOLEAN, TEAM_TOGETHER, LOCK_TEAMS, ALL_TECHS, LOCK_SPEED, ALLOW_CHEATS]
	
	def __init__(self):
		self.__strings = {}
		self.__respath = 'res'
		self.__stringfile = 'strings.pkl'
		self.__loadData()
		self.__replace_treaty_strings()
	
	def __replace_treaty_strings(self):
		min_str = self.getString(RSG.TREATY_LENGTH.MINUTES)
		for k, v in RSG.TREATY_LENGTH.values.items():
			if k != 'NONE':
				RSG.TREATY_LENGTH.values[k] = '%d %s' % (v, min_str)
	
	def getString(self, key):
		return str(self.__strings.get(key, key))
		
	def __extract_strings(self, dict):
		strings = []
		for k, v in dict.items():
			if type(v) is Map:
				v = self.__extract_strings(v)
				strings.extend(v)
			else:
				strings.append(v)
		return strings
	
	def __get_all_used_strings(self):
		codes = []
		for obj in RSG.__ALLSTRMAPS:
			codes.extend(self.__extract_strings(obj))
		return codes
	
	def __generate_string_store(self):
		os.chdir("res")
		files = glob("*.txt")
		dic = {}
		usedkeys = self.__get_all_used_strings()
		for file in files:
			tag = file.split('.')[0]
			dic[tag] = {}
			with open(file, encoding='utf-8') as f:
				lines = f.readlines()
			for line in lines:
				if not line.startswith('//') and len(line.strip()) > 0 :
					idx = line.find(' "')
					if idx > -1:
						k = line[:idx]
						if k in usedkeys:
							v = line[idx+2 : -2]
							dic[tag][k] = v
		with open(self.__stringfile, 'wb') as f:
			pickle.dump(dic, f, protocol=2)
		os.chdir("..")
		return dic

	def __loadData(self):
		lang = locale.getdefaultlocale()[0].split('_')[0]
		if not os.path.exists(os.path.join(self.__respath, self.__stringfile)):
			dic = self.__generate_string_store()
		with open(os.path.join(self.__respath, self.__stringfile), 'rb') as f:
				dic = pickle.load(f)
		self.__strings = dic['en']
		if lang in dic:
			self.__strings.update(dic[lang])
	
	def __singleChoice(self, category, choices = None):
		if choices is None:
			choices = category.values
		elif type(choices) is str:
			choices = category.values[choices]
		elif type(choices) is list:
			ch = Map({})
			for el in choices:
				ch[el] = category.values[el]
			choices = ch
		
		selkey = random.choice(list(choices))
		print("%s: %s" % (self.getString(category.str), self.getString(choices[selkey])))
		return selkey
	
	def __generateSettings(self):
		print()
		game = self.__singleChoice(RSG.GAME)
		map_style = self.__singleChoice(RSG.MAP_STYLE)
		location = self.__singleChoice(RSG.LOCATION, map_style)
		if map_style not in ['REAL_WORLD', 'SPECIAL']:
			map_size = self.__singleChoice(RSG.MAP_SIZE)
		difficulty = self.__singleChoice(RSG.DIFFICULTY)
		if game not in ['DEATHMATCH']:
			resources = self.__singleChoice(RSG.RESOURCES)
		population = self.__singleChoice(RSG.POPULATION)
		speed = self.__singleChoice(RSG.SPEED)
		reveal_map = self.__singleChoice(RSG.REVEAL_MAP)
		if game not in ['DEF_WONDER']:
			starting_age = self.__singleChoice(RSG.STARTING_AGE)
		if game not in ['DEF_WONDER', 'BUILD_WONDER']:
			startageval = RSG.STARTING_AGE.numvalues[starting_age]
			choices = []
			for k, v in RSG.ENDING_AGE.numvalues.items():
				if v >= startageval:
					choices.append(k)
			ending_age = self.__singleChoice(RSG.ENDING_AGE, choices)
		treaty_length = self.__singleChoice(RSG.TREATY_LENGTH)
		victory = None
		if game in ['RM', 'RM_TURBO', 'DEATHMATCH']:
			victory = self.__singleChoice(RSG.VICTORY)
		elif game in ['REGICIDE', 'KING_HILL']:
			victory = self.__singleChoice(RSG.VICTORY, ['STANDARD', 'LAST_MAN'])
		elif game in ['SUDDEN_DEATH']:
			victory = self.__singleChoice(RSG.VICTORY, ['CONQUEST', 'LAST_MAN'])
		if victory:
			if victory in ['TIME_LIMIT']:
				time = self.__singleChoice(RSG.TIME)
			if victory in ['SCORE']:
				score = self.__singleChoice(RSG.SCORE)
		
		# other options
		team_together = self.__singleChoice(RSG.TEAM_TOGETHER)
		if victory not in ['LAST_MAN']:
			lock_teams = self.__singleChoice(RSG.LOCK_TEAMS)
		all_techs = self.__singleChoice(RSG.ALL_TECHS)
		lock_speed = self.__singleChoice(RSG.LOCK_SPEED)
		allow_cheats = self.__singleChoice(RSG.ALLOW_CHEATS)
		
		print()
	
	def run(self):
		while True:
			inp = input('Press Enter to get new random settings (0 to exit): ')
			if inp == '0':
				break
			self.__generateSettings()



if __name__ == '__main__':
	print('-------- Welcome to the Age Of Empires 2 HD Random Settings Generator --------')
	print('This script will generate for you random settings for a crazy game!')
	print()
	os.chdir(os.path.dirname(os.path.abspath(__file__)))
	
	RSG().run()	
