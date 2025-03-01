import sys
import re

def main(argv):
  csv_path = argv[1]
  
  with open(csv_path, "r", encoding="utf-8") as csv_file:
    authors = set()
    periods = dict()

    next(csv_file) # skip header line

    nameMatch = r"(.*?)"
    descMatch = r"(.*?)"
    yearMatch = r"(\d{4})"
    genericMatch1 = r"(.*?)"
    genericMatch2 = r"(.*?)"
    timeMatch = r"(\d{2}:\d{2}:\d{2})"
    idMatch = r"(O\d+)"

    sep = r";"

    regex_str = (
      r"^" +
      nameMatch + sep +
      descMatch + sep +
      yearMatch + sep +
      genericMatch1 + sep +
      genericMatch2 + sep +
      timeMatch + sep +
      idMatch +
      r"$"
    )

    regex = re.compile(regex_str, re.DOTALL)
    segment = ""

    for line in csv_file:
      segment += line

      match = regex.match(segment)

      if match:
        segment = ""

        author = match.group(5)
        authors.add(author)

        period = match.group(4)
        name = match.group(1)
        if period not in periods:
          periods[period] = dict(list = [], quantity = 1)
        periods[period]["list"].append(name)
        periods[period]["quantity"] += 1
    
    authors = sorted(authors)
    # print each author
    print("Lista ordenada alfabeticamente dos compositores musicais:")
    for author in authors: print(author)
    print("")
    
    # print works in each period
    print("Distribuição de obras por período:")
    for period in periods:
      print(f"{period}: " + str(periods[period]["quantity"]))
    print("")

    # print all works
    for period in periods:
      print(f"{period}:")
      for work in periods[period]["list"]:
        print(f"{work}")
      print("")


if __name__ == "__main__":
  main(sys.argv)
