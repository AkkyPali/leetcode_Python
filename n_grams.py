def get_ngrams(n,string):
    ngrams = []
    if n < len(string):
        for i in range((len(string)-1)):
            ngrams.append(string[i:n+i])

        print(ngrams)
        output = {}
        for ngram in ngrams:
            output[ngram] = ngrams.count(ngram)

        return output

get_ngrams(2,'banana')