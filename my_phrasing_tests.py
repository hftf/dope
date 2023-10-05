import my_phrasing

# print(obj_to_phrase(test_obj_1))
'were you'

tests = {
	"":               None,
	"HR-FR":          None,
	"^KPWRAO*EBT":    "will you not have been a",
	"KPWR*B":         "you are not",
	"^KPWR*B":        "are you not",
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
	"SWR-T":          "I have",
	"KPWR-T":         "you have",
	"KWHR-T":         "he has",
	"TWR-T":          "we have",
	"TWH-T":          "they have",
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
	"SWHAUFPB":       "what you find",
	"SWROERPD":       "I should have done",
	"SWRO*ERPD":      "I should not have done",
	#                 "SKPEUBGSZ":   "and I could",
	"SKPEUBGSZ":      "and I became",
	"TWRA*G":         "we cannot go",
	"^KPWRALTD":      "could you tell",
	"^STWR-RPL":      "to remember",
	"^STWR*RPL":      "not to remember",
	"TWHA*":          "they cannot",
	"TWH-RPD":        "they did",
	"SKWHR*D":        "she did not",

	"^+KPWRAO*EBT":   "won't you have been a",
	"+KPWR*B":        "you aren't",
	"^+KPWR*B":       "aren't you",
	"^+KPWRERP":      "have you done",
	"^+KPWRAOLGD":    "would you like",
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
	"^+SWR*B":        "am I not", # aren't I
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
	"+SWHAUFPB":      "what you find",
	"+SWROERPD":      "I should have done",
	"+SWRO*ERPD":     "I shouldn't have done",
	#                 "+SKPEUBGSZ":   "and I could",
	"+SKPEUBGSZ":     "and I became",
	"+TWRA*G":        "we can't go",
	"^+KPWRALTD":     "could you tell",
	"^+STWR-RPL":     "to remember",
	"^+STWR*RPL":     "not to remember",
	"+TWHA*":         "they can't",
	"+TWH-RPD":       "they did",
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
	"^TWRUPL":        "*are we may[*ing]",
	"SWRUPL":         "*I am may[*ing]",
	"STPAT":          "*if has",
	"^STPAEUT":       "*if I have",
	"^SKWHROEUPLT":   "*shall she have been may[*ing] be",
	"^KWHREUB":       "has he been being", #?
	"^SWRA*PB":       "can I not know", # *cannot I know
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
	"+SWR":           "I",
	"SWRUFL":         "I am feeling",
	"+SWRUFL":        "I'm feeling",
	"+SWHAO*E":       "why she",
	"SWR-PLS/+-P":    "*I am seemed",
	"SWR-RGS":        None, # *I cares - TODO: add something to prevent auto suffixation
	"^+SWHAO*ETS":    "why does she have to",
	"^TWR":           "do we",
	"KPWH-GSZ/+-P":   "it was gotten", # by
}

for test, expected in tests.items():
	print(f'{test:18} = {str(expected):30} Result: ', end='')
	error = ''
	try:
		result = my_phrasing.lookup(tuple(test.split('/')), False)
	except KeyError as e:
		result = None
		error = f' ({e})'
		if expected != result:
			raise e
	emoji = "❌✅"[expected == result]
	print(f'{str(result) + error:32} {emoji}')
	# assert expected == result
