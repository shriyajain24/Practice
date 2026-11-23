from django.shortcuts import render, get_object_or_404
from .models import Subject

# 1. Saare Subjects dikhane ke liye (Course List Page)
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'courses/subject_list.html', {'subjects': subjects})

# 2. Kisi ek Subject ke andar ke Notes & Assignments dikhane ke liye
def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    materials = subject.materials.all()
    assignments = subject.assignments.all()
    syllabus = subject.syllabus_topics.all()
    
    context = {
        'subject': subject,
        'materials': materials,
        'assignments': assignments,
        'syllabus': syllabus,
    }
    return render(request, 'courses/subject_detail.html', context)