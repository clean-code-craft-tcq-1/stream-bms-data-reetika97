import unittest
import generate_stream

class GenerateStreamTest(unittest.TestCase):
  def test_within_range_temp(self):
    TestReading=generate_stream.generate_param_reading('temperature')
    self.assertTrue((TestReading>=generate_stream.Battery_parameters_range['temperature'][0]) and (TestReading<=generate_stream.Battery_parameters_range['temperature'][1]))
  def test_within_range_soc(self):
    TestReading=generate_stream.generate_param_reading('temperature')
    self.assertTrue((TestReading>=generate_stream.Battery_parameters_range['temperature'][0]) and (TestReading<=generate_stream.Battery_parameters_range['soc'][1]))
  def test_number_of_readings_generated(self):
    [temp_stream,soc_stream]=generate_stream.generate_param_stream(15)
    self.assertTrue((len(temp_stream)==15) and (len(soc_stream)==15))
  def test_readings_count_in_stream(self):
    [end_of_stream,count_readings]=generate_stream.stream_output(10)
    self.assertTrue( [end_of_stream,count_readings]==[True,10])
      
   
if __name__ == '__main__':
  unittest.main()
