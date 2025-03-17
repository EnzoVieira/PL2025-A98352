import re

def main():
  with open("example.txt", "r") as markdown_file:
    text = markdown_file.read()

    header_pattern = r"(#{1,3}) (.*)"
    bold_pattern = r"\*\*(.*)\*\*"
    italic_pattern = r"\*(.*)\*"

    ordered_list_pattern = r"((?:\d+\.\s+.*(?:\n|$))+)"

    link_pattern = r"(?<!\!)\[(.*)\]\((.*)\)"
    img_pattern = r"\!\[(.*)\]\((.*)\)"

    def replace_ordered_list(match):
      ordered_list = match.group(1)
      lis = re.sub(r"\d+\.\s+(.*)", r"<li>\1</li>", ordered_list)
      return f"<ol>\n{lis}</ol>\n"

    r = re.sub(header_pattern, lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>", text)
    r = re.sub(bold_pattern, r"<b>\1</b>", r)
    r = re.sub(italic_pattern, r"<i>\1</i>", r)
    r = re.sub(ordered_list_pattern, replace_ordered_list, r, 0, re.MULTILINE)
    r = re.sub(link_pattern, r'<a href="\2">\1</a>', r)
    r = re.sub(img_pattern, r'<img src="\2" alt="\1"/>', r)

    print(r)

if __name__ == "__main__":
  main()