from django.contrib import admin
from .models import Instructor, Departamento, Inscripcion, Curso, Estudiante, Tarea

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 1
    verbose_name = "Inscripción"
    verbose_name_plural = "Inscripciones"


class CursoAdmin(admin.ModelAdmin):
    inlines = [InscripcionInline]
    list_display = ('titulo', 'departamento', 'instructor')
    list_filter = ('departamento',)
    search_fields = ('titulo', 'instructor__nombre')


admin.site.register(Departamento)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Tarea)