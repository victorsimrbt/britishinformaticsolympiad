conversion = {
    "A":"B",
    "B":"AB",
    "C":"CD",
    "D":"DC",
    "E":"EE"
    }

text = "DECADE"
index = 10
steps = 2

def a_growth(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return a_growth(n-1)+a_growth(n-2)

def b_growth(n):
    if n == 1 or n == 2:
        return 1
    return b_growth(n-1)+b_growth(n-2)

def convert(text):
    return ''.join([conversion[char] for char in text])

def chart_growth(text,steps):
    growths = []
    for char in text:
        if char == "A":
            growths.append(a_growth(steps))
        elif char == "B":
            growths.append(b_growth(steps))
        else:
            growths.append(2*steps)
    return growths

def relevant_text(index,text,steps):
    growths = chart_growth(text,steps)
    relevant_text = ''
    remaining_chars = index
    for i in range(len(growths)):
        remaining_chars -= growths[i]
        relevant_text += text[i]
        if remaining_chars <= 0:
            break
    return growths,relevant_text,remaining_chars

def count(text,steps):
    counts = [text.count("A"),text.count("B"),text.count("C"),text.count("D"),text.count("E")]
    print(counts)
    for i in range(steps):
        counts[0] += counts[1]
        counts[1] += counts[0]
        counts[2] += counts[3]
        counts[3] += counts[2]
        counts[4] += counts[4]
    return counts
        

print(count("DECADE",1),convert("DECADE"))