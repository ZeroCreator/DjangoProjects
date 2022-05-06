from jinja2 import Template

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Фольксваген', 'price': 21300},
]

digs = [1, 2, 3, 4, 5]

# tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
# tpl = "Суммарная цена автомобилей {{ cs | max(attribute='price') }}"
# tpl = "Суммарная цена автомобилей {{ (cs | min(attribute='price')).model }}"
# tpl = "Суммарная цена автомобилей {{ cs | random }}"
tpl = "Автомобиль {{ cs | replace('о', 'О') }}"
tm = Template(tpl)
msg = tm.render(cs = cars)

tpl1 = "Суммарная цена автомобилей {{ cs | sum }}"
tm1 = Template(tpl1)
msg1 = tm1.render(cs = digs)

print(msg)
print(msg1)


persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''

tm2 = Template(tpl)
msg2 = tm2.render(users=persons)

print(msg2)

html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''

tm3 = Template(html)
msg3 = tm3.render()

print(msg3)

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)