document.getElementById('search-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    const searched = document.getElementById('search').value
    console.log(searched)

    axios.get('/search', {params: {searched: searched}}).then((response)=> {
        console.log('response? ', response)

        // Set modal data
        document.getElementById('search-modal-item').innerHTML = `${response.data.item}`
        document.getElementById('search-modal-img').src = `${response.data.img}`
        document.getElementById('search-modal-price').innerHTML = `$${response.data.price}`
        document.getElementById('search-add-to-cart').value = `item:${response.data.item},price:${response.data.price}`

        // Determine if 'Add to Cart' button should be visible or not
        if(response.data.price === 'SOLD OUT!') {
            document.getElementById('search-add-to-cart').hidden = true;
        } else {
            document.getElementById('search-add-to-cart').hidden = false;
        }
    })
})