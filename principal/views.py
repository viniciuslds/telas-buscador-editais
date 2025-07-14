# principal/views.py

from django.shortcuts import render

def pagina_inicial(request):
    # Criamos dados falsos para simular os editais do banco de dados
    editais_mock = [
        {'titulo': 'Edital de Inovação Tecnológica', 'data_abertura': '10/07/2025', 'data_final': '30/08/2025', 'link_oficial': '#'},
        {'titulo': 'Bolsas de Pesquisa em Biotecnologia', 'data_abertura': '15/07/2025', 'data_final': '15/09/2025', 'link_oficial': '#'},
    ]

    contexto = {
        'editais': editais_mock,
    }
    
    # Renderiza o template home.html, passando os dados falsos
    return render(request, 'home.html', contexto)