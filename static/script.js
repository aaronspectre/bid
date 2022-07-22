let add_button = document.getElementById('add-button')
let form = document.getElementById('add-form')

add_button.addEventListener('click', event => {
	form.style.display = 'flex'
})

document.querySelector('.form-cover').addEventListener('click', event => {
	form.style.display = 'none'
})