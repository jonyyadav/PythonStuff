import logging

from meeting.CustomException import custom_error


def my_middleware(get_response):
  

    def my_function(request):
        print("this is before view")
        db_logger = logging.getLogger('db')
        try:
        #  db_logger.error()
        #  db_logger.info()
        #  db_logger.warning()
         response = get_response(request)
         
         print("this is after view")
         return response
         
        except Exception as e:
             db_logger.exception(e)
        
    return my_function
   


# class MyMiddleware:
#     def __int__(self, get_response):
#         self.get_response = get_response
#         print("one time")

#     def __call__(self, request):
#         print("before view")
#         response = self.get_response(request)
#         print("after view")
#         return response


# from urllib import response
# from meeting.CustomException import custom


# def pagenotfound(get_response):
   
#    def pnf(request):
#        try:
#         response = get_response(request)
#         return response

#        except custom as error:
#            print(error.value)
  