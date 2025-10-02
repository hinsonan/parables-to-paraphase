# Data collected from https://media.bereanbiblesociety.org/wp-content/uploads/2012/08/24214800/ONE-HUNDRED-AND-SEVENTY-BIBLE-LESSONS.pdf
import re

# number words up to 99 (allow space or dash between tens and ones)
# numbers up to 99 (supports dash or space)
ones = r"(one|two|three|four|five|six|seven|eight|nine)"
teens = r"(ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen)"
tens = r"(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)"
two_digit = fr"(?:{teens}|{tens}(?:[ -]{ones})?)"
one_to_99 = fr"(?:{ones}|{two_digit})"

# hundreds
hundreds = fr"{ones} hundred(?: (?:and )?{one_to_99})?"

# full valid number (1–99 or hundreds)
full_number_pattern = fr"(?:{one_to_99}|{hundreds})"

# regex for exactly "lesson <number>"
pattern = re.compile(rf"^lesson {full_number_pattern}$", re.IGNORECASE)

#ChatGPT and I worked together on this REGEX. I would never figure out something like this on my own.

blacklisted_lines = ["Visit the J. C. O’Hair Online Library at https://bereanbiblesociety.org/j-c-ohair-online-library/"]

file_name = "T5vsGemma\\data\\ONE-HUNDRED-AND-SEVENTY-BIBLE-LESSONS.txt"

INDEX_OF_FIRST_lesson = 442

def clean_text(text):
    for line in blacklisted_lines:
        text = text.replace(line, "")
    return text.replace('\f', '').strip().lower()

with open(file_name, "r", encoding="utf-8") as f:
    raw_lessons = f.readlines()

cleaned_lessons = [clean_text(lesson) for lesson in raw_lessons[INDEX_OF_FIRST_lesson:]]
cleaned_lessons = "\n".join([line for line in cleaned_lessons if len(line) > 0])

lessons = []

for line in cleaned_lessons.split("\n"):
    if pattern.match(line):
        lessons.append("")
    else:
        if len(lessons) == 0:
            continue
        lessons[-1] += " " + line


print(f"Number of lessons: {len(lessons)}") #170 Expected

with open("T5vsGemma\\data\\cleaned_lessons.txt", "w", encoding="utf-8") as f:
    f.write("\n".join([line.strip() for line in lessons]))


