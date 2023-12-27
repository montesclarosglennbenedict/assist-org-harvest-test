import assistorgapi
import json

institutions = json.loads(assistorgapi.get_institutions())

for institution in institutions:
    institution_id = str(institution['id'])
    institution_agreements = assistorgapi.get_institutions_agreements(institution_id)
    agreement = json.loads(assistorgapi.get_agreements("117", institution_id, "74", 'major'))
    desired_label = "Data Theory/B.S."
    desired_key = str(next((report["key"] for report in agreement["reports"] if report["label"] == desired_label), None))
    agreement_mod = assistorgapi.get_agreements_mod(desired_key)
    print(desired_key)
    print(agreement_mod)
    output_file_path = "./data_theory_ucla/"+institution_id+".json"
    with open(output_file_path, 'w') as json_file:
        json.dump(agreement_mod, json_file, indent=2)