movies = ['Holy', 1975, 'jones', 91, ['Graham', ['palin', 'john', 'Gilliam', 'Eric', 'terry']]]
def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item)
		else:
			print(each_item)