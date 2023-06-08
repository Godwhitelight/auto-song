from modules.edit.edit_module import Edit


class Effect(Edit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def edit(self, *args, **kwargs):
        raise NotImplementedError
