
document.querySelectorAll('.link').forEach(el => el.addEventListener(('click'), clickhandler))


function clickhandler(event){
    document.querySelector('.hovered').classList.remove('hovered')
    event.currentTarget.classList.add('hovered')
} 
