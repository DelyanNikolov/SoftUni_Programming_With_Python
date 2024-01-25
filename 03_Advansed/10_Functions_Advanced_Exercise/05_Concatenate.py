def concatenate(*args, **kwargs):
    text = "".join(args)

    for key, word in kwargs.items():
        if key in text:
            text = text.replace(key, word)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
