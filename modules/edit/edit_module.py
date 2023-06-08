from modules.base import Base


class Edit(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def edit(self, *args, **kwargs):
        raise NotImplementedError

