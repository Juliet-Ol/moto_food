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



var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        // if (user == 'AnonymousUser'){
        //     console.log('User is not logged in')
        // }else{
        //     updateUserOrder(productId, action)
            
        // }
    })
}

// function updateUserOrder(productId, action){
function updateUserOrder(e){    
    console.log('User is logged in, sending data...')
    var productId = e.target.value
    var url = '/update_item/'
    var data = {productId:productId}
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json', 'X-CSRFToken': csrftoken}, 'X-CSRFToken': csrftoken,
            
            body:JSON.stringify(data)
        // },
        // // body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then(res=>res.json())
    .then((data) => {
        console.log('data:', data)
        location.reload()
    });
    // .catch(error=>{
    //     console.log(error)
    // })
}

