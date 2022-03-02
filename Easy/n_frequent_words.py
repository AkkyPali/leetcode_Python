# Return Top N Frequent Words
posting = "Herbal sauna uses the healing properties of herbs in combination with distilled water. The water evaporates and distributes the effect of the herbs throughout the room. A visit to the herbal sauna can cause real miracles, especially for colds."
  
n = 3

def n_frequent_words(posting,N):
  posting = posting.lower().split()
  hashmap = {}
  for word in posting:
    if word in hashmap.keys():
      hashmap[word] = hashmap[word] + 1
    else:
      hashmap[word] = 1
  return hashmap.items()
  values = sorted(hashmap.items(), key = lambda x:x[1], reverse = True)
  return values[:n]
print(n_frequent_words(posting,n))