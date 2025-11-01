from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from HIRE.models import (
    TBL_QUIZ, TBL_GD_GROUP, TBL_INTERVIEW_SCHEDULE, TBL_STUDENT
)

class Command(BaseCommand):
    help = "Send reminder emails to students and TNP one day before scheduled rounds."

    def handle(self, *args, **options):
        today = timezone.localtime(timezone.now()).date()
        tomorrow = today + timedelta(days=1)

        print(f"🕐 Checking rounds scheduled for {tomorrow}")

        # ✅ 1. Aptitude Tests
        quizzes = TBL_QUIZ.objects.filter(QUIZ_START_DATE=tomorrow)
        for quiz in quizzes:
            job = quiz.JOB
            company = quiz.COMPANY
            college = quiz.COLLEGE
            students = TBL_STUDENT.objects.filter(COLLEGE=college)
            tnp = college.TNP_HEAD if hasattr(college, "TNP_HEAD") else None

            for student in students:
                send_round_email(
                    subject=f"Reminder: Aptitude Test Tomorrow - {company.COMPANY_NAME}",
                    template="emails/reminder_aptitude.html",
                    context={
                        "student_name": student.STUDENT_NAME,
                        "company_name": company.COMPANY_NAME,
                        "job_title": job.JOB_TITLE,
                        "date": quiz.QUIZ_START_DATE,
                        "duration": quiz.QUIZ_DURATION,
                        "college_name": college.COLLEGE_NAME,
                    },
                    recipients=[student.USER.EMAIL],
                )

            if tnp:
                send_round_email(
                    subject=f"Reminder: Aptitude Test Tomorrow for {college.COLLEGE_NAME}",
                    template="emails/reminder_tnp.html",
                    context={
                        "tnp_name": tnp.USER.FULL_NAME,
                        "company_name": company.COMPANY_NAME,
                        "job_title": job.JOB_TITLE,
                        "date": quiz.QUIZ_START_DATE,
                    },
                    recipients=[tnp.USER.EMAIL],
                )

        # ✅ 2. Group Discussion
        gd_groups = TBL_GD_GROUP.objects.filter(SCHEDULE__date=tomorrow)
        for group in gd_groups:
            company = group.COMPANY
            job = group.JOB
            members = group.tbl_gd_group_member_set.select_related("STUDENT__USER")
            tnp = group.COLLEGE.TNP_HEAD if hasattr(group.COLLEGE, "TNP_HEAD") else None

            for member in members:
                send_round_email(
                    subject=f"Reminder: GD Scheduled Tomorrow - {company.COMPANY_NAME}",
                    template="emails/reminder_gd.html",
                    context={
                        "student_name": member.STUDENT.STUDENT_NAME,
                        "company_name": company.COMPANY_NAME,
                        "job_title": job.JOB_TITLE,
                        "schedule": group.SCHEDULE,
                        "meeting_link": group.MEETING_LINK,
                        "group_number": group.GROUP_NUMBER,
                    },
                    recipients=[member.STUDENT.USER.EMAIL],
                )

            if tnp:
                send_round_email(
                    subject=f"Reminder: GD for {college.COLLEGE_NAME} Tomorrow",
                    template="emails/reminder_tnp.html",
                    context={
                        "tnp_name": tnp.USER.FULL_NAME,
                        "company_name": company.COMPANY_NAME,
                        "job_title": job.JOB_TITLE,
                        "date": group.SCHEDULE,
                    },
                    recipients=[tnp.USER.EMAIL],
                )

        # ✅ 3. Technical Interviews
        tech_interviews = TBL_INTERVIEW_SCHEDULE.objects.filter(
            INTERVIEW_DATE__date=tomorrow,
            ROUND__ROUND_TYPE__icontains="Technical"
        )
        send_interview_reminders(tech_interviews, "Technical")

        # ✅ 4. HR Interviews
        hr_interviews = TBL_INTERVIEW_SCHEDULE.objects.filter(
            INTERVIEW_DATE__date=tomorrow,
            ROUND__ROUND_TYPE__icontains="HR"
        )
        send_interview_reminders(hr_interviews, "HR")

        print("✅ All reminder emails processed successfully.")


def send_interview_reminders(interviews, round_type):
    for i in interviews:
        student = i.APPLICATION.STUDENT
        company = i.COMPANY
        job = i.APPLICATION.JOB
        college = student.COLLEGE
        tnp = college.TNP_HEAD if hasattr(college, "TNP_HEAD") else None

        send_round_email(
            subject=f"Reminder: {round_type} Interview Tomorrow - {company.COMPANY_NAME}",
            template="emails/reminder_interview.html",
            context={
                "student_name": student.STUDENT_NAME,
                "company_name": company.COMPANY_NAME,
                "job_title": job.JOB_TITLE,
                "date": i.INTERVIEW_DATE,
                "meeting_link": i.INTERVIEW_LINK,
                "round_type": round_type,
            },
            recipients=[student.USER.EMAIL],
        )

        if tnp:
            send_round_email(
                subject=f"Reminder: {round_type} Interviews Tomorrow - {company.COMPANY_NAME}",
                template="emails/reminder_tnp.html",
                context={
                    "tnp_name": tnp.USER.FULL_NAME,
                    "company_name": company.COMPANY_NAME,
                    "job_title": job.JOB_TITLE,
                    "date": i.INTERVIEW_DATE,
                },
                recipients=[tnp.USER.EMAIL],
            )


def send_round_email(subject, template, context, recipients):
    """Common reusable email sender with HTML templates."""
    html_body = render_to_string(template, context)
    send_mail(
        subject=subject,
        message="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients,
        html_message=html_body,
        fail_silently=True,
    )
