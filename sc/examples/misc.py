import json


CATS = (
    "Rule-of-Thumb Category",
    [
        "morality-ethics",
        "social-norms",
        "advice",  # rarely want these
        # "description",  # off by default, as very rarely want these
    ],
)

with open('../dialogue/train.json') as ofile:
    data = json.load(ofile)

context_set = set()

for x in data:
    context_set.add(data[x]['context'])
final_list = [("Wanting my boyfriend to go on a diet. [attrs] <{varies}> <all> [rot]", CATS)]
for x in context_set:
    final_list.append((x + " [attrs] <{varies}> <all> [rot]", CATS), )

print(final_list)

