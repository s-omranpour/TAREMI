from .models import *

class AnswerRenderer:
    def __init__(self, answer):
        self.answer = answer
        self.field_name = 'ans_%d' % self.answer.question.number

    def read_from_post(self, post_data):
        raise NotImplementedError()

    def render_editable(self):
        raise NotImplementedError()

    def render_fixed(self):
        raise NotImplementedError()


class TextualRenderer(AnswerRenderer):
    def read_from_post(self, post_data):
        self.answer.value = post_data[self.field_name]

    def render_fixed(self):
        return """<div style="background-color:#ff6699;"> Answer : %s</div><br/>""" % self.answer.value

    def render_editable(self):
        return """<input type="text" name="{name}" value="{value}"><br/>""".format(name=self.field_name, value=self.answer.value)

renderers = {TextualAnswer: TextualRenderer, NumericalAnswer: TextualRenderer}

def render_field(answer, editable):
    renderer = renderers[answer.__class__](answer)
    if editable:
        return renderer.render_editable()
    else:
        return renderer.render_fixed()

def render_form(form, response=None, editable=False):
    content = ""
    i = 1
    for q in form.questions.order_by('number'):
        if response is None:
            a = q.typed().make_answer()
            print('new response :: ', a.value)
        else:
            a = response.answers.get(question=q).typed()

        content += """
          <div class="field">
            <label style="background-color:#99ccff;"> Question {i} : {question}</label>
            {answer}
          </div>
        """.format(i=i, question=str(q), answer=render_field(a, editable))
        i += 1

    if editable:
        return """<form class="ui form" method="post">
            {csrf}
            <h1 class="ui header">{title}</h1>
            {content}
            <button class="ui button" type="submit">Submit</button>
            </form>""".format(title=form.info, content=content, csrf='{% csrf_token %}')
    else:
        return """<div class="ui form" method="post">
            <h1 class="ui header">Title: {title}</h1>
             <label>Student : {user}</label>
             <br/><br/>
            {content}
            </div>""".format(title=form.info, user=response.owner.get_full_name(), content=content)

def save_form(form, data, response):
    for q in form.questions.all():
        a = response.answers.get(question=q)
        if a is None:
            a = q.typed().make_answer()
            a.response = response
        else:
            a = a.typed()

        renderers[a.__class__](a).read_from_post(data)
        a.save()
