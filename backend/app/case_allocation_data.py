import pandas as pd

case_allocations = pd.read_csv("streamlit_app/data/case_allocations.csv")

case_allocations.info()

assessor_cases_dict = {}

for assessor in set(case_allocations["first_assessor"]):

    cases = list(set(case_allocations[(case_allocations["first_assessor"] == assessor) |
                                 (case_allocations["second_assessor"] == assessor) |
                                 (case_allocations["third_assessor"] == assessor)]["case"]))
    
    cases.sort()

    assessor_cases_dict[assessor] = [cases]

assessor_cases_df = pd.DataFrame.from_dict(assessor_cases_dict, orient = "index").reset_index().rename(columns = {"index": "clinician",
                                                                                                                  0: "case_list"})

print(assessor_cases_df.head())

assessor_cases_df.to_csv("streamlit_app/data/assessor_cases.csv")

responses_df = pd.DataFrame(columns = ["assessor", "case", "first_prediction", "second_prediction"])

responses_df.to_csv("streamlit_app/data/responses.csv")