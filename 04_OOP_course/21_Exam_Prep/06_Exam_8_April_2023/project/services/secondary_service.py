from project.services.base_service import BaseService


class SecondaryService(BaseService):
    BASE_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.BASE_CAPACITY)

    def details(self):
        if self.robots:
            robots_result = ' '.join([r.name for r in self.robots])
            return f"{self.name} Secondary Service:\nRobots: {robots_result}"
        else:
            robots_result = "none"
            return f"{self.name} Secondary Service:\nRobots: {robots_result}"
