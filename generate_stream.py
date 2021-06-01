import random
import time
no_of_para = 2

Battery_parameters_range= {'temperature':[0,45], 'soc':[20,80]}
#Battery_parameters =['temperature', 'soc'] 

def generate_param_reading(param):
    param_range= Battery_parameters_range[param]
    return (round(random.uniform(param_range[0], param_range[1]),2))

def generate_param_stream(reading_count):
    [temp_stream,soc_stream]=[[],[]]
    for i in range(0,reading_count):
        temp_stream.append(generate_param_reading('temperature'))
        soc_stream.append(generate_param_reading('soc'))
    return ([temp_stream,soc_stream])

def stream_output(reading_count):
    count_readings=0
    end_of_stream=False
    [temp_stream,soc_stream]=generate_param_stream(reading_count)
    for i in range(0,reading_count):
        print(temp_stream[i],',',soc_stream[i])
        time.sleep(1)
        count_readings=count_readings+1
    end_of_stream=True
    return([end_of_stream,count_readings])
