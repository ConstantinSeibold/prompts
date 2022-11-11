from num2word import word as num2word


findings_mimic_template = {
'Enlarged_Cardiomediastinum' :  {
    1: ['Enlarged Cardiomediastinum'.lower()],
},
'Cardiomegaly' :  {
    1: ['Cardiomegaly'.lower()],
},
'Lung_Opacity' :  {
    1: ['Lung Opacity'.lower()],
},
'Lung_Lesion' :  {
    1: ['Lung Lesion'.lower()],
},
'Edema' :  {
    1: ['Edema'.lower()],
},
'Pneumonia' :  {
    1: ['Pneumonia'.lower()],
},
'Consolidation' :  {
    1: ['Consolidation'.lower()],
},
'Atelectasis' :  {
    1: ['Atelectasis'.lower()],
},
'Pneumothorax' :  {
    1: ['Pneumothorax'.lower()],
},
'Pleural_Effusion' :  {
    1: ['Pleural Effusion'.lower()],
},
'Pleural_Other' :  {
    1: ['Pleural Other'.lower()],
},
'Fracture' :  {
1: ['Fracture'.lower()]
},
'Support_Devices' :  {
    1: ['Support Devices'.lower()],
},
}

findings_chexpert_template = findings_mimic_template

findings_chestray14_template = {
'Cardiomegaly': {
    1: ['Cardiomegaly'.lower()],
},
'Emphysema': {
    1: ['Emphysema'.lower()],
},
'Effusion': {
    1: ['Effusion'.lower()],
},
'Hernia': {
    1: ['Hernia'.lower()],
},
'Infiltration': {
    1: ['Infiltration'.lower()],
},
'Mass': {
    1: ['Mass'.lower()],
},
'Nodule': {
    1: ['Nodule'.lower()],
},
'Atelectasis': {
    1: ['Atelectasis'.lower()],
},
'Pneumothorax': {
    1: ['Pneumothorax'.lower()],
},
'Pleural_Thickening': {
    1: ['Pleural Thickening'.lower()],
},
'Pneumonia': {
    1: ['Pneumonia'.lower()],
},
'Fibrosis': {
    1: ['Fibrosis'.lower()],
},
'Edema': {
    1: ['Edema'.lower()],
},
'Consolidation': {
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
