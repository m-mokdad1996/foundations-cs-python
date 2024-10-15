def sumTuples(a,b):
  # Initialize an empty tuple
  result_tuple = ()

  # Loop through the indexes and add corresponding elements
  for i in range(len(a)):
        new_element = a[i] + b[i]
        result_tuple += (new_element,)

  return result_tuple

import json

def dict_to_json(dictionary, filename):
    # Start the JSON string
    json_str = '{\n'
    for key, value in dictionary.items():
        # Format the key
        key_str = f'"{key}"'
        
        # Format the value
        if isinstance(value, str):
            value_str = f'"{value}"'
        elif isinstance(value, bool):
            value_str = 'true' if value else 'false'
        elif value is None:
            value_str = 'null'
        elif isinstance(value, list):
            value_str = '[' + ', '.join(f'"{item}"' if isinstance(item, str) else str(item) for item in value) + ']'
        elif isinstance(value, dict):
            value_str = dict_to_json_str(value, indent=4)  # Recursively handle nested dictionaries
        else:
            value_str = str(value)
        
        # Add the formatted key-value pair to the JSON string
        json_str += f'  {key_str}: {value_str},\n'
    
    # Remove the trailing comma and add the closing brace
    json_str = json_str.rstrip(',\n') + '\n}'
    
    # Write the JSON string to the file
    with open(filename, 'w') as file:
        file.write(json_str)


def json_to_list_of_dicts(filename):
    with open(filename, 'r') as file:
        json_content = file.read()

    # Clean the JSON content
    json_content = json_content.strip()
    json_content = json_content[1:-1]  # Remove the outer brackets

    objects = json_content.split('},{')
    dict_list = []

    for obj in objects:
        obj = '{' + obj.strip('{}') + '}'
        obj_dict = parse_object(obj)
        dict_list.append(obj_dict)

    return dict_list

def parse_object(obj_str):
    obj_dict = {}
    items = obj_str[1:-1].split(',')
    for item in items:
        key, value = item.split(':', 1)
        key = key.strip().strip('"')
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value.strip('"')
        elif value.lower() in ['true', 'false']:
            value = value.lower() == 'true'
        elif value == 'null':
            value = None
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    value = value  # Leave it as a string if it can't be converted
        obj_dict[key] = value
    return obj_dict
def main():
    while True:
      print("1. Sum Tuples") 
      print("2. Export JSON")
      print("3. Import JSON") 
      print("4. Exit")
      choice = int(input("Enter a choice: "))

      if choice == 1:
          tup1 = input("enter a numbers:")
          user_tuple = tuple(map(int, tup1.split(',')))
          tup2 = input("enter a numbers:") 
          user_tuple2 = tuple(map(int, tup2.split(',')))
          assert len(user_tuple) == len(user_tuple2), "Tuples must be of the same length."
          new_tuple = sumTuples(user_tuple,user_tuple2)
          print(new_tuple)
      elif choice == 2:
          def input_dictionary():
              user_dict = {}
              while True:
                 key = input("Enter key (or type 'done' to finish): ")
                 if key == 'done':
                   break
                 value = input("Enter value: ")
                 user_dict[key] = value
              return user_dict
          user_dict = input_dictionary()
          print("Your dictionary is:", user_dict)
          dict_to_json(user_dict, "output.json")
      elif choice == 3:
           filename = 'data.json'
           list_of_dicts = json_to_list_of_dicts(filename)
           print(list_of_dicts)
      elif choice == 4:
          break
      else:
          print("error, please try again another choice")
if __name__ == "__main__":
    main()
         

  