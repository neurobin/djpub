# -*- coding: utf-8 -*-

"""Common views for djpub


-------------------------------------------------------------------
Copyright: Md. Jahidul Hamid <jahidulhamid@yahoo.com>

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)
-------------------------------------------------------------------
"""

from django.http import HttpResponse
from django.views import View

class BaseView(View):
    """Base view to be inherited by other views
    """

    def get(self, request):
        pass
    
    def post(self, request):
        pass