def split_sentence(sentence, max_length=140):
    words = sentence.split()  # Split the sentence into words
    result = []
    current_block = []

    for word in words:
        if len(' '.join(current_block + [word])) <= max_length:
            current_block.append(word)
        else:
            result.append(' '.join(current_block))
            current_block = [word]

    if current_block:
        result.append(' '.join(current_block))

    return result