from django.contrib import admin
from .models import *

# -------------------------------
# ROLE
# -------------------------------
@admin.register(TBL_ROLE)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('ROLE_ID', 'ROLE_TYPE')
    search_fields = ('ROLE_TYPE',)

# -------------------------------
# USER
# -------------------------------
@admin.register(TBL_USER)
class UserAdmin(admin.ModelAdmin):
    list_display = ('USER_ID', 'USER_NAME', 'EMAIL', 'ROLE', 'STATUS', 'CREATED_AT')
    search_fields = ('USER_NAME', 'EMAIL')
    list_filter = ('ROLE', 'STATUS')

# -------------------------------
# EMAIL VERIFICATION
# -------------------------------
@admin.register(TBL_EMAIL_VERIFICATION)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'otp', 'purpose', 'expires_at', 'is_verified')
    list_filter = ('purpose', 'is_verified')
    search_fields = ('user__EMAIL', 'otp')

# -------------------------------
# COLLEGE
# -------------------------------
@admin.register(TBL_COLLEGE)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('COLLEGE_ID', 'COLLEGE_NAME', 'COLLEGE_CODE', 'COLLEGE_UNIVERSITY', 'COLLEGE_EMAIL')
    search_fields = ('COLLEGE_NAME', 'COLLEGE_CODE', 'COLLEGE_UNIVERSITY')
    list_filter = ('COLLEGE_STATUS',)

# -------------------------------
# TNP
# -------------------------------
@admin.register(TBL_TNP)
class TNPAdmin(admin.ModelAdmin):
    list_display = ('TNP_ID', 'TNP_NAME', 'ROLE_TYPE', 'COLLEGE', 'TNP_EMAIL', 'TNP_PHONE_NO')
    search_fields = ('TNP_NAME', 'TNP_EMAIL', 'TNP_PHONE_NO')
    list_filter = ('ROLE_TYPE', 'COLLEGE')

# -------------------------------
# ADMIN
# -------------------------------
@admin.register(TBL_ADMIN)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('ADMIN_ID', 'ADMIN_NAME', 'ROLE_TYPE', 'USER', 'ADMIN_EMAIL', 'ADMIN_PHONE_NO')
    search_fields = ('ADMIN_NAME', 'ADMIN_EMAIL', 'ADMIN_PHONE_NO')
    list_filter = ('ROLE_TYPE',)

# -------------------------------
# COMPANY
# -------------------------------
@admin.register(TBL_COMPANY)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('COMPANY_ID', 'COMPANY_NAME', 'ROLE_TYPE', 'USER', 'COLLEGE', 'COMPANY_EMAIL', 'COMPANY_PHONE_NO')
    search_fields = ('COMPANY_NAME', 'COMPANY_EMAIL', 'COMPANY_PHONE_NO')
    list_filter = ('ROLE_TYPE', 'COLLEGE')

# -------------------------------
# STUDENT
# -------------------------------
@admin.register(TBL_STUDENT)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('STUDENT_ID', 'STUDENT_NAME', 'ROLE_TYPE', 'COLLEGE', 'STUDENT_EMAIL', 'STUDENT_PHONE_NO')
    search_fields = ('STUDENT_NAME', 'STUDENT_EMAIL', 'STUDENT_PHONE_NO')
    list_filter = ('ROLE_TYPE', 'COLLEGE', 'STUDENT_COURSE', 'STUDENT_BRANCH')

# -------------------------------
# INTERNSHIP
# -------------------------------
@admin.register(TBL_INTERNSHIP)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('INTERNSHIP_ID', 'STUDENT', 'COMPANY', 'INTERNSHIP_TITLE', 'INTERNSHIP_DOMAIN', 'INTERNSHIP_START_DATE', 'INTERNSHIP_END_DATE')
    search_fields = ('INTERNSHIP_TITLE', 'INTERNSHIP_DOMAIN', 'STUDENT__STUDENT_NAME', 'COMPANY__COMPANY_NAME')
    list_filter = ('INTERNSHIP_DOMAIN', 'COMPANY')

