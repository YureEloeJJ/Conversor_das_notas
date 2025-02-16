from flask import Flask, render_template, request

app = Flask(__name__)

#escolhendo o metodo
@app.route('/', methods=['GET', 'POST'])
#iniciando o codigo de escolha da moesda
def coversor_de_moedas():
    if request.method == 'POST':
        escolha = int(request.form.get('escolha')) 
        valor_brl = float(request.form.get('valor_brl'))
        resultado = None


        if escolha == 1:
            resultado = valor_brl * 6 #moeda dolar
            moeda = "Dólar"
        elif escolha == 2:
            resultado =  valor_brl * 3 #moeda euro  
            moeda = "Euro"
        else:  
            resultado = "Escolha invalida"
            moeda =  ""


        return render_template('index.html', resultado=resultado, moeda=moeda, valor_brl=valor_brl)    

    return render_template('index.html', resultado=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
  