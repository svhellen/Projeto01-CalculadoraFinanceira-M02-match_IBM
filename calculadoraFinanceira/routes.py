from flask import render_template, request, redirect, url_for
from calculadoraFinanceira import app


@app.route("/", methods=["GET", "POST"])
def validacao_renda():
    renda_limite = 10000

    if request.method == 'POST':
        try:
            nome = request.form['nome']
            renda = request.form['renda']
            renda = float(renda)

            if 0 < renda <= renda_limite:
                return redirect(url_for("calculo_emprestimo", renda=renda))
            else:
                msg = "A renda inserida não é válida ou excede o limite permitido."
                return render_template('index.html', renda_valida=False, msg_error=msg, nome=nome)
        except ValueError:
            msg = "Por favor, insira um valor numérico válido para a renda."
            return render_template('index.html', renda_valida=False, msg_error=msg, nome=nome)

    return render_template('index.html')


@app.route("/calculo_emprestimo/<float:renda>", methods=["GET", "POST"])
def calculo_emprestimo(renda):
    minimo_emprestimo = renda / 4
    limite_emprestimo = renda * 20
    msg_range_emprestimo = f"Insira um valor entre {minimo_emprestimo} e {limite_emprestimo}."

    if request.method == 'POST':
        try:
            valor_emprestimo = float(request.form['valor_emprestimo'])
            # precisa validar prazo
            # e talvez definir limite pro valor da prestacao nao ser maior q a renda
            prazo = int(request.form['prazo'])

            if minimo_emprestimo <= valor_emprestimo:
                if valor_emprestimo <= limite_emprestimo:
                    taxa_juros = 0.05
                    prestacao_mensal = (valor_emprestimo * taxa_juros) / (1 - (1 + taxa_juros) ** -prazo)

                    return redirect(url_for("resultado",
                                            valor_emprestimo=valor_emprestimo,
                                            taxa_juros=taxa_juros,
                                            prestacao_mensal=prestacao_mensal,
                                            prazo=prazo))

                else:
                    msg = f"Valor de empréstimo acima do limite. {msg_range_emprestimo}"
                    return render_template('calculo_emprestimo.html', msg_error=msg, renda=renda)
            else:
                msg = f"Valor de empréstimo abaixo do mínimo. {msg_range_emprestimo}"
                return render_template('calculo_emprestimo.html', msg_error=msg, renda=renda)
        except ValueError:
            msg = "Por favor, insira valores numéricos válidos para o valor do empréstimo e o prazo."
            return render_template('calculo_emprestimo.html', msg_error=msg, renda=renda)
    return render_template('calculo_emprestimo.html', msg_range_emprestimo=msg_range_emprestimo, msg_error=None, renda=renda)


@app.route("/resultado")
def resultado():
    valor_emprestimo = request.args.get('valor_emprestimo')
    taxa_juros = request.args.get('taxa_juros')
    prestacao_mensal = request.args.get('prestacao_mensal')
    prazo = request.args.get('prazo')

    if taxa_juros is not None and prestacao_mensal is not None:
        custo_total = float(prestacao_mensal) * int(prazo)

        return render_template('resultado.html',
                               valor_emprestimo=float(valor_emprestimo),
                               taxa_juros=float(taxa_juros) * 100,
                               prestacao_mensal=float(prestacao_mensal),
                               prazo=int(prazo),
                               custo_total=custo_total)

    return render_template('resultado.html',
                           taxa_juros=None,
                           prestacao_mensal=None,
                           prazo=None,
                           custo_total=None)
