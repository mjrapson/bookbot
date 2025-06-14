def count_words(text):
    return len(text.split())

def get_character_counts(text):
    results = {}
    for char in text:
        if char.lower() in results:
            results[char.lower()] += 1
        else:
            results[char.lower()] = 1
    return results

def sort_on(dict):
    return dict["num"]

def get_sorted_count(character_counts):
    result = []
    for char, count in character_counts.items():
        result.append({"char": char, "num": count})
    
    result.sort(reverse=True, key=sort_on)

    return result
