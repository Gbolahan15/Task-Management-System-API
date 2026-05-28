from rest_framework.pagination import PageNumberPagination

class TaskPagination(PageNumberPagination):
    page_size = 5 # default page size
    page_size_query_param = 'page_size' # allow clients to set the page size using a query parameter
    max_page_size = 100 # to prevent huge requests that can overload the server