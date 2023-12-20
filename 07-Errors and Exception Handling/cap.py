def cap_text(text):
    # return text.title()  # replace .capitalize() with .title()

    # first pass
    #return text.capitalize() 

    # second pass
    retv = []
    for w in text.split(" "):
        retv.append(w.capitalize())
    return ' '.join(retv)