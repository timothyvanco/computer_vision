import json

class Decoder(json.JSONDecoder):
    def decode(self, s):
        result = super().decode(s)
        return self._decode(result)

    def _decode(self, o):
        if isinstance(o, str) or isinstance(o, str):
            try:
                return int(o)
            except ValueError:
                return o

        elif isinstance(o, dict):
            return {k: self._decode(v) for k, v in o.items()}
        elif isinstance(o, list):
            return [self._decode(v) for v in o]
        else:
            return o


data = {}
data['Locations_of_objects'] = []

data['Locations_of_objects'].append({
    'num': '1',
    'center_object_x': '52.86',
    'center_object_y': '49.85',
    'center_object_z': '86.73',
})

data['Locations_of_objects'].append({
    'num': '2',
    'center_object_x': '96.74',
    'center_object_y': '59.76',
    'center_object_z': '88.53',
})

data['Locations_of_objects'].append({
    'num': '3',
    'center_object_x': '93.74',
    'center_object_y': '43.42',
    'center_object_z': '82.16',
})

print(json.loads(data, cls=Decoder))