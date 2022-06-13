
def merge_two_sorted_lists(a,b):
		sorted_list = [] 
		len_a = len(a)
		len_b = len(b)
		i = j = 0
		
		while i < len_a and j < len_b:
				if a[i] <= b[j]:
						sorted_list.append(a[i])
						i+=1
				else:
						sorted_list.append(b[j])
						j+=1
		
		return sorted_list

if __name__ == '__main__':
		a = [33,22,45,82,77]
		b = [99,44,11,54]
		
		print(merge_two_sorted_lists(a,b))
