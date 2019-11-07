from broker.models import *
from users import student,instructor


form = ApplicationForm(course_id='kir', creator=instructor, info='kire khar')
form.save()

q = TextualQuestion(form=form, question='kir?',number=1)
q.save()

res = ApplicationResponse(owner=student)
res.save()

a = TextAnswer(response=res, question=q, value='kun')
a.save()