async function consultarDB(){
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

    try{
        const response = await fetch(`api/consultar/?tipo_doc=${encodeURIComponent(tipoDoc)}&num_doc=${encodeURIComponent(numDoc)}`)
        const data = await response.json();

        if (response.ok && data.encontrado){
            resultadoBox.style.backgroundColor = '#d1e7dd';
            resultadoBox.style.border = '1px solid #badbcc';
            resultadoBox.style.color = '#0f5132';
            resultadoBox.innerHTML = `
                <h3 style="margin-bottom: 10px;">Título Verificado</h3>
                <p><strong>Graduado:</strong> ${data.nombre_completo}</p>
                <p><strong>Programa:</strong> ${data.carrera}</p>
                <p><strong>Seccional/Sede:</strong> ${data.seccional}</p>
                <p><strong>Fecha de Graduación:</strong> ${data.fecha_grado}</p>
                <p><strong>Hash Blockchain:</strong> <code>${data.hash_bloque}</code></p>
            `;
        } else{
            resultadoBox.style.backgroundColor = '#F8D7DA';
            resultadoBox.style.border = '1px solid #F5C2C7';
            resultadoBox.style.color = '#842029';
            resultadoBox.innerHTML = `No se encontró ningun registro`;
        }
    } catch (error){
        console.error('Error al sonsultar:', error);
        resultadoBox.style.backgroundColor = '#fff3cd';
        resultadoBox.style.border = '1px solid #ffecb5';
        resultadoBox.style.color = '#664d03';
        resultadoBox.innerHTML = `Error del servidor: No se pudo establecer conexion con la base de datos`;
    }
    
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