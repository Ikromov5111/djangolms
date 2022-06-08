from rest_framework import pagination

class CoursePageNumberPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'count'
    max_page_size = 5
    page_query_param = 'p'