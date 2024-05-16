from entity.frame import Frame

class Structure():
    def __init__(self, id: int, frames: list[Frame]):
        self.id = id
        self.frames = frames