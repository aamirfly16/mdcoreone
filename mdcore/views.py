from django.shortcuts import render
from mdcore.models import Projects

# Create your views here.
def index(request):

    proj1 = Projects()
    proj1.name = 'Point of sale'
    proj1.desc = 'POS system software empowers retailers with a user-friendly interface that aims to deliver seamless retail experiences.'

    proj2 = Projects()
    proj2.name = 'Weighbridge Management'
    proj2.desc = 'Weight scaling Integration to the Weighbridge machine used to track net weight in trade and manufacturing units'

    proj3 = Projects()
    proj3.name = 'E-Commerce'
    proj3.desc = 'A cloud-based application to facilitate fast, accurate, reliable and easy accessibility web application'

    proj4 = Projects()
    proj4.name = 'Cooperative Society Application'
    proj4.desc = 'Featuring Share accounts, Saving accounts, Fixed Deposit, Loan account, Pigmy deposit, Day book, Advisor Registration, Member Registration'



    return render(request,"index.html", {'proj1':proj1,'proj2':proj2,'proj3':proj3, 'proj4':proj4})