from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.template.response import TemplateResponse

# Create your views here.
from bigbox.models import Box, Activity, CommonInfo, Reason, Prodcut
from django.http import HttpResponsePermanentRedirect

def redireccion(request):
    
    return HttpResponsePermanentRedirect(reverse('box'))


def box(request):

    box_inf = Box.objects.all()
    context = {'box_inf': box_inf}
    return render(request, 'box/box_list.html', context)

def box_slug(request, slug):

    #Lista de Box y el id, se puede mejorar
    box_inf = Box.objects.all()
    box_slug = Box.objects.filter(slug=slug)
    #Muestra de actividades con paginador
    list_activity = Activity.objects.get_queryset().order_by('id')
    paginator = Paginator(list_activity, 5)
    page = request.GET.get('page')
    actividad = paginator.get_page(page)

    context = {'box_slug':box_slug, 'box_inf': box_inf, 'actividad':actividad, 'box_slug':box_slug}
    
    return render(request, 'box/box_id.html', context)

def box_id(request, id):

    #Lista de Box y el id, se puede mejorar
    box_inf = Box.objects.all()
    box_id = Box.objects.filter(id=id)
    #Muestra de actividades con paginador
    list_activity = Activity.objects.get_queryset().order_by('id')
    paginator = Paginator(list_activity, 5)
    page = request.GET.get('page')
    actividad = paginator.get_page(page)

    context = {'box_id':box_id, 'box_inf': box_inf, 'actividad':actividad, 'box_slug':box_slug}
    
    return render(request, 'box/box_id.html', context)

def activity(request, id):
    #Prueba de diccionario sin recorrido de lista en jinja
    box_inf = list(Box.objects.all().values())
    list_box_inf = []
    for list_box_inf in box_inf:
        pass
    
    #Lista de Actividad y Paginador
    list_activity = Activity.objects.get_queryset().order_by('id')
    paginator = Paginator(list_activity, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj, 'list_box_inf': list_box_inf}
    return render(request, 'activity/activity_list.html', context)

def activity_id(request, id, activity_id):

    #Recordemos usar .filter para obtener valores del objeto ya que .get lo vuelve no-iterable
    actividad = Activity.objects.filter(id=activity_id)
    actividad_info = list(actividad.all().values())
    list_actividad_info = []
    for list_actividad_info in actividad_info:
        pass
    context = {'actividad': actividad, 'list_actividad_info': list_actividad_info}

    return render(request, 'activity/activity_id.html', context)