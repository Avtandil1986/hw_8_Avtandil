console.log("Hello World!!!")
const searchInput = document.querySelector("#search-input")
const searchData = document.querySelector("#search-data")
searchInput.addEventListener('keyup', (e) => {
    const search_text = e.target.value
    console.log(search_text)
    fetch('/search/?query=' + search_text, {
        method: 'GET'
    }).then(
        (res) => res.json()
    ).then(
        (data) => {
            console.log(data)
            searchData.innerHTML = ''
            if (data.list.length > 0) {
                data.list.forEach((item) => {
                    searchData.innerHTML += `
                        <span>ID: ${item.id}</span><br/>
                        <a href="/products/${item.id}/">Title: ${item.title} </a><br/>
                        <span>Price: ${item.price}</span>
                         <hr/>
                    `
                })
            }
        }
    )
})