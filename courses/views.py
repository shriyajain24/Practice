from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Subject, Assignment, Submission
from accounts.models import CustomUser

# 1. Saare Subjects dikhane ke liye (Course List Page)
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'courses/subject_list.html', {'subjects': subjects})

# 2. Kisi ek Subject ke Notes, Assignments aur Submission handling
def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    materials = subject.materials.all()
    assignments = subject.assignments.all()

    # Jab student assignment submit kare (POST request)
    if request.method == 'POST':
        assignment_id = request.POST.get('assignment_id')
        uploaded_file = request.FILES.get('submission_file')
        assignment = get_object_or_404(Assignment, id=assignment_id, subject=subject)

        # Logged-in user check (testing ke liye fallback student user)
        if request.user.is_authenticated and getattr(request.user, 'role', '') == 'Student':
            student = request.user
        else:
            student = CustomUser.objects.filter(role='Student').first()

        if student and uploaded_file:
            Submission.objects.update_or_create(
                assignment=assignment,
                student=student,
                defaults={'file': uploaded_file}
            )
            messages.success(request, f'"{assignment.title}" successfully submit ho gaya!')
        else:
            messages.error(request, 'File select karein ya pehle ek Student user banayein.')

        return redirect('subject_detail', subject_id=subject.id)

    context = {
        'subject': subject,
        'materials': materials,
        'assignments': assignments,
    }
    return render(request, 'courses/subject_detail.html', context)