# -------------------------------
# PROJECT
# -------------------------------
@admin.register(TBL_PROJECT)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('PROJECT_ID', 'STUDENT', 'PROJECT_TITLE', 'PROJECT_DOMAIN', 'PROJECT_ROLE', 'PROJECT_STATUS')
    search_fields = ('PROJECT_TITLE', 'PROJECT_DOMAIN', 'STUDENT__STUDENT_NAME')
    list_filter = ('PROJECT_STATUS',)

# -------------------------------
# CERTIFICATION
# -------------------------------
@admin.register(TBL_CERTIFICATION)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('CERTIFICATE_ID', 'STUDENT', 'CERTIFICATE_NAME', 'CERTIFICATE_DOMAIN', 'CERTIFICATE_AUTHORITY', 'CERTIFICATE_DATE')
    search_fields = ('CERTIFICATE_NAME', 'STUDENT__STUDENT_NAME')
    list_filter = ('CERTIFICATE_DOMAIN',)

# -------------------------------
# EDUCATION
# -------------------------------
@admin.register(TBL_EDUCATION)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('EDUCATION_ID', 'STUDENT', 'EDUCATION_LEVEL', 'INSTITUTE_NAME', 'BOARD_UNIVERSITY', 'YEAR_OF_PASSING')
    search_fields = ('STUDENT__STUDENT_NAME', 'INSTITUTE_NAME')
    list_filter = ('EDUCATION_LEVEL',)

# -------------------------------
# JOB
# -------------------------------
@admin.register(TBL_JOB)
class JobAdmin(admin.ModelAdmin):
    list_display = ('JOB_ID', 'COMPANY', 'JOB_TITLE', 'JOB_LOCATION', 'JOB_TYPE', 'JOB_STATUS')
    search_fields = ('JOB_TITLE', 'COMPANY__COMPANY_NAME')
    list_filter = ('JOB_TYPE', 'JOB_STATUS')

# -------------------------------
# APPLICATION
# -------------------------------
@admin.register(TBL_APPLICATION)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('APPLICATION_ID', 'STUDENT', 'JOB', 'APPLICATION_DATE', 'APPLICATION_STATUS')
    search_fields = ('STUDENT__STUDENT_NAME', 'JOB__JOB_TITLE')
    list_filter = ('APPLICATION_STATUS',)

# -------------------------------
# PLACEMENT ROUND
# -------------------------------
@admin.register(TBL_PLACEMENT_ROUND)
class PlacementRoundAdmin(admin.ModelAdmin):
    list_display = ('ROUND_ID', 'JOB', 'ROUND_NAME', 'ROUND_TYPE', 'ROUND_DATE')
    search_fields = ('ROUND_NAME', 'JOB__JOB_TITLE')
    list_filter = ('ROUND_TYPE',)

# -------------------------------
# INTERVIEW SCHEDULE
# -------------------------------
@admin.register(TBL_INTERVIEW_SCHEDULE)
class InterviewScheduleAdmin(admin.ModelAdmin):
    list_display = ('INTERVIEW_ID', 'APPLICATION', 'ROUND', 'INTERVIEW_DATE', 'INTERVIEW_MODE', 'INTERVIEW_STATUS')
    search_fields = ('APPLICATION__STUDENT__STUDENT_NAME', 'ROUND__ROUND_NAME')
    list_filter = ('INTERVIEW_MODE', 'INTERVIEW_STATUS')

# -------------------------------
# ROUND RESULT
# -------------------------------
@admin.register(TBL_ROUND_RESULT)
class RoundResultAdmin(admin.ModelAdmin):
    list_display = ('RESULT_ID', 'STUDENT', 'JOB', 'ROUND_NUMBER', 'RESULT_STATUS', 'UPDATED_AT')
    list_filter = ('ROUND_NUMBER', 'RESULT_STATUS', 'JOB', 'COMPANY')
    search_fields = ('STUDENT__STUDENT_NAME', 'JOB__JOB_TITLE')

