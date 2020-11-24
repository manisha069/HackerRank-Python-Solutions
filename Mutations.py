def mutate_string(string, position, character):
    ss=string[:position]+character+string[position+1:]
    return ss

