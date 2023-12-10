import pytest
from flask import url_for
from calculadoraFinanceira import app

# configuração SERVER_NAME
app.config["SERVER_NAME"] = 'localhost:5000'
app.config["PREFERRED_URL_SCHEME"] = 'http'


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_validacao_renda_erro_renda_invalida(client):
    with app.app_context():
        response = client.post(url_for('validacao_renda'), data=dict(nome='Teste', renda='10000000'), follow_redirects=False)
        assert 'A renda inserida não é válida ou excede o limite permitido.' in response.data.decode('utf-8')


def test_validacao_renda_erro_valor_nao_numerico(client):
    with app.app_context():
        response = client.post(url_for('validacao_renda'), data=dict(nome='Teste', renda='invalido'), follow_redirects=False)
        assert 'Por favor, insira um valor numérico válido para a renda.' in response.data.decode('utf-8')


def test_calculo_emprestimo_erro_valor_abaixo_minimo(client):
    with app.app_context():
        response = client.post(url_for('calculo_emprestimo', renda=10000), data=dict(valor_emprestimo='1000', prazo='12'))
        assert 'Valor de empréstimo abaixo do mínimo.' in response.data.decode('utf-8')


def test_calculo_emprestimo_erro_valor_acima_limite(client):
    with app.app_context():
        response = client.post(url_for('calculo_emprestimo', renda=10000), data=dict(valor_emprestimo='2500000', prazo='12'), follow_redirects=True)
        assert 'Valor de empréstimo acima do limite.' in response.data.decode('utf-8')


def test_calculo_emprestimo_erro_valor_nao_numerico(client):
    with app.app_context():
        response = client.post(url_for('calculo_emprestimo', renda=10000), data=dict(valor_emprestimo='invalido', prazo='12'))
        assert 'Por favor, insira valores numéricos válidos para o valor do empréstimo e o prazo.' in response.data.decode('utf-8')
