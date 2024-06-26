import my_phrasing

tests = {
	"+STWRAOFD":      "would've",
	"^+SWHOUD":       "who'd you",
	"^+SWHAEB":       "what's he",
	"^+SWHAE":        "what's he",
	"^SWHAB":         "what to be",
	"SWHAB":          "what is",
	"+SWHAB":         "what's",
	"^+SWHAUB":       "what're you",
	"^+STWRE":        "to have",
	"^+STWREU":       "to have been",
	"SWRURLG":        "I am really",
	"STWRUFL":        "are feeling",
	"+STWRUFL":       None, # * 're feeling
	"STWREFL":        "have felt",
	"+STWREFL":       None, # * 've felt
	"+STKPWHREUFL":   None, # * 's been feeling,
	"+SKP-B":         None, # * and 's
# }
# foo = {
	"SWR*":           "I do not",
	"SWR*F":          "I do not have",
	"SWR*RP":         "I do not do",
	"SWR*E":          "I have not",
	"SWR*EF":         "I have not had",
	"SWR*ERP":        "I have not done",
	"SWR*U":          "I am not",
	"SWR*UF":         "I am not having",
	"SWR*URP":        "I am not doing",
	"SWR*EU":         "I have not been",
	"SWR*EUF":        "I have not been having",
	"SWR*EURP":       "I have not been doing",
	"^SWR*":          "do I not",
	"^SWR*F":         "do I not have",
	"^SWR*RP":        "do I not do",
	"^SWR*E":         "have I not",
	"^SWR*EF":        "have I not had",
	"^SWR*ERP":       "have I not done",
	"^SWR*U":         "am I not",
	"^SWR*UF":        "am I not having",
	"^SWR*URP":       "am I not doing",
	"^SWR*EU":        "have I not been",
	"^SWR*EUF":       "have I not been having",
	"^SWR*EURP":      "have I not been doing",
	"+SWR*":          "I don't",
	"+SWR*F":         "I don't have",
	"+SWR*RP":        "I don't do",
	"+SWR*E":         "I haven't",
	"+SWR*EF":        "I haven't had",
	"+SWR*ERP":       "I haven't done",
	"+SWR*U":         "I'm not",
	"+SWR*UF":        "I'm not having",
	"+SWR*URP":       "I'm not doing",
	"+SWR*EU":        "I haven't been",
	"+SWR*EUF":       "I haven't been having",
	"+SWR*EURP":      "I haven't been doing",
	"^+SWR*":         "don't I",
	"^+SWR*F":        "don't I have",
	"^+SWR*RP":       "don't I do",
	"^+SWR*E":        "haven't I",
	"^+SWR*EF":       "haven't I had",
	"^+SWR*ERP":      "haven't I done",
	"^+SWR*U":        "aren't I",
	"^+SWR*UF":       "aren't I having",
	"^+SWR*URP":      "aren't I doing",
	"^+SWR*EU":       "haven't I been",
	"^+SWR*EUF":      "haven't I been having",
	"^+SWR*EURP":     "haven't I been doing",
	"SWRO*D":         "I should not",
	"SWRO*FD":        "I should not have",
	"SWRO*RPD":       "I should not do",
	"SWRO*ED":        "I should not have",
	"SWRO*EFD":       "I should not have had",
	"SWRO*ERPD":      "I should not have done",
	"SWRO*UD":        "I should not be",
	"SWRO*UFD":       "I should not be having",
	"SWRO*URPD":      "I should not be doing",
	"SWRO*EUD":       "I should not have been",
	"SWRO*EUFD":      "I should not have been having",
	"SWRO*EURPD":     "I should not have been doing",
	"^SWRO*D":        "should I not",
	"^SWRO*FD":       "should I not have",
	"^SWRO*RPD":      "should I not do",
	"^SWRO*ED":       "should I not have",
	"^SWRO*EFD":      "should I not have had",
	"^SWRO*ERPD":     "should I not have done",
	"^SWRO*UD":       "should I not be",
	"^SWRO*UFD":      "should I not be having",
	"^SWRO*URPD":     "should I not be doing",
	"^SWRO*EUD":      "should I not have been",
	"^SWRO*EUFD":     "should I not have been having",
	"^SWRO*EURPD":    "should I not have been doing",
	"+SWRO*D":        "I shouldn't",
	"+SWRO*FD":       "I shouldn't have",
	"+SWRO*RPD":      "I shouldn't do",
	"+SWRO*ED":       "I shouldn't have",
	"+SWRO*EFD":      "I shouldn't have had",
	"+SWRO*ERPD":     "I shouldn't have done",
	"+SWRO*UD":       "I shouldn't be",
	"+SWRO*UFD":      "I shouldn't be having",
	"+SWRO*URPD":     "I shouldn't be doing",
	"+SWRO*EUD":      "I shouldn't have been",
	"+SWRO*EUFD":     "I shouldn't have been having",
	"+SWRO*EURPD":    "I shouldn't have been doing",
	"^+SWRO*D":       "shouldn't I",
	"^+SWRO*FD":      "shouldn't I have",
	"^+SWRO*RPD":     "shouldn't I do",
	"^+SWRO*ED":      "shouldn't I have",
	"^+SWRO*EFD":     "shouldn't I have had",
	"^+SWRO*ERPD":    "shouldn't I have done",
	"^+SWRO*UD":      "shouldn't I be",
	"^+SWRO*UFD":     "shouldn't I be having",
	"^+SWRO*URPD":    "shouldn't I be doing",
	"^+SWRO*EUD":     "shouldn't I have been",
	"^+SWRO*EUFD":    "shouldn't I have been having",
	"^+SWRO*EURPD":   "shouldn't I have been doing",
	"SWROERPD":       "I should have done",
	"+SWROERPD":      "I should've done",
	"+SWROFD":        "I should've",
	"+SWRAOFD":       "I would've", # * I'd have
	"+STWRAOFD":      "would've",
	"":               None,
	"HR-FR":          None,
	"^KPWRAO*EBT":    "will you not have been a",
	"^KPWRERP":       "have you done",
	"^KPWRAOLGD":     "would you like",
	"KPWRAOULGD":     "you would be liking",
	"SWR*BD":         "I was not",
	"^SWR*BD":        "was I not",
	"SWR*D":          "I did not",
	"^SWR*D":         "did I not",
	"KPWR*BD":        "you were not",
	"^KPWR*BD":       "were you not",
	"KPWR*D":         "you did not",
	"^KPWR*D":        "did you not",
	"KWHR*BD":        "he was not",
	"^KWHR*BD":       "was he not",
	"KWHR*D":         "he did not",
	"^KWHR*D":        "did he not",
	"SWR-F":          "I have",
	"KPWR-F":         "you have",
	"KWHR-F":         "he has",
	"TWR-F":          "we have",
	"TWH-F":          "they have",
	"SWR*B":          "I am not",
	"^SWR*B":         "am I not",
	"SWR*":           "I do not",
	"^SWR*":          "do I not",
	"KPWR*B":         "you are not",
	"^KPWR*B":        "are you not",
	"KPWR*":          "you do not",
	"^KPWR*":         "do you not",
	"KWHR*B":         "he is not",
	"^KWHR*B":        "is he not",
	"KWHR*":          "he does not",
	"^KWHR*":         "does he not",
	"TWR*B":          "we are not",
	"^TWR*B":         "are we not",
	"TWR*":           "we do not",
	"^TWR*":          "do we not",
	"TWH*B":          "they are not",
	"^TWH*B":         "are they not",
	"TWH*":           "they do not",
	"^TWH*":          "do they not",
	"SWR*EB":         "I have not been",
	"^SWR*EB":        "have I not been",
	"SWR*E":          "I have not",
	"^SWR*E":         "have I not",
	"KPWR*EB":        "you have not been",
	"^KPWR*EB":       "have you not been",
	"KPWR*E":         "you have not",
	"^KPWR*E":        "have you not",
	"KWHR*EB":        "he has not been",
	"^KWHR*EB":       "has he not been",
	"KWHR*E":         "he has not",
	"^KWHR*E":        "has he not",
	"SWRAO*RP":       "I will not do",
	"+SWRAORP":       "I'll do",
	"SWHAUFPB":       "what you find",
	# "SKPEUBGSZ":      "and I could",
	# "+SKPEUBGSZ":     "and I could",
	"SKPEUBGSZ":      "and I became",
	"TWRA*G":         "we cannot go",
	"^KPWRALTD":      "could you tell",
	"^STWR-RPL":      "to remember",
	"^STWR*RPL":      "not to remember",
	"TWHA*":          "they cannot",
	"TWH-RPD":        "they did",
	"SKWHR*D":        "she did not",
	"^+KPWRAO*EBT":   "won't you have been a",
	"§^+KPWRERP":     "have you done",
	"§^+KPWRAOLGD":   "would you like",
	"+KPWRAOULGD":    "you'd be liking",
	"+SWR*BD":        "I wasn't",
	"^+SWR*BD":       "wasn't I",
	"+SWR*D":         "I didn't",
	"^+SWR*D":        "didn't I",
	"+KPWR*BD":       "you weren't",
	"^+KPWR*BD":      "weren't you",
	"+KPWR*D":        "you didn't",
	"^+KPWR*D":       "didn't you",
	"+KWHR*BD":       "he wasn't",
	"^+KWHR*BD":      "wasn't he",
	"+KWHR*D":        "he didn't",
	"^+KWHR*D":       "didn't he",
	"+SWR*B":         "I'm not",
	"^+SWR*B":        "aren't I",
	"^SWR*B":         "am I not",
	"+SWR*":          "I don't",
	"^+SWR*":         "don't I",
	"+KPWR*B":        "you aren't",
	"^+KPWR*B":       "aren't you",
	"+KPWR*":         "you don't",
	"^+KPWR*":        "don't you",
	"+KWHR*B":        "he isn't",
	"^+KWHR*B":       "isn't he",
	"+KWHR*":         "he doesn't",
	"^+KWHR*":        "doesn't he",
	"+SWRAO*RP":      "I won't do",
	"§+SWHAUFPB":      "what you find",
	"§+SKPEUBGSZ":     "and I became",
	"+TWRA*G":        "we can't go",
	"§^+KPWRALTD":     "could you tell",
	"§^+STWR-RPL":     "to remember",
	"§^+STWR*RPL":     "not to remember",
	"+TWHA*":         "they can't",
	"§+TWH-RPD":       "they did",
	"+SKWHR*D":       "she didn't",
	"SWHOGDZ":        "who gave",
	"^STHR-B":        "is there",
	"^SWRA":          "can I",
	"+KWHR*PTD":      "he didn't want to",
	"+STWR*BLD":      "didn't believe",
	"SWHA*FRD":       "what it meant",
	"^TWHEG":         "have they gone",
	"KPWR*ES":        "you have not seen", # conflicts with 'empress'
	"KPWR*ES/+":      "you have not seen",
	"+TWRAO*GSZ":     "we wouldn't get",
	"KWHR-PTZ":       "he happens to",
	"^TWR-PL":        "may we",
	"^TWRUPL":        "*are we may",
	"SWRUPL":         "*I am may",
	"STPAF":          "*if has",
	"^STPAEUF":       "*if I have",
	"^SKWHROEUPLT":   "*shall she have been may be",
	"^KWHREUB":       "has he been being", #?
	"^SWRA*PB":       "can I not know", # *cannot I know
	"^+SWRA*PB":      "can't I know",
	"STHRAEULT":      "*there can have been telling",
	"STPHRAOEUPB":    "*there will have been knowing",
	"STPHRAEPB":      "*there can have known",
	"SWR-LT/+-P":     "I am told",
	"SWR-LTD/+-P":    "I was told",
	"^SWR-LT/+-P":    "am I told",
	"^SWR-LTD/+-P":   "was I told",
	"SWR*LT/+-P":     "I am not told",
	"SWR*LTD/+-P":    "I was not told",
	"^SWR*LT/+-P":    "am I not told",
	"^SWR*LTD/+-P":   "was I not told",
	"^SWR*LT/+-P":    "am I not told",
	"^+SWR*LTD/+-P":  "wasn't I told",
	"SWRELT":         "I have told",
	"SWRELT/+-P":     "I have been told",
	"SWRELTD/+-P":    "I had been told",
	"^SWRELT/+-P":    "have I been told",
	"^SWRELTD/+-P":   "had I been told",
	"+SWRELT/+-P":    "I've been told",
	"+SWRELTD/+-P":   "I'd been told",
	"SWREULT":        "I have been telling",
	"SWREULT/+-P":    "I have been being told",
	"SWHR":           "where",
	"TWH-RBT":        "they take",
	"TWH-RBT/+-P":    "they are taken",
	"TWHURBT":        "they are taking",
	"TWHURBT/+-P":    "they are being taken",
	"TWHERBT":        "they have taken",
	"TWHERBT/+-P":    "they have been taken",
	"TWH-RBTD":       "they took",
	"TWH-RBTD/+-P":   "they were taken",
	"TWHURBTD":       "they were taking",
	"TWHURBTD/+-P":   "they were being taken",
	"TWHERBTD":       "they had taken",
	"TWHERBTD/+-P":   "they had been taken",
	"TWHAORBT":       "they will take",
	"TWHAORBT/+-P":   "they will be taken",
	"TWHAOURBT":      "they will be taking",
	"TWHAOURBT/+-P":  "they will be being taken",
	"TWHAOERBT":      "they will have taken",
	"TWHAOERBT/+-P":  "they will have been taken",
	"TWH*RBT":        "they do not take",
	"TWH*RBT/+-P":    "they are not taken",
	"TWH*URBT":       "they are not taking",
	"TWH*URBT/+-P":   "they are not being taken",
	"TWH*ERBT":       "they have not taken",
	"TWH*ERBT/+-P":   "they have not been taken",
	"TWH*RBTD":       "they did not take",
	"TWH*RBTD/+-P":   "they were not taken",
	"TWH*URBTD":      "they were not taking",
	"TWH*URBTD/+-P":  "they were not being taken",
	"TWH*ERBTD":      "they had not taken",
	"TWH*ERBTD/+-P":  "they had not been taken",
	"TWHAO*RBT":      "they will not take",
	"TWHAO*RBT/+-P":  "they will not be taken",
	"TWHAO*URBT":     "they will not be taking",
	"TWHAO*URBT/+-P": "they will not be being taken",
	"TWHAO*ERBT":     "they will not have taken",
	"TWHAO*ERBT/+-P": "they will not have been taken",
	"^STWR-RBT":      "to take",
	"^STWR-RBT/+-P":  "to be taken",
	"^STWRERBT":      "to have taken",
	"^STWRERBT/+-P":  "to have been taken",
	"^STWR*RBT":      "not to take",
	"^STWR*RBT/+-P":  "not to be taken",
	"^STWR*ERBT":     "not to have taken",
	"^STWR*ERBT/+-P": "not to have been taken",
	"SWR":            "I",
	"§+SWR":          "I",
	"SWRUFL":         "I am feeling",
	"+SWRUFL":        "I'm feeling",
	"§+SWHAO*E":      "why she",
	"SWR-PLS/+-P":    "*I am seemed",
	"SWR-RGS":        None, # *I cares - TODO: add something to prevent auto suffixation
	"SWR-SDZ":        None, # *I saws
	"^STWR-D":        "to", # *toed
	"^STWR*D":        "not to", # *not toed
	"^SWHAO*EFT":     "why does she have to",
	"^+SWHAO*EFT":    "why's she have to",
	"^SWHAO*EFTD":    "why did she have to",
	"^SWHAO*EFTDZ":   None,
	"^+SWHAO*EFTD":   "why'd she have to",
	"^TWR":           "do we",
	"KPWH-GSZ/+-P":   "it was gotten", # by
	"STPAEUBD":       "if I were", # irrealis-were
	"^KPWR-BD":       "were you",
	"^KPWRUD":        "were you",
	"^SWR-PBLGS":     "must I",
	"^KPWR-PBLGS":    "must you",
	"^SWR-TDZ":       "did I used to",
	"^KPWR-TDZ":      "did you used to",
	"^SWR-PBLGSZ":    "do I just",
	"^KPWR-PBLGSZ":   "do you just",
	"SWRETDZ":        "I had used to",
	"^SWRETDZ":       "had I used to",
	"KPWHB":          "it is",
	"KPWHU":          "it is",
	"KPWHE":          "it has",
	"+KPWH-B":        "it's",
	"+KPWHU":         "it's",
	"+KPWHE":         "it's",
	"+STHAB":         "that's",
	"+STHA*B":        "that it's",
	"+KPWR-B/+-P":    "*you're been",
	"+KPWREBD":       "you'd been",
	"+KPWRAOUD":      "you'd be",
	"+KPWRAOD/+-P":   "you'd be",
	"^SWHOUD":        "who did you",
	"^+SWHOUD":       "who'd you",
	"^SWHAEB":        "what is he",
	"^+SWHAEB":       "what's he",
	"^SWHAE":         "what does he",
	"^+SWHAE":        "what's he",
	"^SWHAUB":        "what are you",
	"^+SWHAUB":       "what're you",
	"STWR-RBGT":      "work on",
	"^STWR-RBGT":     "to work on",
	"STWRARBGT":      "can work on",
	"§^STWRARBGT":     "can work on",
	"STWRA*RBGT":     "cannot work on",
	"§^STWRA*RBGT":    "cannot work on",
	"+STWRA*RBGT":    "can't work on",
	"§^+STWRA*RBGT":   "can't work on",
	"^+STWRE":        "to have", # *to've
	"^+STWREU":       "to have been", # *to've been
	"STWREU":         "have been",
	"STKPWHREU":      "has been",
	"SWR-FLT":        "I feel like",
	"+STWR*PLT":      "mayn't be",
	"SWRURLG":        "I am really",
}

