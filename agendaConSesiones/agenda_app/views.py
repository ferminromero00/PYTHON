from django.shortcuts import render
from agenda_app.forms import Formulario
from agenda_app.models import Cita

def index(request):
    # Verifica si la clave "agenda" está en la sesión, si no, la inicializa como una lista vacía
    if "agenda" not in request.session:
        request.session["agenda"] = []

    # Si la solicitud es de tipo POST, significa que el formulario ha sido enviado
    if request.method == "POST":
        form = Formulario(request.POST)  # Crea una instancia del formulario con los datos enviados
        if form.is_valid():  # Verifica si el formulario es válido
            descripcion = form.cleaned_data["descripcion"]  # Obtiene la descripción del formulario
            fecha = form.cleaned_data["fecha"]  # Obtiene la fecha del formulario

            # Crear una instancia de Cita y guardarla en la base de datos
            nueva_cita = Cita(description=descripcion, fecha=fecha)
            nueva_cita.save()

            # Guardar la cita en formato de diccionario (serializable) en la sesión
            cita = {
                "descripcion": descripcion,
                "fecha": fecha.strftime("%d-%m-%Y") if fecha else None  # Formatea la fecha si existe
            }

            # Añade la nueva cita a la lista de la sesión y marca la sesión como modificada
            request.session["agenda"].append(cita)
            request.session.modified = True

    else:
        # Si la solicitud no es de tipo POST, crea una instancia vacía del formulario
        form = Formulario()

    # Renderiza la plantilla 'index.html' con el formulario y la lista de citas en la sesión
    return render(request, 'index.html', {'form': form, 'agenda': request.session["agenda"]})