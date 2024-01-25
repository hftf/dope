import re

# Declarative user settings
class Settings:
	# Note: There is duplication between KEY_MAP and STROKE_PARTS;
	# you will have to make changes in both places.
	# TODO refactor this to be more declarative/DRY eventually.
	
	# Mapping of five binary syntactic features to keys.
	KEY_MAP = {
		'question': '^',
		'contract': '+',
		'negation': '*',
		# aspect:
		'have':     'E',
		'be':       'U',
	}

	# Regular expression for validating and parsing strokes.
	# Must contain named capture groups for the following 7 keys:
	# question, contract, starter, modal, negation, aspect, ender
	STROKE_PARTS = re.compile(r'''^\#?
		(?P<question> \^?)
		(?P<contract> \+?)
		(?P<starter>  S?T?K?P?W?H?R?)
		(?P<modal>    A?O?)-?
		(?P<negation> \*?)
		(?P<aspect>   E?U?)
		(?P<ender>    F?R?P?B?L?G?T?S?D?Z?)$''', # note: D is tense
		re.X)

	STROKE_ORDER = [
		'question',
		'contract',
		'cosubordinator', 'subject', 'modal',
		'negation',
		'have', 'be',
		'hyphen',
		#'ender'
	]

	# Parses a stroke and returns a dict of the stroke split into 7 parts.
	@classmethod
	def STROKE_MATCHER(cls, stroke):
		match = cls.STROKE_PARTS.match(stroke)
		if not match:
			raise KeyError(f'Stroke "{stroke}" does not match STROKE_PARTS regex')
		return match.groupdict()
	
	SIMPLE_STARTERS_OVERLOAD = lambda parts: parts['starter'] + parts['modal']
	SIMPLE_PRONOUNS_OVERLOAD = lambda parts: parts['negation'] + parts['aspect']

	FALLBACK_SECOND_STROKE = '+'
	PASSIVE_SECOND_STROKE  = '+-P'

class DefaultSettings(Settings):
	pass

class JosiahSettings(Settings):
	KEY_MAP = {
		'question': 'U',
		'contract': '+',
		'negation': '*',
		# aspect:
		'have':     'F',
		'be':       'E',
	}

	STROKE_PARTS = re.compile(r'''^\#?
		(?P<caret>    \^?)
		(?P<contract> \+?)
		(?P<starter>  S?T?K?P?W?H?R?)
		(?P<modal>    A?O?)-?
		(?P<negation> \*?)
		(?P<be>       E?)
		(?P<question> U?)
		(?P<have>     F?)
		(?P<ender>    R?P?B?L?G?T?S?D?Z?)$''', # note: D is tense
		re.X)
	
	STROKE_ORDER = [
		'contract',
		'cosubordinator', 'subject', 'modal',
		'negation',
		'be', 'question', 'hyphen', 'have',
		#'ender'
	]

	def STROKE_MATCHER(stroke):
		stroke_parts = super(JosiahSettings, JosiahSettings).STROKE_MATCHER(stroke)
		stroke_parts['aspect'] = stroke_parts['be'] + stroke_parts['have']
		return stroke_parts

	SIMPLE_PRONOUNS_OVERLOAD = lambda parts: parts['caret'] + parts['be'] + parts['question']
	# need to also redefine SIMPLE_PRONOUNS in noun_data.py to use ^ instead of *

if __name__ == '__main__':
	# a few tests to debug stroke matching
	all_tests = {
		DefaultSettings: {
			'':    {},
			'TS':  {'starter': 'T', 'ender': 'S'},
			'-TS': {'ender': 'TS'},
			'ST':  {'starter': 'ST'},
			'ZS':  None, # raises KeyError

			'SWR*UTS': {'starter': 'SWR', 'negation': '*', 'aspect': 'U', 'ender': 'TS'},
		},
		JosiahSettings: {
			'SWR*UTS': {'starter': 'SWR', 'negation': '*', 'question': 'U', 'ender': 'TS'},
		},

	}
	for settings, tests in all_tests.items():
		for stroke, stroke_parts in tests.items():
			try:
				result = settings.STROKE_MATCHER(stroke)
				# drop empty keys
				result = {k: v for k, v in result.items() if v}
			except Exception as e:
				result = None
			
			emoji = "❌✅"[stroke_parts == result]
			print(f'Test: {stroke:24} Expect: {str(stroke_parts):40} Result: {str(result):40} {emoji}')

