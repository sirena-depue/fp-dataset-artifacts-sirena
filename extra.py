import json 

input_files  = ["hotpot_dev_distractor_v1.json",     "hotpot_dev_fullwiki_v1.json",     "hotpot_train_v1.1.json"]
output_files = ["hotpot_dev_distractor_v1_MOD.json", "hotpot_dev_fullwiki_v1_MOD.json", "hotpot_train_v1.1_MOD.json"]

for i,input_file in enumerate(input_files):
    with open(input_file, "r") as file:
        data = json.load(file)

    expanded_data = []

    # Process each entry in the original data
    for entry in data:
        hypothesis = entry.get("question")  
        supporting_facts = dict(entry.get("supporting_facts", []))
        type_ = entry.get("type", "")
        level = entry.get("level", "")
        _id = entry.get("_id", "")

        # Process each paragraph in premise
        for paragraph_ in entry.get("context", []):
            title, paragraph = paragraph_
            label = 1 if title in supporting_facts else 0
            new_entry = {
                "_id": _id,
                "hypothesis": hypothesis,
                "premise": paragraph[0],
                "label": label,
                "type": type_,
                "level": level
            }
            expanded_data.append(new_entry)

    output_file = output_files[i]
    with open(output_file, "w") as file:
        json.dump(expanded_data, file, indent=4)

    print(f"Data saved to {output_file}")