## Roles: 
- all roles:
    - are acces la adeverinte si holiday request proprii
    - poate creea, updata si sterge holiday request si certificate request proprii
- manager:
  - are acces la holiday request > aprobare/respingere pentru membrii din echipa
- Hr:
  - are acces la certificate request pentru toti angajatii
  - create, update si delete pentru certificate employee
  - create, update si delete pt employee
  - 
SuperUser
  - Crud pentru toate modelele
  - 


Sa implementez metoda 
 > get_queryset  de unde returnam un queryset pentru clasa respectiva - pt certificate 
> CertificateEmployee.objects.all()
> CertificateEmployee.objects.filter(employee=self.request.user)

- 
- makemigrate
- SuperUser
- admin.py - unde adaug clasele
- adaug angajati - contracte, concedii

Navbar -  prima oara

Pagini : 
- Pagina pentru creare de angajat (view, template, url) - _done_
- Pagina lista angajati  ---//
- Pagina update angajat --//
- Pagina delete angajat --//
- Pagina Dash-board a angajatului - DetailView >> functie  ---//
- Pagina pentru creare cerere concediu
- 

- linkuri pentru pagini in Nav bar - si butoane, chestii la studenti - sa mai fac CSS
- introduc link in nav bar - lista agajati ///
- in employee - sa facem update si detele  //

Contracts


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>{% block title %} {% endblock %}</title>
</head>
<body>
<div class="bg-success p-2 text-white">Have a nice day</div>

{% include 'navbar.html' %}

<header>
    <nav>
        <ul>
            <li><a href="{% url 'home_page' %}">Home</a></li>
            {% if user.is_authenticated %}
                <li><a href="{% url 'logout' %}">Logout</a></li>
            {% else %}
                <li><a href="{% url 'login' %}">Login</a></li>
            {% endif %}
        </ul>
    </nav>
</header>


<div class="container">
    {% block content %}
    {% endblock %}
</div>

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
        integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"
        integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy"
        crossorigin="anonymous"></script>
</body>
</html>