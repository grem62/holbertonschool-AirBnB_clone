#!/usr/bin/python3
"""new class FileStorage"""

import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        """ sets in __objects the obj with key
            <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
           (path: __file_path)
        """
        new_dict = {}

        for key, value in FileStorage.__objects.items():
            new_dict.update({key: value.to_dict()})

        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(new_dict))

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                new_dict = json.load(file)
                cls = "__class__"
                for key, value in new_dict.items():
                    FileStorage.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
