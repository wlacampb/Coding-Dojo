import re

def get_matching_words(regex):
      words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

      print [word for word in words if re.search(regex, word)]

print ""
get_matching_words(r"v") # "r" ensures the regex is not evaluted as a Python expression
get_matching_words(r"ss")
get_matching_words(r".*e$")
get_matching_words(r"b\wb")
get_matching_words(r"b\w+")
get_matching_words(r"b\w*b")
get_matching_words(r"\w*a\w*e\w*i\w*o\w*u")
get_matching_words(r"^[regularexpsion]*$") # "^...$" evaluates from the beginning of the str, parses the first char for the specified chars "regularexpsion," parses the rest of the characters as such, and only prints the item from the arr if each character used corresponds to a char in the specified array
get_matching_words(r"(.)\1")
print ""
