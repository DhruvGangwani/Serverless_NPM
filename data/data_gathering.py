import random
import json

options = ['three point six lakhs per annum', 'five lakhs', 'four lacs', 'seven lpa', 'four point eight lacs per aanum', 'seventy four thousand monthly',  'ninty k per month', 'fifty k monthly', 'three hundred k per year', 'half million', 'seven hundred thousand', 'five lac rupees', 'seventy six thousand per month', 'nine lakhs', 'seven thousand', 'eighteen lacs annually', 'forty four thousand per month', 'three point five', 'seven point nine', 'monthly fourteen k', 'yearly five thousand', 'ninty lakhs per year', 'one crore', 'seventy lakhs', 'fifty thousand monthly', 'seventy thousand only', 'six lac', 'seven lac', 'eleven lac', 'five to seven lpa', 'nine to ten lacs per annum', 'fourteen lacs', 'ten to eleven thousand per month', 'forty to fifty lakhs per annum']
string_options =  ['my current ctc is ', 'my current salary is', 'i earn around', 'my salary is', 'my renumeration is', 'my current package is ', 'my current renumeration is', 'my ctc is', 'my earning is around', 'my package is', 'i am earning', 'i am getting', 'i get', 'i am expecting', 'my expectation is around', 'i receive about', 'i want', 'i need atleast']
no_disclose = ['i dont want to disclose my salary', 'i am not interested to talk about my current package', 'i am not open to disclose my ctc', 'at the moment i dont want to disclose my ctc', 'i will not tell about my package', 'i dont want to tell you my current ctc']



def get_content(options, string_options, no_disclose):
	all_content = list()
	for str_opt in string_options:
		for opt in options:
			text = str_opt + ' ' + opt
			start = text.find(opt)
			end = start + len(opt)
			entity_name = 'amount'
			content = [text, {'entities': [[start, end, entity_name]]}]
			all_content.append(content)

	#including the options directly itself
	for opt in options:
		content = [opt, {'entities': [[0, len(opt), 'amount']]}]
		all_content.append(content)
	
	#adding no disclose examples to the dataset
	for opt in no_disclose:
		content = [opt, {'entities': [[0, 0, 'amount']]}]
		all_content.append(content)

	#shuffling the dataset
	random.shuffle(all_content)
	return all_content

all_content = get_content(options, string_options, no_disclose)
with open('content.json', 'w') as f:
	f.write(json.dumps(all_content))