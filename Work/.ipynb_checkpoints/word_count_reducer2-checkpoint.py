
import sys
current_word = None
current_count = 0
word = None
dictNum = {}
for line in sys.stdin:
    # remove leading and trailing whitespaces
    line = line.strip()
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if current_word == word:
        current_count += count
    else:
        try:    
            if current_word:
                dictNum[word] += count
        except:
                dictNum[word] == count
        current_count = count
        current_word = word
FinalDict = sorted(dictNum.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(FinalDict)
for i in converted_dict:
    print(f"{i}: {converted_dict[i]}")
