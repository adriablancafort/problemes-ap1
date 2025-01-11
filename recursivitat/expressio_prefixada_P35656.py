from yogi import read

def expressio_prefixada():

    primer = read(str)

    if primer.isdigit():
        return int(primer)
    
    segon = expressio_prefixada()
    if primer == "-":
        return -segon

    tercer = expressio_prefixada()   
    if primer == "+":
        return segon + tercer
    
    quart = expressio_prefixada()   
    if primer == "m":
        return max(segon, tercer, quart)

print(expressio_prefixada())

