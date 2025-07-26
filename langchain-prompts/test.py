words = ["bat", "tab", "eat", "tea", "tan", "nat"]

[['bat', 'tab'], ['eat', 'tea'], ['tan', 'nat']]

from collections import defaultdict

def group_words(words):
    anagram = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        anagram[key].append(word)

    return list(anagram.values())

print(group_words(words))

max_salary = Company.objects.aggregate(Max('salary'))
second_max_salary = Company.objects.filter(salary__lt=max_salary).aggregate(Max('salary'))

# author 
# book - author(fk)

authors = Books.objects.values('author').annotate(bookcnt= Count('id'))
                                        .filter(bookcnt_gt=3)
                                        .val