with open('../data/descartes.txt') as f:
    text = f.read()

# Remove line breaks
text = text.replace('\n', ' ')

# Split into sentences
sentences = text.split('  ')

# Split sentences into words
for sentence in sentences:
    print sentence
