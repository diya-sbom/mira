EXTERNAL_DOCS = "/Users/diyaarun/mira-external-knowledge/docs.txt"


def retrieve(query):
    with open(EXTERNAL_DOCS, "r") as f:
        docs = f.read()

    matches = []

    for line in docs.splitlines():
        if any(word.lower() in line.lower() for word in query.split()):
            matches.append(line)

    return matches
