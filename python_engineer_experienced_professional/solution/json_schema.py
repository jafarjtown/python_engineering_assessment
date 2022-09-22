
import json


class JsonScema:
    
    def __init__(self, input, output, lookup_key = None):
        self.input = input
        self.output = output
        self.object = {}
        self.lookup_key = lookup_key
    
    def generate_schema(self):
        with open(self.input) as file:
            python_object : dict = json.load(file)
            if self.lookup_key:
                o = python_object.get(self.lookup_key)
                if o == None:
                    o = python_object
                python_object = o
            self.object = self.createObjectSchema(python_object)
    
        with open(self.output, 'w+') as file:
            json.dump(self.object, file)
            
        return True
    
    def createObjectSchema(self, obj):
        ob = {}
        for key, value in obj.items():
            if type(value) == str:
                ob[key] = self.createStringSchema()
            elif type(value) == dict:
                ob[key] = self.createObjectSchema(value)
            elif type(value) == bool:
                ob[key] = self.createBooleanSchema()
            elif type(value) == list:
                is_all_string = False
                for item in value:
                    if isinstance(item, str):
                        is_all_string = True
                        break
                if is_all_string:
                    ob[key] = self.createListStringSchema()
                else:
                    ob[key] = self.createListSchema()
            elif isinstance(value, int):
                ob[key] = self.createIntergerSchema()
                ...
            
        return ob
    def createStringSchema(self):
        schema = {
            'type': 'string',
            'tag': '',
            'description': '',
            'required': True
        }
        return schema

    def createIntergerSchema(self):
        schema = {
            'type': 'integer',
            'tag': '',
            'description': '',
            'required': True
            
        }
        return schema

    def createListSchema(self):
        schema = {
            'type': 'ARRAY',
            'tag': '',
            'description': '',
            'required': True
            
        }
        return schema

    def createListStringSchema(self):
        schema = {
            'type': 'ENUM',
            'tag': '',
            'description': '',
            'required': True
            
        }
        return schema
    
    def createBooleanSchema(self):
        schema = {
            'type': 'boolean',
            'tag': '',
            'description': '',
            'required': True
            
        }
        return schema

        