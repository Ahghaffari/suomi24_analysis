# Amirhossein Ghaffari - Lab1

# task1 
with open("Keywords.txt", "r") as keyword_file:
    all_keywords = [line.strip() for line in keyword_file]

# Read abstracts from Abstracts.txt
with open("Abstracts.txt", "r") as abstract_file:
    abstracts = abstract_file.read().split('\n\n')  # Split by blank lines

# Remove leading and trailing whitespace from abstracts
abstracts = [abstract.strip() for abstract in abstracts if abstract.strip()]

# Save abstracts to separate files (A1.txt, A2.txt, ..., A20.txt)
for i, abstract in enumerate(abstracts, start=1):
    with open(f"A{i}.txt", "w") as file:
        file.write(abstract)

# task 2

# Function to check if a query exists in the abstract
def query_exists_in_abstract(query, abstract):
    return int(query.lower() in abstract.lower())

# Test queries against abstracts
queries = ["Well-being", "Mental health", "Happiness"]

for query in queries:
    results = [query_exists_in_abstract(query, abstract) for abstract in abstracts]
    print(f"Query: {query} Results: {results}")


# task 3
# Create an inverted file (dictionary) where keys are keywords and values are lists of abstracts containing that keyword
inverted_file = {}
print(">>>>", all_keywords)
for keyword in set(all_keywords):
    if keyword:
        keyword = keyword.lower()
        for i, abstract in enumerate(abstracts, start=1):
            if keyword not in inverted_file:
                inverted_file[keyword] = []
            if keyword in abstract.lower():
                inverted_file[keyword].append(f"A{i}.txt")

print(inverted_file)

# task 4


inverted_file = {}
print(">>>>", all_keywords)
for keyword in set(all_keywords):
    if keyword:
        keyword = keyword.lower()
        for i, abstract in enumerate(abstracts, start=1):
            if keyword not in inverted_file:
                inverted_file[keyword] = []
            if keyword in abstract.lower():
                inverted_file[keyword].append(f"A{i}.txt")

print(inverted_file)



