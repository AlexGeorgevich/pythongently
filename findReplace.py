# Exercise #10: Find and Replace

def findAndReplace(text, oldText, newText):
    replacedText = ''
    i = 0
    while i < len(text):
        # If index i in text is the start of the oldText pattern, add
        # the replacement text:
        if text[i:i + len(oldText)] == oldText:
            # Add the replacement text:
            replacedText += newText
            # Increment i by the length of oldText:
            i += len(oldText)
        # Otherwise, add the characters at text[i] and increment i by 1:
        else:
            replacedText += text[i]
            i += 1

        return replacedText

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'