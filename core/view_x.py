from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from django_filters import FilterSet


class ViewX(View):
    """
    Paginates objects
    Advance filter enabled
    """
    template_path: str = None
    filterset_class: FilterSet = None
    queryset: QuerySet = None
    page_size: int = 10
    page_lookup: str = 'page'
    list_template: str = 'list.html'
    detail_template: str = 'detail.html'
    object_lookup: str = "objects"

    def get_object_lookup(self):
        return self.object_lookup

    def get_list_template(self):
        return self.list_template

    def get_detail_template(self):
        return self.detail_template

    def get_page_size(self) -> int:
        return self.page_size

    def get_page_lookup(self) -> str:
        return self.page_lookup

    def paginate_objects(self, request, queryset):
        page_size = request.GET.get('page_size', self.get_page_size())
        paginator = Paginator(queryset, per_page=page_size)
        param = self.get_page_lookup()
        page = request.GET.get(param, 1)

        current_page = None
        _page = page
        try:
            current_page = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            current_page = paginator.page(1)
            _page = 1
        except EmptyPage:
            # If page is out of range deliver last page of results
            current_page = paginator.page(paginator.num_pages)
            _page = paginator.num_pages
        current_page.adjusted_elided_pages = paginator.get_elided_page_range(_page)
        return current_page

    def filter_objects(self, request, queryset):
        FilterSetClass = self.get_filterset_class()
        if FilterSetClass:
            filtered = FilterSetClass(request.GET, queryset=queryset)
            return filtered.qs
        return queryset

    def get_template_path(self) -> str:
        return self.template_path

    def get_filterset_class(self) -> FilterSet:
        return self.filterset_class

    def get_queryset(self) -> QuerySet:
        return self.queryset

    def get(self, request, *args, **kwargs) -> HttpResponse:
        if (args or kwargs):
            return self.detail(request, *args, **kwargs)
        else:
            return self.list(request)

    def get_context(self, request) -> dict:
        filtered = self.filter_objects(request, queryset=self.get_queryset())
        properties = self.paginate_objects(request, filtered)
        context = {
            self.get_object_lookup(): properties,
        }
        return context

    def list(self, request) -> HttpResponse:
        context = self.get_context(request)
        key = self.get_object_lookup()
        value = context.pop(key)
        context.update({f'{key}_list': value})
        return render(request, self.get_list_template(), context)

    def detail(self, request, *args, **kwargs) -> HttpResponse:
        key = self.get_object_lookup() + '_detail'
        value = self.get_queryset().filter(**kwargs)
        if not value.exists():
            raise Http404()
        context = {
            key: value.first()
        }
        return render(request, self.get_detail_template(), context)
