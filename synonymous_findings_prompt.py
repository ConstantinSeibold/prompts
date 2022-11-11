from num2word import word as num2word
from itertools import chain

from .words import *

findings_mimic_template = {
'Enlarged_Cardiomediastinum' :  {
    0: ['No Enlarged Cardiomediastinum'.lower(),
        *list(chain(*[
        ['{normal_adj} mediastinal {shape_noun}'.format(normal_adj =normal_adj[i], shape_noun = shape_noun[j]) for i in range(len(normal_adj))] for j in range(len(shape_noun))])),
        *['{normal_adj} mediastinum'.format(normal_adj = normal_adj[i]) for i in range(len(normal_adj))],
        ],
    1: [*['{increased_adj}  Cardiomediastinum'.format(increased_adj = increased_adj[i]).lower() for i in range(len(increased_adj))],
    *list(chain(*[
        ['{increased_adj} cardiomediastinal {shape_noun}'.format(increased_adj = increased_adj[i], shape_noun = shape_noun[j]) for i in range(len(increased_adj))] for j in range(len(shape_noun))
    ]))
    ],
},
'Cardiomegaly' :  {
    0: ['No Cardiomegaly'.lower(),
    *list(chain(*[
    ['heart {shape_noun} {normal_adj}'.format(normal_adj=normal_adj[i], shape_noun = shape_noun[j]) for i in range(len(normal_adj))] for j in range(len(shape_noun))])),
    *list(chain(*[
    ['{normal_adj} {shape_noun} of the heart'.format(normal_adj=normal_adj[i], shape_noun = shape_noun[j]) for i in range(len(normal_adj))] for j in range(len(shape_noun))])),
    *['No {indication_noun} of cardiomegaly'.format(indication_noun = indication_noun[i]) for  i in range(len(indication_noun))],
    *list(chain(*[
    ['{normal_adj} cardiac {shape_noun}'.format(normal_adj=normal_adj[i], shape_noun = shape_noun[j]) for i in range(len(normal_adj))] for j in range(len(shape_noun))])),
    ],
    1: ['Cardiomegaly'.lower(),
    *list(chain(*[[
    '{size_noun} of cardiac {shape_noun}'.format(shape_noun = shape_noun[i], size_noun = size_noun[j]) for i in range(len(shape_noun))] for j in range(len(size_noun))])),
    *['Cardiomegaly {unchanged}'.format(unchanged = unchanged[i]) for i in range(len(unchanged))],
    *['{indication_noun} of Cardiomegaly'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    *['{moderate_adj} cardiomegaly'.format(moderate_adj = moderate_adj[i]) for i in range(len(moderate_adj))],
    *['{strong_adj} cardiomegaly'.format(strong_adj = strong_adj[i]) for i in range(len(strong_adj))],
    ],
},
'Lung_Opacity' :  {
    0: ['No Lung Opacity'.lower(),
    'No opacity in the lung',
    *list(chain(*[[
    'no {indication_noun} of {lung_adj} opacities'.format(indication_noun = indication_noun[i], lung_adj = lung_adj[j]) for i in range(len(indication_noun))] for j in range(len(lung_adj))])),
    *list(chain(*[[
    'without {indication_noun} of {lung_adj} opacities'.format(indication_noun = indication_noun[i], lung_adj = lung_adj[j]) for i in range(len(indication_noun))] for j in range(len(lung_adj))])),
       ],
    1: ['Lung Opacity'.lower(),
        *['Lung volumes with {shape_adj} opacities'.format(shape_adj = shape_adj[i]) for i in range(len(shape_adj))],
    ],
},
'Lung_Lesion' :  {
    0: ['No Lung Lesion'.lower(),
    *list(chain(*[[
    'No {lung_adj} lesions {passive_indication_verb}'.format(lung_adj = lung_adj[i], passive_indication_verb = passive_indication_verb[j]) for i in range(len(lung_adj))] for j in range(len(passive_indication_verb))])),
    'Lung without lesions',
    'No lesion indicating pulmonary nodule',
    ],
    1: ['Lung Lesion'.lower()],
},
'Edema' :  {
    0: ['No Edema'.lower(),
    'without pulmonary edema',
    *list(chain(*[[
    'without {moderate_adj} {lung_adj} edema'.format(moderate_adj = moderate_adj[i], lung_adj = lung_adj[j]) for i in range(len(moderate_adj))] for j in range(len(lung_adj))])),
    *list(chain(*[[
    'no {indication_noun} of {lung_adj} edema'.format(indication_noun = indication_noun[i], lung_adj = lung_adj[j])  for i in range(len(indication_noun))] for j in range(len(lung_adj))])),
    ],
    1: ['Edema'.lower(),
    *list(chain(*[[
    'abnormality {passive_indication_verb} of {lung_adj} edema'.format(passive_indication_verb = passive_indication_verb[i], lung_adj = lung_adj[j])  for i in range(len(passive_indication_verb))] for j in range(len(lung_adj))])),
    ],
},
'Pneumonia' :  {
    0: ['No Pneumonia'.lower(),
    'Without Pneumonia'.lower(),
    ],
    1: ['Pneumonia'.lower(),
    *['{indication_noun} consistent with pneumonia'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    *list(chain(*[[
    '{indication_noun} consistent with {lung_adj} inflammation'.format(indication_noun = indication_noun[i],lung_adj = lung_adj[j])  for i in range(len(indication_noun))] for j in range(len(lung_adj))])),
    'Pneumonia in the lung',
    'opacities consistent with pneumonia',
    *['opacities consistent with {lung_adj} inflammation'.format(lung_adj =lung_adj[i]) for i in range(len(lung_adj))],

    ],
},
'Consolidation' :  {
    0: ['No Consolidation'.lower(),
    'No focal consolidation to suggest pneumonia.',
    'no focal areas of consolidation',
    'no focal consolidation',
    *['without {indication_noun} of consolidation'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    ],
    1: ['Consolidation'.lower(),
    *list(chain(*[[
        '{lung_adj} {moderate_adj} consolidation'.format(lung_adj =lung_adj[i],moderate_adj=moderate_adj[j]) for i in range(len(lung_adj))] for j in range(len(moderate_adj))])),
    ],
},
'Atelectasis' :  {
    0: ['No Atelectasis'.lower(),
    'Lung free of atelectasis',
    *['no {indication_noun} of atelectasis'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    'no atelectatic changes',

    ],
    1: ['Atelectasis'.lower(),
    *['{moderate_adj} atelectasis'.format(moderate_adj = moderate_adj[i]) for i in  range(len(moderate_adj))],
    *['{moderate_adj} atelectatic changes'.format(moderate_adj = moderate_adj[i]) for i in  range(len(moderate_adj))],
    *['{indication_noun} of atelectasis'.format(indication_noun = indication_noun[i]) for i in  range(len(indication_noun))],

    ],
},
'Pneumothorax' :  {
    0: ['No Pneumothorax'.lower(),
    'study without pneumothorax',
    *['no {indication_noun} of Pneumothorax'.format(indication_noun = indication_noun[i]) for i in  range(len(indication_noun))],
    ],
    1: ['Pneumothorax'.lower(),
    *['{moderate_adj} pneumothorax'.format(moderate_adj = moderate_adj[i]) for i in  range(len(moderate_adj))],
    *['{indication_noun} of pneumothorax'.format(indication_noun = indication_noun[i]) for i in  range(len(indication_noun))],

    ],
},
'Pleural_Effusion' :  {
    0: ['No Pleural Effusion'.lower(),
    *['no {lung_adj} effusion'.format(lung_adj = lung_adj[i]) for i in  range(len(lung_adj))],
    *['without {indication_noun} of pleural effusion'.format(indication_noun=indication_noun[i]) for i in range(len(indication_noun))],
    ],
    1: ['Pleural Effusion'.lower(),
    *list(chain(*[[
    'Reduced lung volume consistent with {moderate_adj} {lung_adj}  effusion'.format(moderate_adj = moderate_adj[i],lung_adj =lung_adj[j]) for i in range(len(moderate_adj))] for j in range(len(lung_adj))])),
    *list(chain(*[[
    '{moderate_adj} {lung_adj}  effusions'.format(moderate_adj = moderate_adj[i], lung_adj = lung_adj[j])  for i in range(len(moderate_adj))] for j in range(len(lung_adj))])),
    *list(chain(*[[
    '{moderate_adj} {lung_adj}  effusion'.format(moderate_adj = moderate_adj[i], lung_adj = lung_adj[j]) for i in range(len(moderate_adj))] for j in range(len(lung_adj))])),
    *list(chain(*[[
    '{indication_noun} of {lung_adj}  effusion'.format(indication_noun = indication_noun[i], lung_adj = lung_adj[j])  for i in range(len(indication_noun))] for j in range(len(lung_adj))])),
    ],
},
'Pleural_Other' :  {
    0: ['No Pleural Other'.lower(),
    ],
    1: ['Pleural Other'.lower()],
},
'Fracture' :  {
    0: ['No Fracture'.lower(),
    'No rib fractures',
    'No fractures',
    'thorax without fractures',
    ],
1: ['Fracture'.lower(),
 *['{indication_adj} fractures'.format(indication_adj = indication_adj[i]) for i in range(len(indication_adj))],
 'detection of fractures',
]
},
'Support_Devices' :  {
    0: ['No Support Devices'.lower(),
    *['removed {support_dev_noun}'.format(support_dev_noun = support_dev_noun[i]) for i in range(len(support_dev_noun))],
    *list(chain(*[[
    'the {support_dev_noun} {state_verb} removed'.format(support_dev_noun = support_dev_noun[i], state_verb = state_verb[j])  for i in range(len(support_dev_noun))] for j in range(len(state_verb))])),
    ],
    1: ['Support Devices'.lower(),
    *['{support_dev_noun} within the body'.format(support_dev_noun = support_dev_noun[i]) for i in range(len(support_dev_noun))],
    *['{support_dev_noun} in standard placement'.format(support_dev_noun =  support_dev_noun[i]) for i in range(len(support_dev_noun))],
],
},
}


findings_chexpert_template = findings_mimic_template


findings_chestray14_template = {
'Cardiomegaly' :  {
    0: ['No Cardiomegaly'.lower(),
    *list(chain(*[
    ['heart {shape_noun} {normal_adj}'.format(normal_adj=normal_adj[i], shape_noun = shape_noun[j]) for i in range(len(normal_adj))] for j in range(len(shape_noun))])),
    *list(chain(*[
    ['{normal_adj} {shape_noun} of the heart'.format(normal_adj=normal_adj[i], shape_noun = shape_noun[j]) for i in range(len(normal_adj))] for j in range(len(shape_noun))])),
    *['No {indication_noun} of cardiomegaly'.format(indication_noun = indication_noun[i]) for  i in range(len(indication_noun))],
    *list(chain(*[
    ['{normal_adj} cardiac {shape_noun}'.format(normal_adj=normal_adj[i], shape_noun = shape_noun[j]) for i in range(len(normal_adj))] for j in range(len(shape_noun))])),
    ],
    1: ['Cardiomegaly'.lower(),
    *list(chain(*[[
    '{size_noun} of cardiac {shape_noun}'.format(shape_noun = shape_noun[i], size_noun = size_noun[j]) for i in range(len(shape_noun))] for j in range(len(size_noun))])),
    *['Cardiomegaly {unchanged}'.format(unchanged = unchanged[i]) for i in range(len(unchanged))],
    *['{indication_noun} of Cardiomegaly'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    *['{moderate_adj} cardiomegaly'.format(moderate_adj = moderate_adj[i]) for i in range(len(moderate_adj))],
    *['{strong_adj} cardiomegaly'.format(strong_adj = strong_adj[i]) for i in range(len(strong_adj))],
    ],
},
'Emphysema': {
    0: ['no Emphysema'.lower(),
        *['no {indication_noun} of ephysema'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
        '',
    ],
    1: ['Emphysema'.lower(),
    'lung findings consistent with emphysema',
    'consistent with emphysema',
    'consistent emphysema',
    *['{indication_noun} of COPD emphysema'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    *list(chain(*[list(chain(*[[
    '{indication_noun} of {lung_adj} {moderate_adj} emphysema'.format(indication_noun = indication_noun[i], lung_adj = lung_adj[j], moderate_adj = moderate_adj[k]) for i in range(len(normal_adj))] for j in range(len(shape_noun))])) for k in range(len(moderate_adj))])),
    *list(chain(*[list(chain(*[[
    '{indication_noun} of {lung_adj} {strong_adj} emphysema'.format(indication_noun = indication_noun[i], lung_adj = lung_adj[j], strong_adj =  strong_adj[k])  for i in range(len(indication_noun))] for j in range(len(lung_adj))])) for k in range(len(strong_adj))])),
    ],
},
'Effusion': {
    0: ['No Pleural Effusion'.lower(),
    'no Effusion'.lower(),
    *['no {lung_adj} effusion'.format(lung_adj = lung_adj[i]) for i in  range(len(lung_adj))],
    *['without {indication_noun} of pleural effusion'.format(indication_noun=indication_noun[i]) for i in range(len(indication_noun))],
    ],
    1: ['Pleural Effusion'.lower(),
    'Effusion'.lower(),
    *list(chain(*[[
    'Reduced lung volume consistent with {moderate_adj} {lung_adj}  effusion'.format(moderate_adj = moderate_adj[i],lung_adj =lung_adj[j]) for i in range(len(moderate_adj))] for j in range(len(lung_adj))])),
    *list(chain(*[[
    '{moderate_adj} {lung_adj}  effusions'.format(moderate_adj = moderate_adj[i], lung_adj = lung_adj[j])  for i in range(len(moderate_adj))] for j in range(len(lung_adj))])),
    *list(chain(*[[
    '{moderate_adj} {lung_adj}  effusion'.format(moderate_adj = moderate_adj[i], lung_adj = lung_adj[j]) for i in range(len(moderate_adj))] for j in range(len(lung_adj))])),
    *list(chain(*[[
    '{indication_noun} of {lung_adj}  effusion'.format(indication_noun = indication_noun[i], lung_adj = lung_adj[j])  for i in range(len(indication_noun))] for j in range(len(lung_adj))])),
    ],
},
'Hernia': {
    0: [
        'no Hernia'.lower(),
        *['no {indication_noun} of hernia'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))] ,
        *['without {indication_noun} of hernia'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))] ,
        '',
        ],
    1: [
        'Hernia'.lower(),
        *list(chain(*[[
        '{indication_noun} of {moderate_adj} hernia'.format(indication_noun = indication_noun[i], moderate_adj =moderate_adj[j]) for i in range(len(indication_noun))] for j in range(len(moderate_adj))])),
        ]
},
'Infiltration': {
    0: ['no Infiltration'.lower(),
        *list(chain(*[[
        'no {indication_noun} of acute {lung_adj} infiltrates'.format(indication_noun = indication_noun[i], lung_adj = lung_adj[j]) for i in range(len(indication_noun))] for j in range(len(lung_adj))])),
        *['no {lung_adj} effusion'.format(lung_adj = lung_adj[i]) for i in range(len(lung_adj))],
        'Lung without infiltrates',
        '',
    ],
    1: ['Infiltration'.lower(),
        *list(chain(*[list(chain(*[[
    '{indication_noun} of {moderate_adj} {lung_adj} infiltrate'.format(indication_noun = indication_noun[i], moderate_adj = moderate_adj[j], lung_adj = lung_adj[k]) for i in range(len(indication_noun))] for j in range(len(moderate_adj))])) for k in range(len(lung_adj))])),
        *list(chain(*[list(chain(*[[
    '{indication_noun} of {moderate_adj} {lung_adj} infiltrates'.format(indication_noun = indication_noun[i], moderate_adj = moderate_adj[j], lung_adj = lung_adj[k]) for i in range(len(indication_noun))] for j in range(len(moderate_adj))])) for k in range(len(lung_adj))])),
        *list(chain(*[[
    'A {moderate_adj} infiltration {passive_indication_verb}'.format(moderate_adj = moderate_adj[i], passive_indication_verb = passive_indication_verb[j]) for i in range(len(moderate_adj))] for j in range(len(passive_indication_verb))])),
    ],
},
'Mass': {
    0: ['No pulmonary mass'.lower(),
    'no mass'.lower(),
    # *list(chain(*[[
    # 'No {lung_adj} masses {passive_indication_verb}'.format(lung_adj = lung_adj[i], passive_indication_verb = passive_indication_verb[j]) for i in range(len(lung_adj))] for j in range(len(passive_indication_verb))])),
    'Lung without mass',
    ],
    1: ['Mass'.lower()],
},
'Nodule': {
    0: ['No Lung Lesion'.lower(),
    'no Nodule'.lower(),
    # *list(chain(*[[
    # 'No {lung_adj} lesions {passive_indication_verb}'.format(lung_adj = lung_adj[i], passive_indication_verb = passive_indication_verb[j]) for i in range(len(lung_adj))] for j in range(len(passive_indication_verb))])),
    'Lung without lesions',
    'No lesion indicating pulmonary nodule',
    ],
    1: ['Lung Lesion'.lower(),
    'Lung nodule'.lower(),
    *['{indication_noun} of lung lesions'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    *['{indication_noun} of pulmonary nodules'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    ],
},
'Atelectasis': {
    0: ['No Atelectasis'.lower(),
    'Lung free of atelectasis',
    *['no {indication_noun} of atelectasis'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    'no atelectatic changes',

    ],
    1: ['Atelectasis'.lower(),
    *['{moderate_adj} atelectasis'.format(moderate_adj = moderate_adj[i]) for i in  range(len(moderate_adj))],
    *['{moderate_adj} atelectatic changes'.format(moderate_adj = moderate_adj[i]) for i in  range(len(moderate_adj))],
    *['{indication_noun} of atelectasis'.format(indication_noun = indication_noun[i]) for i in  range(len(indication_noun))],

    ],
},
'Pneumothorax': {
    0: ['No Pneumothorax'.lower(),
    'study without pneumothorax',
    *['no {indication_noun} of Pneumothorax'.format(indication_noun = indication_noun[i]) for i in  range(len(indication_noun))],
    ],
    1: ['Pneumothorax'.lower(),
    *['{moderate_adj} pneumothorax'.format(moderate_adj = moderate_adj[i]) for i in  range(len(moderate_adj))],
    *['{indication_noun} of pneumothorax'.format(indication_noun = indication_noun[i]) for i in  range(len(indication_noun))],

    ],
},
'Pleural_Thickening': {
    0: ['no Pleural Thickening'.lower(),
    *['no {indication_noun} of pleural thickening'.format(indication_noun =indication_noun[i]) for i in range(len(indication_noun))],

    ],
    1: ['Pleural Thickening'.lower(),
        *['{moderate_adj} pleural thickening'.format(moderate_adj = moderate_adj[i]) for i in range(len(moderate_adj))],
    ],
},
'Pneumonia': {
    0: ['No Pneumonia'.lower(),
    'Without Pneumonia'.lower(),
    ],
    1: ['Pneumonia'.lower(),
    *['{indication_noun} consistent with pneumonia'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    *list(chain(*[[
    '{indication_noun} consistent with {lung_adj} inflammation'.format(indication_noun = indication_noun[i],lung_adj = lung_adj[j])  for i in range(len(indication_noun))] for j in range(len(lung_adj))])),
    'Pneumonia in the lung',
    'opacities consistent with pneumonia',
    *['opacities consistent with {lung_adj} inflammation'.format(lung_adj =lung_adj[i]) for i in range(len(lung_adj))],

    ],
},
'Fibrosis': {
    0: ['no Fibrosis'.lower(),
        *['no {indication_noun} for the presence of fibrotic lung disease'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
        *['No {indication_noun} of fibrosis'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],

    ],
    1: ['Fibrosis'.lower(),
    *['a {strong_adj} Fibrosis'.format(strong_adj = strong_adj[i]) for i in range(len(strong_adj))] ,
    *['{indication_adj} fibrotic lung disease'.format(indication_adj = indication_adj[i]) for i in range(len(indication_adj))],
    ],
},
'Edema': {
    0: ['No Edema'.lower(),
    'without pulmonary edema',
    *list(chain(*[[
    'without {moderate_adj} {lung_adj} edema'.format(moderate_adj = moderate_adj[i], lung_adj = lung_adj[j]) for i in range(len(moderate_adj))] for j in range(len(lung_adj))])),
    *list(chain(*[[
    'no {indication_noun} of {lung_adj} edema'.format(indication_noun = indication_noun[i], lung_adj = lung_adj[j])  for i in range(len(indication_noun))] for j in range(len(lung_adj))])),
    ],
    1: ['Edema'.lower(),
    *list(chain(*[[
    'abnormality {passive_indication_verb} of {lung_adj} edema'.format(passive_indication_verb = passive_indication_verb[i], lung_adj = lung_adj[j])  for i in range(len(passive_indication_verb))] for j in range(len(lung_adj))])),
    ],
},
'Consolidation': {
    0: ['No Consolidation'.lower(),
    'No focal consolidation to suggest pneumonia.',
    'no focal areas of consolidation',
    'no focal consolidation',
    *['without {indication_noun} of consolidation'.format(indication_noun = indication_noun[i]) for i in range(len(indication_noun))],
    ],
    1: ['Consolidation'.lower(),
    *list(chain(*[[
        '{lung_adj} {moderate_adj} consolidation'.format(lung_adj =lung_adj[i],moderate_adj=moderate_adj[j]) for i in range(len(lung_adj))] for j in range(len(moderate_adj))])),
    ],
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
