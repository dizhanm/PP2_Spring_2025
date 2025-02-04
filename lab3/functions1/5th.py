def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        i = l
        while i <= r:
            s[l], s[i] = s[i], s[l]  
            permute(s, l + 1, r)     
            s[l], s[i] = s[i], s[l]  #
            i += 1

def print_permutations(string):
    s = list(string)
    permute(s, 0, len(s) - 1)


string = input()
print_permutations(string)