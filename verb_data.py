import re
from collections import OrderedDict
from jeff_phrasing import TO_BE
import pprint

irregular_verb_data = {
	# Irregular verbs with 5+ forms (unpredictable -s forms, predictable -ing form)
	'be':         {'en': 'been', 'ed': 'were', 'ed13': 'was', 's': 'are', 's1': 'am', 's3': 'is'},
	'have':       {'en': 'had',  'ed': 'had',                 's': 'has'                        },
	# Irregular verbs with 5 forms (2 different irregular past forms; predictable -s, -ing forms)
	'become':     {'en': 'become',    'ed': 'became'},
	'come':       {'en': 'come',      'ed': 'came'  },
	'do':         {'en': 'done',      'ed': 'did'   },
	'forget':     {'en': 'forgotten', 'ed': 'forgot'},
	'get':        {'en': 'gotten',    'ed': 'got'   }, # he had gotten vs. he had got to (must)
	'give':       {'en': 'given',     'ed': 'gave'  },
	'go':         {'en': 'gone',      'ed': 'went'  },
	'know':       {'en': 'known',     'ed': 'knew'  },
	'run':        {'en': 'run',       'ed': 'ran'   },
	'see':        {'en': 'seen',      'ed': 'saw'   },
	'take':       {'en': 'taken',     'ed': 'took'  },
	# Irregular verbs with 4 forms (same irregular past and past participle form)
	'feel':       {'en': 'felt'       },
	'find':       {'en': 'found'      },
	'hear':       {'en': 'heard'      },
	'keep':       {'en': 'kept'       },
	'leave':      {'en': 'left'       },
	'let':        {'en': 'let'        },
	'make':       {'en': 'made'       },
	'mean':       {'en': 'meant'      },
	'put':        {'en': 'put'        },
	'read':       {'en': 'read'       },
	'say':        {'en': 'said'       },
	'set':        {'en': 'set'        },
	'show':       {'en': 'shown'      },
	'tell':       {'en': 'told'       },
	'think':      {'en': 'thought'    },
	'understand': {'en': 'understood' },
	# Auxiliary verbs with 2 forms
	'can':        'could',
	'will':       'would',
	'shall':      'should',
	'may':        'might',
	# Auxiliary verbs with 1 form
	'must':       False, # have to?
	'used to':    False,
	# Adverbs / words with 1 form
	'just':       False,
	'really':     False,
	'':           False,
}

# For regular verb, exceptions is None or {}
def inflect(verb, suffix, exceptions=None):
	# Irregular verb with 1 form
	if exceptions is False:
		return verb
	# Irregular verb with 2 forms
	if type(exceptions) == str:
		return exceptions if suffix == 'ed' else verb
	# Irregular verb with 4 forms
	if exceptions and 'en' in exceptions and 'ed' not in exceptions:
		exceptions['ed'] = exceptions['en']
	# Irregular verb: use exception if exists
	if exceptions and suffix in exceptions:
		return exceptions[suffix]

	# Build remaining forms
	if not suffix:
		return verb
	if suffix == 'en':
		suffix = 'ed'
	# Double final consonant. Exceptions: consider, remember, happen
	if suffix[0] in 'ei' and re.search(r'[^aeiou](?!e[nr])[aeiou][bcdfgklmnrptvz]$', verb):
		verb += verb[-1]
	# take -ing -> taking 
	if suffix[0] in 'ei' and re.search(r'(?<!^)[^e]e$',  verb):
		verb = verb[:-1]
	# try  -s   -> tries
	if suffix[0] in 'es' and re.search(r'[^aeiou]y$',    verb):
		verb = verb[:-1] + 'i' + 'e'[:suffix[0] in 's']
	# wish -s   -> wishes
	if suffix[0] in 's'  and re.search(r'[osx]$|[cs]h$', verb):
		verb += 'e'

	return verb + suffix

# design constraints:
# verbs with T in present ender paired with another verb that doesn't have an extra word
# verbs with Z in present ender cannot have extra word (only due to finger gymnastics)
verb_ender_data = {
	# Auxiliary verbs
	'':           ('',       None  ),
	'can':        ('BGS',    None  ),
	'may':        ('PL',     'be'  ),
	'must':       ('PBLGS',  'be'  ), # no past tense: taken by just
	'shall':      ('RBL',    None  ),
	'will':       ('RBGS',   None  ),
	# adverbs
	'just':       ('PBLGSZ', None  ),
	'really':     ('RLG',    None  ),

	'ask':        ('RB',     None  ),
	'be':         ('B',      'a'   ),
	'become':     ('RPBG',   'a'   ),
	'believe':    ('BL',     'that'),
	'call':       ('RBLG',   None  ),
	'care':       ('RZ',     None  ),
	'change':     ('PBGZ',   None  ),
	'come':       ('BG',     'to'  ),
	'consider':   ('RBGZ',   None  ),
	'do':         ('RP',     'it'  ),
	'expect':     ('PGS',    'that'),
	'feel':       ('LT',     'like'),
	'find':       ('PBLG',   'that'),
	'forget':     ('RG',     'to'  ),
	'get':        ('GS',     'to'  ), # he had gotten; he had got to
	'give':       ('GZ',     None  ),
	'go':         ('G',      'to'  ),
	'have':       ('T',      'to'  ),
	'happen':     ('PZ',     None  ),
	'hear':       ('PG',     'that'),
	'hope':       ('RPS',    'to'  ),
	'imagine':    ('PLG',    'that'),
	'keep':       ('PBGS',   None  ),
	'know':       ('PB',     'that'),
	'learn':      ('RPBS',   'to'  ),
	'leave':      ('LGZ',    None  ),
	'let':        ('LS',     None  ),
	'like':       ('BLG',    'to'  ),
	'live':       ('LZ',     None  ),
	'look':       ('L',      None  ),
	'love':       ('LG',     'to'  ),
	'make':       ('RPBL',   'a'   ),
	'mean':       ('PBL',    'to'  ),
	'mind':       ('PBLS',   None  ),
	'move':       ('PLZ',    None  ),
	'need':       ('RPG',    'to'  ),
	'put':        ('PS',     'it'  ),
	'read':       ('RS',     None  ),
	'recall':     ('RL',     None  ),
	'realize':    ('RLS',    'that'),
	'remember':   ('RPL',    'that'),
	'remain':     ('RPLS',   None  ),
	'run':        ('R',      None  ),
	'say':        ('BS',     'that'),
	'see':        ('S',      None  ),
	'set':        ('BLS',    None  ),
	'seem':       ('PLS',    'to'  ),
	'show':       ('RBZ',    None  ),
	'take':       ('RBT',    None  ),
	'tell':       ('RLT',    None  ),
	'think':      ('PBG',    'that'),
	'try':        ('RT',     'to'  ),
	'understand': ('RPB',    'the' ),
#	'use':        ('Z',      'to'  ),
	'use':        ('Z',      None  ),
	'used to':    ('TZ',     None  ),
	'want':       ('P',      'to'  ),
	'wish':       ('RBS',    'to'  ),
	'work':       ('RBG',    'on'  ),
	# 'talk':     ('BLGT',   None  , None        ), # conflicts with like to

	# help
}

