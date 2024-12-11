def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()
    d = {}
    for row in rows:
      line = row.strip().split('\t')
      d[line[0]] = line[2]
    return d