t = p = q = 0
for i, (outline, expected_phrase) in enumerate(tests.items()):
	strict = not outline.startswith('§')

	outline = tuple(outline.split('/'))
	# if 45 > i or i > 50:
	# if i > 5:
		# continue
	print(f'{i:03} {"/".join(outline):18} = {str(expected_phrase):30} → ', end='')

	error = ''
	raise_grammar_errors = True
	try:
		result_phrase = my_phrasing.lookup(outline, raise_grammar_errors=raise_grammar_errors, strict=strict)
	except KeyError as e:
		result_phrase = None
		error = f' ({e})'
		if expected_phrase != result_phrase:
			# raise e
			pass
	passed = expected_phrase == result_phrase
	if raise_grammar_errors and not passed and (expected_phrase is None or expected_phrase.startswith('*')):
		passed = True
	emoji = "❌✅"[passed]
	t += 1
	q += passed
	print(f'{str(result_phrase) + error:32} {emoji}⎞')
	# print(my_phrasing.outline_to_avm(outline))
	if not result_phrase:
		print(f'\033[4m{" "*93}\033[0m')
		continue

	error = ''
	try:
		reversed_outlines = list(my_phrasing.reverse_lookup(result_phrase.strip('*'), strict=strict))
	except KeyError as e:
		reversed_outlines = [(None,)]
		error = f' ({e})'
		if outline not in reversed_outlines:
			# raise e
			pass
	emoji = "❌✅"[outline in reversed_outlines]
	p += outline in reversed_outlines
	phrase = my_phrasing.lookup(outline, raise_grammar_errors=False, strict=strict)
	if reversed_outlines and outline not in reversed_outlines and phrase == expected_phrase:
		p += 1j
		emoji = "🉑"
	reversed_outlines_j = ', '.join("/".join(o) for o in reversed_outlines)
	print(f'\033[4m    {str(reversed_outlines_j or []) + error:52}← {phrase:32} {emoji}\033[0m⎠')
	# print(f'{str(reversed_outlines) + error} {emoji}')

