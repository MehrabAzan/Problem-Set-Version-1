def data_difference(experiment1, experiment2):
    return dict(set(experiment1.items()) - set(experiment2.items()))
    

exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

print(data_difference(exp1_data, exp2_data))