from entity.entity import Entity


class StaticEntity(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)