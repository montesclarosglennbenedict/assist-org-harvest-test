import assistorgapi
import json

institutions = json.loads(assistorgapi.get_institutions())

for institution in institutions:
    institution_id = str(institution['id'])
    institution_agreements = assistorgapi.get_institutions_agreements(institution_id)
    agreement = json.loads(assistorgapi.get_agreements("117", institution_id, "74", 'major'))
    desired_label = "Computer Science and Engineering/B.S."
    desired_key = str(next((report["key"] for report in agreement["reports"] if report["label"] == desired_label), None))
    agreement_mod = assistorgapi.get_agreements_mod(desired_key)
    output_file_path = "./ramen/"+institution_id+".json"
    try:
        with open(output_file_path, 'w') as file:
            file.write(agreement_mod)
    except:
        with open(output_file_path, 'w') as file:
            file.write("None")