/*
El siguiente código es para la funcionalidad de la navegación lateral o SideNav
*/

// Función para contraer el SideNav

function contraerSideNav() {
    document.getElementById("sideNav").classList.add('d-none')
    document.getElementById("sideNavContraida").classList.remove('d-none')
    document.getElementById("contenedorMain").style.marginLeft='64px'
}

// Función para des-contraer el SideNav

function desContraerSideNav() {
    document.getElementById("sideNavContraida").classList.add('d-none')
    document.getElementById("sideNav").classList.remove('d-none')
    document.getElementById("contenedorMain").style.marginLeft='280px'
}