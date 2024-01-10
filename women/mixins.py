class DataMixin:
    title_context = None
    cat_selected = 0
    extra_context = {}
    def __init__(self):
        if self.title_context is not None:
            self.extra_context['title'] = self.title_context

        self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_context(self, context, **kwargs):
        context['cat_selected'] = 0
        context.update(kwargs)
        return context
