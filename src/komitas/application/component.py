from typing import Generic, Union
import komitas.html.tags as tg
import komitas.html.attributes as at
from types import NoneType


from komitas.application.base_component import *


class PageBaseModel(ComponentModel):
    title: str = "Page Base!"
    _nav_bar: AppBar | None = PrivateAttr(default=None)
    _innrs: list[Component] = PrivateAttr(default_factory=list)


class PageBase[TX](Component[PageBaseModel, TX]):
    def tag(self) -> tg.Tag:
        return tg.Div(tg.H1(self.model.title), *self.model._innrs)


class InteractiveComponent[T, TX](Component[T, TX]):
    """
    We subclass component and add the funcitonality for updating state.
    """

    # _model_type: type[] | None = None
    # _model_extras_type: type[TXComponentModel] | None = None
    #
    # def __init_subclass__(cls, **kwargs):
    #     """
    #     When someone does:
    #
    #         class MyComp(InteractiveComponent[MyModel, MyExtras]): ...
    #
    #     we grab `MyModel` and store it in `cls._model_type`.
    #     """
    #     super().__init_subclass__(**kwargs)
    #
    #     # Look through the generic bases
    #     for base in getattr(cls, "__orig_bases__", ()):
    #         origin = get_origin(base)
    #         if origin is InteractiveComponent:
    #             args = get_args(base)
    #             if args:
    #                 # args[0] is TComponentModel, args[1] is TXComponentModel
    #                 cls._model_type = args[0]
    #                 cls._model_extras_type = args[1]
    #             break
    #
    # def __init__(
    #     self,
    #     model: Union[TComponentModel, NoneType] = None,
    #     model_extras: Union[TXComponentModel, NoneType] = None,
    #     **kwargs,
    # ) -> None:
    #     assert self._model_type is not None
    #     if self._model_type:
    #         self.model: TComponentModel = model or self._model_type()
    #     assert self._model_extras_type is not None
    #     if model_extras:
    #         self.model_extras: TXComponentModel = (
    #             model_extras or self._model_extras_type()
    #         )

    def update_state(self, params):
        raise NotImplementedError

    def name(self):
        return self.model.name

    def name_safe(self):
        return self.model.name.lower().replace(" ", "-")


class ViewModel(ComponentModel):
    pass


class View[TX](InteractiveComponent[ViewModel, TX]):
    pass


class AppBarModel(ComponentModel):
    _active_view: Union[View, NoneType] = PrivateAttr(default=None)
    _views: list[View] = PrivateAttr(default_factory=list)


class AppBarButton[TX](InteractiveComponent[AppBarModel, TX]):
    pass


class AppBar[TX](InteractiveComponent[AppBarModel, TX]):
    def register_views(self, *args: View):
        self.model._views.extend(args)
        if not self.model._active_view:
            self.model._active_view = args[0]


class ViewContainer[TX](InteractiveComponent[AppBarModel, TX]):
    def update_state(self, params):
        pass

    def __call__(self):
        return (
            tg.Div()
            .attrs(
                (at.Id, "view-container"),
            )
            .innrs(self.model._active_view)
        )
