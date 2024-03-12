let inf = []

function cad() {
    let nome = document.getElementById('nome').value
    let preco = document.getElementById('preco').value
    let qtd = document.getElementById('qtd').value
    let tot = preco * qtd

    inf.push([nome, preco, qtd, tot])

    document.getElementById('nome').value = ""
    document.getElementById('preco').value = ""
    document.getElementById('qtd').value = ""

    // sTable()
}

function sTable() {
        let table = "<table border = 1><tr><th>Nome</th><th>Preço</th><th>Quantidade</th><th>Subtotal</th></tr>"
        inf.forEach(function (item) {
            table += `<tr><td>${item[0]}</td><td>${item[1]}</td><td>${item[2]}</td><td>${item[3]}</td></tr>`
        })
        table += "</table>"
        document.getElementById("table").innerHTML = table
        document.getElementById("table").style.display = "block";
}

function hTable() {
    document.getElementById("table").style.display = "none";
}