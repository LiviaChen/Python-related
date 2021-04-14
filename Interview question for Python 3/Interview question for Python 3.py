input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}

def reverse_nested_dict(input_value) :
    for first, second_layer in input_value.items():
        for second, third_layer in second_layer.items():
            for third, forth_layer in third_layer.items():
                for forth, fifth in forth_layer.items():
                    output_value = {fifth:{forth:{third:{second:first}}}}
                    return output_value

output_value = reverse_nested_dict(input_value)

# unittest
import unittest
class TestStringMethods(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(input_value, reverse_nested_dict(output_value))
if __name__ == '__main__':
    unittest.main()