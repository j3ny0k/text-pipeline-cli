def upper(words):
    return [w.upper() for w in words]
def lower(words):
    return [w.lower() for w in words]
def reverse(words):
    return [w[::-1] for w in words]
def short(words):
    return [w for w in words if len(w) <= 4]

ops = {
    'upper': upper,
    'lower': lower,
    'reverse': reverse,
    'short': short
}

words = input('words: ').split()

operations = input('operations: ').split()

result = words

for name in operations:
    result = ops[name](result)

print(result)