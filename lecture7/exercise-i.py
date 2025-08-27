survey_results = [
    ["python", "javaScipt", "C++"],
    ["python", "javaScipt", "C#"],
    ["python", "Java",],
    ["python", "C++", "javaScipt",],
    ["python", "javaScipt", "C++", "Java"],
]

choices_set = [set(p) for p in survey_results]
common_languages = set.intersection(*choices_set)
print("1. Languages chosen by all paeticcipants:", common_languages)

cm_l = set.union(*choices_set) - choices_set[0] - choices_set[-1]
print("2. Languages Only chosen ny one participant:", cm_l)

num_l = len(survey_results)
print("3.Number of unque languages :",num_l)

J_l = set.union(*choices_set) - choices_set[0] & choices_set[-1]
print("4.Languages chosen by qxactly two participant: ",J_l)

J = set.union(*choices_set) - choices_set[0] - choices_set[-1]
print("5. Participants with the same set of languages: ",J)

