from num2word import word as num2word


findings_mimic_template = {
'Enlarged_Cardiomediastinum' :  {
    0: ['No Enlarged Cardiomediastinum'.lower()],
    1: ['Enlarged Cardiomediastinum'.lower()],
},
'Cardiomegaly' :  {
    0: ['No Cardiomegaly'.lower()],
    1: ['Cardiomegaly'.lower()],
},
'Lung_Opacity' :  {
    0: ['No Lung Opacity'.lower()],
    1: ['Lung Opacity'.lower()],
},
'Lung_Lesion' :  {
    0: ['No Lung Lesion'.lower()],
    1: ['Lung Lesion'.lower()],
},
'Edema' :  {
    0: ['No Edema'.lower()],
    1: ['Edema'.lower()],
},
'Pneumonia' :  {
    0: ['No Pneumonia'.lower()],
    1: ['Pneumonia'.lower()],
},
'Consolidation' :  {
    0: ['No Consolidation'.lower()],
    1: ['Consolidation'.lower()],
},
'Atelectasis' :  {
    0: ['No Atelectasis'.lower()],
    1: ['Atelectasis'.lower()],
},
'Pneumothorax' :  {
    0: ['No Pneumothorax'.lower()],
    1: ['Pneumothorax'.lower()],
},
'Pleural_Effusion' :  {
    0: ['No Pleural Effusion'.lower()],
    1: ['Pleural Effusion'.lower()],
},
'Pleural_Other' :  {
    0: ['No Pleural Other'.lower()],
    1: ['Pleural Other'.lower()],
},
'Fracture' :  {
    0: ['No Fracture'.lower()],
1: ['Fracture'.lower()]
},
'Support_Devices' :  {
    0: ['No Support Devices'.lower()],
    1: ['Support Devices'.lower()],
},
}

findings_chexpert_template = findings_mimic_template

findings_chestray14_template = {
'Cardiomegaly': {
    0: ['no Cardiomegaly'.lower()],
    1: ['Cardiomegaly'.lower()],
},
'Emphysema': {
    0: ['no Emphysema'.lower()],
    1: ['Emphysema'.lower()],
},
'Effusion': {
    0: ['no Effusion'.lower()],
    1: ['Effusion'.lower()],
},
'Hernia': {
    0: ['no Hernia'.lower()],
    1: ['Hernia'.lower()],
},
'Infiltration': {
    0: ['no Infiltration'.lower()],
    1: ['Infiltration'.lower()],
},
'Mass': {
    0: ['no Mass'.lower()],
    1: ['Mass'.lower()],
},
'Nodule': {
    0: ['no Nodule'.lower()],
    1: ['Nodule'.lower()],
},
'Atelectasis': {
    0: ['no Atelectasis'.lower()],
    1: ['Atelectasis'.lower()],
},
'Pneumothorax': {
    0: ['no Pneumothorax'.lower()],
    1: ['Pneumothorax'.lower()],
},
'Pleural_Thickening': {
    0: ['no Pleural Thickening'.lower()],
    1: ['Pleural Thickening'.lower()],
},
'Pneumonia': {
    0: ['no Pneumonia'.lower()],
    1: ['Pneumonia'.lower()],
},
'Fibrosis': {
    0: ['no Fibrosis'.lower()],
    1: ['Fibrosis'.lower()],
},
'Edema': {
    0: ['no Edema'.lower()],
    1: ['Edema'.lower()],
},
'Consolidation': {
    0: ['no Consolidation'.lower()],
    1: ['Consolidation'.lower()],
},
}




view_template = {
    0  : ['Frontal'.lower()] ,
    1  : ['Lateral'.lower()] ,
    2  : ['Costal'.lower()]  ,
}

gender_names_template = {
    0 : ['Female'.lower()],
    1 : ['Male'.lower()],
}

view_detailed_template = {
        0: ['PA'.lower()] ,
        1: ['L'.lower()] ,
        2: ['AP_horizontal'.lower()] ,
        3: ['AP'.lower()] ,
        4: ['COSTAL'.lower()] ,
        17:[ 'EXCLUDE'.lower()] ,
        1: ['Lateral'.lower()] ,
        5: ['LL'.lower()] ,
        6: ['RL'.lower()] ,
        1: ['LATERAL'.lower()] ,
        7: ['LAO'.lower()] ,
        8: ['RAO'.lower()] ,
        9 :[ 'AP AXIAL'.lower()] ,
        10:[ 'SWIMMERS'.lower()] ,
        11:[ 'PA LLD'.lower()] ,
        12:[ 'AP LLD'.lower()] ,
        13:[ 'XTABLE LATERAL'.lower()] ,
        14:[ 'AP RLD'.lower()] ,
        15:[ 'PA RLD'.lower()] ,
        16:[ 'LPO'.lower()] ,
}

age_template = {
     i : [num2word(i).lower() + ' years old'] for i  in range(120)
}
