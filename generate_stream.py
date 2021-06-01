import random
import time

#number of readings in stream to be sent to console 
no_of_readings_in_stream = 10

#BatteryParameterRange = parameter_name : [lowerLimit,upperLimit]
Battery_parameters_range= {'temperature':[0,45], 'soc':[20,80]}

#geneerate single random reading between limits
def generate_param_reading(param):
    param_range= Battery_parameters_range[param]
    return (round(random.uniform(param_range[0], param_range[1]),2))

#generate stream of readings between limits
def generate_param_stream(reading_count):
    [temp_stream,soc_stream]=[[],[]]
    for i in range(0,reading_count):
        temp_stream.append(generate_param_reading('temperature'))
        soc_stream.append(generate_param_reading('soc'))
    return ([temp_stream,soc_stream])

#output to console the stream of readings
def stream_output(reading_count):
    #to test no. of readings
    count_readings=0
    end_of_stream=False
    [temp_stream,soc_stream]=generate_param_stream(reading_count)
    for i in range(0,reading_count):
        print(temp_stream[i],',',soc_stream[i])
        time.sleep(1)
        count_readings=count_readings+1
        
    #to test end of display
    i==reading_count?(end_of_stream=True):(end_of_stream=False)
    return([end_of_stream,count_readings])

stream_output(no_of_readings_in_stream)
