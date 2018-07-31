## coef_hue_angle
#
## written by Quinten Vanhellemont
## 2018-04-18
## modifications:
##                2018-07-18 (QV) changed acolite import name

def coef_hue_angle(file=None):
    if file == None:
            from acolite import config
            pp_path = config['pp_data_dir']
            file = pp_path+'/Shared/hue_angle.cfg'
            
    hac={}
    with open(file, 'r') as f:
        for il, line in enumerate(f.readlines()):
            line=line.strip()
            if len(line) == 0: continue
            if line[0] in ['#', '%', ';']: continue

            sp = line.split('=')
            if sp[0]=='sensor':
                cur_label = sp[1]
                if cur_label not in hac:
                    hac[cur_label] = {}
            if ',' in sp[1]:
                var = sp[1].split(',')
                hac[cur_label][sp[0]]=[float(v) for v in var]
            else:
                hac[cur_label][sp[0]]=sp[1]
    return(hac)