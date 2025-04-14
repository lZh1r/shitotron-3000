if __name__ == '__main__':

    commands = {
        "idle": "00000000",
        "input": "0001",
        "jump": "0010",
        "write": "0011",
        "alu": "0101",
        "clr": "01110000",
        "na": "1000",
        "sum": "1001",
        "sub": "1010",
        "right": "1011",
        "left": "1100",
        "or": "1101",
        "and": "1110",
        "not": "1111"
    }

    filename = input()
    if filename[-4:] != ".ass":
        raise Exception("Unsupported file format")
    else:
        try:
            f = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError

    f = [i.replace('\n', '') for i in f.readlines()]
    compiled = open("assfile", "a")
    compiled.write("v2.0 raw\n")

    for i in f:
        line = i.split(' ')
        match line[0] :
            case "idle":
                compiled.write("0 ")
            case "clr":
                compiled.write("70 ")
            case _:
                if len(line) != 2:
                    raise Exception("Syntax Error!")
                binary = commands[line[0]] + line[1]
                compiled.write(f'{int(binary, 2):X} ')
    print("All done!")