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

processed_list = []
with open('../dialogue/SIQ_CA.json') as ofile:
    for dat in ofile.readlines():
        if 'Situation: ' in dat:
            final = dat[12:-33]
            processed_list.append(final)

processed_list = set(processed_list)

context_set = set()
with open('../dialogue/train.json') as ofile:
    data = json.load(ofile)

for x in data:
    context_set.add(data[x]['context'])
# print(context_set,processed_list)
x = context_set.difference(processed_list)
# print(len(x))
print(len(processed_list),len(context_set))
x = list(x)

# with open('../dialogue/pure.json','w+') as ofile:
#     json.dump(x,ofile)
#
#
# final_list = [("Wanting my boyfriend to go on a diet. [attrs] <{varies}> <all> [rot]", CATS)]
# for xx in context_set:
#     final_list.append(x)
#
# print(len(final_list))

with open('../dialogue/pure.json') as ofile:
    data = json.load(ofile)

context_set = set()

for x in data:
    context_set.add(x)
final_list = list()
for x in context_set:
    final_list.append((x + " [attrs] <{varies}> <all> [rot]", CATS), )
print(len(final_list))
# return final_list

