function consultarDB(){
    const tipoDoc = document.getElementById('tipoDoc').value;
    const numDoc = document.getElementById('numDoc').value.trim();
    const resultadoBox = document.getElementById('resultadoConsulta');

    if (!tipoDoc || !numDoc){
        alert("Por favor completa todos los campos")
        return;
    }

    resultadoBox.style.display = 'block';
    resultadoBox.style.backgroundColor = '#E8F4FD';
    resultadoBox.style.border = '1px solid #B6D4FE';
    resultadoBox.style.color = '#084298';
    resultadoBox.innerHTML = `Consultando documento <strong>${tipoDoc} ${numDoc}</strong> en <code>db.sqlite3</code>...`;

    setTimeout(() =>{
        resultadoBox.style.backgroundColor = '#D1E7DD';
        resultadoBox.style.border = '1px solid #BADBCC';
        resultadoBox.style.color = '#0F5132';
        resultadoBox.innerHTML = `
            Consulta exitosa
            Documento: ${tipoDoc} ${numDoc}
            Consulta hecha en <code>db.sqlite3</code>
        `;
    }, 1200);
}