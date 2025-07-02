def read_csv(file : str) -> list:
    with open(file, "r", encoding="utf8") as f:\
        return [ line.strip().split(',') for line in f.readlines()[1:]]
       