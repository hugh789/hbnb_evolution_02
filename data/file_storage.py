import json
from pathlib import Path

class FileStorage():
    """ Class for reading data from JSON files """

    def load_data(self, is_testing = False):
        """ Load JSON data from file and returns as dictionary """
        data = {}

        models_filepath = "data/models_testing.json" if is_testing else "data/models.json"
        relations_filepath = "data/relations_testing.json" if is_testing else "data/relations.json"

        data['models'] = self.load_models_data(models_filepath)
        data['relations'] = self.load_many_to_many_relations_data(relations_filepath)

        return data

    def load_models_data(self, filepath):
        """ Load JSON data from models file and returns as dictionary """
        temp = {}
        models_data = {}

        if not Path(filepath).is_file():
            raise FileNotFoundError("Data file '{}' missing".format(filepath))

        try:
            with open(filepath, 'r') as f:
                rows = json.load(f)
            for key in rows:
                temp[key] = rows[key]
        except ValueError as exc:
            raise ValueError("Unable to load data from file '{}'".format(filepath)) from exc

        # The data at this point is not directly usable. It needs to be reorganised
        for key, value in temp.items():
            models_data[key] = {}
            for row in value:
                models_data[key][row['id']] = row

        # print(json.dumps(model_data))
        return models_data

    def load_many_to_many_relations_data(self, filepath):
        """ Load JSON data from relations file and returns as dictionary """

        temp = {}
        relations_data = {}

        if not Path(filepath).is_file():
            raise FileNotFoundError("Data file '{}' missing".format(filepath))

        try:
            with open(filepath, 'r') as f:
                rows = json.load(f)
            for key in rows:
                temp[key] = rows[key]
        except ValueError as exc:
            raise ValueError("Unable to load data from file '{}'".format(filepath)) from exc

        # reorganise relations data
        for key, value in temp.items():
            # the key will be in the format like <something>_to_<something>
            keys = key.split('_to_')
            if keys[0] not in relations_data:
                relations_data[keys[0]] = {}

            if keys[1] not in relations_data[keys[0]]:
                relations_data[keys[0]][keys[1]] = {}

            for row in value:
                if row['place_id'] not in relations_data[keys[0]][keys[1]]:
                    relations_data[keys[0]][keys[1]][row['place_id']] = []

                relations_data[keys[0]][keys[1]][row['place_id']].append(row['amenity_id'])

        # print(json.dumps(relations_data))
        return relations_data
