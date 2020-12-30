from django.utils.deprecation import MiddlewareMixin
class BookMiddlewareMixin(MiddlewareMixin):
    # 每次请求都会调用
    def process_request(self,request):
        print("request 每次调用前  都会调用111111111111111")
        pass

    def process_response(self,request,response):
        print("response  每次响应前，  都会调用1111111111111")
        return response


class BookMiddlewareMixin2(MiddlewareMixin):
    # 每次请求都会调用
    def process_request(self,request):
        print("request 每次调用前  都会调用222222222222222")
        pass

    def process_response(self,request,response):
        print("response  每次响应前，  都会调用2222222222222")
        return response