# -------------------------------
# NOTIFICATION
# -------------------------------
@admin.register(TBL_NOTIFICATION)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('NOTIFICATION_ID', 'USER', 'TITLE', 'IS_READ', 'CREATED_AT')
    search_fields = ('TITLE', 'USER__USER_NAME')
    list_filter = ('IS_READ',)

# -------------------------------
# LOGIN HISTORY
# -------------------------------
@admin.register(TBL_LOGIN_HISTORY)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('LOGIN_ID', 'USER', 'LOGIN_TIME', 'LOGOUT_TIME', 'IP_ADDRESS', 'DEVICE_INFO')
    search_fields = ('USER__USER_NAME', 'IP_ADDRESS')

# -------------------------------
# QUIZ
# -------------------------------
@admin.register(TBL_QUIZ)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('QUIZ_ID', 'QUIZ_TITLE', 'JOB', 'COMPANY', 'COLLEGE', 'TOTAL_QUESTIONS', 'QUIZ_DATE')
    search_fields = ('QUIZ_TITLE', 'JOB__JOB_TITLE', 'COMPANY__COMPANY_NAME', 'COLLEGE__COLLEGE_NAME')
    list_filter = ('QUIZ_DATE',)

# -------------------------------
# QUIZ QUESTION
# -------------------------------
@admin.register(TBL_QUIZ_QUESTION)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('QUESTION_ID', 'QUIZ', 'QUESTION_TEXT', 'CORRECT_OPTION')
    search_fields = ('QUESTION_TEXT', 'QUIZ__QUIZ_TITLE')
    list_filter = ('QUIZ',)

# -------------------------------
# STUDENT ANSWER
# -------------------------------
@admin.register(TBL_STUDENT_ANSWER)
class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ('ANSWER_ID', 'STUDENT', 'QUESTION', 'SELECTED_OPTION', 'IS_CORRECT')
    search_fields = ('STUDENT__STUDENT_NAME', 'QUESTION__QUESTION_TEXT')
    list_filter = ('IS_CORRECT',)

# -------------------------------
# CODING QUESTION
# -------------------------------
@admin.register(TBL_CODING_QUESTION)
class CodingQuestionAdmin(admin.ModelAdmin):
    list_display = ('QUESTION_ID', 'QUESTION_TITLE', 'JOB', 'COMPANY', 'COLLEGE', 'DIFFICULTY', 'DURATION_MINUTES')
    search_fields = ('QUESTION_TITLE', 'JOB__JOB_TITLE', 'COMPANY__COMPANY_NAME', 'COLLEGE__COLLEGE_NAME')
    list_filter = ('DIFFICULTY',)

# -------------------------------
# GD GROUP
# -------------------------------
@admin.register(TBL_GD_GROUP)
class GDGroupAdmin(admin.ModelAdmin):
    list_display = ('GROUP_ID', 'JOB', 'COMPANY', 'COLLEGE', 'GROUP_NUMBER', 'SCHEDULE')
    search_fields = ('JOB__JOB_TITLE', 'COMPANY__COMPANY_NAME', 'COLLEGE__COLLEGE_NAME')
    list_filter = ('GROUP_NUMBER', 'SCHEDULE')

# -------------------------------
# GD GROUP MEMBER
# -------------------------------
@admin.register(TBL_GD_GROUP_MEMBER)
class GDGroupMemberAdmin(admin.ModelAdmin):
    list_display = ('GROUP_MEMBER_ID', 'GROUP', 'STUDENT')
    search_fields = ('GROUP__GROUP_NUMBER', 'STUDENT__STUDENT_NAME')
    list_filter = ('GROUP',)
