const custos = []
function add_custo() {
    console.log('aqui')
    let custo = document.getElementById('custos').value
    let quantidade = document.getElementById('quantidade').value
    // let medida = document.getElementById('unidade').value
    custo = JSON.parse(custo.replace(/'/g, '"'))

    let novo_custo = {
        "nome": custo.nome,
        "quantidade": quantidade,
        "unidade": custo.medida,
        "valor": quantidade*custo.valor
    }
    document.getElementById('custos').value = null
    document.getElementById('quantidade').value = null

    custos.push(novo_custo)
    console.log(custos)
    return
}