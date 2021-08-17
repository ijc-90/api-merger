

class JsonMerger:
    def __init__(self):
        self._elements = []
        self._config = {
            "fields": {
                "deductible": {
                    "strategy": "average"
                },
                "stop_loss": {
                    "strategy": "average"
                },
                "oop_max": {
                    "strategy": "average"
                },
            }
        }
        self._fields_metadata = {}

    def add_element(self, element):
        self._elements.append(element)
        for field in self._config.get('fields'):
            self._add_metadata(field, element)

    def _add_metadata(self, field, element):
        if field not in self._fields_metadata:
            self._fields_metadata[field] = {
                "sum": 0,
                "quantity": 0
            }
        new_value = element[field]
        self._fields_metadata[field]['sum'] += new_value
        self._fields_metadata[field]['quantity'] += 1

    def get_result(self):
        output = {}
        fields_config = self._config['fields']
        for field in fields_config:
            output[field] = self._fields_metadata[field]['sum'] / self._fields_metadata[field]['quantity']
        return output


