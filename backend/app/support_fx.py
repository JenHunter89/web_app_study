import pandas as pd

def return_case_list(clinician_id):
    
    case_allocations = pd.read_csv("../../backend/data/case_allocations.csv")

    cases = list(set(case_allocations[(case_allocations["first_assessor"] == clinician_id) |
                                 (case_allocations["second_assessor"] == clinician_id) |
                                 (case_allocations["third_assessor"] == clinician_id)]["case"]))
    
    cases.sort()

    return cases