# generate verb forms
verb_forms = {} #OrderedDict()
for verb in verb_ender_data.keys():
	if verb in irregular_verb_data:
		exceptions = irregular_verb_data[verb] 
	else:
		exceptions = {}
	if type(exceptions) in [str, bool]:
		present_forms = verb
		past_forms    = verb
	else:
		present_forms = {
			None:                 inflect(verb, ''   , exceptions),
			'3ps':                inflect(verb, 's'  , exceptions),
			'present-participle': inflect(verb, 'ing', exceptions),
			'past-participle':    inflect(verb, 'en' , exceptions),
		}
		if 's1' in exceptions:
			present_forms.update({
				None:  exceptions['s'],
				'1ps': exceptions['s1'],
				'3ps': exceptions['s3'],
			})
		past_forms = {
			None:                 inflect(verb, 'ed' , exceptions),
			'root':               inflect(verb, ''   , exceptions),
			'present-participle': inflect(verb, 'ing', exceptions),
			'past-participle':    inflect(verb, 'en' , exceptions),
		}
		if 'ed13' in exceptions:
			past_forms.update({
				'3ps': exceptions['ed13'],
			})

	verb_forms[verb] = [present_forms, past_forms]

def add_key(stroke, key):
	if key in stroke:
		print(f'{key} already in {stroke}')
		return stroke
	# candidate = stroke + key
	candidate = re.sub(re.sub(rf'.*{key}.', '', 'T?S?D?Z?$'), rf'{key}\g<0>', stroke, 1)
	if sum(k in candidate for k in 'TSDZ') == 3:
		print(f'{candidate} not ergonomic')
		candidate = re.sub(r'T?S?D?Z?$', rf'TSDZ', candidate, 1)
	return candidate

verb_enders = {}
for verb, (verb_ender, extra_word) in verb_ender_data.items():
	present_ender            = verb_ender
	past_ender               = add_key(present_ender, 'Z' if 'S' in present_ender and 'Z' not in present_ender else 'D')
	present_ender_extra_word = add_key(present_ender, 'S' if 'T' in present_ender else 'T')
	past_ender_extra_word    = add_key(past_ender,    'S' if 'T' in present_ender else 'T')

	present_verb_data = verb_forms[verb][0]
	past_verb_data    = verb_forms[verb][1]
	queue = [
		(present_ender,            present_verb_data),
		(past_ender,               past_verb_data),
	]
	if extra_word:
		if type(present_verb_data) == str:
			present_verb_data_extra_word = present_verb_data + ' ' + extra_word
			past_verb_data_extra_word    = past_verb_data    + ' ' + extra_word
		else:
			present_verb_data_extra_word = {k: v + ' ' + extra_word for k, v in present_verb_data.items()}
			past_verb_data_extra_word    = {k: v + ' ' + extra_word for k, v in past_verb_data.items()}

		queue += [
			(present_ender_extra_word, present_verb_data_extra_word),
			(past_ender_extra_word,    past_verb_data_extra_word),
		]

	for (ender, verb_data) in queue:
		if ender in verb_forms:
			print(f'{verb}, {ender} already in verb_enders')
		verb_enders[ender] = verb_data

	continue

	if extra_word:
		if 'T' in present_ender:
			x = re.sub("D?Z?$", r"S\g<0>", present_ender, 1)
		else:
			x = re.sub("S?D?Z?$", r"T\g<0>", present_ender, 1)

		verb_forms[x] = ("present",
			m)


	# R -> RD; Z -> DZ
	past_enders = [re.sub("Z?$", r"D\g<0>", present_ender, 1)]
	# SD -> DS, SZ
	# SZ -> SDZ, TSDZ
	if "S" in present_ender:
		if "Z" in present_ender:
			# past_enders.append(re.sub("(?<!T)SZ$", r"TSDZ", present_ender, 1))
			past_enders[0] = re.sub("(?<!T)SZ$", r"TSDZ", present_ender, 1)
		else:
			past_enders[0] = present_ender + "Z"
	for past_ender in past_enders:
		if extra_word:
			if 'T' in past_ender or 'S' in past_ender:
				x = re.sub("T?D?S?Z?$", r"TSDZ", past_ender, 1)
			else:
				x = re.sub("S?D?Z?$", r"T\g<0>", past_ender, 1)

pprint.pprint(verb_enders, width=180)

