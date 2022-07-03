// Handle Search Form
document.getElementById('search-form').addEventListener('submit', (event) => {
    event.preventDefault()

    const searched = document.getElementById('search').value
    console.log(searched)

    axios.get('/search', {params: {searched: searched}}).then((response)=> {
        console.log('response? ', response)

        // Set modal data
        document.getElementById('search-modal-item').innerHTML = `${response.data.item}`
        document.getElementById('search-modal-img').src = `${response.data.img}`

        // Determine if 'Add to Cart' button should be visible or not
        if(response.data.price === 'SOLD OUT!') {
            document.getElementById('search-modal-price').innerHTML = `${response.data.price}`
            document.getElementById('search-add-to-cart').hidden = true;
        } else {
            document.getElementById('search-modal-price').innerHTML = `$${response.data.price}`
            document.getElementById('search-add-to-cart').hidden = false;
        }
        
        // Set the value of that button to the contents of the search result
        document.getElementById('search-add-to-cart').value = `item:${response.data.item},price:${response.data.price}`

        
    })
})

// Increment Cart Quantity
var badge = 0
function incrementCart() {
    badge++
    document.getElementById('cart-badge').textContent = badge
    
};

// when window loads, send get request to backend to get the length of
// cart_list. If len(cart_list) > 0: set 'cart_badge' to that length
window.onload = function setCart() {
    
    axios.get('/cart_counter').then((response)=> {
        badge = response.data.badge
        console.log(`recieved from backend: badge = ${badge}`)
        if(badge > 0) {
            console.log(`setting badge to ${badge}`)
            document.getElementById('cart-badge').textContent = badge
        }
    })
}