from multiprocessing import get_context
from django.shortcuts import render
from django.http import HttpResponse
from django_user_agents.utils import get_user_agent
import subprocess

# Create your views here.

def index(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return HttpResponse('User Using Mobile')
    elif user_agent.is_tablet:
        return HttpResponse('User Using Tablet')
    elif user_agent.is_pc:
        vi = request.META['HTTP_USER_AGENT']
        context = {
            'val': vi
        }
        return render(request, 'index.html', context)
    
def sysInfo(request):
    # traverse the info
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []
    # arrange the string into clear info
    for item in Id:
        new.append(str(item.split("\r")[:-1]))
    for i in new:
        val = i[2:-2]
        with open("sample.txt", "a") as f:
            f.write(val + "\n")
        
    return render(request, 'redir.html')  
    
    
    