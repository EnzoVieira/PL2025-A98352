import sys

class Counter:
  def __init__(self):
    self.acc = 0
    self.isOn = True

  def result(self):
    print(">> " + str(self.acc))
  
  def start(self, line):
    i = 0
    segmentRead = ""

    while i < len(line):
      char = line[i]
      segmentRead += char

      if char.isdigit():
        numberText = char # concat number read to str

        # read entire number
        while i+1 < len(line) and line[i+1].isdigit():
          segmentRead += line[i+1]
          numberText += line[i+1]
          i += 1

        if self.isOn:
          self.acc += int(numberText)

      elif char == "=":
        print(segmentRead)
        self.result()
        segmentRead = ""

      elif char.lower() == "o" and line[i:i+3].lower() == "off":
        self.isOn = False

      elif char.lower() == "o" and line[i:i+2].lower() == "on":
        self.isOn = True

      i += 1

    print(segmentRead)


if __name__ == "__main__":
  counter = Counter()
  for line in sys.stdin:
    counter.start(line.strip())
  counter.result()
