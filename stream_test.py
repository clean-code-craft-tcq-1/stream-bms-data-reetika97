import unittest
import generate_stream

class GenerateStreamTest(unittest.TestCase):
  def test_within_range_temp(self):
    TestReading=generate_stream.generate_param_reading('temperature')
    self.assertTrue((TestReading>=generate_stream.Battery_parameters_range['temperature'][0]) && (TestReading<=generate_stream.Battery_parameters_range['temperature'][1]))
  
   
if __name__ == '__main__':
  unittest.main()
