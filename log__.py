import json

class log:
    def __init__(self, app_name, version, timestamp):
        self.app_name = app_name
        self.version = version
        self.timestamp = timestamp
        self.steps = []
        self.stock = {}

    def save(self):
        arquivo = {
            "app_name": self.app_name,
            "version": self.version,
            "timestamp": self.timestamp,
            "steps": self.steps,
            "stock": self.stock
        }
        with open(f'logs/{self.timestamp}.json', 'w', encoding='utf8') as file:
            json.dump(arquivo, file, indent=2)

    def internal(self, log_name, timestamp, data=None):
        self.stock[log_name] = {
            "log_name": log_name,
            "timestamp": timestamp,
            "success": False,
            "data": data,
            "result": None,
        }

    def internal_finish(self, log_name, success, result=None):
        step = self.stock.pop(log_name)
        step['success'] = success
        step['result'] = result
        self.steps.append(step)

    def show_steps(self):
        return self.steps
    
    def show_steps_error(self):
        return self.stock