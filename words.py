normal_adj = [
    'normal', 'unremarkable', 'clear'
]

shape_noun = [
	'size', 'silhouette', 'area', 'contours'
]

shape_adj = [
    'round',
]

state_verb = [
	'appears', 'is', 'are', 'remains', 'remain', 'appear', 'exists', 'exist'
]

indication_noun = [
	'signs', 'evidence', 'case of', 'presence', 'findings', 'suspicious findings'
]

indication_adj = [
    'noticeable', 'visible', 'seen', 'appearent', 'observable'
]

indication_verb= [
	'indicates', 'suggests', 'suggesting', 'indicating', 'consistent with'
    ]

passive_indication_verb = [
        'can be identified', 'can be seen', 'is present', 'is noted'
        ]

unchanged = [
        'has not improved', 'unchanged', 'remains'
    ]

limits_noun = [
        'limits'
    ]

moderate_adj = [
        'mild', 'moderate', 'extensive', 'small', 'slight', 'stable', 'intact', 'mild-moderate',
    ]

strong_adj = [
        'large', 'significant', 'acute', 'widespread', 'relevant', 'difficult', 'apparent', 'prominent',
        'convincing', 'extensive', 'severe', 'critical', 'altered', 'patchy', 'degenerative', 'substantial',
        'predominant', 'massive', 'noticeable'
    ]

increased_adj = [
	'elevated', 'enlarged', 'increased', 'larger', 'large', 'widened'
    ]

size_noun = [
	'enlargement'
    ]

visible_adj = [
	'visible', 'seen', 'appearent'
    ]

relation_adj = [
	'regarding',' relating to', 'concerning', 'involving'
    ]

support_dev_noun = [
	'catheter', 'tubes', 'support device', 'monitoring device', 'wires', 'pacemaker'
    ]

change = [
	'little change', 'unchanged',
    ]

lung_adj = [
	'pulmonary','pul', 'lung', 'airspace'
    ]

localization_adj = {
 'loc bilateral': 'bilateral',
 'loc diffuse bilateral': 'diffuse bilateral',
 'loc middle mediastinum': 'middle mediastinal',
 'loc basal bilateral': 'basal bilateral',
 'loc basal': 'basal',
 'loc right': 'right',
 'loc hemithorax': 'hemithoracic',
 'loc cervical': 'cervical',
 'loc cardiac': 'cardiac',
 'loc central': 'central',
 'loc coronary': 'coronary',
 'loc esophageal': 'esophageal',
 'loc pleural': 'pleural',
 'loc epigastric': 'epigastric',
 'loc retrocardiac': 'retrocardiac',
 'loc perihilar': 'perihilar',
 'loc mediastinum': 'mediastinal',
 'loc paracardiac': 'paracardiac',
 'loc supra aortic': 'supra aortic',
 'loc costoesternal': 'costoesternal',
 'loc peribronchi': 'peribronchial',
 'loc subsegmental': 'subsegmental',
 'loc lower mediastinum': 'lower mediastinal',
 'loc intersomatic space': 'intersomatic space',
 'loc left': 'left',
 'loc paramediastinum': 'paramediastinal',
 'loc aortic': 'aortic',
 'loc bronchi': 'bronchi',
 'loc subpleural': 'subpleural',
 'loc suprahilar': 'suprahilar',
 'loc anterior mediastinum': 'anterior mediastinal',
 'loc paravertebral': 'paravertebral',
 'loc superior mediastinum': 'superior mediastinal',
 'loc infradiaphragm': 'infradiaphragmatic',
 'loc axilar': 'axilar',
 'loc aortopulmonary window': 'aortopulmonary',
 'loc lumbar vertebrae': 'lumbar',
 'loc humeral neck': 'humeral',
 'loc hilar': 'hilar',
 'loc extrapulmonary': 'extrapulmonary',
 'loc subcutaneous': 'subcutaneous',
 'loc apical': 'apical',
 'loc supraspisnous': 'supraspisnous',
 'loc supradiaphragm': 'supradiaphragmatic',
 'loc hilar bilateral': 'hilar bilateral',
 'loc lobar': 'lobar',
 'loc pectoral': 'pectoral',
 'loc paratracheal': 'paratracheal',
 'loc infrahilar': 'infrahilar',
 'loc extrapleural': 'extrapleural',
}

