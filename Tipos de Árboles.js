class arbol{
    constructor(nombre,origenes,altura,usos,suelo_clima,vegetacion,img){
        this.nombre = nombre,
        this.origenes = origenes,
        this.altura = altura,
        this.usos = usos,
        this.suelo_clima = suelo_clima,
        this.vegetacion = vegetacion,
        this.img = img
    }
    getNombre(){
        return this.nombre
    }
    getOrigenes(){
        return this.origenes
    }
    getImg(){
        return this.img 
    }
    get_altura(){
    return this.altura
    }
    get_usos(){
    return this.usos
    }
}

let array = [1,2,3,4,5,'sdfsdfs']

let var_uno = new arbol('Tepeguaje','Todo México',2.600,['Sus Frutos','cultivos','hoja y corteza para antidisentéricos','antiinflamatorios','antitusivos'],
'En sitios rocosos, barrancas escarpadas, orillas de ríos y caminos',
['secundaria','pastizales con matorral','bosques de encino y pino - encino'],'https://inaturalist-open-data.s3.amazonaws.com/photos/146616825/original.jpg')

let var_dos = new arbol('Tepane, algarrobo',['Yuc.','Chis.','Ver.','Pue.','S.L.P.','Gto.','Gro.','Mich.','Jal.','Nay.','Dgo.'],2.000,['útil para construcciones rurales','elaboración de mangos paraherramientas', 'postes para cercas'],
'En todo tipo de suelo en clima cálido y templado', ['Selvas bajas caducifolias','bosques caducifolios','matorrales'],
'https://www.inaturalist.org/guide_taxa/654641')

let var_tres = new arbol(['Lele','negundo','acecintle'],['Chis.','Hgo.','Jal.','Mich.','N.L.','Ver'],2.600,['elaborar utensilios domésticos','acabado de interiores','muebles baratos y en la fabricación de papel'],
'En cañadas y riberas',['Bosque caducifolio','pinares,encinares','vegetación riparia'],
'http://www1.inecol.edu.mx/publicaciones/resumeness/FLOVER/46-cabrera.pdf')

function mostrar_contenido(parametro,variable){
parametro.addEventListener('submit', e => {
    e.preventDefault()
    let elem_uno = document.createElement('div')
    parametro.appendChild(elem_uno)
    elem_uno.innerHTML = `<em>Nombre del Árbol: ${variable.getNombre()}</em> <br><br>
<strong>Que tiene sus origines en:  ${variable.getOrigenes()}</strong> <br><br>
<img src="${variable.getImg()}" /> <br><br>
<em>Con una altura de aproximadamente: ${variable.get_altura()}</em> <br><br>
<u>Aplicaciones: ${variable.get_usos()}</u>`
})
}

let id_uno = document.getElementById('id_uno')

mostrar_contenido(id_uno,var_uno)
