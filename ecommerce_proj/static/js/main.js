document.getElementById('search-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    const searched = document.getElementById('search').value
    console.log(searched)

    axios.get('/search', {params: {searched: searched}}).then((response)=> {
        console.log('response? ', response)
        // console.log(response.data.img_url)
        document.getElementById('search-modal-item').innerHTML = `${response.data.item}`
        document.getElementById('search-modal-img').src = `${response.data.img}`
        document.getElementById('search-modal-price').innerHTML = `${response.data.price}`

        if(response.data.price === 'SOLD OUT!') {
            document.getElementById('search-cart-button').hidden = true;
        } else {
            document.getElementById('search-cart-button').hidden = false;
        }
    })

    // axios.get('/search')
})