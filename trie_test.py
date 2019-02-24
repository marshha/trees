#!/usr/bin/python3
import sys
import random
import trie

with open("/usr/share/dict/words", "r") as fp:
    words = fp.read().splitlines()

MAX_WORDS = 1024
MAX_ITERS = 1024

sys.stdout.write("\r\n")
for i in range(0, MAX_ITERS):
    sys.stdout.write("\r" + str(i))
    words_list = set()
    for x in range(0, MAX_WORDS):
        word = words[random.randrange(0, len(words))]
        words_list.add(word)

    t = trie.Trie()
    for w in words_list:
        t.insert(w)

    if not [x for x in t.startsWith("")] == sorted(list(words_list)):
        print("Lists don't match")

    for w in words_list:
        if not t.search(w):
            print("Failed to find ", w)

    not_words_list = [ x for x in words if x not in words_list ]
    for w in not_words_list:
        if t.search(w):
            print("Found word not inserted: ", w)

    rand_word = list(words_list)[random.randrange(0, len(words_list))]
    rand_word_prefix = rand_word[:random.randrange(0, len(rand_word))]

    rand_prefix_list = [ x for x in sorted(list(words_list)) if x.startswith(rand_word_prefix)]

    if not rand_prefix_list == [ x for x in t.startsWith(rand_word_prefix)]:
        print("Prefix search failed: ", rand_prefix_list, t.startsWith(rand_word_prefix))

if False:
    t = trie.Trie()
    print(t.search("apple") == False)
    t.insert("apple")
    print(t.search("apple") == True)
    print(t.search("app") == False)
    print(t.search("appl") == False)
    print([x for x in t.startsWith("app")] == ["apple"])

    t.insert("app")
    print([x for x in t.startsWith("")] == ["app", "apple"])

