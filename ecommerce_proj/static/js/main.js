document.getElementById('search-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    const searched = document.getElementById('search').value
    console.log(searched)

    axios.post('/search', {searched: searched}).then((response)=> {
        console.log('response? ', response)
        console.log(response.data.img_url)
        document.getElementById('searched-img').src = `${response.data.img_url}`
    })

    // axios.get('/search')
})