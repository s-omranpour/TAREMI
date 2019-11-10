from broker.models import *
from mock.users import *

def make_form(course_id, creator, info):
    form = ApplicationForm(course_id=course_id, creator=creator, info=info)
    form.save()
    return form

def make_question(form, text, type, number):
    if type == 'numerical':
        q = NumericalQuestion(form=form, question=text, number=number)
    elif type == 'texual':
        q = TextualQuestion(form=form, question=text,number=number)
    q.save()
    return q

def make_answer(response, question, type, value):
    if type == 'numerical':
        a = NumericalAnswer(response=response,question=question, value=value)
    elif type == 'texual':
        a = TextualAnswer(response=response, question=question, value=value)
    a.save()
    return a

def make_response(student, state='p'):
    res = ApplicationResponse(owner=student, state=state)
    res.save()
    return res


form1 = make_form('ce-440', in1, 'TA application for signal and systems')
form2 = make_form('ce-550', in1, 'Welcome to AI application')

q1_1 = make_question(form1, 'nomre darse madaar?', 'numerical', 1)
q2_1 = make_question(form1, 'barname nevisi baladi?', 'texual', 2)

q1_2 = make_question(form2, 'nomre darse amaar?', 'numerical', 1)
q2_2 = make_question(form2, 'khundan neveshtan baladi?', 'texual', 2)

res1 = make_response(st1)
res2 = make_response(st2)

a1_1_1 = make_answer(res1, q1_1, 'numerical', 19.99999999999)
a1_2_1 = make_answer(res1, q2_1, 'texual', 'Bale')
a2_1_1 = make_answer(res2, q1_1, 'numerical', 15.5)
a2_2_1 = make_answer(res2, q2_1, 'texual', 'Na')
