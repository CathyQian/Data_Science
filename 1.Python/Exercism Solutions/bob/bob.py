import re
## problem description is not quite clear

def hey(phrase):
    # remove terminal white space
    phrase = phrase.strip()
    # if yell a question at him -- end with ? and all capital letters
    if phrase.endswith('?') and phrase.isupper():
        return "Calm down, I know what I'm doing!"

    # if ask a question -- end with ?
    elif phrase.endswith('?'):
        return 'Sure.'

    # if you yell at him --- all capital letters
    elif phrase.isupper():
        return 'Whoa, chill out!'

    # if address him without actually saying anything -- no letter input
    elif len(re.sub(r'\s', '', phrase)) == 0:
        return 'Fine. Be that way!'

    # anything else
    else:
        return 'Whatever.'
