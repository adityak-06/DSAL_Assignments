def naive(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n-m+1):
        if text[i:i+m] == pattern:
            print("Found at index", i)

text = input("Enter text: ")
pattern = input("Enter pattern: ")

naive(text, pattern)