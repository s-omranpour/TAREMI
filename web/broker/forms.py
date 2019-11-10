from .models import *

class AnswerRenderer:
    def __init__(answer):
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
        return """<div>%s</div>""" % self.answer.value

    def render_fixed(self):
        return """<input type="text" name="{name}" value="{value}">""".format(name=self.field_name, value=self.answer.value)

renderers = {TextualAnswer: TextualRenderer}

def render_field(answer, editable):
    renderer = renderers[answer.__class__](answer)
    if editable:
        return renderer.render_editable()
    else:
        return renderer.render_fixed()

def render(response, editable):
    content = ""
    for a in response.answers.order_by('question__number'):
        content += """
          <div class="field">
            <label>{question}</label>
            {answer}
          </div>
        """.format(question=str(a.question), answer=render_field(a, editable))

    if editable:
        content += """
          <button class="ui button" type="submit">Submit</button>
        """

    return """<form class="ui form">
        <h4 class="ui dividing header">{title}</h4>
        {content}
        </form>""".format(title=response.get_form().information, content=content)
