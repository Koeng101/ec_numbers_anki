import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

def find_2nd(string, substring):
   return string.find(substring, string.find(substring) + 1)

f = open("first.txt", "w")
f.write("EC 1; Oxidoreductases\n")
f.write("EC 2; Transferases\n")
f.write("EC 3; Hydrolases\n")
f.write("EC 4; Lyases\n")
f.write("EC 5; Isomerases\n")
f.write("EC 6; Ligases\n")
f.close()

t2 = 0
t3 = 0
t4 = 0

pages = []
for i in range(1,7):
    second_level = {}
    third_level = {}
    fourth_level = {}
    p_wiki = wiki_wiki.page("List of EC numbers (EC {})".format(i))
    p_lines = p_wiki.text.split("\n")
    for line in p_lines[2:]:
        if len(line) < 6:
            continue
        num = line.split(" ")[1].split(".")
        if len(num) == 2:
            start = find_2nd(line, " ")
            second_level[line[:start]] = line[start+1:]
        if len(num) == 3:
            start = find_2nd(line, " ")
            if start == -1:
                continue
            third_level[line[:start]] = line[start+1:]
        if len(num) == 4:
            start = find_2nd(line, " ")
            if start == -1:
                continue
            fourth_level[line[:start-1]] = line[start+1:]

    f = open("{}/second.txt".format(i), "w")
    for key, value in second_level.items():
        f.write("{}; {}\n".format(key, value))
    f.close()

    f = open("{}/third.txt".format(i), "w")
    for key, value in third_level.items():
        f.write("{}; {}\n".format(key, value))
    f.close()

    f = open("{}/fourth.txt".format(i), "w")
    for key, value in fourth_level.items():
        f.write("{}; {}\n".format(key, value))
    f.close()

    print("EC {} has {} second level".format(i, len(second_level)))
    print("EC {} has {} third level".format(i, len(third_level)))
    print("EC {} has {} fourth level".format(i, len(fourth_level)))

    t2 += len(second_level)
    t3 += len(third_level)
    t4 += len(fourth_level)

print("\nTotal second level: {}".format(t2))
print("Total third level: {}".format(t3))
print("Total fourth level: {}".format(t4))
