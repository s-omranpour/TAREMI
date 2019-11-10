from broker.models import *
from mock.users import student,instructor


form = ApplicationForm(course_id='kir', creator=instructor, info='kire khar')
form.save()

q = TextualQuestion(form=form, question='kir?',number=1)
q.save()

res = ApplicationResponse(owner=student, state='p')
res.save()

a = TextualAnswer(response=res, question=q, value='kun')
a.save()