print(f'{q}/{t} and {p}/{t} tests passed\n')
	# assert expected == result

test_avm_1 = {
	# coordinator or subordinator (also conjunction, preposition, complementizer)
	# 'cosubordinator': None,
	
	# NOUN (SUBJECT) FEATURES
	'subject': 'I',
	# singular, plural
	'number': 'singular',
	# 1, 2, 3
	'person': '1',

	# VERB FEATURES
	# H  True = have (perfect), False = imperfect
	'have': True,
	# B  True = be (progressive/continuous), False = simple
	'be': True,
	# M  None, will, can, shall, may, must, need to
	'modal':    'can',
	# ‽  False = declarative (statement, indicative), True = interrogative (question, subject–auxiliary inversion)
	'question': True,
	# ±  polarity: False = positive (affirmative), True = negative
	'negation': True,
	# ’  True, False
	'contract': False,
	# T  '' = present, 'ed' = past
	'tense': 'ed',
	# V  main verb
	'verb': 'want',

	# X  to, it, a, the, that, on, like
	'extra_word': 'to',

	# A  None, just, really, even, still, always, never
	# 'adverb': None,

	# P  voice: False = active, True passive
	# 'passive': False,
	# subjunctive (irrealis), imperative

	'strict': True,
}
test_avm_2 = dict(**test_avm_1, passive=True)
avm_tests = [
	("^SWRA*EUPTD",     test_avm_1, "could I not have been wanting to"),
	("^SWRA*EUPTD/+-P", test_avm_2, "could I not have been being wanted to"),
]
for (outline, avm, phrase) in avm_tests:
	result_phrase   = my_phrasing.avm_to_phrase (avm,     raise_grammar_errors=True)
	result_avm      = my_phrasing.outline_to_avm(outline, raise_grammar_errors=True)
	result_outlines = my_phrasing.avm_to_outlines(avm)
	result_outlines_j = ['/'.join(result_outline) for result_outline in result_outlines]
	assert phrase  == result_phrase
	assert avm     == result_avm
	assert outline in result_outlines_j
