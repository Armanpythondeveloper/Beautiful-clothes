from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views import generic

from .forms import FormContact
from .models import (
    AboutHeader,AboutSection,
    OurTeam,AboutIconca,
    AboutPartners,Products,
    JarangProd , Like,
    ContactHeader,Contact,ContactInfo,
    ContactAside,ContactTitles,ProductTitle,
    IndexHeader,HomeNews,
   
    )



def index(request):
    index_list = IndexHeader.objects.all()

    double_list = JarangProd.objects.all()[::-1]
    double_list = double_list[:6]

    home_news = HomeNews.objects.all()[0]

    return render(request,'main/index.html',context={
        'act':'index',
        'index_list':index_list,
        'double_list':double_list,
        'home_news':home_news
                          })
    


def contact(request):

    contact_head = ContactHeader.objects.all()[0]

    info_list = ContactInfo.objects.all()[0]

    aside_list = ContactAside.objects.all()

    about_partners = AboutPartners.objects.all()

    title_list = ContactTitles.objects.all()[0]

    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            form.save()
            return redirect('contact')
    else:
        form = FormContact()


    return render(request,'main/contact.html',context={
        'act':'contact',
        'contact_head':contact_head,
        'form':form,
        'info_list':info_list,
        'aside_list':aside_list,
        'about_partners':about_partners,
        'title_list':title_list

        
    })


def about(request):

    about_header = AboutHeader.objects.all()[0]
    about_section = AboutSection.objects.all()[0]
    about_member = OurTeam.objects.all()
    about_icon = AboutIconca.objects.all()
    about_partners = AboutPartners.objects.all()
    return render(request,'main/about.html',context={
        'act':'about',
        'about_header':about_header,
        'about_section':about_section,
        'about_member':about_member,
        'about_icon':about_icon,
        'about_partners':about_partners
    })


def products(request):

    prod_list = Products.objects.all()
    s = 0
    for item in Like.objects.all().values():
        s += item.get('grade' , 0)
    if not Like.objects.count():
        mean_grade = 5
    else:
        mean_grade = s / Like.objects.count()
    jarang_list = JarangProd.objects.all()

    prod_title = ProductTitle.objects.all()[0]
    
    if request.method == 'POST':
        print(request.POST)
        # Like.objects.create(request.POST)




    return render(request,'main/products.html',context={
        'act':'products',
        'prod_list':prod_list,
        'jarang_list':jarang_list,
        'mean_grade':mean_grade,
        'prod_title':prod_title
    })


# class HomeView(generic.ListView):
#     template_name = 'main/index.html'


#     def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
#         return render(request, self.template_name, 
#                       context={
#                                 'act':'index',

                                            
#                                         })

    