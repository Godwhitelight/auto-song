from modules.edit.effects.effect import Effect


class VideoEffect(Effect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def edit(self, *args, **kwargs):
        raise NotImplementedError