print()

tests3 = {
	"hello":                [],
	"found she":            [],
	"she found":            ['SKWHR-FPBD'],
	"like":                 ['STWR-LG'],
	"feel like":            ['STWR-FLT'],
	"and looked":           ['SKP-LD', 'SKP-LD/+'],
	"and I":                ['SKPEU'], #, 'SKPEUD', '+SKPEU', '+SKPEUD'],
	"and I haven't":        [],
	"and you'd":            ['+SKPUFD'],
	"and you were":         ['SKPUBD'],
	"and it's":             ['+SKP*B', '+SKP*F'],
	"that is":              ['STHAB', 'STWHU', 'STWH-B'],
	"that has":             ['STHAF', 'STWHE', 'STWH-F'],
	"that's":               ['+STHAB', '+STWHU', '+STWH-B', '+STHAF', '+STWHE', '+STWH-F'],
	"that":                 ['STHA', 'STWH'],
	"where":                ['SWHR'],
	"what to do it":        ['^SWHARPT'],
	"that's not a":         [],
	"that isn't a":         ['+STWH*BT'],
	"I do":                 ['SWR-RP'],
	"I does":               [],
	"I did":                ['SWR-RPD'],
	"I do not":             ['SWR*'],
	"I don't":              ['+SWR*'],
	"I did not":            ['SWR*D'],
	"I didn't":             ['+SWR*D'],
	"I did not go":         ['SWR*GD'],
	"I didn't go":          ['+SWR*GD'],
	"I didn't went":        [],
	"I do not do":          ['SWR*RP'],
	"I did not do":         ['SWR*RPD'],
	"I do not did":         [],
	"I do not must":        [],
	"I am not must":        [],
	"I have not must":      [],
	"I will not must":      [],
	"I must not":           ['SWR*PBLGS'],
	"I not must":           [],
	"I do not will":        [],
	"I am not will":        [],
	"I have not will":      [],
	"I will not":           ['SWRAO*'],
	"I not will":           [],
	"am I not":             ['^SWR*U', '^SWR*B'],
	"aren't you":           ['^+KPWR*U', '^+KPWR*B'],
	"aren't I":             ['^+SWR*U', '^+SWR*B'],
	"I aren't":             [],
	"I am":                 ['SWRU', 'SWR-B'],
	"I am not":             ['SWR*U', 'SWR*B'],
	"I am not be":          [],
	"I am not being":       ['SWR*UB'],
	"I am not being been":  ['SWR*UB/+-P'],
	"I am not being being": [],
	"I do not do do":       [],
	"I go":                 ['SWR-G'],
	"I go not":             [],
	"I do not go":          ['SWR*G'],
	"I go not to":          [],
	"I have":               ['SWRE', 'SWR-F'],
	"I have not":           ['SWR*E'],
	"I have not have":      [],
	"I have not had":       ['SWR*EF'],
	"I have not had had":   [],
	"I have not had to":    ['SWR*EFT'],
	"I do not have":        ['SWR*F'],
	"I have to":            ['SWR-FT'],
	"I should be":          ['SWROBD', 'SWROUD'],
	"I should not be":      ['SWRO*BD', 'SWRO*UD'],
	"I became":             ['SWR-BGSZ', 'SWR-BGSD'],
	"can do":               ['STWRARP', 'STKPWHRARP'],
	"cannot I know":        [],
	"did I not go":         ['^SWR*GD'],
	"did not I go":         [],
	"didn't I go":          ['^+SWR*GD'],
	"didn't go I":          [],
	"did go I":             [],
	"did go foo I":         [],
	"go foo I":             [],
	"did":                  ['STKPWHR-RPD', 'STWR-RPD'],
	"not to go":            ['^STKPWHR*G', '^STWR*G'],
	"to not go":            [],
	"why to go":            ['^SWHAOG'],
	"there are":            ['STPHRU', 'STPHR-B'],
	"there must":           ['STHR-PBLGS', 'STPHR-PBLGS'],
	"there must be":        ['STHR-PBLGTS', 'STPHR-PBLGTS'],
	"there be must":        [],
	"there are must":       [],
	"there just":           ['STHR-PBLGSZ', 'STPHR-PBLGSZ'],
	"I am just":            ['SWRUPBLGSZ'],
	"you can":              ['KPWRA'],
	"you could":            ['KPWRAD'],
	"you can go":           ['KPWRAG'],
	"you can goes":         [],
	"I are":                [],
	"be to":                [],
	"to be":                ['^STKPWHRU', '^STKPWHR-B', '^STWRU', '^STWR-B'],
	"to is":                [],
	"to are":               [],
	"to go to":             ['^STKPWHR-GT', '^STWR-GT'],
	"I like":               ['SWR-LG'],
	"I like on":            [],
	"I feel":               ['SWR-FL'],
	"I feel like":          ['SWR-FLT'],
	"I go like":            [],
	"I feel like like":     [],
	"I do not be":          [],
	"I am taken":           ['SWR-RBT/+-P'],
	"I am taking":          ['SWRURBT'],
	"I used to":            ['SWR-TZ', 'SWR-TDZ'],
	"I use to":             [],
	"I using to":           [],
	"he uses to":           [],
	"did I use to":         [],
	"did I used to":        ['^SWR-TDZ'],
	"and they'll":          [],
	"would've":             ['+STKPWHRAOED', '+STKPWHRAOFD', '+STWRAOED', '+STWRAOFD'],
	"to":                   ['^STKPWHR', '^STWR'],
	"to really":            ['^STKPWHR-RLG', '^STWR-RLG'],
	"are feeling":          ['STWRUFL', '+STWRUFL'],
	"have felt":            ['STWREFL', '+STWREFL'],
}
# +STWH-BSZ that said
# +STWH*BSZ that didn't say

for (phrase, outlines) in tests3.items():
	result_outlines = my_phrasing.reverse_lookup(phrase)
	result_outlines_s = ["/".join(o) for o in result_outlines]
	passed = all(o in result_outlines_s for o in outlines) and all(o in outlines for o in result_outlines_s)
	print(f'\033[1m{phrase:24}\033[0m {str(outlines):36} {str(result_outlines_s):36} {"❌✅"[passed]}')
