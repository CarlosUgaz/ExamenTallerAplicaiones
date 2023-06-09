from os import path
from django.urls import path
import gestion.views as v

urlpatterns = [
    path('gestion/', v.home, name='homeGestion'),
    path('Doctor/', v.indexDoctor, name='indexDoctor'),
    path('Doctor/crear_nuevo_doctor', v.crear_nuevo_doctor),
    path('Doctor/editar_doctor_<int:id>', v.editar_doctor),
    path('Doctor/detalles_doctor_<int:id>', v.detalles_doctor),
    path('Doctor/eliminar_doctor_<int:id>', v.eliminar_doctor),
    path('Cita/', v.indexCita, name='indexCita'),
    path('Paciente/', v.indexPaciente, name='indexPaciente'),
    path('Paciente/crear_nuevo_paciente', v.crear_nuevo_paciente),
    path('Paciente/editar_paciente_<int:id>', v.editar_paciente),
    path('Paciente/detalles_paciente_<int:id>', v.detalles_paciente),
    path('Paciente/eliminar_paciente_<int:id>', v.eliminar_paciente),
]
