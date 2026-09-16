from dataclasses import dataclass, asdict

@dataclass
class Todo:
    id: int
    title: str
    description: str
    due_date: str
    priority: str = "Medium"
    category: str = "General"
    status: str = "Pending"

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return Todo(**data)
