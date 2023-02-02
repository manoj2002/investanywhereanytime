const showMenu = (headerToggle, navbarId) =>{
    const toggleBtn = document.getElementById(headerToggle),
    nav = document.getElementById(navbarId)

    // Validate that variables exist
    if(headerToggle && navbarId){
        toggleBtn.addEventListener('click', ()=>{
            // We add the show-menu class to the div tag with the nav__menu class
            nav.classList.toggle('show-menu')

        })
    }
}
showMenu('header-toggle','navbar')


const linkColor =document.querySelectorAll('.nav__link')

function colorLink(){
    linkColor.forEach(L => l.classList.remove('active'))
    this.classList.add('active')
}
linkColor.forEach(L => l.addEventListener('click',colorLink))