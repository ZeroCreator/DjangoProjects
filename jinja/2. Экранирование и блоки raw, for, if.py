from jinja2 import Template
from markupsafe import escape

data = '''{% raw %}Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение{% endraw %}'''

tm = Template(data)
msg = tm.render(name='Федор')

link = '''В HTML-документае ссылки определяются так:
<a href="#">Ссылка</a>'''

# tm1 = Template("{{ link | e }}")
# msg1 = tm1.render(link=link)

msg1 = escape(link)

cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'},]

link1 = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value-"{{c['id']}}">{{c['city']}}</option>
{%elif c.city == "Москва" -%}
    <option>{{c['city']}}</option>
{%else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm2 = Template(link1)
msg2 = tm2.render(cities = cities)



print(msg)
print(msg1)
print(msg2)

