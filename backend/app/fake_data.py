import pandas as pd
import faker as fk
import random

case_nos = list(range(1, 301))

## tabular preop data
ages = []
hbs = []
specialties = []

for i in range(0,300):
    ages.append(random.randint(18, 100))
    hbs.append(round(random.uniform(10, 15),1))
    specialties.append(random.choice(["urology", "gynae", "general"]))

preop_data =  pd.DataFrame({'case_id': case_nos,
                            'age': ages, 
                            'haemoglobin': hbs,
                            'specialty': specialties})

preop_data.to_csv("../data/preop_data.csv")


## ts intraop data

all_timepoints = []
hrs = []
sbps = []
spo2s = []
vent_mode = []

intraop_data =  pd.DataFrame(columns = ['case_id',
                                        'timepoint',
                                        'hr',
                                        'sys_bp',
                                        'spo2',
                                        'vent_mode'
                                        ])

for i in range(0,300):

    timepoints = list(range(0, 24))
    hrs = []
    sbps = []
    spo2s = []
    vent_mode = []
    for t in timepoints:
        hrs.append(random.randint(40, 150))
        sbps.append(random.randint(50, 180))
        spo2s.append(random.randint(88, 101))
        vent_mode.append(random.choice(["PVC", "VCV", "SV"]))

    case_id_list = [i] * 24

    intraop_case =  pd.DataFrame({'case_id' : case_id_list,
                                  'timepoint': timepoints,
                                  'hr': hrs,
                                  'sys_bp': sbps,
                                  'spo2': spo2s,
                                  'vent_mode': vent_mode})

    intraop_data = pd.concat([intraop_data, intraop_case])

print(intraop_data.head())
print(intraop_data.info())

intraop_data.to_csv("streamlit_app/data/intraop_data.csv")
    

