# import the module
from json_schema import JsonScema



def test():
    JsonScema('../data/data_1.json', '../schema/schema_1.json', 'message').generate_schema()
    JsonScema('../data/data_2.json', '../schema/schema_2.json', 'message').generate_schema()





def generate_by_user_input():
    # the file path
    file_path = input('json file path >>> ')

    # the schema file path
    output_file =input('where the schema will be written ? >>> ')

    # json key to create schema for
    lookup_key = input('look up key ? default: None >>> ')

    JsonScema(file_path, output_file, lookup_key).generate_schema()


if __name__ == '__main__':
    test()
    # generate_by_user_input()
    

