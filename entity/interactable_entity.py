from entity.static_entity import StaticEntity

class InteractableEntity(StaticEntity):
    remove_on_interact: bool

    def __init__(self, x, y, remove_on_interact=False):
        super().__init__(x, y)
        self.remove_on_interact = remove_on_interact

    def interact(self, actor):
        """
        Called when another entity (like the player) interacts with this object.
        
        :param actor: The entity performing the interaction (e.g., Player).
        :return: True if interaction succeeded, False otherwise.
        """
        raise NotImplementedError("Subclasses must implement interact()")