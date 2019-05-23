from django.shortcuts import render, get_object_or_404


from .models import News, Category

class ObjDetailMixin():
    model = None
    template = None

    def get(self, request, pk):
        obj = get_object_or_404(self.model, id=pk)
        return render(
            request,
            self.template,
            context={self.model.__name__.lower(): obj })