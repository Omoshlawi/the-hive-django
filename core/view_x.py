from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet
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
