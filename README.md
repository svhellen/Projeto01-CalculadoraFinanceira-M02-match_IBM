# Calculadora Financeira com Validação de Renda

## Descrição do Projeto

Este projeto engloba o desenvolvimento de uma aplicação web de calculadora financeira em Python, proporcionando aos usuários a capacidade de calcular empréstimos com base em sua renda mensal. A aplicação abrange várias etapas e tecnologias, proporcionando uma experiência completa e funcional.

## Funcionalidades Implementadas

1. **Validação de Renda:**
   - Os usuários fornecem informações sobre sua renda mensal.
   - A aplicação verifica se a renda inserida é válida e está dentro de um limite específico.

2. **Cálculo de Empréstimo:**
   - Após a validação bem-sucedida da renda, os usuários podem inserir o valor desejado para o empréstimo e o prazo desejado.
   - A aplicação verifica se o valor do empréstimo está dentro dos limites permitidos,calcula a taxa de juros apropriada e o valor das prestações.

3. **Apresentação dos Resultados:**
   - A aplicação exibe os resultados do cálculo, incluindo o valor das prestações e o custo total do empréstimo.

## Tecnologias Utilizadas

O projeto utiliza as seguintes tecnologias e ferramentas:

- **HTML**, **CSS**, **Bootstrap**: As páginas da aplicação foram estruturadas e estilizadas utilizando HTML, CSS e o framework Bootstrap, proporcionando uma interface visual bem simples, mas atraente e responsiva.

- **Flask:** Utilizado como framework web em Python para o desenvolvimento da lógica da aplicação e para lidar com as requisições HTTP.

- **Python:** Linguagem de programação principal para o desenvolvimento da calculadora financeira.

- **pytest:** Framework de teste em Python para a implementação dos testes automatizados.

## Conhecimentos Aplicados

Durante o desenvolvimento deste projeto, foram aplicados os seguintes conhecimentos:

- **Desenvolvimento Web em Python:** Utilização do HTML5, CSS, Bootstrap e do Flask para criar uma aplicação web que responde a requisições HTTP.

- **Validação de Dados de Usuário:** Implementação de validação para garantir que os dados fornecidos pelos usuários sejam adequados.

- **Cálculos Financeiros:** Aplicação de fórmulas financeiras para calcular a taxa de juros, prestações mensais e custo total do empréstimo.

- **Testes Automatizados:** Utilização do framework pytest para escrever testes automatizados, garantindo a robustez da aplicação.

## Como Executar o Projeto

1. Instale as dependências necessárias:

   ``` pip install -r requirements.txt ```

2. Execute o aplicativo Flask:

    ```flask run ```

Acesse a aplicação em seu navegador, normalmente em http://localhost:5000/.

## Testes Automatizados
Os testes automatizados para este projeto foram implementados utilizando o framework pytest. Eles cobrem cenários de validação de renda e cálculo de empréstimo, garantindo o correto funcionamento da aplicação.

Para executar os testes, utilize o seguinte comando:

``` pytest tests/test_app.py ```

Certifique-se de que o ambiente virtual esteja ativado antes de executar os comandos.

## Estrutura do Projeto
**main.py:** Contém a lógica principal da aplicação Flask.
**calculadoraFinanceira/:** Pacote contendo o código-fonte da aplicação.
**tests/:** Diretório com os testes automatizados.
**README.md:** Este arquivo, fornecendo informações sobre o projeto e instruções de execução.


Projeto concluído como parte dos requisitos para a conclusão do curso Match - Mastertech, em colaboração com a IBM. Este trabalho representa a aplicação prática dos conhecimentos adquiridos ao longo do curso e demonstra a capacidade de desenvolvimento de soluções tecnológicas por meio de uma parceria educacional valiosa.