localization_noun = {
 'loc dorsal vertebrae': 'dorsal vertebrae',
 'loc right upper lobe': 'right upper lobe',
 'loc lower lobe': 'lower lobe',
 'loc carotid artery': 'carotid artery',
 'loc soft tissue': 'soft tissue',
 'loc left upper lobe': 'left upper lobe',
 'loc humerus': 'humerus',
 'loc nipple': 'nipple',
 'loc gallbladder': 'gallbladder',
 'loc middle mediastinum': 'middle mediastinum',
 'loc column': 'column',
 'loc right': 'right hand side',
 'loc hemithorax': 'hemithorax',
 'loc costophrenic angle': 'costophrenic angle',
 'loc upper lobe': 'upper lobe',
 'loc subclavian vein': 'subclavian vein',
 'loc fissure': 'fissure',
 'loc cardiac': 'heart',
 'loc hypochondrium': 'hypochondrium',
 'loc left costophrenic angle': 'left costophrenic angle',
 'loc coronary': 'coronary ateries',
 'loc thymus': 'thymus',
 'loc esophageal': 'esophagus',
 'loc cardiophrenic angle': 'cardiophrenic angle',
 'loc bone': 'bone',
 'loc tracheal': 'trachea',
 'loc pulmonary artery': 'pulmonary artery',
 'loc posterior mediastinum': 'posterior mediastinum',
 'loc cervical vertebrae': 'cervical vertebrae',
 'loc mediastinum': 'mediastinum',
 'loc diaphragm': 'diaphragm',
 'loc lower lung field': 'lower lung field',
 'loc rib cartilage': 'rib cartilage',
 'loc bilateral costophrenic angle': 'bilateral costophrenic angle',
 'loc supra aortic': 'supra aortic',
 'loc peribronchi': 'peribronchi',
 'loc minor fissure': 'minor fissure',
 'loc acromioclavicular joint': 'acromioclavicular joint',
 'loc lower mediastinum': 'lower mediastinum',
 'loc intersomatic space': 'intersomatic space',
 'loc scapula': 'scapula',
 'loc middle lung field': 'middle lung field',
 'loc major fissure': 'major fissure',
 'loc left': 'left hand side',
 'loc paramediastinum': 'paramediastinum',
 'loc humeral head': 'humeral head',
 'loc aortic': 'aortic',
 'loc middle lobe': 'middle lobe',
 'loc right costophrenic angle': 'right costophrenic angle',
 'loc posterior rib': 'posterior rib',
 'loc rib': 'rib',
 'loc shoulder': 'shoulder',
 'loc bronchi': 'bronchi',
 'loc anterior mediastinum': 'anterior mediastinum',
 'loc superior cave vein': 'superior cave vein',
 'loc upper lung field': 'upper lung field',
 'loc superior mediastinum': 'superior mediastinum',
 'loc infradiaphragm': 'infradiaphragm',
 'loc aortic button': 'aortic button',
 'loc aortopulmonary window': 'aortopulmonary window',
 'loc lumbar vertebrae': 'lumbar vertebrae',
 'loc lung field': 'lung field',
 'loc lingula': 'lingula',
 'loc humeral neck': 'humeral neck',
 'loc hilar': 'hilum',
 'loc extrapulmonary': 'extrapulmonary',
 'loc rotator cuff': 'rotator cuff',
 'loc subcutaneous': 'subcutaneous',
 'loc right hypochondrium': 'right hypochondrium',
 'loc left lower lobe': 'left lower lobe',
 'loc brachiocephalic veins': 'brachiocephalic veins',
 'loc left hypochondrium': 'left hypochondrium',
 'loc gastric chamber': 'gastric chamber',
 'loc anterior rib': 'anterior rib',
 'loc supradiaphragm': 'supradiaphragm',
 'loc hilar bilateral': 'bilateral hili',
 'loc clavicle': 'clavicle',
 'loc glenohumeral joint': 'glenohumeral joint',
 'loc airways': 'airways',
 'loc right lower lobe': 'right lower lobe'
}
