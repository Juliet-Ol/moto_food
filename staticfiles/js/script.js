function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



let btns = document.querySelectorAll("#productContainer button")

let incActionBtns = document.querySelectorAll("button[id^='inc_']")

incActionBtns.forEach(btn=>{
    btn.addEventListener("click", () => updateCart(btn, 'inc'))
})

let decActionBtns = document.querySelectorAll("button[id^='dec_']")

decActionBtns.forEach(btn=>{
    btn.addEventListener("click", () => updateCart(btn, 'dec'))
})


btns.forEach(btn=>{
    btn.addEventListener("click", addToCart)
})
function addToCart(e){
    let product_id = e.target.value
    // console.log(product_id)
    let url = '/add_to_cart'

    let data = {id:product_id}
    
    
    
    fetch(url, {
        method:"POST",
        headers: {'Content-Type':'application/json', 'X-CSRFToken': csrftoken,},
        body:JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        document.getElementById("num_of_items").innerHTML = data
        console.log(data)
    })
    .catch(error=>{
        console.log(error)
    })
    
}

function updateCart(el, action = 'inc'){
    
    console.log(el.dataset)
    let product_id = Number(el.dataset.id)
    // console.log(product_id)
    let url = '/update_cart'

    let data = {id:product_id, action }
    
    
    
    fetch(url, {
        method:"POST",
        headers: {'Content-Type':'application/json', 'X-CSRFToken': csrftoken,},
        body:JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        
        document.getElementById("qty_" + product_id).value = data
        let elm = document.getElementById('item_price_' + product_id)
        unitPrice = +elm.dataset.unit_price
        val = data * unitPrice
        elm.innerHTML = 'Ksh ' + val + '.0'
        elm = null
        
        let el2 = document.getElementById('grand_total')
        console.log('grand total ' + el2.dataset.grand)
        let oldG = +el2.dataset.grand
        let grand = action == 'inc' ? (oldG + unitPrice) : (oldG - unitPrice)
        el2.innerHTML = 'Ksh ' + grand + '.0'
        el2.dataset.grand = grand
        // el2 = null
        if (data < 1) {
            document.getElementById("cart_item_" + product_id).remove()
            return
        }
        console.log(data)
    })
    .catch(error=>{
        console.log(error)
    })
    
}