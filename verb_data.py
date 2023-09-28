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

# For regular verb, exceptions is None
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

# generate verb forms
verb_forms = {} #OrderedDict()
for verb, exceptions in irregular_verb_data.items():
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

	verb_forms[verb] = [('present', present_forms), ('past', past_forms)]

	continue

		# if extra_word:
			# m = {k: v + ' ' + extra_word for k, v in present_forms.items()}

	# if present_ender in verb_forms:
	# 	print( present_ender)
	verb_forms[present_ender] = ("present", 
		(present_forms))
	if extra_word:
		if 'T' in present_ender:
			x = re.sub("D?Z?$", r"S\g<0>", present_ender, 1)
		else:
			x = re.sub("S?D?Z?$", r"T\g<0>", present_ender, 1)
		if x in verb_forms:
			print( x)
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
		if not verb or verb[0] != verb[0].lower():
			past_forms = exceptions
			if exceptions:
				past_forms = ' ' + past_forms
			if extra_word:
				m = past_forms + ' ' + extra_word
		else:
			past_forms = {
				None:                 inflect(verb, "ed" , exceptions),
				"root":               inflect(verb, ""   , exceptions),
				# "3ps":                inflect(verb, "s"  , exceptions),
				"present-participle": inflect(verb, "ing", exceptions),
				"past-participle":    inflect(verb, "en" , exceptions),
			}
			if extra_word:
				m = {k: v + ' ' + extra_word for k, v in past_forms.items()}

		if past_ender in verb_forms:
			print( past_ender)
		verb_forms[past_ender] = ("past", 
			(past_forms))
		if extra_word:
			if 'T' in past_ender or 'S' in past_ender:
				x = re.sub("T?D?S?Z?$", r"TSDZ", past_ender, 1)
			else:
				x = re.sub("S?D?Z?$", r"T\g<0>", past_ender, 1)

			if x in verb_forms:
				print( x)
			verb_forms[x] = ("past",
				m)

pprint.pprint(verb_forms, width=180)


# design constraints:
# verbs with T in present ender paired with another verb that doesn't have an extra word
# verbs with Z in present ender cannot have extra word (only due to finger gymnastics)
verbs = {
	# Auxiliary verbs
	# These do not combine naturally with middle/structures.
	'':           ('',       None  ),
	'Can':        ('BGS',    None  ),
	'May':        ('PL',     'be'  ),
	'Must':       ('PBLGS',  'be'  ), # no past tense: taken by just
	'Shall':      ('RBL',    None  ),
	'Will':       ('RBGS',   None  ),
	# Adverbs
	'Just':       ('PBLGSZ', None  ),
	'Really':     ('RLG',    None  ),

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
	'Used to':    ('TZ',     None  ),
	'want':       ('P',      'to'  ),
	'wish':       ('RBS',    'to'  ),
	'work':       ('RBG',    'on'  ),
	# 'talk':     ('BLGT',   None  , None        ), # conflicts with like to

	# help
}
