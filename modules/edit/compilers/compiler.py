from typing import List

from modules.edit.edit_module import Edit
from modules.edit.effects.effect import Effect


class Compiler(Edit):
    def __init__(self, effects: List[Effect], filename: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.effects = effects
        self.filename = filename

    def compile(self):
        raise NotImplementedError
