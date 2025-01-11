from yogi import read

def expressio_prefixada():

    primer = read(str)

    if primer.isdigit():
        return int(primer)
    
    segon = expressio_prefixada()
    tercer = expressio_prefixada()
    
    if primer == "+":
        return segon + tercer
    
    if primer == "-":
        return segon - tercer
    
    if primer == "*":
        return segon * tercer

print(expressio_prefixada())